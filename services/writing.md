# AI SEO for writing

What any system that **writes** for the site applies: articles (`ebs-article-system`), case studies
(`ebs-case-study-system`), service and industry page copy. The rules live in this repo; this file says which
apply, where, and what checks them. It restates no number: they are in `library/ai-seo-limits.md`, and the
scripts read them from there.

## When

- **Articles:** `ebs-discoverability` at R4 (collection), E2 (verification), B1 (generation from locked
  text), per `ebs-article-system/library/pipeline-steps.md`. Never piecemeal.
- **Case studies and pages:** `ebs-discoverability` standalone, before the copy locks.
- **Before a title or keyword settles, anywhere:** `intake/entity-health.md`, then the article system's
  `check_keyword.py check`.

## What applies

| Concern | Part | The rule | Checked by |
|---|---|---|---|
| Title, meta, H1, slug | SEO | `ai-seo-limits.md` § SEO | `article_health.py` MECHANICS · `check_case_copy.py` |
| One keyword, one page | SEO | article `content-map.md`; site `intake/entity-register.md` | `check_keyword.py` |
| Internal links | SEO | interlink obligations per hub | `article_health.py` |
| Fan-out coverage: the sub-questions answered | AEO GEO | the fan-out set in `article-map.md`; `disc/geo-content.md` | `article_health.py` |
| Answer blocks (how-to headings), question headings, paragraph shape | AEO | `ai-seo-limits.md` § AEO; `disc/geo-content.md` | `check_structure.py` · `article_health.py` |
| FAQ from real queries | AEO | AH5; at most 5 | `article_health.py` |
| Entities and terms | GEO | `disc/text-semantics.md`; the Class B bank | `article_health.py` SEMANTICS |
| Key references, citable specifics | GEO | `ai-seo-limits.md` § GEO; `trusted-sources.md` | `article_health.py`; `claim-verification` |
| Trust: byline, bio, reviewer | GEO | `disc/eeat-signals.md` | `article_health.py` TRUST (blockers) |
| Schema matches the visible page | SEO AEO | `disc/machine-signals.md` | `article_health.py` (JSON-LD mirror) |
| Images for search and answer engines | SEO AEO | article rule 24ah | `check_image_seo.py` |
| Freshness | SEO | `dateModified` only on a real change | review at republish |

`disc/` = `skills/ebs-discoverability/references/`. The full concept list is `library/ai-seo-map.md`.

## What writing hands back

- A live page's entities go into `intake/entity-register.md` at B3 (articles) or at publish (case studies).
- A site defect found while writing goes to `reports/site-problems-log.md`, never into the writing repo.
