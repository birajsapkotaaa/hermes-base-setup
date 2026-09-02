# Hermes AI Agent Setup SOP

**Org:** Startup Teams | **Platform:** Discord | **Host:** Proxmox Node 135 (`MIAM-00135`)

---

## Prerequisites
- Access to Proxmox Node 135 Web GUI
- GitHub access to `startupteams` organization
- Discord account + access to Startup Teams server
- API Keys

---

## Step 1: Initialize Your Personal Branch

On your local machine, clone the base template and run the onboarding script:

```bash
git clone https://github.com/startupteams/hermes-base-setup.git
cd hermes-base-setup
python scripts/init_employee.py --name "<your_name>" --role "<your_role>"
git push -u origin <your_name>
```

---

## Step 2: Create a Proxmox LXC Container

1. Start the container and open **Console** → Login as `root`

---

## Step 3: Install Hermes Inside the Container

```bash
# Install dependencies
apt update && apt install -y git python3 python3-pip nano tmux

# Install Hermes CLI
pip3 install hermes-agent --break-system-packages

# Clone your personal branch as the agent brain
# NOTE: Delete ~/.hermes first if it already exists
rm -rf /root/.hermes
git clone -b <your_name> https://github.com/startupteams/hermes-base-setup.git /root/.hermes
cd /root/.hermes
```

---

## Step 4: Configure API Keys

```bash
cp .env.example .env
nano .env
```

```env
OPENAI_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx
OPENAI_BASE_URL=https://api.groq.com/openai/v1
DISCORD_BOT_TOKEN=your_discord_bot_token
GATEWAY_ALLOW_ALL_USERS=true
```

In `config.yaml`, set the model:

```yaml
model:
  provider: custom
  default: llama-3.3-70b-versatile

providers:
  custom:
    base_url: https://api.groq.com/openai/v1
    api_key_env: OPENAI_API_KEY

platforms:
  discord:
    enabled: true
    dm_policy: open
    group_policy: open
```

---

## Step 5: Create a Discord Bot

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications) → **New Application**
2. Under **Bot** → Reset Token → Copy it → Enable **Message Content Intent**
3. Under **OAuth2 → URL Generator** → Scopes: `bot` → Permissions: Send/Read Messages → Invite bot to server
4. Paste the token into `.env` as `DISCORD_BOT_TOKEN`

---

## Step 6: Launch the Agent

Test the LLM connection first:
```bash
hermes -z "Hello, who are you?"
```

Start the Discord gateway inside a `tmux` session:
```bash
tmux new -s hermes
hermes gateway
# Detach: Ctrl+B then D
```

---

## Step 7: Enable Memory Auto-Sync (Cron)

```bash
chmod +x /root/.hermes/scripts/sync_memory.sh
crontab -e
```

Add:
```
*/5 * * * * /bin/bash /root/.hermes/scripts/sync_memory.sh
```

---

## Troubleshooting

| Error | Fix |
| :--- | :--- |
| `destination path already exists` | `rm -rf /root/.hermes` then re-clone |
| `HTTP 404: model '' does not exist` | Use `provider` + `default` keys in `config.yaml` (not `default_provider`) |
| `413 Request payload too large` | Add `skills_in_context: false` and `max_turns: 20` to `config.yaml` |
| `No messaging platforms enabled` | Set `platforms.discord.enabled: true` in `config.yaml` |
| `Model provider failed after retries` | Ensure `providers.custom.base_url` points to Groq URL |
