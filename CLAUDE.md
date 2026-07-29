# CLAUDE.md — SEO workstream

Part of the EBS marketing system (umbrella: `zamolxis72/ebs-marketing-system`). Separate repos, not a monorepo.

## Before any SEO work (in this exact order)
1. Read `library/` — audit checklist, on-page and schema templates, the prioritization method.
2. Pull current data from / into `intake/` — keyword portfolio, target pages, rankings snapshots.

## Producing
- Use the `b2b-seo-audit`, `seo-strategy`, and `search-visibility-suite` skills.
- Metrics come from Ahrefs / Search Console — live or a dated snapshot. Never invent a metric.
- Feed keyword and gap findings to the articles workstream by reference, not by copying content.

## Shipping
- Persist audits and recommendation sets at `reports/<yyyy-mm-audit>/`.
- Commit shipped output as `seo: ship <pass>`.

## Boundary
Cross-workstream planning lives in the umbrella agenda. Do not fold this repo into the umbrella, and do not copy this repo's data there.
