# Entity health — the method

How to tell whether an entity the site claims is actually held, contested, or free. Reusable per
pass, so it is not re-derived. Companion to `../intake/entity-register.md` (the claims) and
`../intake/entity-health.md` (the derived view).

## The three layers, and why they are not one file

| Layer | File | Cadence | Written by |
|---|---|---|---|
| **Claims** | `intake/entity-register.md` | on ship | producers, by hand. **Never holds a metric** |
| **Measurements** | `intake/snapshots/gsc-<date>.md` | each refresh | pulled, immutable, never edited |
| **Decisions** | register decision notes · `reports/site-problems-log.md` | when taken | by hand. Entity calls stay with the entity; **site defects go to the problems log** |
| **→ the read surface** | `intake/entity-health.md` | regenerated | derived from the two above |

**Why not one file.** A claim stays true for a year; a metric is wrong in a fortnight. Side by side
they look equally authoritative, so a stale number gets used to decide a title and nobody notices,
because nobody re-reads a number when they change a field. The case-study workstream already paid
for this exact failure and wrote it down: *"only the commentary rotted, and only because it was in
the wrong file."* Separating by write cadence is the fix.

**Why not three files to read, either.** Three files to consult before naming a page is why nobody
consults any. Hence one generated view. `entity-health.md` is **never hand-edited** — an edit means
either the register or a new snapshot is what should change. That rule is the only thing keeping it
from becoming a fourth hand-maintained file that rots.

## The pull

Two calls, both **free (0 API units)**, against the Ahrefs GSC integration:

```
gsc-pages     project_id=<id>, date_from, date_to, limit=<n>
gsc-keywords  project_id=<id>, date_from, date_to, limit=<n>,
              where={"field":"impressions","is":["gte",40]}
```

- `gsc-pages` → per URL: `top_keyword`, `keywords_count`, clicks, impressions, position.
- `gsc-keywords` → per query: **`urls_count`** (how many of our URLs earned an impression for it) and
  **`top_url`** (the one Google favours).

**Probe queries are observed, never authored.** Each page's `top_keyword` is what the site reports
that page is found for, so no keyword list is invented and the never-invent rule holds. `urls_count`
cannot be filtered server-side; filter impressions instead and read `urls_count` off the rows.

**Always record the floor.** A capped `limit` means pages below the last row are *absent*, not
*zero*. Write the floor into the snapshot, and never let a later reading turn "below the floor" into
"has no traffic".

## The states

Join register to snapshot on URL. Each state carries its own verdict on what may be done.

| State | Test | What can be done |
|---|---|---|
| **OPEN** | no surface claims the entity | **Free to take.** A new window |
| **OWNED** | declared owner == `top_url`, `urls_count` = 1 on a non-brand query | **Support only.** New titles link to the owner and do not re-target it |
| **CONTESTED** | *primary:* `top_url` flips between snapshots. *secondary:* `urls_count` > 1 on a **non-brand** query | **Resolve before adding anything.** Consolidate, differentiate the mechanism, or accept and record why |
| **MISOWNED** | `top_url` ≠ the page we declared | **Fix before extending.** Google picked a different page than intended |
| **UNPROVEN** | claimed, but impressions below the floor | **Do not add a second claimant yet.** Nothing is held to defend |

**MISOWNED is the state a claims register alone cannot see**, and it is the quiet failure: the page
ships, another page absorbs the query, and a cluster gets built on a claim that never landed.

## Two exclusions, or every snapshot is noise

**1. Branded queries are excluded from CONTESTED.** On a navigational brand query Google deliberately
returns sitelinks, so home, about, career and contact all earning impressions is healthy behaviour.
In the 2026-08-14 pull `ebs integrator` returned **24 URLs** and `ebs` returned 10. Left in, the brand
name is flagged as the site's worst cannibalization in every pass, for ever. Exclude the brand and
its variants (`ebs`, `ebs integrator`, `ebs-integrator`, `ebs <anything>`).

**2. Search operators are not queries.** `site:ebs-integrator.com` returned **324 URLs** in the same
pull. That is somebody enumerating the domain, not demand. Exclude `site:`, `filetype:` and the long
operator strings that appear as `top_keyword` on some pages — where a page's observed probe is an
operator string, that page has **no usable probe** and is UNPROVEN until it earns one.

## Reading the first pass

The flip test needs two snapshots, so on a baseline it cannot fire and CONTESTED rests on
`urls_count` alone. Say so in the derived view rather than implying a trend. The second pass is what
proves the design: states should move, and a changed `top_url` should surface as CONTESTED.

## Cadence

Rides the existing ~2-week refresh ritual; no separate schedule. The binding moments are unchanged
and already hooked: **before a title settles** — case studies at the slug lock, articles alongside
`ebs-article-system/library/content-map.md`.

## Boundaries

- `content-map.md` keeps **article keyword ownership**. Health reports on articles; it never
  re-decides what an article owns. Two registries competing is worse than one.
- **No forecasts.** Observed overlap is a fact. "This will derank" is not.
- Every number carries its snapshot date.
