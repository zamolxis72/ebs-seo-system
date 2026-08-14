# Entity register — what the site already claims

The site-wide map of which entities each published surface targets. Read it **before** proposing a
new title, and append to it **after** a surface ships.

**Why it exists.** Every published title claims a set of entities. Without one place recording those
claims, a new title silently competes with a page already live, and two surfaces chasing the same
entity split their own signal instead of compounding it. The register makes the current situation
visible so each new title lands deliberately: it either **supports** an entity the site already holds,
or **opens a new window** on an entity nothing here claims yet. "Competes with our own page" is the
failure case, and it should be a decision taken in the open, never an accident.

## Division of authority — this file does not own keywords

| File | Owns |
|---|---|
| `ebs-article-system/library/content-map.md` | **Article keyword ownership.** Its Rule 1 (one primary keyword = one article, forever) binds every new article. Also holds the blog inventory from the Ahrefs audit of 2026-07-16 |
| **this file** | The **site-wide entity map** across all surfaces — case studies, articles, service and industry pages |

References run one way and by reference only, per the umbrella boundary rule: this file points at
`content-map.md`, never restates it. A new *article* still clears `content-map.md` first; this
register tells it what the rest of the site is already standing on.

## Sourcing and limits — read before trusting a row

- Entities below are **derived from live titles and slugs**, captured from the saved page captures of
  **2026-08-04** (`ebs-case-study-system/intake/*.html`, gitignored). Reading a title for what it
  claims is interpretation of published fact; it is not a metric.
- **No volumes, no difficulty, no positions.** Ahrefs and Search Console were not pulled for this
  pass. Any such column stays empty until it is pulled live or quoted from a dated snapshot, per
  `intake/README.md`.
- The 17 live case studies come from the "Latest Case Studies" strip, which appeared identically on
  both captured pages. Treat the set as **complete as of 2026-08-04**, not as guaranteed exhaustive.
- Overlaps recorded under "Observations" are **observed facts about what is claimed**. Whether an
  overlap costs anything is unmeasured, and nothing here forecasts a ranking.

---

## 1. Live case studies (17, as of 2026-08-04)

URL pattern: `/en/case-studies/<slug>`.

| Slug | Live title | Primary entity | Supporting entities | Cluster |
|---|---|---|---|---|
| `non-bank-factoring-digitalization` | A factoring lender that transformed funding into a 70%-faster edge | factoring digitalization | non-bank lender, straight-through processing, KYC, e-invoicing, credit bureau | Credit & lending |
| `online-credit-system-for-individuals-and-businesses` | Digital credit platform that approves loans 60% faster for a bank | digital credit platform | loan origination, SME lending, bank | Credit & lending |
| `1c-crm-integration-credit-management` | A low-code CRM on top of 1C, that grew a lender's credit portfolio by 33.5% | credit management CRM | low-code, 1C integration, loan portfolio | Credit & lending |
| `banking-app-psd2-ips-compliance` | A modern mobile banking app delivered under urgent PSD2 and IPS rules | mobile banking app | PSD2, instant payments (IPS), regulatory deadline | Banking & payments |
| `mobile-wallet-for-offline-crypto-payments` | A mobile app that transforms cryptocurrency into everyday payments | crypto payments wallet | POS integration, offline payments, EU/Asia | Banking & payments |
| `digital-tax-returns-germany-diaspora` | A tax-return platform that lets the German diaspora file in under 20 minutes | digital tax return platform | Elster integration, cross-border finance, diaspora, multilingual UX | Cross-border finance |
| `educational-platform-for-an-online-english-school` | An educational platform for Moldova's leading English-language school | education platform | online school, systems integration, Moldova | Education |
| `academic-management-system-for-multi-campus-institution` | Replacing a 15-year-old PHP system academic system for a global education organization | academic management system | legacy replacement, multi-campus, scheduling | Education |
| `educational-app-and-platform-for-parents-on-web` | A platform that brought science-based parenting to 2M+ parents | parenting education app | subscription product, consumer scale | Education |
| `e-admission-system-for-moldova` | A platform unifying MD's university admissions for students, universities, and the ministry | university admissions system | e-gov, ministry, multi-stakeholder platform, Moldova | E-gov / public sector |
| `queue-system-for-md-customs` | A digital queue system that lets truck drivers book border crossings in advance | border crossing queue system | customs, logistics, e-gov, Moldova | E-gov / public sector |
| `postal-service-digital-transformation` | A postal transformation that made international shipping affordable | postal digital transformation | international shipping, state operator, logistics | E-gov / public sector |
| `ecommerce-marketplace-for-classified-ads` | A redesigned, mobile-first marketplace built for Tanzania's mobile majority | classifieds marketplace | mobile-first redesign, data migration, Tanzania / emerging market | Marketplace & commerce |
| `marketplace-to-help-pets-find-their-home` | A pet adoption marketplace with AI, escrow, and native apps | pet adoption marketplace | escrow, payment processing, AI, native apps | Marketplace & commerce |
| `digital-optical-showroom-application` | A unified ERP and app connecting Lensa's optical stores and e-commerce | omnichannel retail ERP | optical retail, e-commerce, in-store app, Lensa | Marketplace & commerce |
| `gift-giving-application` | A digital gifting app that makes sending a gift as easy as a text | digital gifting app | consumer app, campaign mechanics | Marketplace & commerce |
| `system-converting-calls-to-insights` | AI call intelligence that made QA review 80% faster for a trading firm | AI call intelligence | speech analytics, QA automation, CRM sync, trading firm | AI & data |

## 2. In the pipeline, not live

**Build Green — carbon platform refactor.** Status per `ebs-case-study-system/case-studies/build-green/locked-content.md`:
`noindex` on, excluded from the sitemap, unlinked. Locked SEO fields:

- Slug `carbon-management-platform-refactor` → `/en/case-studies/carbon-management-platform-refactor`
- SEO title: *Carbon software refactored for BuildGreen | EBS Integrator*
- Declared keywords: carbon accounting software · CSRD reporting · ESG reporting platform ·
  emissions management software · software refactoring · legacy platform modernisation ·
  green construction · building certification

**This one opens a new window.** No live surface claims carbon, ESG, CSRD or emissions. Its only
adjacency to the existing map is *legacy platform modernisation*, which
`academic-management-system-for-multi-campus-institution` also claims (15-year-old PHP replacement) —
worth an internal link, not a conflict, since the verticals do not touch.

**Articles.** Statuses live in `ebs-article-system/library/content-map.md` and are not restated here:
the fintech spoke is FINAL and unpublished, the DX pillar draft is parked. The blog pages that
currently rank, and their three recorded collision notes, are in that file's "Existing article
inventory (Ahrefs audit, 2026-07-16)".

## 3. Observations for the next title decision

Not verdicts. Overlap is recorded because it should be seen before a title is chosen, not because a
cost has been measured.

- **Credit and lending carries three live surfaces** (`non-bank-factoring-digitalization`,
  `online-credit-system-for-individuals-and-businesses`, `1c-crm-integration-credit-management`),
  and `banking-app-psd2-ips-compliance` sits next to them. They differentiate on mechanism —
  factoring, origination speed, portfolio CRM — rather than on entity. A fourth lending case needs
  its own mechanism, or it belongs as a section inside one of these.
- **Education carries four**, split cleanly between institutional
  (`academic-management-system…`, `e-admission-system…`) and consumer
  (`educational-platform-for-an-online-english-school`, `educational-app-and-platform-for-parents…`).
  That split is the differentiator worth preserving in any new title.
- **E-gov and public sector carries three**, all Moldova-adjacent, all distinct services
  (admissions, customs, post). The entity holding them together is the sector, not a product.
- **AI is claimed once on the case-study side** (`system-converting-calls-to-insights`) and is the
  spine of the article side (Cluster 1 and 2 in `content-map.md`). Any new AI case study should be
  chosen to feed those clusters as evidence, since they are the surfaces built to rank for it.
- **Fintech is the deepest vertical here** — factoring, credit, banking, crypto payments,
  cross-border tax — and `content-map.md` Cluster 2 already interlinks into `/en/industries/fintech`.
  That page is the natural hub for these cases.

## 4. How to append

When a surface ships, add its row in the same session, not later:

1. **Before titles are proposed:** read sections 1 and 3. State which existing cluster the new
   surface supports, or which entity nothing here claims yet.
2. **Where two surfaces would claim the same primary entity:** surface it as a decision —
   consolidate, differentiate the mechanism, or accept the overlap and record why. Never resolve it
   silently.
3. **After it ships:** append slug, live title, primary entity, supporting entities, cluster. Record
   what the page actually targets, not what it was hoped to rank for.
4. **Metrics stay out** until pulled live or quoted from a dated snapshot.
