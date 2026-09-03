Before editing any checked-out resource repository from the entrepreneur profile, verify the active git branch is the bot name branch `c01entrepreneur_bot`; if not, create/check out `c01entrepreneur_bot` first.
§
Daily cron jobs for Business Idea Generator: 187b66aee0c1 at 3:00 creates/pushes one idea; 39b5b5288033 at 3:30 commits at least one system improvement. Current workdirs are /home/miam/jordatech/business_ideas and /home/miam/jordatech/business_idea_generator.
§
Business Idea Generator daily idea sources live in `business_ideas/source_locations.md` and cron job 187b66aee0c1. Sources include Reddit (r/AiMoneyMaking, r/AiNova, r/BuildCapital, r/CofounderHunt, r/SomebodyMakeThis), Indie Hackers, Product Hunt, Betalist, HN, TechCrunch, Starter Story, G2/Capterra, GitHub, Stack Overflow, app marketplaces, job boards, and operator communities.
§
Business idea system uses a skeptical investor review step before MVP: Data Moat & Proprietary Advantage, Human-in-the-Loop Approach, Unit Economics, and FAQ for Skeptical Investors; methodology is documented in the business-idea-systems skill.
§
Hermes profile repository for this machine is checked out at `/home/miam/.hermes` with remote `https://github.com/jordatech/crmmiam01_hermes` on branch `main`; it stores portable Hermes profiles, skills, memories, and selected config files.
§
Entrepreneur profile has `caveman` installed from `jordatech/caveman` at `/home/miam/.hermes/profiles/entrepreneur/skills/creative/caveman/SKILL.md`.
§
When syncing profile SOUL.md from an upstream agent identity file, preserve exact bytes including trailing spaces/blank lines; verify with diff against freshly fetched source.
§
`hermes skills install` from direct URLs should use `--category` and `--yes` in non-interactive runs to avoid prompt cancellation.
§
Startup Teams AI server/bot research is stored in `jordatech/knowledge_extraction` under `servers_and_bots_for_startupteams/`; local checkout path is `/home/miam/jordatech/knowledge_extraction` and work should use branch `c01entrepreneur_bot`.