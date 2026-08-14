#!/usr/bin/env python3
"""Regenerate the state tables in intake/entity-health.md.

Reads the claims from intake/entity-register.md and the measurements from the
newest intake/snapshots/gsc-*.json, joins them on URL, and rewrites the block
between the GENERATED markers in intake/entity-health.md.

Everything outside those markers is prose written by a human and is preserved.
State rules are documented in library/entity-health-method.md; if you change
one here, change it there in the same commit.

    python3 scripts/build_entity_health.py [snapshot.json]

Stdlib only. Run from the repo root.
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTER = os.path.join(ROOT, "intake", "entity-register.md")
HEALTH = os.path.join(ROOT, "intake", "entity-health.md")
BEGIN, END = "<!-- BEGIN GENERATED -->", "<!-- END GENERATED -->"

OWNED_MIN_IMPRESSIONS = 100   # below this an entity is claimed, not held
WEAK_POSITION = 40            # held, but off the pages anyone reads

SECTIONS = {  # register heading prefix -> (group key, table title)
    "## 1.": ("case", "Case studies"),
    "### Services": ("commercial", "Service and industry pages"),
    "### Industries": ("commercial", None),
}


def unusable_probe(probe):
    """Return a reason string if the probe cannot carry a health verdict."""
    p = probe.strip().strip("*").lower()
    if not p or p == "—":
        return "below the snapshot floor"
    if p.startswith(("site:", "filetype:")) or "<operator" in p or "<long " in p:
        return "no usable probe (search operator)"
    if re.match(r"^ebs\b", p) or "ebs-integrator" in p:
        return "found by brand only"
    return None


def parse_register(text):
    """Yield (group, path, entity) for every registered row."""
    group = None
    headers = []
    for line in text.split("\n"):
        for prefix, (key, _) in SECTIONS.items():
            if line.startswith(prefix):
                group = key
        if line.startswith("## 3."):
            group = None
        if not group or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if "Primary entity" in cells:
            headers = cells
            continue
        m = re.match(r"^`(/en/[^`]+)`", cells[0])
        if not m or not headers:
            continue
        try:
            entity = cells[headers.index("Primary entity")]
        except (ValueError, IndexError):
            continue
        yield group, m.group(1), entity


def classify(path, pages, queries):
    """Return (state, note) for one registered page. Rules mirror the method file."""
    page = pages.get(path)
    if page is None:
        return "UNPROVEN", "below the snapshot floor — absent, not zero"

    probe = page["top_keyword"]
    reason = unusable_probe(probe)
    if reason:
        return "UNPROVEN", reason

    q = queries.get(probe.lower())
    if q:
        if q["urls_count"] > 1:
            return "CONTESTED", f"{q['urls_count']} of our URLs show for this query"
        if q["top_url"] != page["url"]:
            return "MISOWNED", f"Google picks {q['top_url']}"

    if page["impressions"] >= OWNED_MIN_IMPRESSIONS:
        if page["position"] > WEAK_POSITION:
            return "OWNED, weakly", f"held at position {page['position']:.1f}"
        return "OWNED", "sole URL for its probe"
    return "UNPROVEN", f"{page['impressions']} impressions, below {OWNED_MIN_IMPRESSIONS}"


def table(rows, pages):
    out = ["| Entity | Page | Observed probe | Impr / Pos | State | Why |",
           "|---|---|---|---|---|---|"]
    for path, entity, state, note in rows:
        p = pages.get(path)
        probe = p["top_keyword"] if p else "—"
        metrics = f"{p['impressions']} / {p['position']:.1f}" if p else "below floor"
        if len(probe) > 46:
            probe = probe[:43] + "…"
        out.append(f"| {entity} | `{path}` | {probe} | {metrics} | **{state}** | {note} |")
    return "\n".join(out)


def tally(rows):
    counts = {}
    for _, _, state, _ in rows:
        counts[state] = counts.get(state, 0) + 1
    total = len(rows)
    listed = [f"{n} {s}" for s, n in sorted(counts.items())]
    listed += [f"0 {m}" for m in ("CONTESTED", "MISOWNED") if m not in counts]
    return f"**{total} surfaces — " + " · ".join(listed) + ".**"


def main():
    snapshot_path = sys.argv[1] if len(sys.argv) > 1 else sorted(
        glob.glob(os.path.join(ROOT, "intake", "snapshots", "gsc-*.json")))[-1]
    snap = json.load(open(snapshot_path))

    pages = {}
    for p in snap["pages"]:
        path = re.sub(r"^https?://[^/]+", "", p["url"])
        pages.setdefault(path, p)
    queries = {q["keyword"].lower(): q for q in snap["queries"]}

    groups = {"case": [], "commercial": []}
    for group, path, entity in parse_register(open(REGISTER).read()):
        state, note = classify(path, pages, queries)
        groups[group].append((path, entity, state, note))

    block = [
        BEGIN,
        f"<!-- generated by scripts/build_entity_health.py from {os.path.basename(snapshot_path)}"
        " — do not edit by hand -->",
        "",
        f"*Generated from snapshot `{snap['snapshot']}`, window {snap['window']['from']} to"
        f" {snap['window']['to']}. Rules: `../library/entity-health-method.md`.*",
    ]
    for key, title in (("case", "Case studies"), ("commercial", "Service and industry pages")):
        rows = groups[key]
        block += ["", f"### {title} — state per registered surface", "",
                  table(rows, pages), "", tally(rows)]
    block += ["", END]

    text = open(HEALTH).read()
    if BEGIN in text and END in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END),
                      "\n".join(block), text, flags=re.S)
    else:
        sys.exit(f"markers not found in {HEALTH}; add {BEGIN} / {END} where the tables belong")
    open(HEALTH, "w").write(text)

    total = sum(len(v) for v in groups.values())
    print(f"{total} registered surfaces from {os.path.basename(snapshot_path)}")
    for key in groups:
        print(f"  {key}: {tally(groups[key])}")


if __name__ == "__main__":
    main()
