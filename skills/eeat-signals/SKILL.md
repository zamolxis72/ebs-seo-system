---
name: eeat-signals
description: Audit or apply E-E-A-T (Experience, Expertise, Authoritativeness, Trust) using Google's official Search Quality Evaluator Guidelines, quoted verbatim with section numbers in the bundled reference. Use whenever content is written, reviewed, or audited for a YMYL topic (legal, financial, medical, safety, consumer rights) even if E-E-A-T is never mentioned, and whenever the user mentions trust signals, bylines, credibility, quality raters, YMYL, "will AI cite this", or wants content to look authoritative. Never fabricates credentials or experience — flags them as client inputs instead.
---

# E-E-A-T Signals (strict Google rules)

**First read `references/google-eeat-rules.md`** — verbatim QRG (Sept 11, 2025) quotes with section numbers. Cite sections in every audit; never quote QRG rules from memory. The reference ends with two debunked third-party myths — don't reintroduce them.

## Workflow (raters' own order)

1. **Purpose** — page must exist to help people; search-engine-first intent violates spam policy [HC "Why"].
2. **Classify YMYL** [§2.3] — apply the two-question harm test verbatim; classify clear YMYL / in-between / not YMYL. Legal and consumer-finance content is clear YMYL. On clear YMYL: "highly inexpert" = Untrustworthy = Lowest [§4.5.2].
3. **Main Content test** [§3.2] — effort, originality, talent/skill; for YMYL also "accuracy and consistency with well-established expert consensus". If a fact-verification skill is available, run it here.
4. **The four letters** [§3.4] — Trust first (it's the center; untrustworthy = low E-E-A-T no matter what):
   - **Trust**: accurate, honest, safe, reliable; responsibility and contact info scaled to the trust the page demands [§2.5.2–2.5.3]; honest dates [HC].
   - **Experience**: genuine first-hand material only; on clear YMYL it must also match expert consensus [§3.4.1].
   - **Expertise**: demonstrated in the content itself — correct mechanics, precise terminology, exact sourced figures; a named expert reviewer counts [HC].
   - **Authoritativeness**: byline linked to a bio with externally verifiable credentials [§3.3.4]; independent sources beat self-claims [§2.5]; off-page reputation is recommended, never claimed. Absence of reputation is neutral for small sites [§3.3.5].
5. **Lowest tripwires** [§4.x] — any one sinks the page: fake/embellished author profiles or deceptive expertise claims [§4.5.3]; multiple factual inaccuracies [§4.5]; no responsibility info on YMYL [§4.5.1]; copied/AI content with little effort, originality, or added value [§4.6.6] (AI use alone doesn't determine rating [§4.6.7]; disclose substantial AI assistance [HC "How"]).
6. **Grade against the ladder** [§§5–8] — Low: "a single Low quality attribute is enough"; lacking E-E-A-T cannot be overcome by anything [§5.1]. High requires at least one of: high effort/originality, positive reputation, or high E-E-A-T [§7.0] — "typical" pages are Medium, not High [§7.1]. Highest requires "very high" on one of those; experience alone can earn it [§8.3–8.4].

## Anti-fabrication protocol [§4.5.3, §5.6]

Never invent credentials, degrees, bar admissions, case results, client counts, testimonials, statistics, quotes, or anecdotes. Fake profiles and deceptive expertise claims are deception → Lowest; self-claims aren't evidence anyway ("not just … claims of 'I'm an expert!'"). When a signal needs a real-world fact you lack, insert:

> **[CLIENT INPUT NEEDED: attorney byline — name, bar admission, bio URL]**

and list every such item in the output with the rule it serves.

## Pattern: practitioner author, no schema available

When the platform ships no structured data (true of the EBS blog as of 2026-08-14), the E-E-A-T load moves entirely to the visible layer. For a republished practitioner article (an engineer's Medium/LinkedIn piece brought onto the company blog), the minimum visible set is:

1. Byline as real text under the H1: name + role + employer ("By [Name], DevOps Engineer at EBS Integrator"), name linked to an identity page.
2. A descriptive-anchor link to the original publication (first-hand Experience evidence: the author demonstrably did the work and published it under their own name).
3. The author's first-person evidence (timings, failures, exact numbers) kept verbatim in the body; it is the Experience signal and must never be genericized.
4. An author page on the owning site flagged as CLIENT INPUT NEEDED if it doesn't exist; an external profile alone leaves authority off-site.

Producing the republish package itself is `ebs-article-republish` (project-scoped in `ebs-article-system` — open that repo); this skill judges whether the visible set is sufficient.

## Output format

Always produce:

| Signal | Letter | Google rule | Status (Present/Partial/Missing) | Fix |
|---|---|---|---|---|

Then: (1) YMYL classification with harm-test reasoning, (2) Lowest tripwires found (these outrank everything), (3) ladder grade with the §7/§8 criterion the page could realistically satisfy, (4) CLIENT INPUT NEEDED list, (5) off-page reputation recommendations, separated because raters verify them through independent sources.

## Composition with sibling skills

This skill owns E-E-A-T judgment only. Delegate when available: **verified-facts** (claim-by-claim accuracy against primary sources — feeds Trust), **geo-content** (extraction structure, question headings, schema, clustering, off-page entity building — feeds AI citability). Without them, note accuracy verification and GEO structure as out-of-scope recommendations rather than doing them ad hoc.
