#!/usr/bin/env bash
# Full pipeline: copy -> dedupe/merge -> fix refs -> descriptions -> split long -> catalogs.
# Usage: tools/rebuild.sh <src_dir_with_clones> [repo_dir]
set -euo pipefail
S="${1:?src dir}"; R="${2:-$(cd "$(dirname "$0")/.." && pwd)}"
SW="$(cygpath -w "$S" 2>/dev/null || echo "$S")"   # python on Windows needs a native path
rm -rf "$R"/0[1-4]-*/
bash "$R/tools/build.sh" "$S" "$R"
python -I "$R/tools/curate.py" "$R"
python -I "$R/tools/inventory.py" "$R" >/dev/null
python -I "$R/tools/fixrefs.py" "$R" "$SW" >/dev/null
python -I "$R/tools/inventory.py" "$R" >/dev/null
python -I "$R/tools/descriptions.py" "$R"
python -I "$R/tools/split_long.py" "$R" >/dev/null
python -I "$R/tools/inventory.py" "$R"
python -I "$R/tools/check_frontmatter.py" "$R"
python -I "$R/tools/gen.py" "$R"
