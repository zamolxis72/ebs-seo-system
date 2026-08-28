# The Ahrefs engine — the pulls, owned here

**This is the ENGINE: which endpoint answers which question, with what parameters, at what cost.**
It is surface-agnostic — an article, a case study, a page or this workstream's own portfolio work
all run the same pulls. What a result DECIDES and WHERE it lands belongs to the consumer's own
rules (for articles: `ebs-article-system/library/collection-recipe.md`, which names these pulls by
id). Split out of that recipe 2026-08-28: the SEO system owns the engine, the workstream owns the
rules.

## Cost discipline (binds every pull)

Every keyword-endpoint call costs units (~33/row). A pull runs ONCE at the consumer's named step,
dated, and cached into the consumer's files; monitors and edit loops read the files, never the
API. Re-pull only when a decision depends on fresh data (a KD that moved, a SERP that changed
class). Before a new expensive pull class, verify unit cost against
`subscription-info-limits-and-usage`.

## The pulls

**E1 — Demand and SERP overview.** `keywords-explorer-overview` · country `us` · select
`keyword,volume,difficulty,parent_topic,traffic_potential,serp_features`.
Answers: is this ground one page or two (parent topic), is there SERP evidence at all, what
features gate the SERP. Semantics: **parent topic** is the keyword sending the most traffic to the
page ranking top for the term — keywords sharing a parent can be one page, keywords with different
parents need separate pages. A keyword returning **null KD / null parent / null TP has no SERP
evidence**. `ai_overview` + `question` in serp_features means question-shaped headings are
checked, not preferred.

**E2 — What winning pages DISCUSS.** `keywords-explorer-related-terms` · `terms=also_talk_about` ·
`view_for=top_10` · US, for the target keyword. The entity cluster measured rather than reasoned.
(Reference run: 1,260 units / 60 rows, 2026-08-24.)

**E3 — What Google actually REWARDS.** `serp-overview` for the target keyword to get the winning
URLs, then `site-explorer-organic-keywords` on the **top 3 only** (cap it). Discussion data and
outcome data are different evidence: E2 says what a page talks about, E3 says what Google ranks it
for. A term in both is the strongest candidate there is.

**E4 — Level every survivor.** `keywords-explorer-overview` on the surviving candidates for
`parent_topic, volume, difficulty`. This is what keeps topic and entity clustering ONE vocabulary:
a candidate whose parent is the target's parent is in-page vocabulary; a candidate whose parent is
its own is a topic in its own right.

**E5 — The question set.** `keywords-explorer-matching-terms` · `match_mode=terms` on the target
keyword's stem, filtered to question forms — real queries people ran, each with volume and date,
never invented.

**E6 — Measurement (post-publish).** Rank and AI-citation tracking per `seo-strategy`'s method;
GSC pulls for entity health per `entity-health-method.md` (0 API units).

## Who runs what

`seo-strategy` runs E1/E4/E6 (demand, leveling, measurement); `ebs-discoverability` runs E2/E3/E5
(the entity engine and the question set). Consumers cite pulls by id — a workstream recipe that
restates an endpoint here has forked the engine.
