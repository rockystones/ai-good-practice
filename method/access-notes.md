---
status: published
durability: dated
last-reviewed: 2026-08-13
review-by: 2026-11
---

# Access playbook for research tooling

Working routes and known blocks for our WebFetch-based research agents, accumulated per session so they stop being rediscovered. As of August 2026.

## Working routes

- **arXiv**: abstract pages fetch fine; full text via `arxiv.org/html/<id>v1` (2024+ papers) or `ar5iv.labs.arxiv.org/html/<id>` (older). Raw `/pdf/` URLs return undecodable binary.
- **Reader proxy** `https://r.jina.ai/<full-url>` works for: openai.com pages, cdn.openai.com PDFs (incl. system cards), writings.stephenwolfram.com (TLS error direct), link.springer.com (direct = institutional-login redirect).
- **academic.oup.com**: direct fetch works; the proxy hits a CAPTCHA — go direct first (opposite of Springer).
- **PubMed Central** (`pmc.ncbi.nlm.nih.gov`): direct works; often the best route to a paywalled paper's item-level data.

## Blocked or unreliable

- **web.archive.org**: blocked entirely for our fetcher.
- **YouTube transcripts**: 401 direct and via proxy (page metadata fetches fine). Gap: verbatim quotes from talks need dedicated transcript tooling or the browser pane.
- **openreview.net** (incl. api2): bot challenge — peer-review comments unreachable; use iclr.cc/virtual or institutional portals for acceptance status.
- **403 to direct fetch**: help.openai.com, platform.openai.com, damiencharlotin.com, classcentral.com, mdpi.com (some), chenowethlaw.com.
- **Tool-refused domains**: theguardian.com, ig.ft.com.
- **Paywalled**: ACM DL (FAccT papers), NYT, New Yorker — use corroborated secondary quotation and say so, or defer to a browser-pane session.

## Practice notes

- When a claim's only route is search-snippet synthesis, mark the source entry with the access caveat and treat the claim as needing verification before print (see the Numbers Rule in [research-protocol.md](research-protocol.md)).
- Search summarizers sometimes attribute arXiv's site-wide Simons Foundation footer as a paper's funding acknowledgment — a known false pattern; never repeat funding claims from snippets.
