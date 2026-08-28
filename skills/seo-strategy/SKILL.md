---
name: seo-strategy
description: Build and maintain the search strategy layer — keyword portfolio construction, SERP composition analysis, prioritization math, competitive gaps, and rank/AI-citation measurement — grounded in Google's official ranking documentation and Ahrefs' official metric definitions (verbatim in the bundled reference). Use whenever the user mentions keyword research, keyword strategy, SERP analysis, competitor SEO analysis, prioritizing keywords, SEO roadmap, when content-strategy needs demand and winnability evidence (its step 3), or when the article pipeline's Step 1 keyword hypothesis needs real volumes and KD. Traffic-drop and not-ranking DIAGNOSIS belongs to b2b-seo-audit (this skill supplies the demand/SERP-shift evidence when the audit asks). Uses Ahrefs tools when connected; never invents metrics — every number is pulled live, quoted from Search Console, or flagged unvalidated.
---

# SEO Strategy (demand, competition, measurement)

**First read `references/official-seo-rules.md`** — Google's five ranking signal families, the official traffic-drop taxonomy, and Ahrefs' exact metric semantics. Two laws govern everything: (1) evidence discipline — no invented numbers, dated snapshots, tools named; (2) AI continuity — "optimizing for generative AI search … is still SEO," so this one strategy serves rankings and AI citations together.

## Mode A: Portfolio construction (default)

### 1. Seed and expand

Start from content-strategy's cohorts and topics (or gather them — audience before keywords). Expand seeds via keyword tooling (Ahrefs `keywords-explorer-*`: matching terms, related terms, search suggestions) and observable evidence (PAA pools, autocomplete). Without tooling, build the qualitative portfolio and mark every demand cell "unvalidated — requires keyword data."

### 2. Score with metrics used correctly (per the reference semantics)

- Judge topics by **traffic potential** (what the #1 page earns from the whole cluster), not raw volume
- Dedupe by **parent topic** — two keywords sharing a parent get one page, not two (cannibalization guard)
- Read **KD** as top-10 entry cost, weighed against the site's actual authority (site-explorer DR/backlinks when available)
- Use **CPC** as commercial-value proxy (in dollars — Ahrefs returns cents)
- Check **seasonality** via monthly history for time-sensitive topics

### 3. Read the SERP, not just the metrics

For every priority keyword, pull the live SERP (engine pull AH3's first half — `library/ahrefs-engine.md` — or a search): who ranks (DR, page type), which features show (`ai_overview`, PAA, local pack), and what format wins. Classify the realistic win: **rankable** (commercial/modest-DR winners), **citation play** (high-DR institutional domination — target the AI Overview/PAA slot), or **local play** (local pack). Date every SERP snapshot; PAA and AI Overviews are rotating pools.

### 4. Prioritize with transparent math

Score = f(traffic potential, winnability, commercial intent, strategic fit) — show the formula and the inputs so the user can re-weight. Output tiers: quick wins (low KD + intent), strategic builds (high TP, needs authority), citation plays, and declined keywords with reasons (wrong intent, cannibalization, unwinnable + no citation slot). Map each keyword to a page — existing (optimize) or planned (route to content-strategy).

### 5. Measurement design

Per keyword tier: rank tracking cadence, GSC queries/pages baselines, the **Generative AI performance report** for AI visibility, AI-citation spot checks (Brand Radar if connected), and the business metric. "Impressions and clicks are ultimately the measure of success" — position is a diagnostic, not the goal.

## Mode B: Diagnosis (rankings/traffic dropped)

Follow the official taxonomy in order, cheapest checks first: (1) Data anomaly (Search Console data issues page), (2) seasonality (16-month range + Google Trends: is the drop web-wide?), (3) technical (Crawl Stats, Page Indexing, site-wide vs page-group via the Pages table), (4) security/spam (Security Issues, Manual Actions reports), (5) algorithmic update (check update timing; small position drop on a performing page → officially, don't make radical changes; large drop → whole-site people-first self-assessment, route to ebs-discoverability's trust layer), (6) SERP change (new AI Overview/feature absorbing clicks — impressions stable + clicks down also implicates title/snippet, route to ebs-discoverability's semantics layer). Deliver: diagnosis with evidence, severity, owner, and fix route.

## Output format

Portfolio mode: (1) scored keyword table with source-and-date column per metric, (2) SERP classification per priority keyword (rankable/citation/local + evidence), (3) keyword→page map with cannibalization check, (4) prioritized tiers with the scoring formula shown, (5) declined list with reasons, (6) measurement plan. Diagnosis mode: cause, evidence, fix, owner, recheck date. Label throughout: Official rule / Tool evidence (dated) / Judgment.

## Composition

**content-strategy** owns what to publish and why (this skill is its evidence engine — step 3); **ebs-discoverability** owns page-level execution once a keyword is assigned (citability layer) and executes technical fixes found in diagnosis (machine layer); **claim-verification** checks any market claim that ends up in client-facing strategy docs. This skill owns the numbers, the SERPs, and the monitoring loop.
