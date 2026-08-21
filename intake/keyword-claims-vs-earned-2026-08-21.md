# Claimed vs earned — case studies, 2026-08-21

Source: `ebs-article-system/intake/snapshots/gsc-keywords-case-studies-2026-08-21.json`
(GSC via Ahrefs MCP, 2026-05-21 → 2026-08-20, impressions ≥ 10, 38 rows) read against the keyword
claims in `ebs-article-system/library/content-map.md`, as rendered by the cluster graph.

## The finding

**16 case studies carry a claimed primary keyword. Not one of them earns the keyword it claims.**

- **7** earn nothing at all above the floor.
- **9** earn something — but for a different query than the one on record.

| Page | Claims | Actually earns |
|---|---|---|
| postal-service-digital-transformation | postal digital transformation | **innovative postal services** — 143 |
| non-bank-factoring-digitalization | factoring digitalization | **factoring platform** — 124 |
| 1c-crm-integration-credit-management | credit management crm | **microlending crm** — 63 |
| e-admission-system-for-moldova | university admissions system | **eadmitere** — 58 |
| mobile-wallet-for-offline-crypto-payments | crypto payments wallet | **ebs wallet** — 23 |
| educational-platform-for-an-online-english-school | education platform | a pasted Google search-operator string — 16 |
| online-credit-system-for-individuals-and-businesses | digital credit platform | **commercial loan engagement platform** — 15 |
| academic-management-system-for-multi-campus-institution | academic management system | **integrated academic management system** — 10 |
| gift-giving-application | digital gifting app | **prsnt** — 10 |
| banking-app-psd2-ips-compliance | mobile banking app | nothing above the floor |
| digital-optical-showroom-application | omnichannel retail erp | nothing above the floor |
| digital-tax-returns-germany-diaspora | digital tax return platform | nothing above the floor |
| ecommerce-marketplace-for-classified-ads | classifieds marketplace | nothing above the floor |
| educational-app-and-platform-for-parents-on-web | parenting education app | nothing above the floor |
| marketplace-to-help-pets-find-their-home | pet adoption marketplace | nothing above the floor |
| queue-system-for-md-customs | border crossing queue system | nothing above the floor |

## The pattern, which is the useful part

The claims are **abstractions** — *digitalization*, *transformation*, *platform*, *system*. The demand
splits two ways, and neither is an abstraction:

1. **Brand and navigational terms.** `ebs wallet`, `prsnt`, `eadmitere`. People already looking for the
   product by name. Nothing in the register targets these.
2. **Concrete product nouns.** `factoring platform`, `innovative postal services`, `microlending crm`,
   `commercial loan engagement platform`. Named things, not named outcomes.

Only **one** keyword in the whole portfolio is held on measured evidence: `big data in retail`, on a blog
article at 815 impressions — and it is a concrete noun too.

## What this does NOT say

- **Absent is not zero.** The floor is 10 impressions for case studies, 25 for blog. A page below it is
  missing from the pull, not proven to earn nothing.
- The blog pull returned **100 rows against a limit of 400**, the same as the 08-20 pull. That looks like an
  API page cap rather than the true tail, so the blog side is a sample.
- One drift finding cleared since 08-20 (`education platform` no longer reads "page found for nothing")
  **only because the page picked up 16 impressions on a junk operator query.** Its keyword node still says
  `held: not-proven`. Read that as noise clearing, not progress.

## Where a decision would go

`ebs-article-system/library/content-map.md`, then rebuild the vault. The graph is generated read-only, so
editing it directly is lost on the next build.
