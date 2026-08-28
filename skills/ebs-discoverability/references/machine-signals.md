# machine-signals — instrument layer (absorbed 2026-08-28, was a standalone skill)

> One layer of ebs-discoverability. Former routing contract, first 200 chars: Implement and audit the machine-readable layer of an article or page — Article/ProfilePage schema, author markup, byline dates, structured-data policy compliance, DOM visibility, and crawler access fo…


# Machine Signals (the machine-readable layer)

**First read `official-machine-rules.md`** — verbatim rules from Google, OpenAI, Perplexity, and Anthropic docs, including the crawler matrix and an explicit list of things NOT officially documented (never assert those as fact). Every recommendation cites its source doc.

## The one law above all [SP]

**Markup must mirror visible content.** "Don't mark up content that is not visible to readers of the page"; structured data "must be a true representation of the page content." Deceptive markup (fake reviews, impersonation) risks manual actions. So this skill never adds a signal the page doesn't visibly carry — it either surfaces the visible element first or flags it as missing. This is the technical twin of eeat-signals' anti-fabrication rule.

## Workflow

### 1. Crawler access audit (who can even see the page?)

Check robots.txt, CDN/WAF rules, and meta robots against the visibility matrix in the reference: `Googlebot` (Search + AI Overviews), `Google-Extended` (Gemini apps + Vertex grounding — blocking it removes Gemini visibility but not AI Overviews), `OAI-SearchBot` (ChatGPT search answers), `PerplexityBot`, `Claude-SearchBot`. Distinguish training bots (`GPTBot`, `ClaudeBot`) from search/answer bots — blocking training is a policy choice that mostly doesn't cost answer visibility, except Google-Extended which bundles both. Also check: `nosnippet`/`data-nosnippet`/`max-snippet` (suppress snippets and AI display), 15MB crawl limit, and that bot-protection isn't serving challenges to documented crawler IPs.

### 2. DOM visibility audit (is the content in the served/rendered HTML?)

Google renders JavaScript (headless Chromium) but "does not interact with your page" — content requiring clicks, tabs, or scroll events is invisible; other vendors document no rendering at all, so assume worse. Verify the main content, FAQ answers, and tables exist as text in the HTML response. Anything hidden behind interaction goes back to text-semantics/design to surface.

### 3. Author signal chain (the machine-readable E-E-A-T)

Build the chain: visible byline → `author` markup (`Person`, name only in `author.name`, one field per author) → `author.url` pointing to a bio page → bio page marked up as `ProfilePage` (`mainEntity`, `description` = credential, `sameAs` → state bar / LinkedIn / directories) → external profiles that actually corroborate. Each link in the chain must exist visibly before it's marked up; missing links are CLIENT INPUT NEEDED (names, bar numbers, bio URLs come from eeat-signals' list).

### 4. Date signals

Visible, prominently placed, labeled date ("Published" / "Last updated") + `datePublished`/`dateModified` in ISO 8601 with timezone, **matching the visible date exactly**. No future dates; the date describes the page, not the events in it; minimize stray dates on the page. Never freshen a date without substantive content change (helpful-content warning sign).

### 5. Schema completeness

`Article` (or `BlogPosting`) with headline (concise), images (16x9/4x3/1x1, ≥50K px), dates, authors per best practices; `FAQPage` only if visible Q&A exists; `Organization`/`LegalService` for the responsible entity. "The more recommended properties … the higher quality" — but completeness never overrides the mirror law. Validate (Rich Results Test) and note: rich results are never guaranteed.

## Paste-ready examples

`schema-examples.md` — the EBS-shaped JSON-LD blocks (absorbed 2026-08-25 from the
stock schema skill, which lost the comparison on everything except having examples): the article
`@graph` (Article + Breadcrumb + Organization + FAQ, `@id`-linked; author stays the Organization
until a visible byline exists), the author chain, the `Service` type for hub pages (never
`Product`/`Offer`/ratings — engagements have no visible prices or ratings to mirror), and the
Next.js server-render rule. Built at packaging from locked text only; every `[BRACKET]` is a
confirm, never a guess.

## Output format

| Signal | Source doc | Status | Visible counterpart present? | Fix |
|---|---|---|---|---|

Then: (1) crawler access matrix for this site (per engine: visible/blocked/unknown), (2) the author-chain diagram with missing links marked, (3) ready-to-paste JSON-LD for everything whose visible counterpart exists, (4) CLIENT INPUT NEEDED list, (5) items explicitly not verifiable without site access (Search Console GenAI toggle, robots.txt, CDN behavior).

## Composition

**text-semantics** owns the words and their visible arrangement; this skill verifies and mirrors them. **eeat-signals** decides which trust signals should exist; this skill encodes the ones that do. **geo-content** consumes the access matrix in its eligibility gate. **claim-verification** has verified any factual claim before it gets marked up.
