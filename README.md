# EBS SEO system

The SEO workstream of the EBS marketing system: keyword strategy, on-page and technical optimization, and search-visibility reporting for EBS Integrator. Three layers, each feeding the next.

> **Part of the EBS marketing system.** This is the *SEO* workstream — one repository among several, coordinated by the umbrella repo [`zamolxis72/ebs-marketing-system`](https://github.com/zamolxis72/ebs-marketing-system). Boundary: cross-workstream planning lives in the umbrella; SEO data and outputs live here and only here. Deliberately separate repos, not a monorepo — do not fold this repo into the umbrella and do not copy its data there.

## Structure

| Path | Role |
|---|---|
| `intake/` | The facts: keyword portfolio, target pages, and current rankings data. |
| `library/` | The reference: audit checklist, on-page and schema templates, the prioritization method. |
| `reports/` | The outputs: shipped audits and recommendation sets, one folder per pass. |

## How it connects

- Planning cadence comes from the umbrella's marketing agenda (in `zamolxis72/ebs-marketing-system`, `planning/`).
- Production uses `b2b-seo-audit` (diagnosis) plus `seo-strategy` (demand/portfolio), `text-semantics` (arrangement), `machine-signals` (markup/access), `geo-content` (AI visibility), `verified-facts` (before ship); live metrics come from the Ahrefs tools, never invented.
- The articles workstream (`zamolxis72/ebs-article-system`) consumes this repo's keyword and gap findings by reference.

## Status

Scaffold only — no audits shipped yet. Structure mirrors the case-studies workstream (`zamolxis72/ebs-case-study-system`).
