# EBS SEO system

The SEO workstream of the EBS marketing system: keyword strategy, on-page and technical optimization, and search-visibility reporting for EBS Integrator. Three layers, each feeding the next.

> **Part of the EBS marketing system.** This is the *SEO* workstream — one repository among several, coordinated by the umbrella repo [`zamolxis72/ebs-marketing-system`](https://github.com/zamolxis72/ebs-marketing-system). Boundary: cross-workstream planning lives in the umbrella; SEO data and outputs live here and only here. Deliberately separate repos, not a monorepo — do not fold this repo into the umbrella and do not copy its data there.

## Structure

| Path | Role |
|---|---|
| `intake/` | The facts: keyword portfolio, target pages, and current rankings data. Also the entity layer — `entity-register.md` (claims), `snapshots/` (dated GSC pulls, immutable), and `entity-health.md` (the generated read surface). |
| `library/` | The reference: audit checklist, on-page and schema templates, the prioritization method, and `entity-health-method.md`. |
| `reports/` | The outputs: shipped audits and recommendation sets, one folder per pass, plus the living `site-problems-log.md`. |

### The entity layer, in one line each

Read **`intake/entity-health.md`** before any new title is proposed anywhere on the site. It says, per entity, whether we hold it, are splitting it, lost it to another of our pages, claim it without ranking, or have never claimed it — and what may be done in each case. It is generated from the claims in `entity-register.md` joined to the latest dated pull in `snapshots/`, and it is never hand-edited. The split exists because claims stay true for a year and metrics are wrong in a fortnight; keeping them in one file is how a stale number ends up deciding a title.

## How it connects

- Planning cadence comes from the umbrella's marketing agenda (in `zamolxis72/ebs-marketing-system`, `planning/`).
- Production uses `b2b-seo-audit` (diagnosis) plus `seo-strategy` (demand/portfolio), `text-semantics` (arrangement), `machine-signals` (markup/access), `geo-content` (AI visibility), `verified-facts` (before ship); live metrics come from the Ahrefs tools, never invented.
- The articles workstream (`zamolxis72/ebs-article-system`) consumes this repo's keyword and gap findings by reference.

## Status

No audit pass shipped yet. The **entity layer is live** as of 2026-08-14: register seeded from the 17 live case studies, first GSC baseline snapshot pulled, health view generated, method recorded. Structure mirrors the case-studies workstream (`zamolxis72/ebs-case-study-system`).
