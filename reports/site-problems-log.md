# Site problems log (for future investigation / fixes)

Evidence-based issues found during article pipeline work. Each item: evidence, why it matters, proposed owner. Update status as items get fixed. Last updated: **2026-08-14** (P8 added; P1 and P3 corroborated from Search Console).

## P1 — GitLab instance publicly exposed and dominating the link graph — SEVERITY: HIGH

**Evidence (Ahrefs internal-links, 2026-07-16):** pages.ebs-integrator.com is a live, publicly crawlable GitLab (project explorer, sign-in pages, hundreds of .atom feeds). Its URLs receive 2,600+ internal links each — 28x more than the homepage (95). Project/topic names are exposed (client project names visible, e.g. "NettBureau platform").
**Why it matters:** (a) possible confidentiality issue — internal project names publicly listed; (b) crawl budget and link-graph dilution — the crawlable surface of the "site" is mostly GitLab noise, not marketing pages.
**Fix direction:** block pages.* from indexing (robots + noindex) or put it behind auth entirely. Check what's publicly visible ASAP (open pages.ebs-integrator.com/explore in incognito — my fetch returned empty, unconfirmed).
**On robots.txt:** NOT sufficient alone. robots.txt only asks crawlers not to crawl; it does not remove indexed URLs (Google keeps them, un-crawled) and does not stop humans. Correct order: (1) GitLab Admin → Visibility and access controls → restrict "Public" visibility (or VPN/IP-allowlist the instance), (2) GSC property for pages.* → Removals, (3) robots.txt disallow-all as belt-and-braces AFTER access is closed. Disavow is irrelevant here (that tool is for external spam backlinks only).
**Owner:** DevOps + management (confidentiality call). **Status: OPEN — investigate first.**

**Corroborated from Search Console, 2026-08-14** (`intake/snapshots/gsc-2026-08-14.md`): `pages.ebs-integrator.com` is not merely crawlable, it is **earning impressions in Google**. `pages.ebs-integrator.com/explore/projects/topics/meapp` drew 248 impressions at position 11.0, and `pages.ebs-integrator.com/` a further 47. The query `site:ebs-integrator.com` returns **324 URLs** with a GitLab project-topic page as `top_url`. The "my fetch returned empty, unconfirmed" caveat above is now resolved: it is indexed, and someone is running site: queries against the domain. Severity holds at HIGH.

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

**Corroborated from Search Console, 2026-08-14:** over the 90 days to 2026-08-13 the page drew **45 impressions and 0 clicks**, and its `top_keyword` is the operator `site:ebs-integrator.com` — meaning the only query reliably surfacing it is somebody enumerating the domain, not demand. The same pattern holds for `/en/it-services/software-development` (57 impressions, same operator probe). "Ranks for zero keywords" is now measured rather than inferred.

## P4 — Case-studies listing renders client-side only — SEVERITY: MEDIUM

**Evidence:** /en/case-studies shows "Loading..." without JavaScript (agent fetch, 2026-07-16). Individual case pages exist but the listing's links may not be reliably crawled; several cases rank for nothing.
**Why it matters:** case studies are EBS's best proof assets and interlink targets for the whole article strategy.
**Fix direction:** SSR/prerender the listing, or add static links (footer sitemap page). Verify in Google Search Console: which case URLs are indexed.
**Owner:** web dev. **Status: OPEN — verify indexation in GSC first.**

## P5 — Redirect-hop internal links — SEVERITY: LOW

**Evidence:** 94 internal links each point to non-/en URLs (e.g. /it-services/consulting) that 307-redirect to /en/ versions. 307 (temporary) instead of 301/308 (permanent) for most.
**Why it matters:** minor equity loss + crawl waste; temporary redirects don't consolidate signals.
**Fix direction:** internal links should target final /en/ URLs directly; make redirects permanent (308/301).
**Owner:** web dev. **Status: OPEN.**

## P6 — Orphaned / broken case study assets — SEVERITY: LOW

**Evidence:** German diaspora tax-return case shown on homepage rail but its page is a noindex placeholder (no discoverable URL). Legacy URL patterns (/case-studies/cloud-schedule/, /en/about/case-studies/*) still indexed by Google.
**Fix direction:** publish or remove the tax case; 301 legacy patterns to current URLs.
**Owner:** web dev + content. **Status: OPEN.**

## P7 — robots.txt + structured data (schema) audit on the main site — SEVERITY: MEDIUM (enhancement)

**To investigate:** (a) does ebs-integrator.com/robots.txt exist, what does it allow/block, does it reference the sitemap; (b) is /en/sitemap.xml valid and submitted in GSC; (c) which pages carry JSON-LD today — needed: Organization (sitewide), Article (blog posts), BreadcrumbList; FAQ schema only where a real FAQ exists (service pages have FAQs — check if marked up).
**Why it matters:** schema won't fix rankings by itself but improves rich results, entity recognition, and AI-search citability (Brand Radar relevance). Cheap wins.
**Note:** the article pipeline handles its own part — every new article ships with Article + Organization JSON-LD from day one (added to playbook step 6).
**Owner:** web dev + SEO pass (fold into the b2b-seo-audit run). **Status: OPEN — documented, deferred.**

## P8 — Two URL variants of the homepage rank independently — SEVERITY: MEDIUM

**Evidence (Search Console via Ahrefs project 9118279, 90 days to 2026-08-13, `intake/snapshots/gsc-2026-08-14.md`):** both `https://ebs-integrator.com/en/home` (139 keywords, 1,851 impressions, 340 clicks, avg pos 14.3) and `http://www.ebs-integrator.com/` (54 keywords, 1,249 impressions, 19 clicks, avg pos 7.4) earn impressions, and both report `ebs integrator` as their top keyword. Two protocol/host variants of the same destination are being served and measured separately.

**Why it matters:** the `www` + `http` variant carries a *better* average position than the canonical one but converts at 1.5% CTR against 18.4%, so the variant Google sometimes prefers is the weaker experience. Signals that should accumulate on one URL are being reported against two, and the split is invisible on the page itself.

**What this is NOT:** the same pull shows `ebs integrator` returning **24 URLs** and `ebs` returning 10. That is *not* a defect — Google returns sitelinks on a navigational brand query, so home, about, career and contact all appearing is expected behaviour. Only the protocol/host duplication above is actionable. Recorded because the 24-URL figure looks alarming and will be re-encountered; `library/entity-health-method.md` excludes branded queries for this reason.

**Fix direction:** confirm `http://` and `www.` both 301 to the canonical `https://ebs-integrator.com/en/home` in one hop, and confirm the canonical tag agrees. Check whether the GSC property set covers both variants (it evidently reports them separately). Verify with a redirect trace before changing anything — this may already be configured and mis-measured rather than genuinely duplicated.

**Owner:** web dev / DevOps. **Status: OPEN — verify the redirect chain first.**

---

**Suggested next step when ready:** run the full b2b-seo-audit skill against the site — P1/P2/P3 found incidentally; a systematic pass will catch the rest.

**GSC access now exists** (Ahrefs project 9118279, verified; `gsc-pages` and `gsc-keywords` cost 0 API units), so the P4 verification noted here as blocked is now cheap to run. Snapshots land in `intake/snapshots/`; the standing method is `library/entity-health-method.md`.
