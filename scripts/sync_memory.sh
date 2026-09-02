#!/usr/bin/env bash
set -Eeuo pipefail

# ==============================================================================
# Hermes Agent Memory Auto-Sync Script
# Periodically commits and pushes memory updates to the active employee branch.
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
LOCK_FILE="$REPO_DIR/.git/hermes_sync.lock"
LOG_FILE="$REPO_DIR/.git/hermes_sync.log"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*" >> "$LOG_FILE"
}

fail() {
  log "ERROR: $*"
  printf 'Hermes git sync failed: %s\n' "$*" >&2
  exit 1
}

cd "$REPO_DIR"

# Ensure non-overlapping execution using file descriptor 9
{
  flock -n 9 || {
    log "Another sync process is currently running. Exiting cleanly."
    exit 0
  }

  current_branch="$(git branch --show-current)"
  if [ -z "$current_branch" ]; then
    fail "Detached HEAD state; cannot determine active branch."
  fi

  log "Starting sync on branch '$current_branch'..."

  # Check for local uncommitted changes
  if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    git add -A >> "$LOG_FILE" 2>&1 || fail "git add failed"
    
    commit_msg="chore(hermes): auto-sync memory & state [$(date -u '+%Y-%m-%d %H:%M:%S UTC')]"
    git commit -m "$commit_msg" >> "$LOG_FILE" 2>&1 || fail "git commit failed"
    log "Committed local memory updates: $commit_msg"

    # Only push if an upstream remote is configured
    if git remote get-url origin >/dev/null 2>&1; then
      git push origin "$current_branch" >> "$LOG_FILE" 2>&1 || log "Warning: git push failed or remote unavailable."
    fi
  else
    log "No changes detected. Memory is up to date."
  fi

} 9>"$LOCK_FILE"
