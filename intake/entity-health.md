# Entity health — read this first

**Generated, never hand-edited.** Derived from `entity-register.md` (claims) joined to
`snapshots/gsc-2026-08-14.md` (measurements). If a line here is wrong, the register or the next
snapshot is what changes — an edit here would be a fourth hand-maintained file, and it would rot.
Method: `../library/entity-health-method.md`.

**Built from:** snapshot `gsc-2026-08-14` · window 2026-05-14 → 2026-08-13 · **baseline pass**,
extended 2026-08-14 with the service and industry pages once they entered the register.
There is no prior snapshot, so the flip test cannot fire yet and every CONTESTED verdict below would
rest on `urls_count` alone. None does. The second pass is what makes trend readable.

---

## The headline: there is no measured cannibalization

**Every non-brand query at or above 40 impressions returns `urls_count` = 1.** One page, one query,
across the whole reported surface. The only multi-URL queries are the brand terms (`ebs integrator`
24 URLs, `ebs-integrator` 13, `ebs` 10) and the `site:` operator (324) — none of which is a
cannibalization signal, both excluded by method.

**That is not the same as "the overlaps are fine."** It is mostly the absence of anything to
cannibalize. Ten of the seventeen live case studies sit below the reporting floor or near it, so the
credit-and-lending pile-up and the four education pages recorded in the register are **not costing
anything measurable, because none of those pages is holding an entity yet.** The risk the register
was built to catch is real and still ahead of us; it has simply not been paid for yet.

**The finding that matters more.** The site's search surface is the **blog**, not the case studies
and not the service pages. Six of the seven highest-impression URLs are blog posts. The single
biggest entity the site holds — `big data in retail`, 1,672 impressions on the head term and six
variants — belongs to a 
post with **0 clicks** at position 13.5. Meanwhile `/en/it-services/digital-transformation`, the
conversion target of the planned pillar, drew **45 impressions** and its observed probe is a `site:`
operator, meaning it is found by people enumerating the domain rather than by demand.

---

## Case studies — state per registered surface

Declared owner is the registered page. Observed values are from the snapshot.

| Entity (registered) | Page | Observed probe | urls_count | Impr / Pos | State | What can be done |
|---|---|---|---|---|---|---|
| postal digital transformation | `postal-service-digital-transformation` | e postal service · innovative postal services | 1 | 565 / 31.7 | **OWNED** | Support only. Best-performing case study on the site. Link new logistics or e-gov work to it |
| factoring digitalization | `non-bank-factoring-digitalization` | factoring cloud · **factoring platform** (138 impr, pos 16.3) | 1 | 451 / 32.0 | **OWNED** | Support only. Holds "factoring platform" outright — the fintech article's named case, and its strongest link target |
| crypto payments wallet | `mobile-wallet-for-offline-crypto-payments` | ebs wallet *(brand-qualified)* | 1 | 192 / 35.0 | **OWNED**, weakly | Support. 36 keywords but the probe is branded, so the entity is held by name recognition, not demand |
| university admissions system | `e-admission-system-for-moldova` | e admi | 1 | 125 / **9.4** | **OWNED** | Support. **Best position of any case study.** The e-gov cluster's natural anchor |
| credit management CRM | `1c-crm-integration-credit-management` | integrated credit reporting | 1 | 109 / 33.4 | **OWNED**, weakly | Support. Holds a narrow entity at a weak position |
| academic management system | `academic-management-system-for-multi-campus-institution` | integrated campus management | 1 | 39 / 41.8 | **UNPROVEN** | No second claimant yet. Nothing held to defend |
| pet adoption marketplace | `marketplace-to-help-pets-find-their-home` | pets4homes payment fee | 1 | 33 / 28.5 | **UNPROVEN** | Probe is a competitor's brand, not our entity |
| digital credit platform | `online-credit-system-for-individuals-and-businesses` | ebs loans *(brand)* | 1 | 26 / 54.4 | **UNPROVEN** | Six keywords total. The lending entity is not held |
| digital gifting app | `gift-giving-application` | prsnt *(product name)* | 1 | 27 / 18.4 | **UNPROVEN** | Found by product name only |
| classifieds marketplace | `ecommerce-marketplace-for-classified-ads` | `site:` operator | — | 28 / 25.3 | **UNPROVEN** | **No usable probe.** Found by domain enumeration, not demand |
| mobile banking app | `banking-app-psd2-ips-compliance` | — | — | below floor | **UNPROVEN** | Below the 25-impression floor of this pull. Absent, not proven zero |
| digital tax return platform | `digital-tax-returns-germany-diaspora` | — | — | below floor | **UNPROVEN** | as above |
| education platform | `educational-platform-for-an-online-english-school` | — | — | below floor | **UNPROVEN** | as above |
| parenting education app | `educational-app-and-platform-for-parents-on-web` | — | — | below floor | **UNPROVEN** | as above |
| border crossing queue system | `queue-system-for-md-customs` | — | — | below floor | **UNPROVEN** | as above |
| AI call intelligence | `system-converting-calls-to-insights` | — | — | below floor | **UNPROVEN** | as above |
| omnichannel retail ERP | `digital-optical-showroom-application` | — | — | below floor | **UNPROVEN** | as above |

**Seventeen surfaces: five OWNED** (three outright, two marked *weakly* — held, but by a branded or
narrow probe rather than by demand) **, twelve UNPROVEN, zero CONTESTED, zero MISOWNED.** *Weakly* is
a qualifier on OWNED, not a sixth state.

## Service and industry pages — state per registered surface

Registered in `entity-register.md` §2. These are the permanent commercial surfaces and the hubs that
case-study clusters route into, so their state governs whether a cluster has an authority target.

| Entity (registered) | Page | Observed probe | Impr / Pos | State | What can be done |
|---|---|---|---|---|---|
| retail and ecommerce software | `/en/industries/retail-ecommerce` | integrated ecommerce solutions… | 1,139 / 59.7 | **OWNED**, weak | The only hub earning real impressions. Anchor for the four Marketplace & commerce cases, though position 59.7 means it is held loosely |
| data engineering and AI | `/en/it-services/data-engineering-ai` | engineering data integration services | 315 / 76.3 | **OWNED**, weak | Holds a long-tail service phrase at the bottom of page 7 |
| CTO as a service | `/en/it-services/consulting/cto-as-a-service` | cto consulting services | 320 / 54.1 | **OWNED**, weak | Highest-impression service page. Outside the main nav |
| fintech software development | `/en/industries/fintech` | ebs fintech *(brand)* | 125 / 16.7 | **UNPROVEN** on demand | **The deepest vertical's hub holds no non-brand entity.** Six fintech cases route into a page found only by brand |
| e-gov and public sector software | `/en/industries/egov-public-sector` | egov service remote | 44 / 11.0 | **UNPROVEN** | Near the floor, but position 11.0 on its probe |
| business analysis | `/en/it-services/consulting/business-analysis` | business analysis integration services | 51 / 44.4 | **UNPROVEN** | Outside the main nav |
| staff augmentation | `/en/it-services/staff-augmentation` | engineering staff augmentation services | 49 / 53.2 | **UNPROVEN** | — |
| IT services *(hub)* | `/en/it-services` | ebs *(brand)* | 202 / 3.7 | **UNPROVEN** on demand | Found by brand only |
| IT consulting | `/en/it-services/consulting` | ebs integrator *(brand)* | 183 / 11.1 | **UNPROVEN** on demand | Found by brand only |
| industries *(hub)* | `/en/industries` | ebs-integrator *(brand)* | 62 / 6.3 | **UNPROVEN** on demand | Found by brand only |
| digital transformation consulting | `/en/it-services/digital-transformation` | `site:` operator | 45 / 10.8 | **UNPROVEN** | **No usable probe.** Corroborates P3 — the pillar's conversion target is found only by domain enumeration |
| custom software development | `/en/it-services/software-development` | `site:` operator | 57 / 28.6 | **UNPROVEN** | **No usable probe.** The most commercially load-bearing service page holds nothing |
| agile development teams | `/en/it-services/agile-development-teams` | `site:` operator | 27 / 41.8 | **UNPROVEN** | No usable probe |
| edtech software development | `/en/industries/edtech` | `site:` operator | 39 / 6.0 | **UNPROVEN** | No usable probe. Four education cases route into it |
| AI consulting | `/en/it-services/ai-consulting` | — | below floor | **UNPROVEN** | Absent from the pull. **The site's AI service page holds nothing**, while AI is the spine of both article clusters |
| cloud engineering | `/en/it-services/cloud-engineering` | — | below floor | **UNPROVEN** | Absent from the pull |

**Sixteen surfaces: three OWNED** (all *weakly* — held by a long-tail service phrase, none outright)
**, thirteen UNPROVEN, zero CONTESTED, zero MISOWNED.** Of the sixteen, **four have no usable probe
at all** (a `site:` operator), **four are found only by brand**, and **two are below the floor
entirely** — so ten of sixteen commercial pages are not found by demand.

## Blog — the entities that actually earn the impressions

Deliberately **not** in the register: `content-map.md` holds the blog inventory and its collision
notes, and duplicating it would create a competing registry. Listed here because any new title has to
be chosen against these, and because they are what the site's search presence actually consists of.

| Entity | Holder | Impr / Pos | State | What can be done |
|---|---|---|---|---|
| big data in retail *(+6 variants)* | `/en/blog/what-does-big-data-mean-for-modern-retail` | 3,771 / 17.5 | **OWNED**, 0 clicks | `content-map.md` already reserves this. A future AI × retail spoke must not re-target it — upgrade this post or pick a distinct primary and interlink |
| retail technology & store digitalization | `/en/blog/how-technology-and-data-helps-your-store…` | 1,837 / 23.8 | **OWNED** | Second retail holder. Any retail spoke has two incumbents to route around, not one |
| customer pain points | `/en/blog/customer-pain-points` | 1,534 / 42.7 | **OWNED**, weak | Held at a poor position |
| data-centric vs data-driven | `/en/blog/basics-data-centric-vs-data-driven…` | 1,240 / 33.9 | **OWNED** | Adjacent to the DX pillar's territory. Interlink, do not re-target |
| django orm vs sqlalchemy | `/en/blog/django-orm-vs-sql-alchemy` | 1,222 / 9.2 | **OWNED** | Off-cluster dev topic, ranks well. Protect, ignore |
| banking process automation | `/en/blog/what-is-banking-process-automation…` | 1,199 / 21.7 | **OWNED** | Already flagged in `content-map.md` as adjacent to reserved "ai in banking". **This post, not the banking case study, is the site's banking entity holder** |
| dx digital transformation | `/en/blog/what-digital-transformation-dx-is-for-business-today` | 846 / 15.4 | **OWNED** | **The planned DX pillar has an incumbent.** Resolve ownership before the pillar publishes |

**The shape of the site, in one line:** the blog holds the entities, the service and industry pages
hold almost nothing, and the case studies sit between the two. A blog post outranks the service page
it should be feeding.

## What this changes

1. **The register's overlap observations stand, but are not urgent.** Credit-and-lending ×3 and
   education ×4 are claims, not contests. Nothing is splitting, because nothing is ranking. Revisit
   when one of them moves to OWNED.
2. **The DX pillar has a live incumbent** at `/en/blog/what-digital-transformation-dx-is-for-business-today`
   (846 impressions, position 15.4). That is an ownership decision to take before publishing, not
   after. Route it through `content-map.md`, which owns article keyword ownership.
3. **Banking is held by a blog post, not the banking case study.** A new banking surface should
   support that post rather than compete with it.
4. **Three case studies have no usable probe** — their observed `top_keyword` is a `site:` operator
   or a competitor's brand. They are findable by name, not by demand.
5. **The commercial layer holds almost nothing.** Of sixteen service and industry pages, three are
   OWNED weakly and none outright. Four are found only by `site:` enumeration —
   `digital-transformation`, `software-development`, `agile-development-teams` and `edtech` — which
   corroborates P3 in the problems log and extends it well beyond the one page P3 named.
6. **Every cluster's hub is weaker than the cluster.** Six fintech cases route into a hub found only
   as "ebs fintech"; four education cases route into an edtech page with no usable probe. Linking a
   case to its hub is still right, but the hub is not currently an authority target — it is a
   destination that needs building.
7. **AI is a structural gap, not a collision.** `ai-consulting` is below the floor, the one AI case
   study is below the floor, and there is no AI industry hub. The site's entire AI weight sits in
   `content-map.md`'s article clusters, which have not published yet.

## Next pass

Re-run the two calls with the same window length in ~2 weeks. What to look for: any `top_url` that
has changed (CONTESTED), any UNPROVEN case study that has crossed the floor, and whether the DX
incumbent holds.
