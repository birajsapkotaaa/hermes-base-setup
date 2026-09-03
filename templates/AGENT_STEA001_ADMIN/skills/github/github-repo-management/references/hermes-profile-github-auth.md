# Hermes profile HOME vs GitHub authentication

Session-specific pattern captured from cloning a private `jordatech` repository from the admin Hermes profile.

## Symptom

- User says GitHub auth has been set.
- `gh auth status` inside the Hermes profile still reports:

```text
You are not logged into any GitHub hosts. To log in, run: gh auth login
```

- `git ls-remote --heads https://github.com/org/private-repo.git` fails:

```text
fatal: could not read Username for 'https://github.com': No such device or address
```

## Root cause

Hermes profiles can set `HOME` to a profile-scoped sandbox, e.g.:

```text
/home/miam/.hermes/profiles/admin/home
```

GitHub CLI credentials may be stored under the real Linux user home instead:

```text
/home/miam/.config/gh/hosts.yml
```

So `gh` and `git` are looking in the wrong home directory for credentials.

## Working fix

```bash
# Verify where gh auth exists
HOME=/home/miam gh auth status

# Let gh configure git's HTTPS credential helper in that home
HOME=/home/miam gh auth setup-git

# Run git commands with the same HOME
HOME=/home/miam git ls-remote --heads https://github.com/jordatech/obsidian_vault_jordan_ulmer.git
HOME=/home/miam git clone https://github.com/jordatech/obsidian_vault_jordan_ulmer.git
```

## Notes

- SSH can still fail (`Permission denied (publickey)`) if there are no SSH keys, even when `gh` HTTPS auth is valid.
- Do not print tokens. `gh auth status` masks tokens by default and is safe enough for status checks.
- If cloning into a Hermes profile resources directory, it is fine to keep the target path under the profile while using `HOME=/home/miam` only for credential lookup.
