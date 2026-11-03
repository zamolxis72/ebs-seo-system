"""test_ai_seo.py: test scenarios for the AI SEO system (2026-11-03).

Checks that the limits file is the single home of every number, that every consumer script reads it, fails loudly
without it, and moves when it changes; that the article monitor did not regress against origin/main; and that the
map and service files point only at files that exist. Read-only on the repos: every altered limits file is a temp
copy passed through AI_SEO_LIMITS. Needs ebs-article-system and ebs-case-study-system cloned beside this repo.

    python3 scripts/test_ai_seo.py        exit 0 all pass, 1 any fail
"""
import json, os, re, subprocess, tempfile, glob

G = os.path.expanduser("~/Documents/GitHub")
SEO, ART, CASE = (os.path.join(G, x) for x in ("ebs-seo-system", "ebs-article-system", "ebs-case-study-system"))
LIM = os.path.join(SEO, "library", "ai-seo-limits.md")
ORIG = open(LIM, encoding="utf-8").read()
TMP = tempfile.mkdtemp(prefix="aiseo-")
results = []


def run(cmd, cwd, env_lim=None):
    env = dict(os.environ)
    if env_lim is not None:
        env["AI_SEO_LIMITS"] = env_lim
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def variant(name, text):
    p = os.path.join(TMP, name + ".md")
    open(p, "w", encoding="utf-8").write(text)
    return p


def check(sid, desc, ok, detail=""):
    results.append((sid, desc, ok, detail))


def health(slug, lim=None):
    return run(["python3", "scripts/article_health.py", "articles/" + slug], ART, lim)


def line(out, label):
    m = re.search(r"^\s+(PASS|FAIL) " + re.escape(label) + r".*$", out, re.M)
    return m.group(0).strip() if m else None


machine = json.loads(re.search(r"^## Machine values\b.*?```json\n(.*?)```", ORIG, re.M | re.S).group(1))

# T1 the table and the machine block agree
tbl = ORIG.split("\n## Machine values\n")[0]  # the phrase also appears in the intro
pairs = [("meta", "120–155", (machine["seo"]["meta_min"], machine["seo"]["meta_max"]) == (120, 155)),
         ("title", "≤ 60 characters", machine["seo"]["title_max_with_suffix"] == 60),
         ("paragraph", "≤ 75 words", machine["aeo"]["paragraph_words_max"] == 75),
         ("answer", "40–60 words", machine["aeo"]["answer_block_words"] == [40, 60]),
         ("faq", "at most 5", machine["aeo"]["faq_max"] == 5),
         ("refs", "2–4 primary", machine["geo"]["key_references"] == [2, 4]),
         ("links", "at least 2, target 3+", (machine["seo"]["internal_links_min"], machine["seo"]["internal_links_target"]) == (2, 3)),
         ("slug", "≤ 60 characters", machine["seo"]["slug_max"] == 60)]
bad = [k for k, phrase, ok in pairs if not (ok and phrase in tbl)]
check("T1", "table and machine values say the same numbers", not bad, ", ".join(bad))

# T2 baseline: every article runs (text, --json, --html), no crash
slugs = sorted(os.path.basename(p.rstrip("/")) for p in glob.glob(os.path.join(ART, "articles", "*/")))
crash = []
for s in slugs:
    for extra in ([], ["--json"], ["--html"]):
        rc, out = run(["python3", "scripts/article_health.py", "articles/" + s] + extra, ART)
        if "Traceback" in out:
            crash.append(s + " " + " ".join(extra))
check("T2", "monitor runs on all %d articles in text, --json and --html" % len(slugs), not crash, "; ".join(crash))

# T3 regression: publish blockers equal to main's code
base = {}
for s in slugs:
    base[s] = re.search(r"(\d+) publish blocker", health(s)[1]).group(1)
wt = os.path.join(TMP, "art-main")
subprocess.run(["git", "worktree", "add", "-q", "--detach", wt, "origin/main"], cwd=ART, capture_output=True)
diff = []
for s in slugs:
    rc, out = run(["python3", os.path.join(wt, "scripts", "article_health.py"), "articles/" + s], ART)
    m = re.search(r"(\d+) publish blocker", out)
    if not m or m.group(1) != base[s]:
        diff.append("%s main=%s now=%s" % (s, m.group(1) if m else "?", base[s]))
subprocess.run(["git", "worktree", "remove", "--force", wt], cwd=ART, capture_output=True)
check("T3", "publish blockers identical to main on every article (no regression)", not diff, "; ".join(diff))

# T4 missing limits file stops each script with a clear message
for name, cmd, cwd in [("article_health", ["python3", "scripts/article_health.py", "articles/" + slugs[0]], ART),
                       ("check_structure", ["python3", "scripts/check_structure.py", "articles/" + slugs[0]], ART),
                       ("check_case_copy", ["python3", "scripts/check_case_copy.py"], CASE)]:
    rc, out = run(cmd, cwd, os.path.join(TMP, "nope.md"))
    check("T4." + name, "%s: missing limits file stops with a message" % name,
          rc != 0 and "not found at" in out and "Traceback" not in out, out.strip()[:90])

# T5 a limits file without the machine block is refused
p = variant("noblock", ORIG.split("\n## Machine values\n")[0])
rc, out = health(slugs[0], p)
check("T5", "file with no Machine values block is refused, no traceback", rc != 0 and "Machine values" in out and "Traceback" not in out, out.strip()[:90])

# T6 broken JSON in the block
p = variant("badjson", ORIG.replace('"meta_max": 155,', '"meta_max": 155,,'))
rc, out = health(slugs[0], p)
check("T6", "malformed JSON in the block fails loudly", rc != 0, "traceback" if "Traceback" in out else out.strip()[:90])

# T7 one edit in the file moves the article check (single home)
art = "uneven-ai-adoption"
before = line(health(art)[1], "meta description")
p = variant("meta160", ORIG.replace('"meta_max": 155', '"meta_max": 160'))
after = line(health(art, p)[1], "meta description")
check("T7", "meta_max 155→160 in the file flips %s's meta line FAIL→PASS" % art,
      bool(before and after and before.startswith("FAIL") and after.startswith("PASS")), "%s | %s" % (before, after))

# T8 the same edit moves the case-study check
rc0, o0 = run(["python3", "scripts/check_case_copy.py"], CASE)
rc1, o1 = run(["python3", "scripts/check_case_copy.py"], CASE, p)
w0, w1 = o0.count("SEO Description is"), o1.count("SEO Description is")
check("T8", "same edit changes case-study description warnings (%d → %d)" % (w0, w1), w1 < w0, "")

# T9 paragraph limit change reaches check_structure
howto = next((s for s in slugs if "type how-to" in run(["python3", "scripts/check_structure.py", "articles/" + s], ART)[1]), None)
if howto:
    o_a = run(["python3", "scripts/check_structure.py", "articles/" + howto], ART)[1]
    p = variant("para200", ORIG.replace('"paragraph_words_max": 75', '"paragraph_words_max": 200'))
    o_b = run(["python3", "scripts/check_structure.py", "articles/" + howto], ART, p)[1]
    n_a, n_b = o_a.count("plain: up to 5 and"), o_b.count("plain: up to 5 and")
    check("T9", "paragraph limit 75→200 changes %s's structure findings (%d → %d)" % (howto, n_a, n_b), n_b <= n_a and o_a != o_b or n_a == 0, "")

# T10 empty SERP title fails (the fixed bug)
o = health("shadow-ai")[1]
check("T10", "an empty SERP title reads FAIL (was a false PASS at 17ch)", (line(o, "SERP title") or "").startswith("FAIL"), line(o, "SERP title"))

# T11 the italic series line is not read as the lede
o = health(art)[1]
lede = line(o, "lede at most two sentences") or ""
check("T11", "series line skipped: %s's lede counts sentences > 0" % art, bool(re.search(r"\s[1-9]\s", lede)), lede)

# T12 evidence-budget: off lifts the reference cap
o = health(art)[1]
check("T12", "evidence-budget: off lifts the 2-4 reference cap", "cap lifted by evidence-budget: off" in (line(o, "key references") or ""), line(o, "key references"))

# T13 every path the new docs name exists
docs = [os.path.join(SEO, x) for x in ("library/ai-seo-map.md", "services/writing.md", "services/auditing.md", "services/web-design.md")]
missing = []
roots = {"disc/": "skills/ebs-discoverability/references/", "audit/": "skills/b2b-seo-audit/references/", "strat/": "skills/seo-strategy/references/"}
for d in docs:
    for ref in set(re.findall(r"`((?:disc|audit|strat)/[\w.-]+\.md)`", open(d).read())):
        pre = ref.split("/")[0] + "/"
        if not os.path.exists(os.path.join(SEO, roots[pre], ref[len(pre):])):
            missing.append(ref)
    for ref in set(re.findall(r"`((?:library|services|skills|reports|intake)/[\w./-]+\.(?:md|py|json))`", open(d).read())):
        if "<" not in ref and "*" not in ref and not os.path.exists(os.path.join(SEO, ref)):
            missing.append(ref)
check("T13", "every file the map and service files point to exists", not missing, ", ".join(sorted(set(missing))))

# T14 consumer pointers resolve
ptr = {"ebs-article-system/CLAUDE.md": "services/writing.md", "ebs-case-study-system/CLAUDE.md": "services/writing.md",
       "ebs-website-system/CLAUDE.md": "services/web-design.md", "ebs-web-components/CLAUDE.md": "services/web-design.md"}
bad = [k for k, v in ptr.items() if ("ebs-seo-system/" + v) not in open(os.path.join(G, k)).read() or not os.path.exists(os.path.join(SEO, v))]
check("T14", "all four consumer repos point at an existing service file", not bad, ", ".join(bad))

# T15 no script still hardcodes the moved numbers
hard = []
for f, pats in {os.path.join(ART, "scripts/article_health.py"): [r"<= ?160\b", r"120 <= mc", r"len\(slug\) <= 60"],
                os.path.join(ART, "scripts/check_structure.py"): [r"40 <= w <= 60", r"wc\(b\) > 75"],
                os.path.join(CASE, "scripts/check_case_copy.py"): [r"SEO_DESC_WARN = 160", r"SEO_TITLE_MAX = 60 "]}.items():
    s = open(f).read()
    hard += ["%s:%s" % (os.path.basename(f), x) for x in pats if re.search(x, s)]
check("T15", "no moved number is still hardcoded in a script", not hard, ", ".join(hard))


# T16 a numbered list is not counted as a long paragraph (E59)
lst = variant("lists", ORIG)
fake = os.path.join(TMP, "listcheck.py")
open(fake, "w").write("import sys,re; sys.path.insert(0, %r); import article_health as A\n"
    "b=\"Intro line.\\n\\n1. \" + \"word \"*200 + \"\\n2. more\\n\\nShort closing paragraph.\"\n"
    "ps=[p for p in b.split('\\n\\n') if p.strip() and not re.match(r'\\d+\\.\\s', p.strip()) and len(p.split())>75]\n"
    "src=open(%r).read(); print('OK' if 'a numbered list is not a paragraph' in src and not ps else 'BAD')\n"
    % (os.path.join(ART, "scripts"), os.path.join(ART, "scripts", "article_health.py")))
rc, out = run(["python3", fake], ART)
check("T16", "a 200-word numbered list is not reported as a long paragraph", "OK" in out, out.strip()[:90])

for sid, desc, ok, detail in results:
    print("%-5s %-4s %s%s" % (sid, "PASS" if ok else "FAIL", desc, ("  [" + detail + "]") if detail and not ok else ""))
print("\n%d/%d pass" % (sum(r[2] for r in results), len(results)))
raise SystemExit(0 if all(r[2] for r in results) else 1)
