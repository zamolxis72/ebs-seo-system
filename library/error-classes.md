# Error classes: the AI SEO system

What goes wrong in this system, how it was caught, and what now prevents it. Same rule as the article system's
register (`ebs-article-system/library/error-classes.md`, Andrei 2026-10-13): an error that blocks is fixed in the
same run; one that doesn't is stacked; **a class seen a second time gets a prevention in code**, then it is
`learned`. A class with no prevention is `open`. Errors in the article or case-study scripts are recorded in
their own repo's register; this one holds errors in the rules, the research and the links between systems.

Started 2026-11-03, from the AI SEO build, its `/aif-review` and the test run (`scripts/test_ai_seo.py`).

| id | class | caught by | prevention | state |
|---|---|---|---|---|
| S01 | one limit stated in several homes with different values (meta description 150–160 in `b2b-seo-audit`, 120–160 in the article monitor, ~150 in case studies) | the AI SEO limits triage (2026-11-03) | one home, `library/ai-seo-limits.md`; scripts load it with no fallback; `test_ai_seo.py` T1 and T15 | learned |
| S02 | an undocumented claim stated as fact in a research reference (AI crawlers "do not run JavaScript"), against the repo's own "never state as fact" list | `/aif-review` of PR #9 | none in code; a review catches it | open |
| S03 | a reference to something that exists only on an unmerged branch. Seen **three times** on 2026-11-03: P23 cited from `main`; board cards `ART.COST1` and `M7.gitlab` link to branch-only file URLs; the problem log is split (P1–P22 on `main`, P23–P28 only on `findings/a0-live-defects-2026-09-10`, unmerged since 2026-09-10) | `/aif-review`; the test run | `test_ai_seo.py` T17 (every cited P-number exists on `origin/main`) and T18 (no doc or board card links a file on a non-main branch; proven to fail on the old card URL); the two cards re-pointed at `main` paths | learned |
| S04 | a method written down but never run (AI-citation tracking until 2026-11-03; the full site audit, never; the 2-week GSC refresh, 11 weeks late) | the coverage audit (2026-11-03) | `services/auditing.md` cadence table with a last-run line; the map's State column | detection only |
| S05 | a rule extended beyond the owner's decision without saying so (the how-to's 40–60-word answer block applied to every article's lede) | the rule-value check (2026-11-03) | Andrei, 2026-11-03: the lede check dropped; the 40–60 rule back to how-to question headings, where he set it | learned |
| S06 | a rule labelled with the wrong purpose (the 2–4 key-reference cap filed under GEO, while the held GEO evidence says citing sources raises AI visibility; the cap is a reader rule, 24ac) | the rule-value check (2026-11-03) | relabelled: GEO floor 2, reader cap 4 (24ac), in the limits table and the monitor line | learned |
| S07 | the strongest measured factor missing from the map (query fan-out coverage, r = 0.77 in the Ahrefs AI Overview study held in `ai-visibility.md`; the article monitor checks it, the map never listed it) | the rule-value check (2026-11-03) | the map's first row is fan-out coverage; `services/writing.md` lists it | learned |
