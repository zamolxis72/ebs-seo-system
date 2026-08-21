# Entity register — what the site already claims

> **Read `entity-health.md` first.** This file is the **claims** layer: what each surface was built
> to target. It never holds a metric. Whether a claim is actually held, contested or free is the
> **health** view, derived from a dated GSC snapshot — and that is the file to consult before a title
> settles. Method: `../library/entity-health-method.md`.

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
- **No volumes, no difficulty, no positions here.** The only measured column in this file is the
  observed probe, and it is a query rather than a number. Everything else lives in `entity-health.md`
  against its snapshot date, per `intake/README.md`.
- The 17 live case studies come from the "Latest Case Studies" strip, which appeared identically on
  both captured pages. Treat the set as **complete as of 2026-08-04**, not as guaranteed exhaustive.
- The **service and industry pages come from the site navigation** in the same capture, so that set is
  as complete as the nav was. Two consulting sub-pages exist outside the nav and were found in the
  GSC pull instead; there may be more, and only a crawl would settle it.
- **Blog posts are deliberately absent.** `ebs-article-system/library/content-map.md` holds the blog
  inventory and its collision notes. Duplicating them here would create the competing registry this
  file exists to avoid.
- Overlaps recorded under "Observations" are **observed facts about what is claimed**. Whether an
  overlap costs anything is unmeasured, and nothing here forecasts a ranking.

---

## 1. Live case studies (17, as of 2026-08-04)

URL pattern: `/en/case-studies/<slug>`.

The **observed probe** column is the query GSC reports the page is actually found for
(`gsc-pages.top_keyword`, snapshot 2026-08-14). It is the join key to `entity-health.md` — observed,
not authored, which is why it is allowed in this file when no other metric is. `—` means the page sat
below that snapshot's reporting floor: absent, not proven zero.

| Slug | Live title | Primary entity | Supporting entities | Cluster | Observed probe |
|---|---|---|---|---|---|
| `/en/case-studies/non-bank-factoring-digitalization` | A factoring lender that transformed funding into a 70%-faster edge | factoring digitalization | non-bank lender, straight-through processing, KYC, e-invoicing, credit bureau | Credit & lending | factoring cloud · factoring platform |
| `/en/case-studies/online-credit-system-for-individuals-and-businesses` | Digital credit platform that approves loans 60% faster for a bank | digital credit platform | loan origination, SME lending, bank | Credit & lending | ebs loans *(brand)* |
| `/en/case-studies/1c-crm-integration-credit-management` | A low-code CRM on top of 1C, that grew a lender's credit portfolio by 33.5% | credit management CRM | low-code, 1C integration, loan portfolio | Credit & lending | integrated credit reporting |
| `/en/case-studies/banking-app-psd2-ips-compliance` | A modern mobile banking app delivered under urgent PSD2 and IPS rules | mobile banking app | PSD2, instant payments (IPS), regulatory deadline | Banking & payments | — |
| `/en/case-studies/mobile-wallet-for-offline-crypto-payments` | A mobile app that transforms cryptocurrency into everyday payments | crypto payments wallet | POS integration, offline payments, EU/Asia | Banking & payments | ebs wallet *(brand)* |
| `/en/case-studies/digital-tax-returns-germany-diaspora` | A tax-return platform that lets the German diaspora file in under 20 minutes | digital tax return platform | Elster integration, cross-border finance, diaspora, multilingual UX | Cross-border finance | — |
| `/en/case-studies/educational-platform-for-an-online-english-school` | An educational platform for Moldova's leading English-language school | education platform | online school, systems integration, Moldova | Education | — |
| `/en/case-studies/academic-management-system-for-multi-campus-institution` | Replacing a 15-year-old PHP system academic system for a global education organization | academic management system | legacy replacement, multi-campus, scheduling | Education | integrated campus management |
| `/en/case-studies/educational-app-and-platform-for-parents-on-web` | A platform that brought science-based parenting to 2M+ parents | parenting education app | subscription product, consumer scale | Education | — |
| `/en/case-studies/e-admission-system-for-moldova` | A platform unifying MD's university admissions for students, universities, and the ministry | university admissions system | e-gov, ministry, multi-stakeholder platform, Moldova | E-gov / public sector | e admi |
| `/en/case-studies/queue-system-for-md-customs` | A digital queue system that lets truck drivers book border crossings in advance | border crossing queue system | customs, logistics, e-gov, Moldova | E-gov / public sector | — |
| `/en/case-studies/postal-service-digital-transformation` | A postal transformation that made international shipping affordable | postal digital transformation | international shipping, state operator, logistics | E-gov / public sector | e postal service · innovative postal services |
| `/en/case-studies/ecommerce-marketplace-for-classified-ads` | A redesigned, mobile-first marketplace built for Tanzania's mobile majority | classifieds marketplace | mobile-first redesign, data migration, Tanzania / emerging market | Marketplace & commerce | *(`site:` operator — no usable probe)* |
| `/en/case-studies/marketplace-to-help-pets-find-their-home` | A pet adoption marketplace with AI, escrow, and native apps | pet adoption marketplace | escrow, payment processing, AI, native apps | Marketplace & commerce | pets4homes payment fee *(competitor brand)* |
| `/en/case-studies/digital-optical-showroom-application` | A unified ERP and app connecting Lensa's optical stores and e-commerce | omnichannel retail ERP | optical retail, e-commerce, in-store app, Lensa | Marketplace & commerce | — |
| `/en/case-studies/gift-giving-application` | A digital gifting app that makes sending a gift as easy as a text | digital gifting app | consumer app, campaign mechanics | Marketplace & commerce | prsnt *(product name)* |
| `/en/case-studies/system-converting-calls-to-insights` | AI call intelligence that made QA review 80% faster for a trading firm | AI call intelligence | speech analytics, QA automation, CRM sync, trading firm | AI & data | — |

## 2. Live service and industry pages (13 + 2 hubs, as of 2026-08-04)

The permanent commercial surfaces. Unlike case studies these are not added to over time, so the
register's job here is different: it records **which hub each case-study cluster should be routing
into**, and which service entities the site claims but does not yet hold.

Slugs from the same 2026-08-04 nav capture. Observed probes from snapshot `gsc-2026-08-14`.

### Services — `/en/it-services/<slug>`

| Slug | Primary entity | Supporting entities | Observed probe |
|---|---|---|---|
| `/en/it-services` *(hub)* | IT services | — | ebs *(brand)* |
| `/en/it-services/digital-transformation` | digital transformation consulting | DX strategy, modernisation | *(`site:` operator — no usable probe)* |
| `/en/it-services/ai-consulting` | AI consulting | AI strategy, adoption | — |
| `/en/it-services/consulting` | IT consulting | advisory | ebs integrator *(brand)* |
| `/en/it-services/consulting/cto-as-a-service` | CTO as a service | fractional CTO, technical leadership | cto consulting services |
| `/en/it-services/consulting/business-analysis` | business analysis | requirements, discovery | business analysis integration services |
| `/en/it-services/software-development` | custom software development | product engineering | *(`site:` operator — no usable probe)* |
| `/en/it-services/cloud-engineering` | cloud engineering | cloud migration, infrastructure | — |
| `/en/it-services/data-engineering-ai` | data engineering and AI | data integration, pipelines | engineering data integration services |
| `/en/it-services/agile-development-teams` | agile development teams | dedicated teams, delivery | *(`site:` operator — no usable probe)* |
| `/en/it-services/staff-augmentation` | staff augmentation | dedicated engineers, capacity | engineering staff augmentation services |

`consulting/cto-as-a-service` and `consulting/business-analysis` were **not in the captured nav** —
they surfaced in the GSC pull. They are live and earning impressions but sit outside the main
navigation, which is worth knowing before anything is linked to them.

### Industries — `/en/industries/<slug>`

Each industry hub is the **link target for a case-study cluster** recorded in section 1. That mapping
is the main reason these pages belong in the register.

| Slug | Primary entity | Case-study cluster it should anchor | Observed probe |
|---|---|---|---|
| `/en/industries` *(hub)* | industries served | — | ebs-integrator *(brand)* |
| `/en/industries/fintech` | fintech software development | **Credit & lending (3), Banking & payments (2), Cross-border finance (1)** — the deepest vertical, 6 cases | ebs fintech *(brand)* |
| `/en/industries/retail-ecommerce` | retail and ecommerce software | **Marketplace & commerce (4)** | integrated ecommerce solutions for your business |
| `/en/industries/egov-public-sector` | e-gov and public sector software | **E-gov / public sector (3)** | egov service remote |
| `/en/industries/edtech` | edtech software development | **Education (4)** | *(`site:` operator — no usable probe)* |

**Every case study in section 1 has an industry hub to route into, and one cluster has none.** The
AI & data cluster (`system-converting-calls-to-insights`) has no matching industry page; its natural
home is a service page (`ai-consulting` or `data-engineering-ai`) rather than an industry hub.

## 3. In the pipeline, not live

**Build Green — carbon platform refactor.** Status per `ebs-case-study-system/case-studies/build-green/locked-content.md`:
`noindex` on, excluded from the sitemap, unlinked. Locked SEO fields:

- Slug `carbon-management-platform-refactor` → `/en/case-studies/carbon-management-platform-refactor`
- SEO title: *Carbon software refactored for BuildGreen | EBS Integrator*
- Declared keywords: carbon accounting software · CSRD reporting · ESG reporting platform ·
  emissions management software · software refactoring · legacy platform modernisation ·
  green construction · building certification

⚠ **CORRECTION 2026-08-21 — the status above is contradicted by the live site.** BuildGreen is
**live and in the sitemap**, at `/en/case-studies/test-page-case-1`, serving H1 *"Refactored carbon
and CSRD platform for green building certification"*. So `noindex` / excluded-from-sitemap / unlinked
are all untrue as stated, and the declared slug
`/en/case-studies/carbon-management-platform-refactor` serves site chrome with no case-study content.
The locked-content file in `ebs-case-study-system` has not been re-read here, so it is unknown whether
it is also stale or whether the site diverged from it.

**Nothing above is edited, because what it should say depends on a decision that has not been taken:**
does this case ship at a real slug, or come down? Filed as **P9** in
`reports/site-problems-log.md`. The keyword claims below are left as recorded — they were the plan for
a page at the declared slug, and that page does not exist yet.

**This one opens a new window.** No live surface claims carbon, ESG, CSRD or emissions. Its only
adjacency to the existing map is *legacy platform modernisation*, which
`academic-management-system-for-multi-campus-institution` also claims (15-year-old PHP replacement) —
worth an internal link, not a conflict, since the verticals do not touch.

**Articles.** Statuses live in `ebs-article-system/library/content-map.md` and are not restated here:
the fintech spoke is FINAL and unpublished, the DX pillar draft is parked. The blog pages that
currently rank, and their three recorded collision notes, are in that file's "Existing article
inventory (Ahrefs audit, 2026-07-16)".

## 4. Observations for the next title decision

Not verdicts. Overlap is recorded because it should be seen before a title is chosen, not because a
cost has been measured.

> **As measured on 2026-08-14, none of the overlaps below is contested** — they are claims, not
> contests, because most of these pages hold nothing yet. The numbers behind that verdict, the
> per-page states, and the entities other surfaces hold instead all live in `entity-health.md`. They
> are deliberately not repeated here: this file carries claims, and a metric copied into it would be
> wrong within a fortnight with nothing to signal that it had gone stale.

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
- **The service pages claim entities they do not hold.** Four of the eleven are found only by `site:`
  enumeration or a brand term, including `digital-transformation` and `software-development` — the
  two most commercially load-bearing. A service entity is claimed by having a page; it is held by
  ranking for the service, and on this evidence most are not. New titles cannot lean on a service
  page as an authority target until that changes.
- **Every case cluster has a hub except AI & data.** Section 2 maps the four industry hubs to their
  clusters. The AI case study has no industry page, and the site's AI weight sits entirely in the
  article clusters, so an AI hub is a structural gap rather than a title collision.

## 5. How to append

When a surface ships, add its row in the same session, not later:

1. **Before titles are proposed:** read `entity-health.md` first, then sections 1, 2 and 4 here.
   State which existing cluster the new surface supports, or which entity nothing here claims yet.
   For a case study, name the industry hub it routes into (section 2); if none fits, say so.
2. **Where two surfaces would claim the same primary entity:** surface it as a decision —
   consolidate, differentiate the mechanism, or accept the overlap and record why. Never resolve it
   silently.
3. **After it ships:** append slug, live title, primary entity, supporting entities, cluster. Record
   what the page actually targets, not what it was hoped to rank for.
4. **Metrics stay out** until pulled live or quoted from a dated snapshot.
