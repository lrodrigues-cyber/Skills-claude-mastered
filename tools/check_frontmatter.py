"""Every top-level SKILL.md must have YAML frontmatter with name == folder and a description <= 1024 chars."""
import glob, io, os, re, sys
import yaml
bad = []
for f in glob.glob(os.path.join(sys.argv[1], "0[123]*", "**", "SKILL.md"), recursive=True):
    if os.sep + "merged" + os.sep in f or os.sep + "references" + os.sep in f:
        continue
    t = io.open(f, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---", t, re.S)
    try:
        d = yaml.safe_load(m.group(1))
        assert d["name"] == os.path.basename(os.path.dirname(f)), "name != folder"
        assert 0 < len(d["description"]) <= 1024, "description length"
    except Exception as e:
        bad.append(f"{f}: {str(e)[:100]}")
print(len(bad), "bad"); print("\n".join(bad[:30]))
