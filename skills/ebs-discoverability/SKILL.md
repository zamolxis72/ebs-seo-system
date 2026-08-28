---
name: ebs-discoverability
description: "The EBS Integrator search and answer-engine layer. Owns one job for any EBS surface, article, service page, industry hub or case study: can it be FOUND by search and CITED by answer engines, to EBS's standard. Plugs into ebs-article-builder (project-scoped in ebs-article-system — open that repo to run the pipeline) at three named steps — R4 (collection), E2 (verification), B1 (generation from locked text) — per the canonical ladder in ebs-article-system/library/pipeline-steps.md, and standalone on any published or draft surface. Use for \"run the SEO pass\", \"optimise this for search\", \"will AI cite this\", \"AEO\", \"GEO\", \"schema for this page\", \"does this rank\", \"is this YMYL\", \"byline and trust signals\", \"entity coverage\", \"why isn't this being cited\". It is THE search-execution skill: its four instrument layers — text-semantics (arrangement), geo-content (citability), machine-signals (schema/crawler access), eeat-signals (E-E-A-T and the YMYL bar) — are bundled references inside it (absorbed 2026-08-28; formerly standalone skills), read per pass and never run piecemeal; it routes to b2b-seo-audit at site scope, and it supplies the EBS-specific logic the official references cannot carry, inheriting voice from ebs-integrator-communication-style, source tiers from the article workstream's trusted-sources.md, keyword ownership from content-map.md, and stat classes from the Class S/F ledger. NOT portfolio or demand strategy (seo-strategy for demand, content-strategy for the publishing plan). NOT fact verification (claim-verification). NOT section-coverage auditing (the JTBD wheels, which are a separate instrument and not a pipeline step). NOT writing or editing the copy (communication-style for editorial, copywriting for conversion, b2b-copy-editing for the sweeps)."
metadata:
  version: 1.0.0
---

# EBS Discoverability

One job: **can this be found by search, and cited by answer engines, to EBS's standard.**

That job was previously split across four thin, brand-neutral skills plus an on-page auditor, each a
fragment, none of them knowing anything about EBS. Running one of them and calling the step done is
the failure this skill exists to prevent, and it happened: article A0 had its search pass "completed"
on a check of title lengths and keyword counts, while the term **AI maturity** was missing from a
piece whose entire argument is a maturity ladder. The consolidation completed 2026-08-28: the four
instruments are now this skill's own reference layers (`references/<name>.md`, each carrying the
official documentation verbatim), so a piecemeal run is structurally impossible; the auditor stays
a sibling skill, entered at site scope only.

**This file carries no generic best practice.** The instruments own that, and they are read, not
restated. What lives here is the sequence, the EBS adaptation, and the standing rules that generic
advice cannot know.

## The instruments (read them, don't restate them)

| Layer | Reference (bundled here) | The question it answers |
|---|---|---|
| 1. Semantics | `references/text-semantics.md` | Does the piece carry the terms and entities a comprehensive answer is expected to hold, in load-bearing positions? |
| 2. Citability | `references/geo-content.md` | Would an answer engine lift this, and what would it cite EBS **for**? |
| 3. Machine | `references/machine-signals.md` (+ schema examples, official machine rules) | Can a crawler and an extractor parse it: schema, tables, headings, access? |
| 4. Trust | `references/eeat-signals.md` (+ the rater guidelines verbatim) | Would a quality rater trust it, and is the bar raised because the topic is YMYL? |
| 0. Mechanics | the surface's monitor · `text-semantics` | Title, meta, headings, internal links — MEASURED by script (for articles, `article_health.py`'s MECHANICS group); arrangement fixes are `text-semantics`'s, wording is the canon's. `b2b-seo-audit` enters at SITE scope only (live surfaces: crawl, indexation, CWV — findings to `ebs-seo-system`) |

Run mechanics first because it is scripted and free, then semantics, citability, machine, trust. Trust last
because its findings are usually the ones that need a human input rather than an edit.

## The EBS adaptation, which is why this skill exists

### Inherit, never re-decide

- **Voice** is `ebs-integrator-communication-style`. Any wording this pass proposes obeys it: no
  em-dashes, no banned words, sentence case, second person, no invented evidence. A keyword is never
  a reason to break the canon. If an entity cannot be added in EBS voice, it does not go in.
- **Sources** follow the article workstream's `library/trusted-sources.md`, which is the system's
  single source authority: Part 1 tiers where research may look, Part 2 says what can anchor a
  decision-grade claim per industry and carries the volatility traps. An instrument's bundled source
  list is a suggestion layered under it, never over it.
- **Keyword ownership** is `library/content-map.md`. This pass never claims a keyword; that was
  settled at brief time. It works inside the claim already registered.
- **Stat reuse** is the Class S/F ledger. If this pass wants to add a statistic, check the ledger
  first: a Class S stat spent on another article gets a link to that article, not a second hero use.

### The Class B semantic keyword bank (in-article layer, indexed in content-map.md)

The model is hub-and-spoke with one exclusivity boundary on each side. **Primaries are exclusive**:
one parent keyword per article, title and H1, never shared (Rule 1, enforced by `check_keyword.py`).
**Bank terms are the opposite**: secondary, semantic and long-tail vocabulary indexed as the
**Class B ledger in `content-map.md`**, attached to L1/L2 areas, and **reuse across the cluster's
articles is expected** — that recurrence is how topical authority compounds.

This pass works the bank in both directions:

- **Consume:** at E2, read the area's bank and map unused terms into the draft where they fit
  naturally — H2s and H3s only where the section genuinely is about the term, body and FAQ answers
  elsewhere; definitions and question-shaped headings go to the highest-intent terms (the snippet
  and AI-Overview positions). Canon voice always wins: a term that cannot be used naturally stays
  unused. One deliberate use beats three forced ones. Update the row's "Used by" column.
- **Feed:** when the measured pull (rule 9) surfaces new qualifying terms, file them into the bank
  in the same session, through its entry filters (attaches to a registered area · not any
  article's primary · distinctive, no generic tokens · TYPED: keyword / long-tail / question /
  entity, the reuse contract · provenance recorded and dated). A term used
  in an article without a bank row is drift.

The bank renders into the Obsidian vault automatically: `build_cluster_graph.py` writes each area's
bank table into that area's keyword note, so the L1/L2 view shows both the exclusive claims (nodes)
and the shared vocabulary (in the note), without bank terms ever masquerading as protected keywords
in the graph.

### Two different clusterings, and only one of them is this skill's

The word "clustering" means two unrelated things in this system and conflating them is why the
intra-article layer went unrun for so long:

- **Portfolio clustering** decides *which surface owns which keyword*, hub by hub. It lives in
  `content-map.md`, is enforced by `check_keyword.py`, and is settled before a word is written.
  Not this skill.
- **Intra-article clustering** asks whether *this piece* carries the co-occurring terms and named
  entities that make it read as topically complete. Counting keyword occurrences is not this. It is
  layer 1 above, and it is this skill's.

### EBS industries set the entity expectations

The entity cluster a comprehensive answer needs is domain-specific. For EBS that means knowing the
real authorities per hub, and they are not generic: fintech answers are expected to touch EBA, ECB,
PSD2, DORA; e-gov answers touch the national digitalisation strategy and the relevant ministry;
anything AI touches the AI Act and its current dates. An article that argues well and names none of
its domain's authorities reads as an opinion piece to both a rater and a model.

### Local evidence is Moldova

Where a piece needs a local layer, the local layer is **Moldova**, not Romania. Romania enters only
on explicit request. EU-wide data is fine as the EU layer; a Romanian cut of it is not the local one.

## AI visibility: the ladder and the access layer

`references/ai-visibility.md` (absorbed 2026-08-25 from the stock ai-seo skill, wrapped here rather
than adopted — it has no EBS rules, no measured monitor, no ownership concept). It adds the two
things this layer lacked: the **visibility ladder** (retrieved → cited → mentioned → recommended,
plus recommended-against — citation is earned by content, recommendation by web-wide consensus, and
a self-promotional listicle can hand the model your competitor research: 69% of such citations
recommended competitors in the 2026 Lily Ray study), and the **machine-access layer** (AI-crawler
reachability, content in initial HTML, llms.txt — site-level, findings route to `ebs-seo-system`).
Google's own guardrails come with it as rules: never chunk content "for AI", never write separate
AI-targeted variants. Tooling is Ahrefs only.

## Standing EBS rules this pass enforces

Each of these was learned the expensive way. They are rules, not suggestions.

1. **A framework EBS authored ships with a name.** The single most valuable thing an EBS piece can
   own is the asset that can only be attributed to EBS. An unnamed framework means a model cites the
   third-party statistics around it and treats EBS as a conduit. Name it, in the sentence directly
   above it.
2. **An EBS-authored framework never ships as an image.** Tables, ladders and matrices go to the CMS
   as real HTML with `<caption>` and `th scope`. A framework rendered as an SVG or a PNG is invisible
   to every retriever, and the piece's uniqueness collapses to nothing.
3. **Never strip sample sizes in a concision pass.** In-sentence attribution with the n disclosed
   ("in a 2,500-person survey run by GoTo, 62% of respondents...") is a complete, liftable unit and
   is usually the strongest property an EBS piece has. Cutting the n to save words is the single most
   damaging edit available.
4. **Name every source in-sentence, not only in the footnote.** A lifted passage does not carry the
   reference list with it, so a statistic sourced only at `[4]` travels as an unattributed number.
5. **Name the commercial interest, including our own.** EBS names GoTo's and ManageEngine's interest
   in-sentence. A piece that does that and then presents its own framework and links its own service
   page without disclosing that EBS sells the service has an asymmetry a rater notices.
6. **Every reference carries a URL to the primary.** A regulator citation with no link is
   unverifiable to a crawler, an assistant and a reader alike.
7. **Mark up only what the page visibly shows.** Never an author who appears as a quoted source,
   never a cut FAQ, never a claim the page does not make.
8. **Check the feature still exists before optimising for it.** FAQ rich results were deprecated in
   May 2026 and their documentation removed. Ship valid schema, but never shape an editorial decision
   around a dead feature.
9. **Measure the entity cluster; never ship it reasoned-only.** When Ahrefs is connected, pull
   engine pull AH2 (`library/ahrefs-engine.md` in this repo — never restate its endpoint) for the primary keyword: that is
   what top-ranking pages actually discuss, against which the reasoned list is checked. The first
   time this was done (A0, 2026-08-24) the reasoned list was partly unsupported (hallucination was
   asserted as high-co-occurrence and is not) and missing the biggest measured terms (industrial
   revolution at 127k, ai agents at 48k, large language models at 32k). Then label every proposed
   addition as one of two kinds, because they are argued differently: an **entity-gap fix** (the
   data shows top pages discuss it and we don't) or a **differentiation choice** (deliberately
   absent from the cluster, our declared drift — like naming the EBS AI maturity ladder). Both are
   legitimate. Conflating them produces false SEO justifications for strategy choices and vice versa.
10. **A difficulty figure is dated, and a decision resting on it expires with it.** KD moves: the
   `ai maturity model` area was ruled out of reach at KD 57 and measured four days later at KD 22.
   Before acting on any recorded "out of reach" or "winnable" verdict, re-pull the number, and when
   it moved materially, flag the row in `content-map.md` rather than silently re-deciding.
11. **Expect an AI Overview on everything.** In the first measured cluster, all eight keywords
   carried `ai_overview` + `ai_overview_sitelink`. For EBS's question-shaped queries the AI-served
   answer is the normal case, so the citability layer is first-class, never a finishing touch.

## The signing rule (trust, and why it is not optional)

Most EBS decision-grade content is YMYL-adjacent the moment it cites a regulation or advises on
spend. The guidelines are blunt about the consequence: a single Low quality attribute is enough, and
no reputation compensates for inadequate E-E-A-T on a page stating regulatory obligations.

**An unsigned page is that attribute.** Sourcing rigour earns nothing while nobody has signed it.
So this pass always reports byline state, and never treats immaculate citations as a substitute.

Never fabricate a credential, an author, an experience or a review artifact. Anything requiring a
real-world fact EBS must supply is output as a named input with its exact shape, never invented.

## Which layer owns which check

Getting this wrong is how an audit misclassifies its own findings. Two real slips from the first
full run: a **SERP title** rewrite was filed under citability when a title is on-page metadata, and
**three accuracy corrections** were filed under SEO when they are evidence. Neither changed the
article; both made the audit describe itself wrongly.

| Question | Layer | Not to be confused with |
|---|---|---|
| Can a passage be lifted out and still make sense, and still credit us? | citability (`geo-content`) | the title and description, which are on-page metadata |
| Does the piece carry the terms a comprehensive answer holds? | semantics (`text-semantics`) | portfolio keyword ownership, settled at brief time |
| Title, description, headings, internal links, slug | mechanics (measured by the monitor; arrangement fixes to `text-semantics`; `b2b-seo-audit` only at site scope) | citability, which is about the body |
| Schema, table semantics, heading tree, crawler access | machine (`machine-signals`) | anything about wording |
| Is the claim true, and does its source resolve? | evidence (`claim-verification`) | SEO. A corrected fact is an evidence fix |
| Would a rater trust it, and is it signed? | trust (`eeat-signals`) | evidence. Rigorous sourcing on an unsigned page still fails |

**The test when a finding is ambiguous:** name the skill that would have to fix it. That is the layer
it belongs to, and it is also the group it appears under in the health monitor.

## Output

One record per run, into the surface's `review/` folder:

1. **Findings per layer**, each with its exact location and a specific fix, ordered by value.
2. **Word cost or saving per fix.** EBS pieces run to a length tier, and an entity pass that silently
   inflates a draft past its tier has traded one constraint for another. State the net.
3. **Paste-ready artifacts** for packaging: JSON-LD, semantic table HTML, meta description; the OG
   copy tags come from `ebs-og-meta`, which owns that craft (ceilings, alt template) — route to it,
   never restate it. These go to `cms-paste.md`, never into the draft.
4. **Named inputs EBS must supply**, especially byline and framework provenance.
5. **What was not covered**, explicitly. A part-run is recorded as part-done, never as complete.

## Boundaries

- **Demand and portfolio** are `seo-strategy` (which keywords have demand) and `content-strategy`
  (what to publish and in what order). Both are upstream of this and settled at brief time.
- **Fact verification** is `claim-verification`. It checks whether a claim is true; this pass checks
  whether a true claim can be found and cited. Note the gap between them, because it is real: claim
  verification checks figures, not the prose wrapping them, and three accuracy defects on A0 lived in
  that gap.
- **Section coverage** is the JTBD wheels. They are a separate instrument, used when coverage
  confidence is worth the ceremony, and deliberately **not** a pipeline step.
- **Writing and editing** belong to `ebs-integrator-communication-style` (editorial),
  `ebs-integrator-copywriting` (conversion) and `b2b-copy-editing` (the craft sweeps). This pass
  proposes wording only as a fix to a finding, in canon voice, and hands it back.
- **Site-level health** (sitemaps, crawl errors, duplicate slugs, Core Web Vitals) is
  `b2b-seo-audit` at site scope, and findings go to `ebs-seo-system/reports/site-problems-log.md`,
  which owns them.
