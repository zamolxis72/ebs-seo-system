# Media / page-health test — method and interface

How to test any page's health when the question is weight, media, or Core Web Vitals, and
how to report the result. The method is general; every concrete number that appears in
brackets is a worked-example figure from the page this was first built on (an EBS
case-study page, audited 2026-08-05), there to show magnitudes — never a spec to reapply.

## The interface: benchmark → instruments → gap → options

A health test is delivered in this four-part shape. It was arrived at by correction — a
findings-first draft was rejected as "too much in this report" — and the benchmark-first
cut was approved as-is. It is the standing interface for health reports:

1. **The benchmark's full health profile.** One best-in-class site in the same genre,
   measured with the identical commands, all metrics + weight + request count, both form
   factors. It answers "is the target reachable?" before any finding is argued.
   *(Worked example: an animation-heavy agency site scoring 98 mobile / 100 desktop —
   with 13 videos on the page — while the audited page scored 44.)*
2. **The instruments the benchmark uses.** Read from its live source and network behavior,
   each instrument mapped to the health element it wins (e.g. deferred media bytes → LCP;
   lazy discipline → Speed Index; lean JS → blocking time). This turns the benchmark from
   a shaming number into a toolset the fix plan can adopt.
3. **The audited page against it.** One comparison table with multipliers (N× weight,
   N× images, N× JS), then the named offender assets, each tagged with the instrument it
   is missing. Also list what is already healthy and must be protected through the fixes.
4. **Options as effort tiers, with result vs cost.** Least effort first (asset re-exports,
   no code) → moderate (markup/template fixes) → most (capability additions such as a
   video slot). Each tier: estimated weight, LCP, score per form factor, cost. Today's row
   labeled *measured*; projections labeled *est*. Close with verification gates the owner
   can re-run themselves.

**Generic verification gates** (tune per engagement, judge on mobile): total payload under
~1–1.5 MB for a content/marketing page, LCP ≤ 2.5 s, no single image above ~100 KB
estimated savings in Lighthouse's image-delivery audit, and — where a page loads media
per-interaction (tabs, pills, carousels) — a first-paint network check confirming only the
default variant loaded. HTTP Archive's ~2.5 MB median is the bloated web's average, not a
target.

## Getting the numbers: local Lighthouse

The keyless PSI API shares one global anonymous quota and is often exhausted; the
pagespeed.web.dev UI can hang on the same quota. Lighthouse locally is the identical
engine behind PSI's lab section:

```bash
npx -y lighthouse "URL" --only-categories=performance \
  --output=json --output-path=lh.json --quiet \
  --chrome-flags="--headless=new"          # mobile (default)
# add  --preset=desktop  for the desktop run — ALWAYS run both
# if npm's cache is broken/root-owned, prefix: NPM_CONFIG_CACHE=$PWD/.npm-cache
```

Read the JSON, not the summary. Audits that matter: `largest-contentful-paint`,
`total-byte-weight`, `image-delivery-insight` (per-image wasted bytes + reason),
`lcp-breakdown-insight` / `lcp-discovery-insight` (names the LCP element),
`network-requests` (sum `transferSize` by `resourceType` for the weight-by-type table),
`redirects`, cache-lifetime audits, `total-blocking-time`, `unused-javascript`,
`bootup-time`.

Judge by **mobile**: Google indexes mobile-first, and desktop passes a full tier earlier —
a green desktop score can mask a failing page. Lab scores wobble between runs; report
payload and LCP, not the single score. Lab data is not field data: real-user CWV (the
number Google ultimately ranks on) appears in PSI's top section only once the page has
traffic.

## Measurement traps

Each of these produced a wrong conclusion at least once before being caught:

- **In-page JS undercounts cross-origin weight.** `performance.getEntriesByType('resource')`
  reports `transferSize: 0` for hosts without `Timing-Allow-Origin` (typical for CMS asset
  servers). Never total page weight from in-page resource timing alone. *(Worked example:
  a console measurement said 480 KB; Lighthouse said 8.3 MB.)*
- **CSS `background-image` bypasses everything.** It cannot take `loading="lazy"`, the
  preload scanner never sees it, and `<img>`-based sweeps skim past it. Check computed
  `backgroundImage` across elements, and match animated formats too — GIFs hide as
  backgrounds. A CSS-background LCP element is a structural finding: the fix is markup
  (a real `<img>` with priority, or a preload hint), not just a smaller file.
- **Fake-vector SVGs.** An "SVG" weighing tens-to-hundreds of KB is usually a raster in
  disguise: `<rect fill="url(#pattern…)">` over embedded base64. A true vector logo is
  single-digit KB. Common in CMS-uploaded logo strips; multiply by strip length.
- **Image-optimizer bypass.** On sites with an image CDN/optimizer, confirm each heavy
  asset is actually requested through it and not direct from storage — a bypassing slot
  ships whatever was uploaded, at full stored size.
- **The one eager image.** Count lazy coverage and verify deferral in the network log, not
  just the attributes. *(Worked example: the single `<img>` missing `loading="lazy"` was
  also the heaviest asset on the page.)*
- **Oversized originals hide behind optimizers.** Stored dimensions matter separately from
  transfer size: OG scrapers and direct links skip the optimizer and get the full file.
- **Interaction-loaded media is genuinely free.** Lighthouse measures the load trace only;
  media fetched on click/scroll is invisible to it. That is the legitimate fix for
  media-heavy pages, not a cheat — and the reason a page can carry many animations at a
  near-perfect score. Verify which variant loads at load-time before assuming.

## Animated-media format ladder

For motion content, magnitude ordering (a ~10 s screen recording as reference): GIF is
worst by 5–10× → animated WebP (plays in `<img>`, the stopgap when a slot only accepts
images) → MP4 (H.264, universal) → WebM (VP9/AV1, smallest, needs an MP4 fallback for
older Safari/iOS). Real video with deferred bytes (poster + `preload="none"`) costs a page
almost nothing at load. Delivery specifics belong to the surface's own skill — for EBS
case-study pages, `ebs-case-study-video` holds the embed options; this audit only flags
the format finding and routes it.
