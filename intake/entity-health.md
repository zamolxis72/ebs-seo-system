# Entity health — read this first

**Generated, never hand-edited.** Derived from `entity-register.md` (claims) joined to
`snapshots/gsc-2026-08-14.md` (measurements). If a line here is wrong, the register or the next
snapshot is what changes — an edit here would be a fourth hand-maintained file, and it would rot.
Method: `../library/entity-health-method.md`.

**Built from:** snapshot `gsc-2026-08-14` · window 2026-05-14 → 2026-08-13 · **baseline pass.**
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

## Entities the site actually holds — and who holds them

Not in the register, because the register covers case studies and articles. These are what earns the
impressions, and any new title has to be chosen against them.

| Entity | Holder | Impr / Pos | State | What can be done |
|---|---|---|---|---|
| big data in retail *(+6 variants)* | `/en/blog/what-does-big-data-mean-for-modern-retail` | 3,771 / 17.5 | **OWNED**, 0 clicks | `content-map.md` already reserves this. A future AI × retail spoke must not re-target it — upgrade this post or pick a distinct primary and interlink |
| retail technology & store digitalization | `/en/blog/how-technology-and-data-helps-your-store…` | 1,837 / 23.8 | **OWNED** | Second retail holder. Any retail spoke has two incumbents to route around, not one |
| customer pain points | `/en/blog/customer-pain-points` | 1,534 / 42.7 | **OWNED**, weak | Held at a poor position |
| data-centric vs data-driven | `/en/blog/basics-data-centric-vs-data-driven…` | 1,240 / 33.9 | **OWNED** | Adjacent to the DX pillar's territory. Interlink, do not re-target |
| banking process automation | `/en/blog/what-is-banking-process-automation…` | 1,199 / 21.7 | **OWNED** | Already flagged in `content-map.md` as adjacent to reserved "ai in banking". **This post, not the banking case study, is the site's banking entity holder** |
| integrated ecommerce / retail ERP | `/en/industries/retail-ecommerce` | 1,139 / 59.7 | **OWNED**, weak | An industry hub that ranks; the natural hub for the optical-retail case |
| dx digital transformation | `/en/blog/what-digital-transformation-dx-is-for-business-today` | 846 / 15.4 | **OWNED** | **The planned DX pillar has an incumbent.** Resolve ownership before the pillar publishes |
| django orm vs sqlalchemy | `/en/blog/django-orm-vs-sql-alchemy` | 1,222 / 9.2 | **OWNED** | Off-cluster dev topic, ranks well. Protect, ignore |
| fintech (branded) | `/en/industries/fintech` | 125 / 16.7 | **UNPROVEN** on demand | Found as "ebs fintech". `content-map.md` Cluster 2 interlinks here; the hub itself holds no non-brand entity yet |

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
5. **Two service pages are found only by domain enumeration** (`/en/it-services/digital-transformation`,
   `/en/it-services/software-development`), which independently corroborates P3 in the problems log.

## Next pass

Re-run the two calls with the same window length in ~2 weeks. What to look for: any `top_url` that
has changed (CONTESTED), any UNPROVEN case study that has crossed the floor, and whether the DX
incumbent holds.
