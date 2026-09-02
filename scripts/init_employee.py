#!/usr/bin/env python3
"""
Hermes AI Agent - Employee Onboarding & Branch Initialization Utility
Generates tailored SOUL.md, USER.md, and MEMORY.md files for any team member.
"""

import argparse
import subprocess
import sys
from pathlib import Path

def run_git_command(cmd, cwd):
    try:
        res = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(cmd)}\nError: {e.stderr.strip()}", file=sys.stderr)
        return None

def init_employee(name: str, role: str, root_dir: Path, create_branch: bool = True):
    name_clean = name.strip().lower().replace(" ", "_")
    print(f"\n==================================================")
    print(f" Initializing Hermes Agent Brain for: {name}")
    print(f" Role: {role}")
    print(f"==================================================\n")

    # 1. Switch or create git branch if requested
    if create_branch:
        print(f"[*] Creating and checking out Git branch '{name_clean}'...")
        run_git_command(["git", "checkout", "-b", name_clean], cwd=root_dir)

    # 2. Write personalized USER.md
    user_md_content = f"""# User Profile: {name}

- **Name:** {name}
- **Role:** {role}
- **Organization:** Startup Teams
- **Preferences:**
  - Concise, structured technical answers.
  - Actionable CLI and development commands.
  - Provide root-cause explanations for technical issues.
"""
    user_file = root_dir / "memories" / "USER.md"
    user_file.parent.mkdir(parents=True, exist_ok=True)
    user_file.write_text(user_md_content, encoding="utf-8")
    print(f"[+] Created: {user_file.relative_to(root_dir)}")

    # 3. Write personalized SOUL.md
    soul_md_content = f"""# Hermes Agent Persona for {name}

You are {name}'s dedicated AI Technical Partner at Startup Teams.

## 1. Identity & Operational Stance
- You are a specialized assistant tailored for {name} ({role}).
- You are direct, pragmatic, and technically sharp.
- You provide ready-to-run commands, automation scripts, and clear architectures.

## 2. Directives
- Repeatability First: Favor automated and reproducible solutions.
- Durable Learning: Record useful environment discoveries, conventions, and solutions in `memories/MEMORY.md`.
"""
    soul_file = root_dir / "SOUL.md"
    soul_file.write_text(soul_md_content, encoding="utf-8")
    print(f"[+] Created: {soul_file.relative_to(root_dir)}")

    # 4. Write personalized MEMORY.md
    memory_md_content = f"""# Working Memory for {name}

- **Branch:** `{name_clean}`
- **Active Role:** {role}
"""
    mem_file = root_dir / "memories" / "MEMORY.md"
    mem_file.write_text(memory_md_content, encoding="utf-8")
    print(f"[+] Created: {mem_file.relative_to(root_dir)}")

    print(f"\n[✓] Successfully initialized Hermes agent profile for {name}!")

def main():
    parser = argparse.ArgumentParser(description="Initialize Hermes AI Agent Profile for an Employee")
    parser.add_argument("--name", required=True, help="Employee name (e.g. biraj, robin, susmita)")
    parser.add_argument("--role", default="Engineer", help="Employee role/title")
    parser.add_argument("--no-branch", action="store_true", help="Do not create a new git branch automatically")

    args = parser.parse_args()
    root_dir = Path(__file__).resolve().parent.parent

    init_employee(
        name=args.name,
        role=args.role,
        root_dir=root_dir,
        create_branch=not args.no_branch
    )

if __name__ == "__main__":
    main()
