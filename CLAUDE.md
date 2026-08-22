# CLAUDE.md — SEO workstream

Part of the EBS marketing system (umbrella: `zamolxis72/ebs-marketing-system`). Separate repos, not a monorepo.

## Before any SEO work (in this exact order)
1. Read `library/` — audit checklist, on-page and schema templates, the prioritization method.
2. Read `reports/site-problems-log.md` — **the living site/SEO health log, and this repo owns it.**
   Every known site problem (evidence, why it matters, owner, status) lives there; whichever
   workstream finds a site-health issue appends it THERE, never to its own library. Update statuses
   as fixes land.
3. Read `intake/entity-health.md` — **the single read surface for entity status, and this repo owns
   it.** Read it before any new title is proposed anywhere: it says per entity whether the site holds
   it (OWNED), is splitting it (CONTESTED), lost it to a different page (MISOWNED), claims it without
   ranking (UNPROVEN), or has never claimed it (OPEN) — and what may be done in each case. It is
   **generated, never hand-edited**, from the claims in `intake/entity-register.md` joined to the
   latest dated pull in `intake/snapshots/`. Method: `library/entity-health-method.md`. Producers
   append their page's entities to the **register** once live; the health view is regenerated, not
   written. Article *keyword* ownership stays with `ebs-article-system/library/content-map.md`; the
   two reference each other and never merge.
4. Pull current data from / into `intake/` — keyword portfolio, target pages, rankings snapshots.
   **The entity-health refresh rides the ~2-week agenda ritual**, not a schedule of its own: re-run
   the two GSC calls in `library/entity-health-method.md` (0 API units), record the rows into a new
   `intake/snapshots/gsc-<date>.json`, then run `python3 scripts/build_entity_health.py` and read the
   diff — the states that moved are the point. Snapshots are immutable; corrections go in the next
   one. Never hand-edit between the `BEGIN GENERATED` markers, and if a state rule needs changing,
   change the script and the method file in the same commit.

## Producing
- Use `b2b-seo-audit` (diagnosis) with `seo-strategy` (demand/portfolio), `text-semantics` (arrangement), `machine-signals` (markup/access), `geo-content` (AI visibility), `verified-facts` (before ship).
- Metrics come from Ahrefs / Search Console — live or a dated snapshot. Never invent a metric.
- Research discovery follows the article workstream's `library/trusted-sources.md` (the
  cross-workstream discovery whitelist — it plays its own role and is never overridden by a
  skill's bundled source list; those are suggestions).
- Feed keyword and gap findings to the articles workstream by reference, not by copying content.

## Shipping
- Persist audits and recommendation sets at `reports/<yyyy-mm-audit>/`.
- Commit shipped output as `seo: ship <pass>`.

## Boundary
Cross-workstream planning lives in the umbrella agenda. Do not fold this repo into the umbrella, and do not copy this repo's data there.

## Reporting — feed the activity log
Work shipped or decided here is a loggable activity. At the END of a session, use the `pack-chat` skill to record it to `~/Personal/activity-log`, tagged:
- **Area:** `Marketing / SEO`
- **Objective:** the specific outcome this session served (the "why").

Consistent Area labels roll marketing work up under the Marketing objective in EBS Activity/Sprint reports.
