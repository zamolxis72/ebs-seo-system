# AI SEO map

Every search concept the EBS system handles, in one table: which part of AI SEO it belongs to, where its
research is held, where the EBS rule lives, what checks it, and which served system applies it. Built
2026-11-03 from the "How SEO is viewed" checklist (Emilia Möller, LinkedIn), checked against this repo and its
consumers. Update a row when its rule, check or research moves.

**This repo is the AI SEO system: it serves the others.** It owns the research and the rules; the systems that
make things apply them through one service file each:

| Served system | Service file | Who reads it |
|---|---|---|
| **Writing**: articles, case studies, page copy | `services/writing.md` | `ebs-article-system`, `ebs-case-study-system`, the copy skills |
| **Auditing**: live site health | `services/auditing.md` | this repo's own audits (`b2b-seo-audit`), findings to `reports/site-problems-log.md` |
| **Web design**: templates, components, rendering | `services/web-design.md` | `ebs-web-components`, `ebs-website-system`, front end via the board |

The numbers live in `library/ai-seo-limits.md`; this map never restates them.

## How to read a row

- **Part:** SEO (found and ranked) · AEO (lifted as the direct answer) · GEO (cited by a generative engine).
- **Research:** the official text held word for word. `—` = no official source exists; the rule is ours.
- **Checked by:** a script = enforced on every piece; *judged* = a skill's pass, no script; *audit* = checked
  only when a site audit runs; **none** = a gap.
- **Serves:** W writing · A auditing · D web design.

References are under `skills/`: `disc/` = `ebs-discoverability/references/`, `audit/` =
`b2b-seo-audit/references/`, `strat/` = `seo-strategy/references/`.

## The map

| Concept | Part | Research | EBS rule | Checked by | Serves | State |
|---|---|---|---|---|---|---|
| SEO / AEO / GEO, AIO | all | `disc/google-ai-search-rules.md`; KB `seo-aeo-geo/2026-08-19-seo-vs-aeo-vs-geo-comparison.md` | `ai-seo-limits.md` (the three parts); AIO = AI Overviews, below | — | W A D | covered |
| SXO (page experience) | SEO | `audit/official-site-rules.md` § Page experience | the six page-experience questions per template | *audit*; Core Web Vitals measured | A D | **rule new 2026-11-03; no audit run yet** |
| AI citations | GEO | `disc/ai-visibility.md`; `strat/official-seo-rules.md` §6 (Bing AI Performance) | `disc/geo-content.md` | AH6: `intake/snapshots/ai-citations-*.json` | W A | **baseline 2026-11-03: 1 citation (ChatGPT)** |
| Query fan-out coverage | AEO GEO | `disc/geo-content.md` (Google's fan-out mechanism); `disc/ai-visibility.md` (Ahrefs AI Overview study: the strongest on-page factor, r = 0.77) | answer the sub-questions a head question spawns; the fan-out set in each `article-map.md` | `article_health.py` (fan-out set) | W | covered; **the strongest measured factor** |
| Content structure | AEO | `disc/google-text-rules.md` | answer-first blocks, question headings, element map | `article_health.py`, `check_structure.py` | W D | covered |
| Passage indexing / ranking | AEO | `strat/official-seo-rules.md` §6 | every section self-contained, answer-first (`disc/geo-content.md`) | `check_structure.py` (answer blocks, paragraph length) | W | covered |
| Entity signals | GEO | `disc/text-semantics.md` (Google language matching) | entity coverage; `intake/entity-register.md` | `article_health.py` SEMANTICS; `build_entity_health.py` | W A | covered |
| E-E-A-T | GEO | `disc/google-eeat-rules.md` (rater guidelines) | `disc/eeat-signals.md`; article system `eeat-profiles.md` | `article_health.py` TRUST (blockers) | W | covered |
| Search intent | SEO | `strat/official-seo-rules.md` §1 (Meaning) | every brief declares `intent:` | brief status block | W | covered |
| Client-side / server-side rendering | SEO GEO | `audit/official-site-rules.md` § Rendering | text, links and schema in the first HTML response | *audit*; **none** in components | A D | **rule new 2026-11-03; P4 open** |
| Topic clusters | SEO | `disc/geo-content.md` (query fan-out rewards clusters) | hub model (article system `content-map.md`) | `check_keyword.py`, `check_arc.py` | W | covered |
| Internal linking | SEO | `strat/official-seo-rules.md` §6; `disc/google-text-rules.md` § Links and images | interlink obligations per hub | `article_health.py` (min 2, target 3) | W D | covered |
| Zero-click results | SEO AEO | — (measured) | `strat/official-seo-rules.md` §7 | each GSC snapshot read | A | **method new 2026-11-03** |
| Crawlability | SEO GEO | `disc/official-machine-rules.md` (robots, AI crawlers); `audit/official-site-rules.md` | `disc/machine-signals.md` | *audit*; `reports/site-problems-log.md` | A D | **written, no full audit run** |
| AI Overviews | AEO | `disc/google-ai-search-rules.md` | answer blocks; question set from real queries | `check_structure.py`; SERP `ai_overview` flag (AH1) | W | covered |
| Link building | SEO | `strat/official-seo-rules.md` §6 (link spam) | earn and qualify, never buy; AH7 anchor health | AH7 (not yet run) | A | **rule new; 2 of 13 board items done** |
| Schema markup | SEO AEO | `disc/official-machine-rules.md`, `disc/schema-examples.md` | only types matching visible content | `article_health.py` (JSON-LD mirror) | W D | **site: 1 of 17 board items done** |
| Featured snippets | AEO | `disc/google-text-rules.md` § Featured snippets | write the snippet by writing the page | **none** (not tracked) | W | rule covered, not measured |
| Semantic search | GEO | `disc/text-semantics.md` | Class B term bank (article system) | `article_health.py` SEMANTICS | W | covered |
| Submission (Bing, IndexNow) | GEO | `audit/official-site-rules.md` § Submission | Bing Webmaster Tools verified; IndexNow on publish | **none** | A D | **gap: neither set up** |
| Keyword density | — | `disc/google-eeat-rules.md` (stuffing is spam) | rejected (`ai-seo-limits.md` § Rejected) | — | W | rejected on purpose |

## Open gaps, in the order the 2026-11-03 baseline ranks them

1. **Submission:** Bing Webmaster Tools + IndexNow. ChatGPT is the one engine that cited us, and it draws on Bing.
2. **Live-site fixes already found:** P1, P8, P11 (on the board as `M7.gitlab` and `M7.rootdomain`).
3. **The first full site audit**, which is where SXO, rendering and crawlability get checked at all.
4. **Featured-snippet and zero-click tracking** in each snapshot read.
