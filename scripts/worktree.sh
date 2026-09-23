#!/usr/bin/env bash
# Isolated feature worktrees and deliberate release integration for La Malice.
set -euo pipefail

checkout_root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "ERROR: run from a Git checkout." >&2
  exit 1
}
project_root="$(git worktree list --porcelain | awk '
  /^worktree / { path = substr($0, 10) }
  $1 == "branch" && $2 == "refs/heads/main" { print path; exit }
')"
[[ -n "$project_root" ]] || {
  echo "ERROR: no worktree owns main." >&2
  exit 1
}
main_branch="main"

fail() { echo "ERROR: $*" >&2; exit 1; }

usage() {
  cat <<'EOF'
Usage: scripts/worktree.sh <start|assert|status|merge|integrate> <topic>

  start TOPIC      Create or reopen ../la-malice.fr-TOPIC on feat/TOPIC from origin/main.
  assert TOPIC     Check that the current checkout is the expected feature worktree.
  status TOPIC     Print the expected branch and worktree path.
  merge TOPIC      Merge a clean feature locally into a clean, current main. Does not push.
  integrate TOPIC  Merge, push main, verify origin/main, then remove the local unit and branch.
EOF
}

require_topic() {
  [[ "$1" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || fail "topic must use lowercase letters, digits and single hyphens."
}

branch_for() { printf 'feat/%s\n' "$1"; }
unit_for() { printf '%s-%s\n' "$(dirname "$project_root")/$(basename "$project_root")" "$1"; }

require_clean() {
  local path="$1"
  [[ -z "$(git -C "$path" status --porcelain)" ]] || fail "$(git -C "$path" rev-parse --show-toplevel) is not clean; preserve or commit its changes first."
}

require_main() {
  [[ "$checkout_root" == "$project_root" ]] || fail "start, merge and integrate must run from the main worktree."
  [[ "$(git -C "$project_root" branch --show-current)" == "$main_branch" ]] || fail "the integration worktree is not on main."
}

fetch_main() {
  git -C "$project_root" fetch origin "$main_branch" --prune
  git -C "$project_root" rev-parse --verify "origin/$main_branch" >/dev/null
}

unit_path_for_branch() {
  git -C "$project_root" worktree list --porcelain | awk -v wanted="refs/heads/$1" '
    /^worktree / { path = substr($0, 10) }
    $1 == "branch" && $2 == wanted { print path; exit }
  '
}

print_status() {
  local topic="$1" branch unit current
  branch="$(branch_for "$topic")"
  unit="$(unit_for "$topic")"
  current="$(unit_path_for_branch "$branch")"
  printf 'FEATURE_BRANCH=%s\nEXPECTED_WORKTREE=%s\n' "$branch" "$unit"
  printf 'REGISTERED_WORKTREE=%s\n' "${current:-none}"
}

start() {
  local topic="$1" branch unit registered
  require_main
  require_clean "$project_root"
  fetch_main
  branch="$(branch_for "$topic")"
  unit="$(unit_for "$topic")"
  registered="$(unit_path_for_branch "$branch")"
  [[ ! -e "$unit" || "$registered" == "$unit" ]] || fail "expected unit path exists but is not $branch: $unit"
  [[ -z "$registered" || "$registered" == "$unit" ]] || fail "$branch is already open in $registered"

  if [[ "$registered" == "$unit" ]]; then
    echo "REOPENED_WORKTREE=$unit"
  elif git -C "$project_root" show-ref --verify --quiet "refs/heads/$branch"; then
    git -C "$project_root" worktree add "$unit" "$branch"
  elif git -C "$project_root" show-ref --verify --quiet "refs/remotes/origin/$branch"; then
    git -C "$project_root" worktree add -b "$branch" "$unit" "origin/$branch"
  else
    git -C "$project_root" worktree add -b "$branch" "$unit" "origin/$main_branch"
  fi
  print_status "$topic"
}

assert_unit() {
  local topic="$1" branch expected
  branch="$(branch_for "$topic")"
  expected="$(unit_for "$topic")"
  [[ "$(git -C "$checkout_root" branch --show-current)" == "$branch" ]] || fail "current branch is not $branch"
  [[ "$checkout_root" == "$expected" ]] || fail "current worktree is $checkout_root; expected $expected"
  [[ "$(unit_path_for_branch "$branch")" == "$expected" ]] || fail "$branch is not registered at $expected"
  echo "OK: $branch owns $expected"
}

require_ready_unit() {
  local topic="$1" branch unit
  branch="$(branch_for "$topic")"
  unit="$(unit_for "$topic")"
  [[ -d "$unit" ]] || fail "no worktree found for $branch"
  [[ "$(unit_path_for_branch "$branch")" == "$unit" ]] || fail "$branch is not registered at $unit"
  require_clean "$unit"
}

merge_local() {
  local topic="$1" branch
  require_main
  require_clean "$project_root"
  fetch_main
  [[ "$(git -C "$project_root" rev-parse HEAD)" == "$(git -C "$project_root" rev-parse "origin/$main_branch")" ]] || fail "local main differs from origin/main; resolve it before integration."
  branch="$(branch_for "$topic")"
  require_ready_unit "$topic"
  git -C "$project_root" merge --no-ff "$branch" -m "Merge $branch into $main_branch"
  echo "LOCAL_MERGE=complete"
}

integrate() {
  local topic="$1" branch unit
  merge_local "$topic"
  branch="$(branch_for "$topic")"
  unit="$(unit_for "$topic")"
  git -C "$project_root" push origin "$main_branch"
  git -C "$project_root" fetch origin "$main_branch"
  git -C "$project_root" merge-base --is-ancestor HEAD "origin/$main_branch" || fail "push verification failed; local unit is preserved."
  git -C "$project_root" worktree remove "$unit"
  git -C "$project_root" branch -d "$branch"
  echo "INTEGRATED=origin/$main_branch"
}

[[ $# -eq 2 ]] || { usage >&2; exit 2; }
command="$1"
topic="$2"
require_topic "$topic"
case "$command" in
  start) start "$topic" ;;
  assert) assert_unit "$topic" ;;
  status) print_status "$topic" ;;
  merge) merge_local "$topic" ;;
  integrate) integrate "$topic" ;;
  *) usage >&2; exit 2 ;;
esac
