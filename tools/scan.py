#!/usr/bin/env python3
"""Sensitive-info scanner for this public repo.

Run before every commit and push (the hooks in tools/hooks do this automatically):

    python tools/scan.py --staged   # staged content (pre-commit)
    python tools/scan.py --all      # tracked + untracked-unignored files (pre-push / audit)

Exit code 1 on any BLOCK finding; WARN findings print but do not fail the run.
False positives: add the exact matched text to tools/scan-allow.txt (one per line,
with a comment line above explaining why).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWLIST_PATH = ROOT / "tools" / "scan-allow.txt"
EXCLUDED = {"tools/scan-allow.txt"}  # holds approved strings; would self-trigger
MAX_BYTES = 2_000_000

ALLOWED_EMAIL_SUFFIXES = (
    "@users.noreply.github.com",
    "@anthropic.com",  # Co-Authored-By noreply line in commit templates/docs
)
ALLOWED_EMAIL_DOMAINS = {"example.com", "example.org", "example.net", "example.invalid"}
ALLOWED_IPS = {"0.0.0.0", "127.0.0.1", "255.255.255.255", "192.0.2.0", "192.0.2.1", "203.0.113.0"}
PLACEHOLDER_PATH_MARKERS = ("<you>", "<user>", "<name>", "username", "$user", "%userprofile%")

RULES = [
    ("private-key",  "BLOCK", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("github-token", "BLOCK", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("api-key",      "BLOCK", re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{20,}\b")),
    ("aws-key",      "BLOCK", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("slack-token",  "BLOCK", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("google-key",   "BLOCK", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("email",        "BLOCK", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("user-path",    "BLOCK", re.compile(r"(?:[A-Za-z]:[\\/]Users[\\/]|/home/|/Users/)[A-Za-z0-9._~+-][^\s\\/\"'<>|:*?]*")),
    ("bearer",       "WARN",  re.compile(r"\b[Bb]earer\s+[A-Za-z0-9_\-.=]{20,}")),
    ("ip-address",   "WARN",  re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("card-digits",  "WARN",  re.compile(r"\b\d{15,16}\b")),
    ("password",     "WARN",  re.compile(r"(?i)\b(?:password|passwd|secret)\s*[:=]\s*\S{6,}")),
]


def load_allowlist():
    if not ALLOWLIST_PATH.exists():
        return set()
    lines = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace").splitlines()
    return {ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")}


def git_out(*args):
    return subprocess.run(["git", *args], capture_output=True, cwd=ROOT).stdout


def target_files(staged):
    if staged:
        raw = git_out("diff", "--cached", "--name-only", "-z", "--diff-filter=ACM")
    else:
        raw = git_out("ls-files", "-z") + git_out("ls-files", "-z", "-o", "--exclude-standard")
    files = [f for f in raw.decode("utf-8", "replace").split("\0") if f]
    return sorted(set(files) - EXCLUDED)


def read_content(path, staged):
    if staged:
        out = subprocess.run(["git", "show", f":{path}"], capture_output=True, cwd=ROOT)
        if out.returncode == 0:
            return out.stdout
    try:
        return (ROOT / path).read_bytes()
    except OSError:
        return None


def is_false_positive(rule, text):
    if rule == "email":
        low = text.lower()
        if any(low.endswith(s) for s in ALLOWED_EMAIL_SUFFIXES):
            return True
        return low.rsplit("@", 1)[-1] in ALLOWED_EMAIL_DOMAINS
    if rule == "ip-address":
        if text in ALLOWED_IPS:
            return True
        return any(int(o) > 255 for o in text.split("."))  # version strings, not IPs
    if rule == "user-path":
        low = text.lower()
        return any(m in low for m in PLACEHOLDER_PATH_MARKERS)
    return False


def main():
    ap = argparse.ArgumentParser(description="Sensitive-info scanner")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="scan staged content")
    mode.add_argument("--all", action="store_true", help="scan tracked + untracked files")
    args = ap.parse_args()

    allow = load_allowlist()
    counts = {"BLOCK": 0, "WARN": 0}
    for path in target_files(args.staged):
        blob = read_content(path, args.staged)
        if blob is None or len(blob) > MAX_BYTES or b"\0" in blob[:8192]:
            continue  # unreadable, huge, or binary
        text = blob.decode("utf-8", "replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            for rule, severity, rx in RULES:
                for m in rx.finditer(line):
                    hit = m.group(0)
                    if hit in allow or is_false_positive(rule, hit):
                        continue
                    counts[severity] += 1
                    shown = hit if len(hit) <= 60 else hit[:57] + "..."
                    print(f"[{severity}] {rule:12s} {path}:{lineno}: {shown}")

    if counts["BLOCK"] + counts["WARN"] == 0:
        print("scan: clean")
    else:
        print(f"scan: {counts['BLOCK']} BLOCK, {counts['WARN']} WARN")
    return 1 if counts["BLOCK"] else 0


if __name__ == "__main__":
    sys.exit(main())
