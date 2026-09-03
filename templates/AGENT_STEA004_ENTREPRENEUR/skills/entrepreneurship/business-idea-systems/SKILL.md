---
name: business-idea-systems
description: "Build and operate business-idea repositories, validation workflows, and lightweight idea-viewer apps."
version: 1.0.0
author: c01entrepreneur_bot
license: MIT
metadata:
  hermes:
    tags: [entrepreneurship, business-ideas, market-research, customer-discovery, SaaS, automation]
    related_skills: [github-repo-management, github-pr-workflow, hermes-agent, popular-web-designs]
---

# Business Idea Systems

Use this skill when the user asks to generate, store, display, validate, or automate business ideas, SaaS niches, customer personas, market research plans, or entrepreneurship knowledge systems.

The goal is not just to brainstorm ideas. The goal is to produce a durable system that software teams, sales teams, and founders can use: human-readable ideas, structured metadata, assumptions to validate, and a repeatable customer-discovery loop.

## Triggers

Use this skill when asked to:

- Create a business idea generator, niche hunter, opportunity database, or SaaS idea repository.
- Convert entrepreneurship frameworks into reusable templates, prompts, or product screens.
- Generate a business idea around a persona, pain, market, or product category.
- Develop a partial business-model brief into a full market, MVBP, revenue, risk, and validation plan.
- Store ideas in GitHub, Obsidian, markdown, JSON, Airtable, Notion, or a web app.
- Set up recurring idea generation or recurring improvements to the idea-generation system.
- Add or maintain recurring opportunity-source locations such as Reddit communities, forums, directories, LinkedIn Jobs signals, or trend feeds.
- Build a private founder dashboard or Vercel/Next.js viewer for idea content.

## Core Principle

Start with **persona and pain**, not product features.

A strong idea entry should answer:

1. Who is the specific persona?
2. What painful situation do they repeatedly experience?
3. What outcome are they already trying to achieve?
4. What alternatives or workarounds do they use today?
5. What assumptions must be validated before building?
6. What is the minimum viable business product / MVBP?
7. What market research conversation should happen next?

## Recommended Source Frameworks

Blend these frameworks when creating or evaluating an idea:

- **Bill Aulet / Disciplined Entrepreneurship:** beachhead market, end user profile, TAM, persona, full lifecycle use case, quantified value proposition, MVBP, pricing, sales process, key assumptions.
- **Paul Cheek / Startup Tactics:** tactical implementation of Disciplined Entrepreneurship and structured experimentation.
- **Allan Dib / One Page Marketing Plan:** before/during/after marketing, target market, message, media, lead capture, nurturing, conversion, lifetime value, referrals.
- **Giff Constable / Talking to Humans + Testing with Humans:** assumptions mapping, customer discovery, lightweight experiments, evidence quality.
- **Rob Fitzpatrick / The Mom Test:** ask about past behavior and specifics; avoid compliments, hypotheticals, and pitching.

When Jordan asks for a critical market-validation audit across a portfolio, roleplay the advisor panel but make the output operational: add idea-specific validation status, priority, recruiting channel, evidence required, experiments, data to capture, and kill/advance criteria. Move concrete validation steps up into the `Test the riskiest assumption first` area or equivalent early validation section so the founder sees the next test before reading long critique. Never leave advisor-panel commentary generic across every idea: each Bill Aulet / Paul Cheek / Allan Dib / Giff Constable / Rob Fitzpatrick / skeptical investor comment should mention the idea's actual title, persona, pain, market/category, MRR ambition, or execution risk. See `references/expert-panel-market-validation-model.md`.

## Idea Document Shape

Prefer human-readable Markdown with YAML frontmatter when the user wants durable Git-backed ideas.

Minimum frontmatter:

```yaml
title: "Idea title"
slug: "idea-title"
date: "YYYY-MM-DD"
persona: "specific user segment"
pain: "specific painful situation"
category: "SaaS / technology / market category"
tags:
  - SaaS
  - customer discovery
status: draft
confidence: medium-low until validated
created_by: c01entrepreneur_bot
```

Recommended body sections:

```markdown
# Idea Title

## One-line summary

## Next actions

## Persona

## Pain

## Product Concept

## Business Model

## Assumptions to Validate

## First 10 clients

For every new business idea, include at least 10 specific prospective clients, communities, partners, or buyer organizations. Each entry must include a linked client name, the client-specific need tied to the idea, and a public contact path such as a contact page, demo form, partnership page, community, or support route. Treat this as outbound/customer-discovery source intelligence, not validation.

## Preliminary Market Research Strategy

## Mom Test Interview Questions

## Minimum Viable Business Product

## Risks
```

Put `Next actions` directly under the one-line summary for founder-facing briefs. The user should see what to do next before reading the long model. Add a `First 10 clients` section near the top of every idea so the founder immediately sees who to interview or sell to first; include at least 10 specific linked prospects with their likely need and a public contact path. Treat these as outbound/customer-discovery hypotheses, not validated customers. Validate portfolio-wide edits with `scripts/validate_first_10_clients.py`; see `references/first-10-clients-prospect-lists.md`. When reordering existing idea Markdown, also update any local viewer snapshots (`data/ideas/*.md`) so deployed fallback content stays consistent.

For Niche Hunter-style opportunity views, avoid arbitrary scores. Store and calculate `goodness_score` from explicit inputs: Competition, Potential, Est. MRR, and Difficulty. Include a visible formula/rationale plus opportunity analysis, market gap, recommended move, market analysis snapshot, linked potential competitors, key learnings, improvement opportunities, and risks. See `references/opportunity-goodness-scoring.md` and `references/competitor-analysis-pattern.md`.

When Jordan provides a batch of rough ideas, domains, personas, pains, prototype links, or monetization notes, convert them into one durable brief per idea instead of only summarizing in chat. Preserve the source intent, normalize each concept into a clear slug/title/persona/pain/product, add Niche Hunter-style scoring and competitor analysis, update `ideas.json`, sync the viewer snapshot, build, commit/push both repos, deploy, and verify Basic Auth. See `references/batch-idea-intake-and-analysis.md`.

When Jordan provides one rough idea/domain plus an external article, use the article as source intelligence for pricing, risks, COGS, and positioning — not as buyer validation. If `bs4` is unavailable during article extraction, use a stdlib `html.parser` fallback rather than adding a dependency for a one-off scrape. See `references/single-idea-source-article-intake.md`.

When adding or changing an idea in `jordatech/business_ideas`, treat `business_idea_generator/data/` as a checked-in fallback snapshot that can drift behind the source repo. Copy the updated source `ideas.json`, copy the changed idea Markdown, check for any other source-indexed Markdown missing from the viewer snapshot, then validate JSON and run the viewer build before committing both repos. See `references/business-ideas-source-to-viewer-sync.md`.

When converting business ideas into requirements and test cases, use the `jordatech/requirements_management_obsidian` template pattern: keep Obsidian wikilinks intact, avoid `.obsidian/` edits unless requested, preserve fixed filenames when instructed, and generate concise system/software requirement plus system/software test-case examples from each idea's persona and pain. When the user wants those examples added into both `business_ideas` and `business_idea_generator`, copy the checked-in `BUSINESS_IDEA_REQUIREMENT_EXAMPLES.md` into the source repo root and the viewer repo `data/` snapshot, add a founder-visible `/requirements-examples` page in the Next.js app plus nav links, then rebuild, deploy, and verify the protected Vercel alias still returns `401` without credentials. See `references/business-ideas-to-obsidian-requirements.md`.

## Repository Pattern

For a private GitHub-backed idea system:

1. Create an ideas repository, e.g. `business_ideas`.
2. Store ideas under `ideas/<slug>.md`.
3. Maintain a lightweight index such as `ideas.json` for small/medium corpora.
4. Create a viewer app repository, e.g. `business_idea_generator`.
5. Keep secrets out of both repositories. Use environment variables for private repo access.
6. Use a bot branch for implementation work when the active agent profile defines one.
7. Commit meaningful checkpoints, but do not commit more than needed.

### Private GitHub + Vercel Pattern

If the viewer app needs to read a private ideas repo:

- Add `.env.example` documenting required variables only.
- Use `GITHUB_TOKEN` or a narrower fine-grained GitHub token at runtime/build time when live private-repo refresh is required.
- Store the real token in Vercel environment variables or GitHub Actions secrets, never in source.
- For a deployable viewer that should work **without secrets**, check in a sanitized local snapshot such as `data/ideas.json` plus `data/ideas/*.md`, and make the app try GitHub first, then fall back to local files.
- Document `GITHUB_TOKEN` as optional when a checked-in snapshot exists; the token becomes an enhancement for live refresh, not a hard deploy dependency.
- If Vercel GitHub repository linking fails but CLI auth works, an upload-based `vercel deploy --prod --yes` can still produce a valid production deployment. Report the link failure separately because automatic Git-triggered deploys may need Vercel/GitHub permission repair.
- If Vercel CLI is unauthenticated, stop at documentation and report the blocker; do not invent credentials.
- For Basic Auth-protected production deployments, a browser auth failure or unauthenticated `401` can be expected. Verify safely with `curl -I`, `vercel inspect`, and `vercel env ls production` rather than exposing credentials. See `references/focused-idea-query-view-and-vercel-basic-auth-verification.md`.

## Next.js Viewer Pattern

A practical v0 viewer can be simple:

- `app/page.tsx` renders idea cards and detail sections.
- `lib/ideas.ts` fetches/parses `ideas.json` or Markdown from the private repo.
- Fallback sample data is acceptable for local builds when no token is available.
- `docs/improvement_backlog.md` captures postponed improvements for scheduled jobs.

For a founder-facing dashboard, bias the homepage toward skimmable action:

- A clear hero explaining the job: find ideas worth testing before building.
- Search/filter controls for persona, pain, category, status, confidence, and tags.
- A "top ideas" card row like niche/opportunity sites, with concise pain snippets, calculated goodness score, and Competition/Potential/Est. MRR/Difficulty metrics.
- A short "how to use it" section that tells the founder to pick a buyer, read next actions, run one test, and kill weak ideas.
- Detail content with a Niche Hunter-style score/metrics panel above the Markdown brief plus short paragraphs, visible headings, and `Next actions` near the top.
- Always show the selected business model title immediately above the score/goodness panel. Do not make the user infer which model the score belongs to from the Markdown body below.
- Standalone detail pages must keep brief text readable. If the global app theme is dark, explicitly style the standalone `.brief-body` or equivalent content area so paragraph/list/heading text has high contrast (for example black text on a light panel) rather than inheriting white text on a light background.
- Selected business models should be easy to export: provide a direct `.md` download from the canonical/fallback Markdown, a clean standalone printable page, and browser print-to-PDF controls rather than adding PDF-generation dependencies by default. See `references/business-model-export-actions.md`.
- In focused brief views (`/?idea=<slug>#brief`), keep export/action links visually consistent with the search UI. If the user asks to match the Search button color, scope CSS to the focused action row (for example `.brief-link-row .nav-cta`) so global nav CTAs are not unintentionally restyled; verify computed styles in the browser for both `Open standalone brief` and `Download .md` against the Search button color.
- A `Potential competitors` section modeled on Niche Hunter's "Trending Apps" tab: linked competitors with Monthly Growth, Est. MRR, Strong Market, Category, Key Strengths, Weaknesses, and verification checks.
- Copy should follow Ruben Hassid-style readability: short paragraphs, direct address, concrete steps, minimal jargon, no hype, no generic AI phrasing.

When the root page supports query-selected briefs like `/?idea=<slug>#brief`, treat that as a **focused idea view**: hide homepage-only hero/how-it-works/top-ideas/database-list content and show only the selected business model brief, while preserving search and an obvious link back to the Business Idea Generator home. When search/filter query params are active without an `idea` param, treat that as a **search results view**: show the search form, active filters, and ranked result cards only; do not render the homepage hero or the selected-detail workspace. See `references/focused-idea-query-view-and-vercel-basic-auth-verification.md`.

See `references/private-founder-dashboard-layout.md` for session notes from a Niche Hunter-inspired redesign.

Verification:

```bash
npm install
npm run build
npm audit --audit-level=moderate
```

If `npm audit fix --force` proposes a breaking downgrade or major version change, do not apply it automatically. Document the advisory and wait for a safe upgrade path or user approval.

## Opportunity Source Locations

When the user provides sources for business ideas — Reddit communities, individual threads, forums, newsletters, directories, social feeds, LinkedIn job listings, app stores, marketplaces, or competitor lists — capture them durably instead of leaving them only in chat.

If LinkedIn feed/posts are login-gated, public LinkedIn Jobs can be used as hiring-demand signals. Label this clearly as **source intelligence, not validation**: a job post indicates headcount/budget around a workflow but not necessarily willingness to buy software. Cluster job postings by painful workflow, preserve title/company/date/URL when available, rank with skeptical-investor criteria, and document the access limitation. See `references/linkedin-jobs-opportunity-signals.md`.

Recommended handling:

1. Add/update a source document in the idea repo, e.g. `source_locations.md`.
2. Summarize what each source is good for and the cautions/quality risks.
3. Update recurring idea-generation automation so future runs consult the source document.
4. Treat community posts as **opportunity signals, not validation**.
5. Look for repeated pains, current workarounds, money/time lost, and consequences of doing nothing.
6. Add source URLs to idea frontmatter/body when a specific thread materially inspired the idea.
7. For a batch of recent Reddit-sourced technology-service ideas, preserve post date, subreddit, score/comment count, URL, and the business consequence that makes the pain investable.
8. When the user asks for a skeptical angel-investor lens, filter for buyer urgency, budget triggers, defensibility, and kill criteria; avoid generic "AI for X" summaries.

See `references/reddit-opportunity-source-locations.md` for a concrete Reddit source pattern used in Jordan's business idea system.
See `references/reddit-skeptical-investor-batch.md` for the workflow used to turn recent Reddit pain signals into full skeptical-investor business-model entries and a deployed viewer update.
See `references/source-intelligence-cron-updates.md` for the pattern used to add broader technology watering holes, Starter Story gap analysis, repo docs, and live Hermes cron prompt updates.
See `references/large-source-catalog-expansion.md` for the pattern used when Jordan asks for 100+ new internet places: group by source class, give every source a `Use for` and `Caution`, update the mirrored cron instructions doc, and patch both live cron jobs so the expansion changes actual scheduled behavior.

## Sensitive Data / Data Marketplace Ideas

When developing ideas that collect, broker, or sell user data — especially phone sensors, location, camera, audio, biometrics, health, children, bystander, or workplace data — treat the business as a **trust and compliance product**, not just a data-supply product.

Recommended handling:

1. Reframe risky wording like "scraping" into permissioned, opt-in, task-specific collection.
2. Identify the exact data buyer persona and the last expensive/unmet dataset problem they had.
3. Sequence the MVBP from lower-risk data modalities before sensitive modalities.
4. Prefer bounded active tasks over always-on background collection.
5. Include consent provenance, deletion/withdrawal, data minimization, redaction, fraud detection, quality scoring, and buyer-use restrictions in the business model.
6. Validate both sides separately: buyer willingness to pay and participant trust/permission drop-off.

For mobile-sensor AI dataset businesses, see `references/permissioned-mobile-sensor-data-businesses.md`.

When adding market evidence for data-collection or AI-training-data ideas, look for specific dataset bounty and active recruitment pages. Add each opportunity as source intelligence with the organization link, dataset/task requirements, and the lesson for the proposed business. Put this section near the top of the brief so it informs the MVBP and validation plan, and add the URLs to frontmatter `source_urls`. See `references/dataset-bounty-demand-signals.md`.

## Recurring Automation Pattern

For daily idea generation:

1. Schedule a first job that creates exactly one new idea, updates indexes, commits, and pushes.
2. Schedule a second job shortly after that commits at least one system improvement.
3. The second job should read a backlog file and either complete a small improvement or add/refine documentation if no safe code change is obvious.
4. Each job must verify the correct branch and avoid committing secrets.
5. When adding new watering holes or market-gap sources, update both durable repository docs and the live Hermes cron prompt; do not assume editing `source_locations.md` alone changes scheduled behavior. See `references/source-intelligence-cron-updates.md`.
6. If the repo has a mirrored operator doc such as `docs/daily_cron_idea_generation_instructions.md`, update it too so the checked-in instructions match the live cron prompt.
7. For large source expansions (for example 100+ new places), group additions by source class, give every source a `Use for` and `Caution`, and update both the idea-creation cron and the follow-up improvement cron so the scheduled system actually uses and preserves the broader source rotation. See `references/large-source-catalog-expansion.md`.
8. In the entrepreneur WSL environment, current checked-out business idea repos may live under `/home/miam/jordatech/`; use `HOME=/home/miam` if GitHub auth or Node tooling is unexpectedly missing due to profile-home isolation.

Example schedules:

- Idea generation: `0 3 * * *`
- System improvement: `30 3 * * *`

## Customer Discovery Quality Bar

A generated idea is not "validated" until there is evidence from real people or market behavior. Label untested ideas as draft or medium-low confidence.

Good validation questions:

- "Tell me about the last time this happened."
- "What did you do next?"
- "What tools or people did you use?"
- "How much time or money did it cost?"
- "What happens if you do nothing?"

Avoid:

- "Would you use this?"
- "Would you pay for this?"
- "Do you think this is a good idea?"
- Pitching before learning.

## Skeptical Investor Review (Enhanced Validation)

After initial customer discovery, run ideas through a skeptical investor lens to uncover weaknesses before pitching. This helps identify gaps in data moats, unit economics, and defensibility that might not surface in customer interviews alone.

**When to apply:** After conducting 5-10 customer discovery interviews but before building MVP. Also apply this framing earlier when the user explicitly asks to act as a skeptical angel investor; label the result as a draft hypothesis until customer evidence exists.

**How to conduct:**
1. **Data Moat Assessment**: Where is the proprietary data? Why can't competitors replicate it in 3 months? How does usage create a data flywheel?
2. **Vertical Integration Check**: Is this just a novelty tool or does it redesign industry workflows?
3. **Unit Economics Deep Dive**: What are the actual COGS (including AI inference costs)? What's the path to >80% gross margin?
4. **Human-in-the-Loop Evaluation**: Does the solution augment humans or replace them? Where is human oversight critical for liability and quality?
5. **Red Flag Screening**: Eliminate ideas with:
   - "Uber for X + AI" framing
   - Claims of "no API costs" or self-built foundational models
   - Founders who can't explain how the AI actually works
   - Solutions to "nice-to-have" rather than "must-have" problems

**Skeptical Investor Questions to Answer:**
- If I gave you $500k, how much goes to OpenAI APIs vs. proprietary development?
- Which specific, non-public dataset are you utilizing?
- When OpenAI releases a model that does this, what's your unfair advantage?
- Why does this need to be an AI company? Could a Python script solve it?

**Output:** Add these sections to your idea document:
- **Data Moat & Proprietary Advantage**: Specific data sources and network effects
- **Human-in-the-Loop Approach**: How humans augment the AI system
- **Unit Economics**: Detailed COGS, pricing, and margin analysis
- **FAQ for Skeptical Investors**: Direct answers to the four questions above

This process doesn't replace customer discovery—it complements it by forcing concrete thinking about defensibility and business model viability before investment.

## Pitfalls

- Do not confuse a product idea with a business opportunity; capture persona, pain, willingness to pay, and route to market.
- Do not call an idea validated just because it sounds plausible.
- Do not treat Reddit/forum/social posts as validation by themselves; they are source signals that require customer discovery or stronger market evidence.
- Do not use trust-destroying language like "scraping" for permissioned user-data businesses; explicitly design consent, transparency, minimization, and user value into the model.
- Do not start sensitive-data products with every possible sensor/modality; sequence from low-risk bounded tasks to higher-risk camera/audio/location only after demand and trust are proven.
- Do not let `ideas.json` become the only source of truth; keep human-readable Markdown primary unless the user chooses a database.
- Do not use arbitrary vanity scores such as `88`, `87`, `86` in opportunity cards; define a scoring rubric, store the inputs, calculate the displayed score, and expose the rationale.
- Do not present competitor Monthly Growth or Est. MRR as confirmed unless you have a source; label these as directional benchmarks or hypotheses when they are estimates.
- Do not add competitor names without links in business idea briefs; linked headings make the dashboard useful for follow-up research.
- Do not commit GitHub, Vercel, OpenAI, or analytics tokens.
- Do not deploy private-repo readers or checked-in private data snapshots to public Vercel URLs without access control; if exposure happens, immediately remove the Vercel project/deployment and verify public URLs no longer contain private markers.
- Before cleanup or redeploy work on a sensitive Vercel exposure, preserve the current revisions in pushed snapshot branches whose names include `vercel` when the user asks for a deploy-state snapshot.
- For a free/simple private Next.js idea viewer on Vercel, prefer app-level HTTP Basic Auth via Next.js `proxy.ts` with credentials in Vercel env vars; Vercel native Password Protection is not the free default because it is Enterprise or paid Pro add-on. For non-interactive Vercel CLI setup, pipe env values into `vercel env add`; using `vercel deploy -e KEY=value` can attach variables to one deployment but should not replace persisted project env vars for future deploys.
- When sharing generated Basic Auth credentials because the user explicitly asks, share them only in the final user channel, never commit them, and avoid printing them in logs except when needed to hand them off.
- When a profile's `HOME` is isolated, GitHub/Vercel auth may live in the real user home. Use `HOME=/home/miam` in the entrepreneur environment when CLI auth unexpectedly fails.

## References

- `references/first-10-clients-prospect-lists.md` — pattern, quality bar, and validation commands for adding `## First 10 clients` sections with 10 linked prospect/customer-discovery targets per business idea.
- `scripts/validate_first_10_clients.py` — reusable validator for checking source and viewer Markdown snapshots contain valid `## First 10 clients` sections.
- `references/batch-idea-intake-and-analysis.md` — workflow for converting Jordan's rough numbered idea lists/prototype notes into full business idea briefs, `ideas.json` entries, synced viewer snapshots, and deployment verification.
- `references/single-idea-source-article-intake.md` — workflow for turning one rough idea/domain plus a supporting article into a full sourced idea brief, including stdlib article extraction fallback and Vercel Basic Auth verification.
- `references/business-ideas-source-to-viewer-sync.md` — source-to-viewer fallback sync pattern for `business_ideas` and `business_idea_generator`, including missing Markdown detection, JSON validation, build, and two-repo commit verification.
- `references/opportunity-goodness-scoring.md` — Niche Hunter-style scoring rubric and detail-page analysis pattern for calculated `x/100` goodness scores based on Competition, Potential, Est. MRR, and Difficulty.
- `references/competitor-analysis-pattern.md` — Niche Hunter-style linked competitor analysis pattern with Monthly Growth, Est. MRR, Strong Market, Category, Key Strengths, Weaknesses, and verification checks.
- `references/private-founder-dashboard-layout.md` — Niche Hunter-inspired private founder dashboard layout pattern, Ruben-style copy/readability notes, and verification checklist.
- `references/focused-idea-query-view-and-vercel-basic-auth-verification.md` — focused root-query idea page pattern (`/?idea=<slug>#brief`) plus safe Vercel Basic Auth deployment verification commands.
- `references/focused-brief-legibility-and-validation-content.md` — focused/standalone brief title placement, readable Markdown CSS checks, and idea-specific validation/expert-panel update pattern.
- `references/business-model-export-actions.md` — Markdown download routes, standalone print/PDF controls, print CSS, and verification steps for selected business model exports.
- `references/private-github-nextjs-cron-idea-system.md` — session-specific implementation notes for a private GitHub-backed Next.js idea viewer with daily Hermes cron jobs.
- `references/private-github-vercel-snapshot-deploy.md` — fallback-snapshot pattern for deploying a private GitHub-backed Next.js idea viewer to Vercel without requiring secrets, including CLI auth and GitHub-linking pitfalls.
- `references/private-nextjs-vercel-protection-and-takedown.md` — emergency Vercel takedown verification, `vercel` snapshot branch preservation, and free Next.js Basic Auth protection plan for private idea viewers.
- `references/linkedin-jobs-opportunity-signals.md` — fallback workflow for using public LinkedIn Jobs as recent opportunity/demand signals when LinkedIn posts/feed content is login-gated, including skeptical-investor ranking and documentation cautions.
- `references/expert-panel-market-validation-model.md` — repo-wide/per-idea market validation audit pattern using Bill Aulet, Paul Cheek, Allan Dib, Giff Constable, Rob Fitzpatrick, and a skeptical investor lens, with segment-specific experiment playbooks and sync steps.
- `references/reddit-opportunity-source-locations.md` — Reddit communities/threads and evidence rubric for recurring idea-source monitoring.
- `references/reddit-skeptical-investor-batch.md` — workflow for turning recent Reddit pain signals into full skeptical-investor technology-service business-model entries, syncing both repos, and deploying the viewer.
- `references/permissioned-mobile-sensor-data-businesses.md` — pattern for developing opt-in phone-sensor/data-marketplace business models, including MVBP, architecture, revenue, trust, and validation notes.
- `references/dataset-bounty-demand-signals.md` — pattern and examples for adding active dataset bounty / paid data collection source intelligence to data-marketplace ideas, including requirements, lessons, and sync/deploy handling.
- `references/source-intelligence-cron-updates.md` — pattern for adding technology watering holes and market-gap sources to `source_locations.md`, creating source-specific docs/scripts, updating live Hermes cron prompts, and handling auth/build pitfalls in the business idea repositories.
- `references/skeptical-investor-review.md` — process for reviewing business ideas through a skeptical investor lens to uncover weaknesses in data moats, unit economics, and defensibility before pitching.
- `references/business-ideas-to-obsidian-requirements.md` — workflow for turning business ideas into Obsidian-linked requirements and test-case examples while preserving fixed filenames, wikilinks, and `.obsidian/` boundaries.
