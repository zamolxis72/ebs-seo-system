# AI visibility — the ladder, the platforms, the access layer

**Provenance.** Absorbed 2026-08-25 from the stock `ai-seo` skill (v2.4.0), wrapped under
`ebs-discoverability` rather than adopted as a skill: the stock skill has no EBS rules, no measured
monitor, and no keyword-ownership concept, so it can only ever be a reference layer under ours.
Tooling note: **Ahrefs only** — every Semrush mention in the source is dropped, we don't have it.
Every citation-share number in here is a **dated snapshot** (the source itself proves why: ChatGPT's
August 2026 retrieval change nearly wiped Reddit as a citation source within days). Check the date
before betting on any of them; verify against our own monitoring.

## The visibility ladder — the one strategic concept our system lacked

Being cited and being recommended are different outcomes governed by different systems:

| rung | means | governed by |
|---|---|---|
| 1 retrieved | the model read you while building the answer | crawlability, parseable structure |
| 2 cited | your page appears as a source | content usefulness: structure, statistics, clarity, freshness |
| 3 mentioned | your brand is named in the answer | entity recognition + how the web talks about you |
| 4 recommended | you are on the buyer's shortlist | **web-wide consensus** — reviews, forums, analysts, press — largely independent of your own content |

Plus the shadow rung: **recommended against** — on requirements-heavy prompts, models now name
products to avoid, with sources. Monitor the *framing* around mentions, not just the count.

**The self-promotional listicle risk, on record.** Lily Ray's 2026 study of 100 B2B "best
[category]" queries: self-promotional listicles earned 323 AI Overview citations, and in **69% of
them the answer recommended competitors instead** of the publishing brand — the model harvests your
competitor research and makes its recommendation from consensus, where incumbents win. Established
leaders get both outcomes; emerging brands get the citation and shape the category framing, not the
shortlist. **How this maps to EBS:** our architecture already avoids the trap — the hub sells and
the article informs, and articles never target the hub's commercial keywords — but the ladder still
rules any future "best X for Y" piece: for ground where EBS is not the consensus pick, weight
effort toward the off-site consensus surfaces, and set the expectation as citation-and-framing, not
shortlist.

**The test before any self-ranked piece:** if a model ignored everything on our domain, would the
rest of the web still put us on the shortlist? If not, that gap is the priority, and it is
`ebs-seo-system`'s ground, not an article's.

## Google's guardrails (their own AI-features guidance, absorbed as rules)

- **Never chunk content "for AI"** and never write separate AI-targeted variants — Google names
  this scaled-content-abuse territory. Our liftable 40–80w passages are ordinary good paragraphs,
  not AI-bait fragments; the moment a passage reads written-for-a-machine, it is off-canon anyway.
- **No special files or markup are required for Google AI Overviews** — AIO runs on core Search
  plus E-E-A-T. The extractable-structure work pays on the *other* engines (ChatGPT, Perplexity,
  Claude) and does not hurt Google.
- **The measured hierarchy (the evidence home — stated here once, pointed at everywhere else):**
  per Ahrefs' AI Overview study, fan-out query coverage is the strongest on-page factor (r=0.77,
  +161% citation likelihood) and word count has near-zero correlation (Spearman 0.04), so length
  is a craft rule, never a search one.
- **Fan-out is Google's own mechanism** — their AI generates concurrent related queries and
  retrieves for each, which is exactly why the fan-out set in `article-map.md` is measured from
  keyword data and checked by the monitor.

## Platform factors (dated snapshot, 2026; verify before relying)

| platform | index | what moves citation there |
|---|---|---|
| Google AIO | Google + E-E-A-T | schema, sourced citations in-content, topical clusters; only ~15% of AIO sources overlap the organic top 10 |
| ChatGPT | Bing-based | freshness (sub-30-day content cited ~3.2x more), domain authority, **content-answer fit** — matching how it structures answers |
| Perplexity | own + Google | FAQPage schema, public PDFs, self-contained paragraphs, publishing velocity |
| Copilot | Bing | Bing Webmaster Tools + IndexNow, sub-2s loads, LinkedIn/GitHub presence |
| Claude | Brave Search | factual density, named sources, dated statistics; verify presence at search.brave.com |

Princeton GEO study (KDD 2024), the sourced factor list: citing sources +40%, statistics +37%,
quotations +30%, authoritative tone +25%; **keyword stuffing −10%, it actively hurts**. Best
combination: fluency + statistics. These align with what the canon already mandates (every claim
earns a number, sources named in-sentence), which is why EBS articles need no separate "AI version".

## The machine-access layer (site-level; findings route to ebs-seo-system)

Two questions before any content optimization matters: can an AI crawler reach the page, and is the
content in the initial HTML? **Audited for ebs-integrator.com 2026-08-25:**

| check | state | verdict |
|---|---|---|
| content in initial HTML, no JS needed | article text present in raw fetch | **PASS** — the layer that matters most |
| AI crawlers allowed | robots.txt is allow-all; GPTBot UA fetch returned 200 | **PASS**, though no explicit AI-crawler stance is declared |
| sitemap | root 307s to `/en/sitemap.xml`, resolves, fresh lastmod | PASS, minor: robots.txt points at the root URL |
| llms.txt | **404** — locale middleware redirects even `/llms.txt` to `/en/llms.txt` | **GAP** — serving one needs a routing exception |
| llms-full.txt | same | same gap, lower priority |

Logged in `ebs-seo-system/reports/site-problems-log.md` — site health is that repo's ground, per
the boundary. Free scoring tools when acting on it: `npx is-agentic ebs-integrator.com`,
frase.io/tools/agent-readiness (both vendor tools; the checks are the value, not the pitch).

## Absorbed, parked, rejected

- **Absorbed:** the ladder + listicle risk · Google's guardrails · platform table (dated) ·
  machine-access checklist · Princeton GEO factors (sourced) · robots.txt AI-bot allowlist
  (GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, anthropic-ai, Google-Extended, Bingbot; CCBot
  blockable as training-only).
- **Parked, revisit on trigger:** `/pricing.md` (EBS sells engagements, no tiers — an
  `engagement-model.md` is the analogous idea if agent-mediated buying reaches services) · OKF
  bundles (v0.1, nothing reads them yet; its own skip-criteria apply) · the YouTube text-layer
  anatomy (until EBS produces video) · llms-full.txt (after llms.txt exists).
- **Rejected:** Semrush tooling (Ahrefs only) · third-party presence tactics as article work
  (Wikipedia, Reddit, review sites are `ebs-seo-system`/marketing ground, and the source's own
  volatility note is the argument: never concentrate in one surface) · every unsourced
  citation-share stat as a planning basis (snapshots, labeled).
