# text-semantics — instrument layer (absorbed 2026-08-28, was a standalone skill)

> One layer of ebs-discoverability. Former routing contract, first 200 chars: Format and adapt the text of a page — headings, paragraphs, titles, meta descriptions, vocabulary, anchor text, snippet-ready sections — so search engines and AI systems can parse, snippet, and quote …


# Text Semantics (how to write text machines can lift)

**First read `google-text-rules.md`** — verbatim rules from Google's current docs, including officially debunked folklore (heading order doesn't matter to Search; no ideal word count; featured snippets can't be requested). Cite the doc when recommending; never dress accessibility practice up as a ranking trick.

## Principles (each traceable to the reference)

1. **Write the snippet by writing the page.** Snippets come from page content, chosen per-query — so every important section needs a lift-ready sentence: self-contained, subject named (not "it"), fact included. Featured snippets deep-link to the exact section they lifted; a section that can't stand alone can't be featured.

2. **Nothing important behind interaction.** Google states it does not interact with pages: content in collapsed accordions, tabs, or click-to-expand is invisible to extraction. If it matters, it renders as visible text on load. (FAQ accordions that are open in the HTML and merely styled closed are fine only if the text is in the served DOM — verify with machine-signals.)

3. **Structure serves navigation, not magic.** Break long content into sections with descriptive headings because readers and screen readers need them — Google says order and count don't matter to ranking. Phrase headings as the questions readers ask (this aligns sections with query fan-out; see geo-content), and put the answer in the first sentence under each.

4. **Vocabulary spread beats keyword repetition.** Google officially: novices and experts search different words, and varied natural wording matches more queries; repeating one phrase is spam. So write dual-register — term of art plus plain-language equivalent ("furnisher (the bank or lender reporting the debt)") — which covers both query populations and is the officially safe form of "keyword coverage."

5. **One clear main title.** A page needs exactly one visually dominant title matching the `<title>`, first `<h1>`, unique across the site, descriptive not vague, no stuffing — otherwise Google rewrites it from whatever else is prominent. Meta description: a unique, human-readable pitch per page; length limits are display truncation, not rules.

6. **Anchor text and image context carry meaning.** Link text must describe the destination ("FCRA § 605B block rules", never "click here"); untrusted external links get `nofollow`. Images sit next to the text they illustrate, with alt text describing the relationship.

## Workflow

1. Read the draft; list its sections. For each: does the first sentence under the heading answer the heading? Is it self-contained (named subject, included fact)? Fix the ones that aren't.
2. Check title/meta: one dominant title, unique, descriptive; meta description written as a pitch.
3. Vocabulary pass: identify the expert terms and the novice phrasings for the topic; ensure both appear naturally (dual-register); kill repetition that reads as stuffing.
4. Visibility pass: flag any content the design will hide behind interaction; either surface it or note it for machine-signals to verify in the served DOM.
5. Links/images pass: descriptive anchors, contextual image placement, alt text.

## Output

A marked-up edit (or rewrite) plus a short table: | Element | Rule (doc) | Before | After |. Flag anything that needs the technical layer (DOM visibility, markup consistency) as a handoff to **machine-signals**; strategy-level structure (fan-out coverage, clusters) to **geo-content**; factual claims to **claim-verification**.
