#!/usr/bin/env bash
# Build only explicitly approved public files, then check the resulting inventory.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$root/_site}"
case "$out" in /*) ;; *) out="$PWD/$out" ;; esac
[[ "$out" != "$root" && "$out" != / && ! -L "$out" ]] || { echo 'Unsafe output path' >&2; exit 1; }
# Refuse to overwrite an existing directory: callers own cleanup.
[[ ! -e "$out" ]] || { echo "Output already exists: $out" >&2; exit 1; }
files=(index.html festival-impro-malice-2026.html CNAME .nojekyll assets/img/logo-la-malice-noir-bleu-tr.png
  assets/img/accueil-essai.webp
  assets/img/instagram/agenda-13-novembre-2026.jpg
  assets/img/instagram/retrouvailles-24-octobre-2026.jpg
  assets/img/instagram/retrouvailles-11-novembre-2026.jpg)
for file in "${files[@]}"; do
  [[ -f "$root/$file" && ! -L "$root/$file" ]] || { echo "Missing or unsafe public file: $file" >&2; exit 1; }
  mkdir -p "$out/$(dirname "$file")"
  cp "$root/$file" "$out/$file"
done
expected="$(printf '%s\n' "${files[@]}" | LC_ALL=C sort)"
actual="$(cd "$out" && find . -type f -print | sed 's|^./||' | LC_ALL=C sort)"
[[ "$actual" == "$expected" ]] || { echo 'Unexpected artifact inventory' >&2; exit 1; }
echo "Pages artifact verified: $out"
