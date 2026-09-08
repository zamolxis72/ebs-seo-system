# Site problems log (for future investigation / fixes)

Evidence-based issues found during article pipeline work. Each item: evidence, why it matters, proposed owner. Update status as items get fixed. Last updated: **2026-09-08** (P22 added — two AI articles share one meta description; the tag system that answers P21's editorial half is now specified). Before that: **2026-09-07, second pass** (the blog retag closed P16 and P17 and cut P15 from 22 disagreements to 6; P18–P21 added from the same re-verification — a draft article served to readers, records served with no listing, seven URLs returning empty 200s, the related strip out of date order, and a filter vocabulary that no longer matches what articles carry. Earlier: P15–P17 added from blog tag curation — two disagreeing tag fields, 14 of 45 blog articles unreachable from the index, and a live test post; before that P14 llms.txt 404s behind the locale middleware, P13 the unsourced AI-page statistic, and P9–P12 from the sitemap reconciliation; P3 and P4 corroborated; P6 partially RESOLVED).

**Fetching this log:** every item is `## P<n> — <title> — SEVERITY: <level>` with an
`**Owner:** … **Status:** …` line, so one grep answers "what's open and whose is it":
`grep '^## P\|Status:' reports/site-problems-log.md`. The statuses in the item bodies are the
single source of truth — no summary table exists to drift from them. Fix owners named **web dev**
are consumed by the `ebs-website-system` workstream, which points here rather than keeping its
own issue stack.

## P1 — GitLab instance publicly exposed and dominating the link graph — SEVERITY: HIGH

**Evidence (Ahrefs internal-links, 2026-07-16):** pages.ebs-integrator.com is a live, publicly crawlable GitLab (project explorer, sign-in pages, hundreds of .atom feeds). Its URLs receive 2,600+ internal links each — 28x more than the homepage (95). Project/topic names are exposed (client project names visible, e.g. "NettBureau platform").
**Why it matters:** (a) possible confidentiality issue — internal project names publicly listed; (b) crawl budget and link-graph dilution — the crawlable surface of the "site" is mostly GitLab noise, not marketing pages.
**Fix direction:** block pages.* from indexing (robots + noindex) or put it behind auth entirely. Check what's publicly visible ASAP (open pages.ebs-integrator.com/explore in incognito — my fetch returned empty, unconfirmed).
**On robots.txt:** NOT sufficient alone. robots.txt only asks crawlers not to crawl; it does not remove indexed URLs (Google keeps them, un-crawled) and does not stop humans. Correct order: (1) GitLab Admin → Visibility and access controls → restrict "Public" visibility (or VPN/IP-allowlist the instance), (2) GSC property for pages.* → Removals, (3) robots.txt disallow-all as belt-and-braces AFTER access is closed. Disavow is irrelevant here (that tool is for external spam backlinks only).
**Owner:** DevOps + management (confidentiality call). **Status: OPEN — investigate first.**

**Corroborated from Search Console, 2026-08-14** (`intake/snapshots/gsc-2026-08-14.json`): `pages.ebs-integrator.com` is not merely crawlable, it is **earning impressions in Google**. `pages.ebs-integrator.com/explore/projects/topics/meapp` drew 248 impressions at position 11.0, and `pages.ebs-integrator.com/` a further 47. The query `site:ebs-integrator.com` returns **324 URLs** with a GitLab project-topic page as `top_url`. The "my fetch returned empty, unconfirmed" caveat above is now resolved: it is indexed, and someone is running site: queries against the domain. Severity holds at HIGH.

## P2 — 95 internal links point to a 404 — SEVERITY: HIGH

**Evidence:** https://ebs-integrator.com/en/about/case-studies returns 404 yet receives 95 dofollow internal links (site-wide nav/footer scale — same count as live nav pages).
**Why it matters:** a site-wide template link leads users and crawlers to a dead page; wasted equity, bad quality signal.
**Fix direction:** find the template link (likely footer/nav "About > Case studies") and point it to /en/case-studies, plus 301 the old URL.
**Owner:** web dev. **Status: OPEN.**

## P3 — DX service page starved of internal links — SEVERITY: HIGH (verdict: it DOES matter)

**Evidence:** /en/it-services/digital-transformation receives exactly 3 internal links. Every nav service page receives 95. It ranks for zero keywords (top-pages audit) despite being a full, live page.
**Investigated the "maybe it's reachable other ways" hypothesis:** being reachable/indexed is not the bar. Internal links carry ranking equity; 3 vs 95 means Google sees this page as unimportant regardless of sitemap presence. This is the CTA target of the pillar article — its weakness directly caps the article's conversion path.
**Fix direction:** add to services nav/footer alongside the other six services; link from /en/it-services hub; pillar article will add 1 more.
**Owner:** web dev (nav change — trivial). **Status: OPEN, HIGH-PRIORITY, cheap fix.**

**Corroborated from the live site, 2026-08-21:** the defect is wider than DX. `/en/it-services` links
**7 of the 10 live service pages**. Not linked from their own index: `digital-transformation`,
`consulting/cto-as-a-service`, `consulting/business-analysis` — all three live with real content
(H1s verified). So the "3 internal links" figure for DX has a visible cause: its own index page does
not list it. The fix for P3 should cover all three, not just DX.

**Corroborated from Search Console, 2026-08-14:** over the 90 days to 2026-08-13 the page drew **45 impressions and 0 clicks**, and its `top_keyword` is the operator `site:ebs-integrator.com` — meaning the only query reliably surfacing it is somebody enumerating the domain, not demand. The same pattern holds for `/en/it-services/software-development` (57 impressions, same operator probe). "Ranks for zero keywords" is now measured rather than inferred.

## P4 — Case-studies listing renders client-side only — SEVERITY: MEDIUM

**Evidence:** /en/case-studies shows "Loading..." without JavaScript (agent fetch, 2026-07-16). Individual case pages exist but the listing's links may not be reliably crawled; several cases rank for nothing.
**Why it matters:** case studies are EBS's best proof assets and interlink targets for the whole article strategy.
**Fix direction:** SSR/prerender the listing, or add static links (footer sitemap page). Verify in Google Search Console: which case URLs are indexed.
**Owner:** web dev. **Status: OPEN — verify indexation in GSC first.**

**Still true on 2026-08-21:** a fetch of `/en/case-studies` returned navigation and footer only —
zero case-study links in the served HTML. Indexation itself is not the problem (the sitemap lists
every case URL and GSC reports impressions for nine of them); the listing page is simply not a
crawlable path to them, so all internal discovery depends on the sitemap and the homepage rail.

## P5 — Redirect-hop internal links — SEVERITY: LOW

**Evidence:** 94 internal links each point to non-/en URLs (e.g. /it-services/consulting) that 307-redirect to /en/ versions. 307 (temporary) instead of 301/308 (permanent) for most.
**Why it matters:** minor equity loss + crawl waste; temporary redirects don't consolidate signals.
**Fix direction:** internal links should target final /en/ URLs directly; make redirects permanent (308/301).
**Owner:** web dev. **Status: OPEN.**

## P6 — Orphaned / broken case study assets — SEVERITY: LOW

**Evidence:** German diaspora tax-return case shown on homepage rail but its page is a noindex placeholder (no discoverable URL). Legacy URL patterns (/case-studies/cloud-schedule/, /en/about/case-studies/*) still indexed by Google.
**Fix direction:** publish or remove the tax case; 301 legacy patterns to current URLs.
**Owner:** web dev + content. **Status: PARTIALLY RESOLVED 2026-08-21.**

**The tax case is published.** `/en/case-studies/digital-tax-returns-germany-diaspora` is live with
real content and its own results (-67% time to declare, -80% input errors, 1,000+ declarations daily,
1M+ users per year), and it is in the sitemap. The "noindex placeholder" half of this item is closed.
The legacy-URL half stands: not re-verified in this pass.

## P7 — robots.txt + structured data (schema) audit on the main site — SEVERITY: MEDIUM (enhancement)

**To investigate:** (a) does ebs-integrator.com/robots.txt exist, what does it allow/block, does it reference the sitemap; (b) is /en/sitemap.xml valid and submitted in GSC; (c) which pages carry JSON-LD today — needed: Organization (sitewide), Article (blog posts), BreadcrumbList; FAQ schema only where a real FAQ exists (service pages have FAQs — check if marked up).
**Why it matters:** schema won't fix rankings by itself but improves rich results, entity recognition, and AI-search citability (Brand Radar relevance). Cheap wins.
**Note:** the article pipeline handles its own part — every new article ships with Article + Organization JSON-LD from day one (added to playbook step 6).
**Owner:** web dev + SEO pass (fold into the b2b-seo-audit run). **Status: OPEN — documented, deferred.**

## P8 — Two URL variants of the homepage rank independently — SEVERITY: MEDIUM

**Evidence (Search Console via Ahrefs project 9118279, 90 days to 2026-08-13, `intake/snapshots/gsc-2026-08-14.json`):** both `https://ebs-integrator.com/en/home` (139 keywords, 1,851 impressions, 340 clicks, avg pos 14.3) and `http://www.ebs-integrator.com/` (54 keywords, 1,249 impressions, 19 clicks, avg pos 7.4) earn impressions, and both report `ebs integrator` as their top keyword. Two protocol/host variants of the same destination are being served and measured separately.

**Why it matters:** the `www` + `http` variant carries a *better* average position than the canonical one but converts at 1.5% CTR against 18.4%, so the variant Google sometimes prefers is the weaker experience. Signals that should accumulate on one URL are being reported against two, and the split is invisible on the page itself.

**What this is NOT:** the same pull shows `ebs integrator` returning **24 URLs** and `ebs` returning 10. That is *not* a defect — Google returns sitelinks on a navigational brand query, so home, about, career and contact all appearing is expected behaviour. Only the protocol/host duplication above is actionable. Recorded because the 24-URL figure looks alarming and will be re-encountered; `library/entity-health-method.md` excludes branded queries for this reason.

**Fix direction:** confirm `http://` and `www.` both 301 to the canonical `https://ebs-integrator.com/en/home` in one hop, and confirm the canonical tag agrees. Check whether the GSC property set covers both variants (it evidently reports them separately). Verify with a redirect trace before changing anything — this may already be configured and mis-measured rather than genuinely duplicated.

**Owner:** web dev / DevOps. **Status: OPEN — verify the redirect chain first.**

## P9 — Case studies published on `test-page` slugs, and BuildGreen indexed while believed unpublished — SEVERITY: HIGH

**Evidence (sitemap + direct fetches, 2026-08-21):** the sitemap's case-study section holds **19**
URLs. Seventeen are the real cases in `intake/entity-register.md`. The other two are live, carry real
content, and sit on throwaway slugs:

| URL | H1 as served |
|---|---|
| `/en/case-studies/test-page` | *"FDA-compliant software that saves sales by remote 20%"* |
| `/en/case-studies/test-page-case-1` | *"Refactored carbon and CSRD platform for green building certification"* |

**The second one is BuildGreen.** Section 3 of `intake/entity-register.md` declares BuildGreen
*"`noindex` on, excluded from the sitemap, unlinked"* at slug `carbon-management-platform-refactor`.
All three of those are contradicted: it is live, it **is** in the sitemap, and it is on a test slug.
The intended slug `/en/case-studies/carbon-management-platform-refactor` serves site chrome with no
case-study content — a soft 404 in appearance, though HTTP status was not confirmed by fetching.

**Why it matters:** a workstream believes an asset is unpublished while Google is being invited to
index it, under a URL nobody would choose. The first H1 also reads as unfinished or mangled copy
(*"saves sales by remote 20%"*), which is a live client-facing page. And the entity register — the
file every new title is checked against — is wrong about a case study's state, so decisions taken
from it inherit the error.

**Fix direction:** decide per page whether it ships or goes. If it ships, move it to a real slug and
301 the test URL; if not, remove it from the sitemap and return 410/404. Then correct the register's
section 3 to match whatever is true. Check the CMS for how a test slug reached the sitemap at all —
if drafts are sitemap-eligible, this will recur.

**Owner:** content + web dev; register correction is the SEO workstream's. **Status: OPEN.**

**Note:** the article workstream has **dropped all three URLs** from the content system
(`ebs-article-system/library/content-map.md`, 2026-08-21) so nothing is planned or interlinked
against them. That does not unpublish them, which is why this item exists.

## P10 — The `ai-consulting` hub is absent from the sitemap — SEVERITY: HIGH

**Evidence (sitemap + direct fetch, 2026-08-21):** the sitemap lists **9** service pages and
`/en/it-services/ai-consulting` is **not among them**. The page is live — H1 *"Integrating AI takes 8
levels"*, title *"AI adoption and consulting for business | EBS Integrator"* — and it **is** linked
from `/en/it-services`. Every other service page appears in the sitemap.

**Why it matters:** this is the commercial destination for the AI content programme. Six planned
keywords route into it (`ai readiness assessment`, `ai governance framework`, `ai roi`,
`ai training for employees`, `ai change management`, `eu ai act compliance` — see the article
workstream's map). A hub omitted from the sitemap is a hub Google discovers only by crawling, on a
site whose listing pages already render client-side.

**Why it is separate from P3:** P3 is about *internal links* to service pages. This is about *sitemap
inclusion*, and it affects a different page. The two together mean the service layer is discoverable
inconsistently: some pages are in the sitemap but not the index page, and one is in the index page
but not the sitemap.

**Fix direction:** find why this URL is excluded — CMS flag, sitemap generator rule, or manual list —
and confirm no other commercial page is missing. Compare the sitemap against a crawl rather than
against the nav.

**Owner:** web dev. **Status: OPEN.**

## P11 — Duplicate URLs, both submitted for indexing — SEVERITY: MEDIUM

**Evidence (sitemap 2026-08-21; GSC pull 2026-08-20, project 9118279):**

1. **The same article on two slugs.** `/en/blog/ecommerce-audit-guide-eu-stores-2025` (41 impressions)
   and `/en/blog/ecommerce-audit-guide-eu-stores` (3 impressions). **Both are in the sitemap.**
2. **The same article on two paths.** `/en/blog/education-management-systems-without-integration`
   (11 impressions) and `/blog/education-management-systems-without-integration` (6 impressions) both
   earn impressions. Only the `/en/` form is in the sitemap, so the non-`/en/` form is indexed without
   being declared.

**Why it matters:** two URLs for one article split whatever signal it earns, and case 1 is worse than
an accident of redirects — both are declared in the sitemap, so the site is actively asking for both
to be indexed.

**Fix direction:** pick the canonical slug for each, 301 the other, and remove the loser from the
sitemap. Case 2 is the `/en/` prefix inconsistency also behind P5; a single rule for prefixing would
fix both.

**Owner:** web dev. **Status: OPEN.**

## P12 — Sitemap hygiene and an orphaned live article — SEVERITY: LOW

**Evidence (sitemap 2026-08-21):**

- **A live article nothing links to.** `/en/blog/scalable-it-solutions-business-growth` — H1
  *"Building scalable IT solutions that deliver results"*, published May 2023. It is in the sitemap,
  it is **not** on the `/en/blog` listing (30 articles shown), and it drew **no impressions above the
  25-impression floor** in the 90 days to 2026-08-19. Live, undiscoverable, unread.
- **A stray URL:** `/en/blog/blogs` is in the sitemap and is not an article.
- **An unencoded character:** `/en/blog/why-omnichannel-your-online-&-physical-stores` carries a raw
  `&` in the path. It earns impressions (258), so it resolves, but a bare `&` in a URL is fragile
  across parsers and sharing contexts.
- **Scale, for context:** the sitemap lists **45** blog URLs. Only **27** earned any impressions in
  the window, and the whole blog drew **14,418 impressions for 10 clicks** in 90 days — four pages
  account for all ten. That is a titles-and-intent problem owned by the article workstream, not a
  site defect, and is recorded here only so the 45-vs-27 gap is not later mistaken for an indexation
  failure.

**Fix direction:** decide whether the orphaned article is worth linking or removing; drop
`/en/blog/blogs` from the sitemap; percent-encode or re-slug the `&` URL.

**Owner:** web dev + content. **Status: OPEN.**

## P13 — AI page carries an unsourced statistic ("91%") — SEVERITY: MEDIUM

**Evidence (verification pass for article A0, 2026-08-22/24):** the AI consulting page states
"91% of companies cannot show what AI delivered." A `claim-verification` pass found no source
supporting this claim. The closest real 91% is a **different assertion about a different
population** (91% of 1,800 legal/tax/audit/compliance professionals say organisations aren't
realising AI's full value — Thomson-Reuters-adjacent professional survey). Nothing supports the
sentence as published.

**Why it matters:** the page anchors the AI-maturity ladder — the framework the whole article
series stands on. An unsourced hero statistic on that page is exactly the credibility failure the
articles are being built to avoid, and any article citing the page inherits it (A0 has already
declined to reuse the number for this reason; decision on record in
`ebs-article-system/articles/is-ai-overhyped/review/evidence-pack-v1.md`).

**Fix direction:** either source the 91% to a real primary, replace it with a verified equivalent
(candidate found during the same pass: PwC 2026 Global CEO Survey — 56% of 4,454 CEOs report AI
delivered no significant financial benefit, on-whitelist Tier 1B), or remove it.

**Owner:** web dev + content. **Status: OPEN.**

---

**Suggested next step when ready:** run the full b2b-seo-audit skill against the site — P1/P2/P3 found incidentally; a systematic pass will catch the rest.

**GSC access now exists** (Ahrefs project 9118279, verified; `gsc-pages` and `gsc-keywords` cost 0 API units), so the P4 verification noted here as blocked is now cheap to run. Snapshots land in `intake/snapshots/`; the standing method is `library/entity-health-method.md`.

---

## P14 — llms.txt unreachable: locale middleware 404s the machine-access layer (2026-08-25)

**Found during** the ai-seo skill evaluation in the article workstream; logged here because site
health is this repo's ground.

**The audit** (live fetches, 2026-08-25):

- **PASS** — article content is present in the initial HTML: agents and AI crawlers that never
  execute JavaScript read the full text. This is the single most important agent-access property
  and the site has it.
- **PASS** — AI crawlers reachable: robots.txt is allow-all and a fetch as `GPTBot/1.0` returned
  HTTP 200. No explicit AI-crawler stance is declared, which is acceptable but implicit.
- **MINOR** — robots.txt points at `https://ebs-integrator.com/sitemap.xml`, which 307-redirects to
  `/en/sitemap.xml` (which resolves, fresh lastmod). Crawlers handle it; pointing at the final URL
  is cleaner.
- **FAIL** — `/llms.txt` returns **404**, and the locale middleware redirects the request to
  `/en/llms.txt` first, meaning a machine-readable file at the domain root cannot currently be
  served at all without a routing exception. `/llms-full.txt` same.

**Fix shape:** a routing exception for root-level machine files (`/llms.txt`, later
`/llms-full.txt`), then an llms.txt naming what EBS is, who it serves, and the handful of pages an
answer engine should read first (the AI consulting hub, the maturity ladder, the live articles).
Non-Google engines read it; Google needs nothing (their AIO requires no special files, per their
own guidance).

**Deliberately not raised as problems:** OKF bundles (v0.1, nothing consumes them yet) and
`/pricing.md` (EBS sells engagements, not tiers). Both parked with triggers in
`ebs-seo-system/skills/ebs-discoverability/references/ai-visibility.md`.

## P15 — The blog shows two different tag sets for the same article — SEVERITY: MEDIUM (2026-09-07)

**Found during** blog tag curation in the article workstream; logged here because the fix is
front-end, not editorial. Curation record and full per-article table:
`ebs-article-system/library/blog-tag-taxonomy.md`.

**The defect.** The tag chips on a blog index card and the chips on the article's own page are
populated from two different CMS fields. Of the 34 live articles where both are readable, **22
disagree**. Verified in the browser 2026-09-07 on
`/en/blog/data-privacy-protection-and-why-it-matters-for-ecommerce`: the index card reads
`Data Analytics & AI · Software Security`, the article hero reads `DevOps · Data engineering` —
no overlap at all.

**Why it matters.** A reader filters the blog by one vocabulary and lands on a page asserting a
different one. It also means retagging alone cannot fix what a reader sees: whichever field the
CMS is curated in, the other surface keeps rendering the stale one.

**Fix direction:** decide which field is authoritative, point both the index card and the article
hero at it, and retire the other. Confirm against a page with a known disagreement (the one above)
rather than a page where the two happen to match.
**Owner:** web dev (decide the authoritative field) + marketing (curate it once, per the taxonomy
record). **Status: OPEN — much smaller after the 7-Sep retag.**

**Re-verified 2026-09-07 after the retag** (`ebs-article-system/intake/snapshots/blog-tags-2026-09-07.json`):
the disagreement is down from **22 of 34** to **6 of 38** — `ai-big-data-fintech-pilot-to-production`,
`education-data-silos-higher-education-administration`, `how-ar-lets-you-try-before-you-buy`,
`how-businesses-sell-modern-commerce`, `is-ai-overhyped`,
`what-is-banking-process-automation-and-why-it-matters`. The page named in the original evidence now
agrees on both surfaces. One of the six is the worse case: `education-data-silos-…` renders **two chips
on its card and none on its page**. The underlying defect is unchanged — two fields, one reader — and
curating in one field will keep producing this until the front end reads a single field.

## P16 — 14 of 45 live blog articles are unreachable from the blog index — SEVERITY: MEDIUM (2026-09-07)

**Found during** blog tag curation in the article workstream.

**The defect.** `/en/blog` server-renders 31 post cards and offers **no pagination control** — the
accessibility tree contains none, and `?page=2` returns the client-side shell with zero posts. The
sitemap declares 45 blog URLs. So 14 live articles can be reached only by direct URL, search, or a
related-articles strip.

Not reachable from the index (2026-09-07): `a-look-at-the-future-of-transport-and-logistics`,
`a-transition-story-clean-desk-and-clean-screen-policy`,
`blockchain-and-its-future-with-digital-transformation`,
`chatbots-artificial-intelligence-and-customer-service`,
`cross-platform-vs-hybrid-two-different-stories`, `customer-pain-points`,
`digital-transformation-workshop-for-empowering-moldovan-smes`,
`eastern-europe-postal-service-transformation`, `ecommerce-audit-guide-eu-stores`,
`fintech-is-changing-the-future-of-financial-services`,
`government-and-technology-continue-to-create-a-better-life-for-citizens-in-2024`,
`scalable-it-solutions-business-growth`, `shopping-is-good`,
`technology-your-retail-needs-to-grow-in-2024`.

**Why it matters.** It caps the value of any tag work: a curated tag on an article the index never
lists sorts nothing. It also compounds **P12** (orphaned live article).

**Fix direction:** add pagination or infinite scroll to `/en/blog`, server-rendered so the
additional pages are crawlable. Verify by counting cards reachable without JavaScript against the
sitemap's 45.
**Owner:** web dev. **Status: RESOLVED 2026-09-07** — re-measured after the retag: `/en/blog` serves
**38 cards** in the payload and the sitemap declares the same 38 blog articles (plus the junk
`/blog/blogs` page, still listed). Nothing is index-unreachable any more. It resolved by the
inventory shrinking rather than by pagination arriving: seven of the 45 were withdrawn (see **P19**),
so a future 39th article may bring the cap straight back. Re-check the card count against the
sitemap the next time an article ships.

## P17 — A test post is live and indexed on the blog — SEVERITY: HIGH (2026-09-07)

**Found during** blog tag curation in the article workstream.

**The defect.** `/en/blog/shopping-is-good` is live, in the sitemap, and its H1 reads
**"This is the coolest title and is H1"**. It carries a real tag (`Cloud Application Engineering`)
and a real posted date (2025-02-24). GSC recorded 5 impressions at avg position 70.2, so it is
indexed, not merely live.

**Why it matters.** Same class as **P9** (case studies on `test-page` slugs): placeholder content
published under the brand, reachable by search.

**Fix direction:** unpublish and remove from the sitemap, or replace with real content. If the URL
earned any links, 301 it rather than 404 it. Confirm no other placeholder titles are live by
scanning the sitemap's blog set for template strings.
**Owner:** marketing (unpublish call) + web dev (sitemap/redirect). **Status: RESOLVED 2026-09-07**
— `/en/blog/shopping-is-good` is off the index and off the sitemap. The unpublish half is done; the
URL half is not: it returns **HTTP 200 with an empty page** rather than a 404, 410 or redirect, which
is **P19**.

## P18 — A draft article and two unlisted records are served to readers — SEVERITY: HIGH (2026-09-07)

**Found during** the second-pass blog tag verification. Evidence:
`ebs-article-system/intake/snapshots/blog-tags-2026-09-07.json`.

**The defect.** Draft state in the CMS does not keep an article off the public surfaces.
`/en/blog/customer-pain-points` carries `"status":"draft"` in the served payload and is rendered on
`/en/blog` anyway. Separately, three records that appear on **no** listing — not the index, not the
sitemap — are still served as related-article cards: `a` (a junk slug, on 2 pages),
`boost-your-business-with-optimized-work-processes-for-it-solutions-and-products` (9 pages), and
`digital-transformation-workshop-for-empowering-moldovan-smes` (14 pages, and its own page is empty
— **P19**).

**Why it matters.** Unfinished and undeclared content is publicly reachable and linkable, and the
editorial inventory cannot be trusted: the blog is 38 articles by the index and at least 41 records
by what the front end will actually render. It also means "set it to draft" is not a working
withdrawal mechanism for marketing.

**Fix direction:** the status field must gate every surface, not just the index — the listing, the
related strip, the homepage feed and the sitemap read one published-only query. Verify with the two
named cases: `customer-pain-points` must disappear from `/en/blog`, and `boost-your-business-…` must
disappear from the nine pages that show it.

**But read the activity before acting on `customer-pain-points` (2026-09-08):** it earns **1,577
impressions at position 42** over the 90 days to 13 Aug — the third most-seen blog URL, top query
*business pain point*. The draft state is the defect, not the article. Publish it properly (tags:
Business Strategy · IT Consulting, Cross-industry) rather than hide it; hiding it throws away the
blog's third-largest search footprint. `boost-your-business-…`, by contrast, has zero impressions.
**Owner:** web dev. **Status: OPEN.** Tracked on the marketing board as `M7.blogdraft`.

## P19 — Seven withdrawn blog URLs return HTTP 200 with an empty page — SEVERITY: MEDIUM (2026-09-07)

**Found during** the second-pass blog tag verification.

**The defect.** Seven articles withdrawn in the 7-Sep pass still answer on their URLs: HTTP 200, a
~96KB shell with no `<h1>`, no body copy and no chips. `digital-transformation-workshop-for-empowering-moldovan-smes`,
`eastern-europe-postal-service-transformation`, `ecommerce-audit-guide-eu-stores`,
`government-and-technology-continue-to-create-a-better-life-for-citizens-in-2024`,
`scalable-it-solutions-business-growth`, `shopping-is-good`,
`technology-your-retail-needs-to-grow-in-2024`.

**Why it matters.** A soft 404 is the one response a crawler cannot act on: Google keeps the URL and
eventually flags it as a soft-404 rather than dropping or redirecting it. One of the seven is worse
than that — the workshop article leads the related strip on 14 live pages (**P18**), so readers are
sent to an empty page from a third of the blog. `ecommerce-audit-guide-eu-stores` is the duplicate of
`…-2025` and had accumulated its own history, so it wants a 301, not a 404.

**Fix direction:** an unpublished article must return 410 (gone) or 301 to its replacement, never 200.
Decide per URL: 301 the duplicate to `ecommerce-audit-guide-eu-stores-2025`, 410 the test post, and
either restore or 410 the five real articles — the three eGov ones took the entire
`egov-public-sector` industry off the blog with them.
**Owner:** web dev (response codes) + marketing (restore-or-retire call on the five).
**Status: OPEN.**

**Activity read 2026-09-08** from `ebs-article-system/intake/snapshots/gsc-blog-2026-08-20.json`
(Search Console, 90 days to 2026-08-13), so the retire-or-restore call rests on numbers rather than
sentiment. `technology-your-retail-…` 14 impressions, `eastern-europe-postal-…` 12,
`digital-transformation-workshop-…` 12, `shopping-is-good` 5, `government-and-technology-…` 4,
`ecommerce-audit-guide-eu-stores` 3 — every one of them with `site:ebs-integrator.com` as its top
query except the workshop piece, meaning the only thing surfacing them was somebody enumerating the
domain. `scalable-it-solutions-…`, `boost-your-business-…`, `a` and `/blog/blogs` do not appear at
all: zero impressions. **On activity, all of these are 410s** (the duplicate audit guide a 301); the
two eGov pieces are the only ones with an editorial reason to restore, and it is coverage, not
demand. **The exception is not on this list — it is in P18:** `customer-pain-points`, the draft
that renders anyway, earns **1,577 impressions at position 42**, the third most-seen blog URL. That
one is published, not removed.

## P20 — The related-articles strip is out of date order and uses half the blog — SEVERITY: MEDIUM (2026-09-07)

**Found during** the second-pass blog tag verification. Measured on all 38 article pages, in DOM order.

**The defect.** The strip is not ordered by publish date and does not reach most of the blog:

- **26 of 38** strips are not newest-first.
- On **23 of 38** the first card is one of the three undeclared records from **P18**.
- On **1 of 38** is the first card the latest article sharing a tag.
- The strip only ever draws from **19 of the 38** live articles; the other 19 are never shown as a
  related card anywhere on the site.
- The cards link to `/blog/<slug>` without `/en/` — corroborates **P11**.

The ordering it does follow looks like CMS record age: the three leaders were all last modified
2023-12-27, the oldest records in the collection.

**Why it matters.** The strip is the only internal path to the 19 articles the index shows last, and
it currently spends that link equity on a junk slug and an empty page. For a reader, "read next"
offers a 2023 post before a 2026 one on the same subject.

**Fix direction:** select on the shared tag, exclude anything not published, order by publish date
descending, cap at N. Verify on a page whose tag has a recent sibling — the first card must be the
newest article carrying that tag. Note that date ordering is only as sound as the date it sorts on,
which is why this pairs with the hand-typed publish date (marketing board `M7.blogdate`).
**Owner:** web dev. **Status: OPEN.** Tracked on the marketing board as `M7.blogtagorder`.

## P21 — The blog filters offer four terms nobody carries and hide four that articles do — SEVERITY: LOW (2026-09-07)

**Found during** the second-pass blog tag verification. Filter vocabularies read in the browser on
`/en/blog`; applied terms read from the served payload of all 38 articles.

**The defect.** The filter vocabulary and the applied vocabulary have drifted apart in both
directions. Offered but carried by no article: `Business Strategy & Growth`,
`Regulatory & Compliance Advisory`, `Operational Efficiency`, and `Egovernment` on the industry axis
— four filters that return an empty blog. Carried by articles but not offered:
`Agile Project Management`, `Retail & Consumer Goods`, `Data Engineering` (a second term differing
from `Data engineering` only in case), `AR/VR` — four chips a reader can see but cannot filter by.
`All Capabilities` and `All Industries` are still offered as options, and `All Industries` is also
stored as a real value on 18 of 38 articles.

**Why it matters.** A filter that returns nothing reads as a broken site, and a chip that filters
nothing reads as a broken tag. Both are cheap to fix once the vocabulary is one list.

**Fix direction:** the filter options should be derived from the terms actually in use, not from a
term collection that keeps retired entries. The editorial half — which term each article should
carry, and the collapse onto the site's 14 hubs — is
`ebs-article-system/library/blog-tag-taxonomy.md`; this item is the front-end half.
**Owner:** web dev (derive the options) + marketing (apply the taxonomy). **Status: OPEN.**

## P22 — Two blog articles ship the same meta description — SEVERITY: MEDIUM (2026-09-08)

**Found while** assigning tags from each article's own title and summary.

**The defect.** `/en/blog/is-ai-overhyped` and `/en/blog/ai-big-data-fintech-pilot-to-production`
carry an identical `description` in the CMS, word for word: *"AI in fintech is everywhere, yet few
systems would survive an audit. Why projects stall, what regulators expect, and the three steps
that fix it."* The text belongs to the fintech article; it was copy-pasted onto the AI-hype one.

**Why it matters.** These are the two newest AI articles and the entry points to the AI ladder, so
the duplication sits on exactly the pages the AI-page cluster depends on. A shared description means
Google picks its own snippet for at least one of them and the two pages read as near-duplicates to
an answer engine deciding which to cite.

**Fix direction:** rewrite the `is-ai-overhyped` description against its own argument (the refusal
rung: whether the hype is justified and what to do about it). Then sweep the other 36 descriptions
for repeats — a copy-paste that happened once usually happened twice.
**Owner:** marketing (rewrite in the CMS). **Status: OPEN.**
