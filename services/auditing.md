# AI SEO for auditing

How the **live site** is checked. Auditing is this repo's own job: `b2b-seo-audit` at site scope, findings to
`reports/site-problems-log.md`, fixes to the board through Andrei (board first, then push). The numbers are in
`library/ai-seo-limits.md`; the research is in `skills/b2b-seo-audit/references/official-site-rules.md` and the
discoverability references.

## Cadence

| What | When | Cost | Output |
|---|---|---|---|
| GSC refresh + entity health | the ~2-week agenda ritual | 0 units | `intake/snapshots/gsc-<date>.json`, `intake/entity-health.md` |
| AI-citation count (AH6) | same ritual | ~120 units | `intake/snapshots/ai-citations-<date>.json` |
| Zero-click read | every GSC snapshot | 0 | rows in the snapshot's read (method: `seo-strategy` refs §7) |
| Anchor health (AH7) | same ritual, once set up | verify first | snapshot |
| Full site audit | **not run yet**: first pass is open | Ahrefs Site Audit + live checks | `reports/<yyyy-mm-audit>/` |

Last run: GSC and AI citations 2026-11-03 (the previous GSC pull was 2026-08-14).

## The full audit's checklist, by part

- **SEO:** crawl and indexation (robots, sitemap, status codes, canonicals, redirects in one hop), Core Web
  Vitals at the 75th percentile, mobile, HTTPS, internal-link health, duplicate URLs.
- **SXO:** the six page-experience questions, per template (`official-site-rules.md` § Page experience).
- **Rendering:** is the text, every link and the schema in the first HTML response (`official-site-rules.md`
  § Rendering)? Checked per template, because the template decides it, not the page.
- **AEO / GEO:** AI crawlers allowed (`disc/official-machine-rules.md`), llms.txt reachable, schema matching
  visible content, submission set up (Bing Webmaster Tools, IndexNow).
- **Off-page:** link spam exposure and the exact-match anchor share (AH7).

## Where a finding goes

1. `reports/site-problems-log.md`, as `## P<n>` with evidence, why it matters, owner, status.
2. A template or component fix is the web-design service's (`services/web-design.md`); copy is writing's.
3. It reaches the board only by Andrei's decision, and Teamwork only when he arms the card.
