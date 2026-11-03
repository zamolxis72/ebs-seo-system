# Library: SEO reference

The reference layer. The reusable method so it is not re-derived per pass: the audit checklist, on-page and schema (structured-data) templates, the prioritization math that ranks opportunities — and `ahrefs-engine.md`, **the engine**: every Ahrefs pull (AH1–AH7) with endpoint, parameters and cost, cited by id from the workstream recipes (the article system's collection recipe holds the RULES over these pulls; restating an endpoint outside the engine is a fork).

**`error-classes.md`** records what went wrong in the rules, research and links between systems, and what prevents it.
`scripts/test_ai_seo.py` tests the wiring end to end (exit 1 on any fail).

**`ai-seo-map.md` is the index of the whole AI SEO system** (every concept, research, rule, check, served
system). **`ai-seo-limits.md` is the single home of every measurable limit** (title, meta, slug, links, answer block,
paragraph, FAQ, key references, Core Web Vitals), split into SEO · AEO · GEO under the umbrella name AI SEO.
Scripts in the article and case-study systems read its `## Machine values` block; a number restated elsewhere
is a fork.

Grounded in this repo's own search suite: `seo-strategy`, `ebs-discoverability` (whose bundled layers quote Google and vendor documentation verbatim, never paraphrased from memory) and `b2b-seo-audit`. New checks discovered during an audit get added here, then merged into the owning skill periodically.
