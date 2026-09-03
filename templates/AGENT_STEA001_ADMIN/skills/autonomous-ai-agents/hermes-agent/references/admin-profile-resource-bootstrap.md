# Admin Profile Resource Bootstrap

This reference captures the reusable workflow from a session where Jordan asked the admin profile to inspect its updated `SOUL.md` and check out the resource repositories named there.

## Trigger

Use this when a user says the Hermes profile/soul file changed, asks the agent to "explore the soul file," or asks to check out resource repositories referenced by a profile document.

## Observed admin profile facts

- Admin profile path: `/home/miam/.hermes/profiles/admin/`
- Soul file path: `/home/miam/.hermes/profiles/admin/SOUL.md`
- Bot name in the soul file: `c01admin_bot`
- Resource checkout base used successfully: `/home/miam/.hermes/profiles/admin/resources/`
- Git identity requested by the soul file:
  - `git config --global user.email "jordatech@gmail.com"`
  - `git config --global user.name "jordatech"`

## Resource repositories found in the admin SOUL.md

- `https://github.com/jordatech/obsidian_vault_jordan_ulmer/tree/master/Agents/admin/`
- `https://github.com/jordatech/Fabric`
- `https://github.com/jordatech/armory`
- `https://github.com/jordatech/awesome-design-md`

The first URL points to a subdirectory in a repository. Clone the repository root (`obsidian_vault_jordan_ulmer.git`) and then navigate to `Agents/admin/`.

## Clone/checkout recipe

```bash
set -euo pipefail
base="/home/miam/.hermes/profiles/admin/resources"
mkdir -p "$base"
cd "$base"

git config --global user.email "jordatech@gmail.com"
git config --global user.name "jordatech"

for spec in \
  "Fabric https://github.com/jordatech/Fabric.git" \
  "armory https://github.com/jordatech/armory.git" \
  "awesome-design-md https://github.com/jordatech/awesome-design-md.git" \
  "obsidian_vault_jordan_ulmer https://github.com/jordatech/obsidian_vault_jordan_ulmer.git"; do
  name=${spec%% *}
  url=${spec#* }
  echo "== $name =="

  if [ -d "$name/.git" ]; then
    cd "$name"
    git remote set-url origin "$url" || true
    git fetch origin --prune
  else
    git clone "$url" "$name"
    cd "$name"
  fi

  if git show-ref --verify --quiet refs/remotes/origin/c01admin_bot; then
    git checkout c01admin_bot
    git pull --ff-only origin c01admin_bot || true
  else
    default_branch=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##' || true)
    [ -n "$default_branch" ] || default_branch=main
    if git show-ref --verify --quiet refs/heads/c01admin_bot; then
      git checkout c01admin_bot
    else
      git checkout -b c01admin_bot "origin/$default_branch"
    fi
  fi

  git status --short --branch | head -1
  cd "$base"
done
```

## Authentication pitfall

If a repo is private or GitHub CLI is unauthenticated, `git clone https://github.com/...` can fail with:

```text
fatal: could not read Username for 'https://github.com': No such device or address
```

Check auth explicitly:

```bash
gh auth status 2>&1 || true
git ls-remote --heads https://github.com/jordatech/<repo>.git
```

Do not treat partial failure as total failure: clone all public/accesssible repos, report the inaccessible ones, and state that GitHub auth or private repo access is needed.

## Verification

```bash
base="/home/miam/.hermes/profiles/admin/resources"
for repo in Fabric armory awesome-design-md obsidian_vault_jordan_ulmer; do
  if [ -d "$base/$repo/.git" ]; then
    printf '%s | ' "$repo"
    git -C "$base/$repo" status --short --branch | head -1
    git -C "$base/$repo" remote get-url origin
  else
    echo "$repo | not cloned"
  fi
done
```

## Durable-memory boundary

It is reasonable to save durable facts such as the profile path, soul file path, resource checkout base, and stable repo list. Do not save session progress such as "cloned today" unless it describes the durable environment location future sessions should use.
