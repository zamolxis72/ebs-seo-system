# geo-content — instrument layer (absorbed 2026-08-28, was a standalone skill)

> One layer of ebs-discoverability. Former routing contract, first 200 chars: Optimize content for citation by AI answer engines — Google AI Overviews/AI Mode and Gemini (grounded in Google's official 2026 generative-AI optimization guide, quoted verbatim in the bundled referen…


# GEO Content (AI-search citability)

**First read `google-ai-search-rules.md`** — verbatim rules from Google's official AI-optimization guide (July 2026), including six officially debunked myths. Never recommend a debunked practice (llms.txt, special AI schema, mandatory chunking, inauthentic mentions) as if it were required; the reference's scope note separates Google rules from adaptation practices for other engines.

## The mechanism you're optimizing for

Google's AI features work by **grounding**: core Search ranking retrieves pages, then the model quotes and links the ones that support its answer. Plus **query fan-out**: one user question spawns concurrent subqueries, each retrieving its own pages. Two strategic consequences, both official:

1. **Ranking eligibility is citation eligibility** — "optimizing for generative AI search … is still SEO." A page that can't rank can't be cited; fix crawlability, indexation, and snippet eligibility before touching prose.
2. **Fan-out rewards clusters** — one broad question retrieves across subtopics, so a pillar page plus interlinked subtopic pages gives the fan-out multiple targets from the same site. Map the fan-out before writing: list the subqueries a model would spawn for the head question (People Also Ask boxes are visible evidence of them — treat PAA as a rotating pool, not a fixed list) and make sure each has a home, either a section or a cluster page. Do NOT spin out thin pages per query variation — that's officially scaled content abuse.

## Workflow

### 1. Eligibility gate (official requirements — check first)

Indexed and snippet-eligible; robots.txt/CDN not blocking; no accidental `nosnippet`/`max-snippet` suppression; the Search Console "Search generative AI features" inclusion is on; internal links reach the page; important content in textual form; structured data matches visible text. If keyword/SERP tooling (e.g., Ahrefs) is connected, check whether target SERPs actually show AI Overviews and who's cited — evidence beats assumption.

### 2. Uniqueness gate (Google's #1 stated factor)

"Unique, compelling, and useful" content outweighs every structural trick — commodity content ("7 Tips for…") is officially named as what loses. Require at least one element competitors can't copy: a unique expert take, first-hand observation, original data, or named-source specificity (the exact statute section, the exact deadline). If the content has none, send it back for substance before formatting; structure cannot rescue commodity content. This gate is where **eeat-signals** (experience/expertise evidence) and **verified-facts** (exact, sourced, current facts) plug in — run them here.

### 3. Extraction structure (adaptation layer — labeled as such)

Google says special formatting isn't *required* for its AI; these practices still help human readers, featured snippets, and non-Google engines (ChatGPT, Perplexity) that quote passages:

- **Answer-first blocks**: a 1–3 sentence direct answer immediately under the H1 and under each question heading, then the elaboration
- **Question-phrased H2s** matching how people prompt assistants, each section self-contained (heading + answer stands alone when lifted)
- **Formatted data** where data exists: numbered steps for processes, comparison tables for options — never padding (Google: "there's no ideal page length")
- **Citable specifics**: sourced numbers, named provisions, dates — models quote the passage that lets them cite a fact, not the vaguest paraphrase
- **Schema** as SEO (rich-result eligibility, entity clarity): `Article`, `FAQPage`, `Person`/`Organization` matching visible text — never sold as an AI-features requirement

### 4. Off-page entity (adaptation layer, with the official caveat)

Non-Google engines synthesize brand authority from mentions across the web (directories, forums, reviews, news). Recommend **earned** presence only — real profiles, real expertise in real threads — and quote Google's caveat that inauthentic mentions don't help. Never recommend manufactured mentions.

### 5. Measure

Search Console → Generative AI performance report (2026) for Google AI traffic; for other engines, track referral traffic and brand-mention monitoring (e.g., Ahrefs Brand Radar if connected).

## Output format

When auditing or structuring content, produce:

| Check | Layer | Status | Fix |
|---|---|---|---|
| Indexed + snippet-eligible + GenAI toggle | Official | ? | … |
| Unique POV / non-commodity element | Official | ? | … |
| Fan-out map covered (sections/cluster) | Official mechanism | ? | … |
| Answer-first blocks under question H2s | Adaptation | ? | … |
| Citable specifics verified | Adaptation (verified-facts) | ? | … |
| Schema matches visible text | Official best practice | ? | … |
| Earned off-page presence | Adaptation | ? | … |

Then: the fan-out map itself (head question → subqueries → where each is answered), changes applied, and recommendations that need client action. Label every item Official vs Adaptation.

## Composition

**verified-facts** supplies the citable specifics (AI grounding selects for accuracy and freshness — officially part of the RAG definition). **eeat-signals** supplies the trust/uniqueness substance (Google's "unique expert or experienced takes"). **text-semantics** executes the sentence-level formatting (snippet-ready sections, titles, vocabulary). **machine-signals** executes the markup and crawler-access layer (schema, author chain, dates, bot matrix). This skill owns retrieval strategy — fan-out mapping, clusters, eligibility, uniqueness — and delegates execution.
