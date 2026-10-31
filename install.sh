#!/usr/bin/env bash
# Usage: ./install.sh <pack-dir> [target]   ex: ./install.sh 02-motion-design
# Copies every skill of a pack (any folder holding a SKILL.md) into ~/.claude/skills (or [target]).
set -euo pipefail
pack="${1:?usage: ./install.sh <01-web-design|02-motion-design|03-code-backend-workflow> [target]}"
target="${2:-$HOME/.claude/skills}"
mkdir -p "$target"
n=0
while IFS= read -r f; do
  d="$(dirname "$f")"; name="$(basename "$d")"
  if [ -e "$target/$name" ]; then echo "skip (exists): $name"; continue; fi
  cp -r "$d" "$target/$name"; n=$((n+1))
done < <(find "$pack" -name SKILL.md)
echo "$n skills installed in $target"
