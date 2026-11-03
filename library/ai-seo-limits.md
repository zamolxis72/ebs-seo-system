# AI SEO limits

The measurable limits for every EBS surface (articles, case studies, service and industry pages), in one place.
**AI SEO** is the umbrella term. It has three parts, and each limit sits in exactly one of them:

| Part | The question it answers | Where it is won |
|---|---|---|
| **SEO** | Can the page be found and ranked in classic search? | tags, URL, speed, links, keyword ownership |
| **AEO** (answer engine optimization) | Can a passage be lifted as *the* direct answer (featured snippet, AI Overview, voice)? | answer blocks, FAQ, paragraph shape, visible content |
| **GEO** (generative engine optimization) | Will ChatGPT, Perplexity or Gemini cite EBS as a source? | sources, citable specifics, entities, trust |

This file holds the **numbers**. The method that produces a passing page stays in `ebs-discoverability`
(its four layers) and `b2b-seo-audit` (site scope). Scripts read the numbers from the `## Machine values`
block at the bottom, so **a limit is changed here or nowhere**. A constant restated in a script is a fork.

Each limit is labelled with its **class**:
- **Official**: Google or web.dev states the number, quoted below.
- **Adaptation**: our own working number. Google gives no figure or says there is none. It's kept because it's cheap to check and guards against a known failure.

Origin: triage of the "Updated AEO limits" infographic (Apoorva Mathe, LinkedIn), 2026-11-03. The source is
uncited, so no row was adopted on its authority. Every row was checked against the official documentation
this repo already holds word for word, or fetched live on 2026-11-03 (marked below).

## SEO: found and ranked

| Limit | Value | Class | Enforced by | Why |
|---|---|---|---|---|
| SERP title | ≤ 60 characters **including** ` \| EBS Integrator` (17 characters) | Adaptation | `article_health.py` · `check_case_copy.py` | Google: "there's no limit on how long a `<title>` element can be", but it is "truncated … typically to fit the device width" (title-link doc, fetched 2026-11-03). 60 keeps the brand visible. |
| Meta description | 120–155 characters | Adaptation | `article_health.py` · `check_case_copy.py` | Google: "There's no limit on how long a meta description can be, but the snippet is truncated" (`google-text-rules.md`). 155 avoids the cut on desktop, 120 avoids wasting the space. Decided 2026-11-03, replacing 120–160 and 150–160. |
| H1 | exactly 1 | Official | `article_health.py` | One dominant title matching `<title>` (`text-semantics.md` rule 5). |
| Slug | lowercase, no spaces, no year, ≤ 60 characters, as short as stays clear | Adaptation | `article_health.py` | The infographic's 50–75 sets a *minimum*, which forces long URLs. Rejected. |
| Internal links (body) | at least 2, target 3+ | Adaptation | `article_health.py` | Orphan and under-linked pages are an audit finding (`b2b-seo-audit` §3). No upper cap: links follow the reader, not a quota. |
| Primary keyword | one per page, one page per keyword | Official (cannibalization) | `content-map.md` (articles) · `intake/entity-register.md` | Ownership decided there, never counted on the page. |
| Secondary keywords | no count | n/a | `content-map.md` | Replaced by entity coverage (`text-semantics.md`). |
| Core Web Vitals | LCP ≤ 2.5 s · INP ≤ 200 ms · CLS ≤ 0.1, at the 75th percentile of page loads, mobile and desktop | Official | `b2b-seo-audit` (site scope, live pages) | web.dev/articles/vitals, fetched 2026-11-03. Not scriptable per draft. |
| Structured data | only types whose content is visible on the page; no count | Official | `article_health.py` (JSON-LD mirror) · `machine-signals.md` | The infographic's "1–3 per page" isn't a Google rule. The real rule is that markup must match what's visible. |
| Freshness | `dateModified` moves only on a substantive change; every live page is **reviewed** at least every 90 days | Adaptation | not tracked yet (no script reads the review dates) | Google lists "changing the date of pages to make them seem fresh when the content has not substantially changed" as a warning sign (`google-eeat-rules.md`). A review that changes nothing changes no date. |
| Backlinks · anchor text | monitored, never a quota: exact-match anchors under ~10% of referring anchors is the alert line | Adaptation | `seo-strategy` (AH7) | Off-page. A per-month link target invites buying links. |

## AEO: lifted as the answer

| Limit | Value | Class | Enforced by | Why |
|---|---|---|---|---|
| Answer block | the first paragraph under the H1 (the lede, still at most two sentences and citing nothing) and under each question heading is 40–60 words | Adaptation | `article_health.py` (lede) · `check_structure.py` (question headings, how-to) | The how-to spec already used 40–60 (`article-types.md` § How-to structure, 2026-10-20); the number now lives here and covers every type's lede. Makes `geo-content.md`'s "1–3 sentence direct answer" measurable. |
| Paragraph length | ≤ 75 words per body paragraph | Adaptation | `article_health.py` · `check_structure.py` | The number is rule 24ad's (plain English, 2026-10-28); it now lives here. The infographic's "2–4 lines" depends on screen width, so we count words instead. A self-contained passage lifts cleanly. One-line paragraphs stay allowed (voice). |
| FAQ | real queries decide which questions go in (AH5, each with volume and date); at most 5 | Adaptation | `article_health.py` · `pipeline-steps.md` §6 | Decided 2026-11-03. **Google retired FAQ rich results** ("no longer shown in Google Search results", FAQPage doc, 2026-06-15, fetched 2026-11-03). The FAQ is there for readers and for answer engines that read FAQPage (Perplexity, `ai-visibility.md`), not for a Google rich result. |
| Question headings | checked, not preferred | Adaptation | `pipeline-steps.md` §6 | Real question data decides. Not every H2 becomes a question. |
| Visibility | answer content is visible without a click (no tabs or accordions) | Official | `machine-signals.md` | "Make sure content is immediately visible on the page to a human" (`google-text-rules.md`). |

## GEO: cited as a source

| Limit | Value | Class | Enforced by | Why |
|---|---|---|---|---|
| Key references | 2–4 primary sources from `trusted-sources.md`, each named with its evidence; a brief's `evidence-budget: off` lifts the cap | Adaptation | `article_health.py` · `eeat-profiles.md` floors | The cap is rule 24ac's (2026-10-28): cite few, prove with what you name. The infographic's "2–5" lands in the same place. |
| Citable specifics | sourced numbers, named provisions, dates | judged | `geo-content.md` · `claim-verification` | No count. A count would reward padding. |
| Entity coverage | the terms a complete answer is expected to hold, in load-bearing positions | judged | `text-semantics.md` · `article_health.py` (SEMANTICS) | Replaces keyword density (see Rejected). |
| Trust | byline, author bio, named reviewer per the YMYL profile | Official (rater guidelines) | `article_health.py` (TRUST, blockers) · `eeat-signals.md` | |

## Rejected: do not add back

| Infographic row | Why not |
|---|---|
| Keyword density 0.5–1.5% | Google: stuffing "is against Google's spam policies" and "language matching systems … understand how your page relates to many queries, even if you don't explicitly use the exact terms." Article A0 passed a keyword count while missing its central term. |
| Content length 800–2,500 words | Google: "there's no magical word count target". Length is a craft rule, set per article type (rule 17a, `article-types.md`). |
| Sentence length 8–16 words | Already covered, better: rule 24ad sets an *average* of 10–15 with none over 25, and the voice needs varied sentence length (variation ≥ 0.35). A fixed 8–16 per sentence would flatten it. Not restated here; it's a craft rule. |
| H2 3–8 · H3 5–15 per page | Structure follows the argument and the element map, not a count. H2 count is visible in the monitor's DISTRIBUTION. |
| URL 50–75 characters | Sets a minimum length. See Slug. |
| Page load < 2.5 s | Repeats LCP under a vaguer name. |
| Voice answer 20–40 words | No primary source. The 40–60 answer block covers it. |
| Update every 30–90 days | As a publishing calendar it creates fake freshness: a date moved without a substantive change. Kept only as a review cadence, see Freshness. |
| Backlinks 5–20 per month | A quota, not a limit. Monitored under SEO, never targeted. |

## Machine values

Read by `ebs-article-system/scripts/ai_seo_limits.py` (used by `article_health.py` and `check_structure.py`) and
`ebs-case-study-system/scripts/check_case_copy.py`.
Edit the table above and this block in the same commit.

```json
{
  "version": "2026-11-03",
  "seo": {
    "title_max_with_suffix": 60,
    "title_suffix": " | EBS Integrator",
    "meta_min": 120,
    "meta_max": 155,
    "h1_count": 1,
    "slug_max": 60,
    "internal_links_min": 2,
    "internal_links_target": 3
  },
  "aeo": {
    "answer_block_words": [40, 60],
    "paragraph_words_max": 75,
    "faq_max": 5
  },
  "geo": {
    "key_references": [2, 4]
  }
}
```
