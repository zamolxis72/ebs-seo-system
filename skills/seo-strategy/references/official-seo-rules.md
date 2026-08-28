# Official grounding for SEO strategy, verbatim

Sources: **[HSW]** google.com/search/howsearchworks (ranking results) · **[TD]** Debugging Search traffic drops (developers.google.com, 2025-12-10) · **[AIO]** Generative AI optimization guide (2026-07-10) · **[AH]** Ahrefs API v3 official metric definitions (via Ahrefs docs).

## 1. Google's five ranking signal families [HSW]

- **Meaning**: "we build language models to try to decipher how the relatively few words you enter into the search box match up to the most useful content available" — incl. spelling correction and a "sophisticated synonym system."
- **Relevance**: "The most basic signal that information is relevant is when content contains the same keywords as your search query." Plus "aggregated and anonymized interaction data."
- **Quality**: systems "identify signals that can help determine which content demonstrates expertise, authoritativeness, and trustworthiness. For example … if other prominent websites link or refer to the content."
- **Usability**: "When all other signals are relatively equal, content that people will find more accessible may perform better" (mobile-friendly, fast).
- **Context**: location, history, settings. Weighting varies by query: "when searching for current news topics, content freshness plays a bigger role than dictionary definitions."

Strategy consequence: portfolio decisions map to these families — relevance is content coverage, quality is authority/links/E-E-A-T, usability is technical, and the freshness weight is query-dependent (verify per SERP, don't assume).

## 2. AI-search continuity [AIO]

"From Google Search's perspective, optimizing for generative AI search is optimizing for the search experience, and thus still SEO." AI features run on core ranking (grounding/RAG) — a keyword strategy IS an AI-citation strategy. Measure via "the Generative AI performance report in Search Console."

## 3. Traffic-drop diagnosis (the maintenance half of strategy) [TD]

Official cause categories: **algorithmic update** ("there might not be anything fundamentally wrong with your content"; small position drops → "avoid making radical changes if your page is already performing well"; large drops → "self-assess your whole website overall (not just individual pages)"), **technical** (site-wide vs page-level; Crawl Stats + Page Indexing reports), **security** (Security Issues report), **spam** (Manual Actions report), **seasonality** ("check them on Google Trends to understand if the drop was only for your website or throughout the web"), **site moves** (weeks+ to reprocess).

Diagnostics: "If both impressions and clicks dropped, check the … most common reasons. If your impressions remain the same but your clicks drop, you might not be generating the best page title and snippet." · Use 16-month ranges to rule out seasonality; compare periods; "you shouldn't focus too much on your absolute position. Impressions and clicks are ultimately the measure of success." · Check the Data Anomalies page before panicking.

## 4. Ahrefs metric semantics [AH] — use metrics for what they measure

- **Difficulty (KD)**: "An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale." Top-10 entry, not #1.
- **Volume**: "average monthly number of searches … over the latest known 12 months." Averages hide seasonality — check `volume_monthly_history` for seasonal topics.
- **Traffic potential**: "The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for." → judge topics by TP, not volume; one page ranks for the whole cluster.
- **Parent topic**: "determines if you can rank for your target keyword while targeting a more general topic on your page instead." → dedupe the portfolio by parent topic to avoid cannibalization.
- **CPC**: "average price that advertisers pay for each ad click … in USD cents" → commercial-value proxy; divide by 100 for dollars.
- **SERP features** per keyword (incl. `ai_overview`, `question`/PAA) and **serp-overview** (who ranks: position, DR, page traffic) — the composition read: high-DR .gov/institutional domination means the realistic win is AI citation/PAA, not position 1; commercial winners at modest DR mean the ranking is winnable.
- Traffic estimates are estimates; Ahrefs' own rater docs note traffic data "is not related to … reputation." Use GSC as ground truth for your own site.

## 5. Evidence discipline (suite rule)

Every number in a strategy deliverable is either pulled live from a named tool, quoted from GSC, or flagged "unvalidated — requires keyword data." SERP claims (who ranks, AI Overview presence) must come from a live check, dated — SERPs and PAA are rotating pools, so snapshots are labeled as snapshots.
