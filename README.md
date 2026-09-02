# STEA Hermes AI Agent Base Template

The modern, standardized template for deploying individual Hermes AI agent instances for Startup Teams / STEA team members.

---

## Architecture: Brain-as-Code

This repository serves as the persistent brain for an employee's Hermes Agent instance:
- Compute runs inside a **Proxmox VM or LXC Container on Node 135 (`MIAM-00135`)**.
- The repository is mounted at `~/.hermes/` inside the container or VM.
- All persistent identity, memory, tools, and learned conventions live in Git.

```
┌─────────────────────────────────────────────────────────────┐
│                 Proxmox Node 135 (MIAM-00135)               │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │               Hermes Agent Runtime                  │   │
│   │   (Python / CLI / Docker Service in VM/LXC)         │   │
│   └──────────────────────────┬──────────────────────────┘   │
│                              │ Mounts ~/.hermes/            │
│                              ▼                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │         Local Employee Repository / Branch          │   │
│   │                                                     │   │
│   │   ├── SOUL.md          (Persona & Directives)       │   │
│   │   ├── memories/        (USER.md & MEMORY.md)        │   │
│   │   ├── skills/          (Modular Tool Capabilities)  │   │
│   │   └── config.yaml      (Agent & LLM Config)         │   │
│   └──────────────────────────┬──────────────────────────┘   │
│                              │                              │
│                   Auto-Sync Cron (5 Minutes)                │
│                   scripts/sync_memory.sh                    │
└──────────────────────────────┼──────────────────────────────┘
                               ▼
               ┌──────────────────────────────┐
               │      GitHub Remote Repo      │
               │   (Branches: main, biraj...) │
               └──────────────────────────────┘
```

---

## Directory Structure

```
.
├── .gitignore                   # Strict security whitelist (blocks secrets & session DBs)
├── .env.example                 # Example API keys template
├── README.md                    # This documentation
├── SOUL.md                      # Core agent persona, tone, and directives
├── config.yaml                  # Hermes agent configuration (LLM models, tools, limits)
│
├── memories/                    # Durable Long-Term Memory Store
│   ├── USER.md                  # Facts about the employee (role, preferences, workflow)
│   └── MEMORY.md                # Learned environment facts, node IPs, tool quirks
│
├── skills/                      # Modular Skill Library
│   └── devops/
│       └── proxmox/             # Proxmox node & VM management tooling
│
├── scripts/
│   ├── sync_memory.sh           # File-locked, branch-aware Git backup script
│   └── init_employee.py         # 1-command employee agent generator
│
└── templates/
    └── systemd/
        └── hermes-agent.service # Systemd service unit for 24/7 background execution
```

---

## How to Initialize a New Employee Agent

To onboard a new employee, run the built-in generator script:

```bash
python scripts/init_employee.py --name "<your_name>" --role "<your_role>"
```

This will automatically:
1. Create a dedicated Git branch with your_name.
2. Populate `memories/USER.md` with the employee's details.
3. Configure `SOUL.md` tailored to the employee's role.
4. Prepare `memories/MEMORY.md` with infrastructure defaults.

---

## Running on Proxmox Node 135

1. **Deploy the Systemd Service:**
   ```bash
   sudo cp templates/systemd/hermes-agent.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now hermes-agent.service
   ```

2. **Check Logs:**
   ```bash
   journalctl -u hermes-agent.service -f
   ```

3. **Enable Memory Sync Cron:**
   Add to `crontab -e`:
   ```cron
   */5 * * * * /bin/bash /opt/hermes/scripts/sync_memory.sh >> /tmp/hermes_sync.log 2>&1
   ```
