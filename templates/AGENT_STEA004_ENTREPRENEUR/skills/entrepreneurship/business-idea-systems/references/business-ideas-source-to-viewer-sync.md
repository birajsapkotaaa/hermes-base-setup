# Business Ideas Source-to-Viewer Sync Pattern

Use this when Jordan asks to add or refine an idea in `jordatech/business_ideas` and the `jordatech/business_idea_generator` viewer should stay usable from checked-in fallback data.

## Repositories

- Source of truth: `/home/miam/.hermes/profiles/entrepreneur/resource_repositories/business_ideas`
  - Markdown: `ideas/<slug>.md`
  - Index: `ideas.json`
- Viewer fallback snapshot: `/home/miam/.hermes/profiles/entrepreneur/resource_repositories/business_idea_generator`
  - Markdown: `data/ideas/<slug>.md`
  - Index: `data/ideas.json`
  - Runtime code may fetch the private source repo first and fall back to `data/` when `GITHUB_TOKEN` is absent.

## Workflow

1. Verify both remotes are `jordatech/*` and both branches are the bot branch, typically `c01entrepreneur_bot`.
2. Add or edit the canonical Markdown idea in `business_ideas/ideas/<slug>.md`.
3. Update `business_ideas/ideas.json` with matching metadata and `file: "ideas/<slug>.md"`.
4. Sync the viewer fallback snapshot from the source repo, not just the single new file:
   - Copy `business_ideas/ideas.json` to `business_idea_generator/data/ideas.json`.
   - Copy the new or changed idea Markdown to `business_idea_generator/data/ideas/<slug>.md`.
   - Check whether the source index references markdown files missing from `business_idea_generator/data/ideas/`; copy those too so fallback data does not drift behind the source.
5. Validate both JSON indexes with `python3 -m json.tool`.
6. Run the viewer build, usually `npm run build` from `business_idea_generator`.
7. Commit and push each repository separately, then verify clean status and the GitHub commit URLs.

## Pitfalls

- The viewer may look correct in production when it has `GITHUB_TOKEN`, while local/build fallback data is stale. Always update the checked-in `data/` snapshot when the task asks to update both repos or the viewer.
- Do not rely on `ideas.json` alone. Each indexed `file` should have a corresponding Markdown file in the source repo and, when snapshotting, in the viewer `data/ideas/` directory.
- If a build updates generated framework folders, check status carefully and avoid committing unrelated artifacts unless the repository expects them.
- For investment/health/legal/other regulated ideas, frame claims carefully and add compliance caveats in the idea brief rather than presenting the product as turnkey regulated advice.
