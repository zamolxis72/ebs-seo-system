# AI SEO for web design

What the **templates, components and front end** must do so a page can be found, lifted and cited. Read by
`ebs-web-components` (tokens and components) and `ebs-website-system` (pages), and handed to front end as
board cards. Written 2026-11-03: until then no SEO rule reached web design except the problem log.

A page's copy can be perfect and still fail here: if the template hides it, renders it late or links it with
something a crawler can't follow, writing's work never reaches the index or an answer engine.

## The rules a template or component must meet

| # | Rule | Part | Source |
|---|---|---|---|
| D1 | **The text, every link and the structured data are in the first HTML response.** Server-side or static rendering; client-side rendering only for what no crawler needs. | SEO GEO | `skills/b2b-seo-audit/references/official-site-rules.md` § Rendering |
| D2 | Links are `<a href>` elements. No click-handler navigation, no `#fragment` routing. | SEO | same |
| D3 | `noindex` and status codes come from the server, never set or removed by JavaScript; an unknown route answers a real 404. | SEO | same |
| D4 | Nothing an answer needs sits behind a tab, accordion or "read more" that needs a click to load. | AEO | `disc/google-text-rules.md` § Visibility |
| D5 | One H1 per page, matching the title; heading levels follow the content, never chosen for size. | SEO AEO | `disc/text-semantics.md` |
| D6 | Each page template has its schema slot, filled from the page's own fields (board S0–S6). | SEO AEO | `disc/machine-signals.md`; `disc/schema-examples.md` |
| D7 | Core Web Vitals pass at the 75th percentile: the numbers are in `library/ai-seo-limits.md` § SEO. | SEO | web.dev |
| D8 | Page experience: secure, mobile-ready, no intrusive interstitials, ads never crowding the main content, main content clearly distinct. | SEO | `official-site-rules.md` § Page experience |
| D9 | Images: real alt field, set width and height, lazy below the fold, modern formats (article rule 24ah). | SEO AEO | `ebs-article-system` `check_image_seo.py` |
| D10 | Every section heading can carry its own anchor, so a passage can be linked and cited on its own (board M3.anchors). | AEO GEO | `strat/official-seo-rules.md` §6 (passage ranking) |

`disc/` = `skills/ebs-discoverability/references/`, `strat/` = `skills/seo-strategy/references/`.

## How it is checked

- **Per component:** before a component ships in `ebs-web-components`, D2, D4, D5, D9 and D10 are checkable in
  its own markup. Add them to the component's acceptance list.
- **Per template, live:** D1, D3, D6, D7 and D8 need the rendered page: the auditing service checks them
  (`services/auditing.md`).
- **Live examples today:** P4 (case-study listing renders client-side only) breaks D1; P8 and P11 (duplicate
  URLs) are routing, on the board as `M7.rootdomain`.
