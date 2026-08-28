# Schema examples — paste-ready JSON-LD, EBS-shaped

**Provenance.** Absorbed 2026-08-25 from the stock `schema` skill (v2.0.0), which lost the
comparison to this skill on everything except this: ready-to-paste blocks. Every example below is
adapted to EBS surfaces and **subordinate to the one law** (markup mirrors visible content — a
block whose visible counterpart doesn't exist is not pasted, it's a CLIENT INPUT NEEDED line).
Values in `[BRACKETS]` are placeholders that must be confirmed, never guessed.
**Organization constants come from ONE source: `ebs-brand-assets/manifest.json`** (contact,
address, email are there today; the hosted logo URL and LinkedIn are manifest gaps to fill THERE
— brand facts live in brand-assets, schema only mirrors them).

**When these are built:** at packaging (builder 5.1), **from the locked text only** — never from a
draft. A0's packaging owes exactly the article `@graph` below.

## The article page `@graph` (the EBS default: Article + Breadcrumb + Organization + FAQ)

One script, four nodes, `@id`-linked so the graph is one object, not four floating ones:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://ebs-integrator.com/#organization",
      "name": "EBS Integrator",
      "url": "https://ebs-integrator.com",
      "logo": { "@type": "ImageObject", "url": "[MANIFEST GAP: brand-assets manifest.json has doc-kit logo files, no hosted URL — add one there, then fill]" },
      "sameAs": ["[MANIFEST GAP: LinkedIn URL absent from manifest.json — add there, then fill]"],
      "address": "[from brand-assets manifest.json → contact.address]",
      "email": "[from manifest.json → contact.email]"
    },
    {
      "@type": "Article",
      "@id": "https://ebs-integrator.com/en/blog/[slug]#article",
      "headline": "[the H1, verbatim]",
      "image": "[the OG/cover image URL, 16x9]",
      "datePublished": "[ISO 8601 with timezone, MATCHING the visible published date exactly]",
      "dateModified": "[ISO 8601, MATCHING the visible last-updated date exactly]",
      "author": { "@id": "https://ebs-integrator.com/#organization" },
      "publisher": { "@id": "https://ebs-integrator.com/#organization" },
      "description": "[the meta description, verbatim from cms-paste]",
      "mainEntityOfPage": { "@type": "WebPage", "@id": "https://ebs-integrator.com/en/blog/[slug]" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://ebs-integrator.com/en/home" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://ebs-integrator.com/en/blog" },
        { "@type": "ListItem", "position": 3, "name": "[article title]", "item": "https://ebs-integrator.com/en/blog/[slug]" }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "[FAQ question, verbatim from the visible H3]",
          "acceptedAnswer": { "@type": "Answer", "text": "[the visible answer, verbatim — never a rewrite]" }
        }
      ]
    }
  ]
}
```

**Two rules baked into that block:**
- `author` is the **Organization until a visible byline exists** — marking up a Person the page
  doesn't show violates the mirror law (this is A0's current state and its known blocker). The day
  the byline ships, `author` becomes the Person node below and the chain must be complete.
- FAQ `text` is the visible answer **verbatim**. A rewritten "schema version" of an answer is
  marked-up content the reader can't see.

## The author chain (when the byline exists)

```json
{
  "@type": "Person",
  "@id": "https://ebs-integrator.com/en/authors/[slug]#person",
  "name": "[Name exactly as the visible byline shows]",
  "url": "https://ebs-integrator.com/en/authors/[slug]",
  "sameAs": ["[LinkedIn profile]", "[other corroborating profile]"]
}
```

And the bio page itself as `ProfilePage` with `mainEntity` pointing at the Person. Every link in
the chain (byline → author page → external profiles) must exist visibly before any of it is marked
up — the chain spec is in SKILL.md step 3.

## The hub / service page (`Service`, the EBS type — not Product)

EBS sells engagements. `Product`, `Offer` with prices, `aggregateRating` and `review` are the
stock skill's SaaS types and are **never used here** (no visible price tiers exist, and marked-up
ratings without visible ratings are the exact deceptive-markup case the mirror law names):

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "[the service as the page names it, e.g. AI consulting]",
  "provider": { "@id": "https://ebs-integrator.com/#organization" },
  "serviceType": "[category]",
  "areaServed": "[as visibly stated, e.g. Moldova, Romania, EU]",
  "description": "[the page's own description, verbatim]"
}
```

## Implementation note (the site is Next.js)

Server-render the script — never inject client-side (the audit rule: JS-injected JSON-LD is
invisible to static fetches, and non-Google engines document no rendering at all). In the App
Router, emit the `<script type="application/ld+json">` in the page component's server output, one
`@graph` per page. We verified 2026-08-25 the site serves content in initial HTML, so schema
emitted the same way inherits that property.

## Validation

Google Rich Results Test (renders JS) + validator.schema.org, then Search Console enhancement
reports post-publish. Rich results are never guaranteed — eligibility, not entitlement.

## Rejected from the stock catalog, on record

`Product` and `SoftwareApplication` (nothing to price), `LocalBusiness` (not a storefront;
`Organization` carries the entity), `Event` (adopt only if webinars ship, with visible dates),
`HowTo` (only if a page shows real numbered steps — an article's prose argument is not a HowTo),
`aggregateRating`/`review` anywhere (no visible ratings exist), and the WebSite `SearchAction`
(no site search box — marking one up would claim UI the site doesn't have).
