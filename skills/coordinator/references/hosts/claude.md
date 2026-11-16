# Coordinator host note: Claude Code

Read this only when running in Claude Code. It maps Coordinator's generic routes and rules to Claude Code names.

## Skill sources

- Load catalog skills through the `Skill` tool.
- Claude Code reads `~/.claude/skills` and applicable project `.claude/skills`; personal entries may be symlinks into the shared source `~/.agents/skills`. Resolve and deduplicate by real path.
- Built-in and plugin skills are namespaced, such as `anthropic-skills:*` and `ponytail:*`; use the catalog source and do not hard-code plugin versions or edit managed caches.
- Internal agents use the `Agent` tool. User-owned sessions are started with `mcp__ccd_session__start_session`: never without an explicit request.

## Route names

| Generic route | Claude Code skill or tool |
|---|---|
| Documents, PDFs, presentations, spreadsheets, visualizations | `anthropic-skills:docs` (editable docs, default) or `anthropic-skills:docx`, `anthropic-skills:pdf`, `anthropic-skills:pptx`, `anthropic-skills:xlsx`; visualizations: `dataviz` or an Artifact (`artifact-design`); connected Google files: `anthropic-skills:google-workspace` with the Google Drive connector |
| Website or shareable page | An Artifact (`Artifact` tool, `artifact-design` skill) |
| Bitmap image or reusable artifact template | No bitmap image generation: offer an SVG/HTML Artifact. Templates: Artifact types (`Artifact` tool `quickstart`, or `list` with `scope: types`) |
| New reusable skill | Installed `skill-creator` or the catalog’s `anthropic-skills:skill-creator`; inspect the selected source and available tools |
| Skill installation, plugin management | `find-skills`; `ListPlugins`, `SearchPlugins`, `SuggestPluginInstall` |
| Product/configuration/API questions | The `claude-code-guide` agent or the `claude-api` skill |
| Project Manager role | `Agent` tool with `subagent_type: project-manager` (`~/.claude/agents/project-manager.md`) when listed |

## Agent roles (capability-creation)

Inspect the installed CLI version/help and only relevant agent/config keys or files. Never print the full user config, tokens or credential stores. Check current official guidance through the `claude-code-guide` agent when the installed behavior is unclear or the schema has changed.

Current documentation supports personal subagents in `~/.claude/agents/*.md` and project subagents in `.claude/agents/*.md` (project wins on a name collision). Each is Markdown with YAML frontmatter defining `name` and `description`; the body holds the instructions. `name` determines the role, not the filename. Avoid built-in names (such as `general-purpose`, `Explore`, `Plan`) unless intentionally replacing one. An optional `model` value overrides the inherited model. Omit it unless specifically needed and authorized. Subagents inherit parent permissions and MCP servers; a role does not replace those controls. An optional `tools` list can reduce tool availability. [Subagents](https://code.claude.com/docs/en/sub-agents)

Minimal example, to adapt to an evidenced role rather than install automatically:

```markdown
---
name: evidence-checker
description: Check material claims against supplied sources without editing or publishing.
---

Review only the assigned artifact and relevant evidence.
Distinguish observations, assumptions and unresolved questions.
Return source-backed findings, limitations and the next needed decision.
Do not edit files, publish, or take the proposed operational action.
```

Do not assume an arbitrary Markdown file outside those directories is discovered. Preserve existing definitions rather than migrating them gratuitously.

Use project scope for a project-specific role and personal scope only for a reusable personal role. Do not change `~/.claude/settings.json` or permission settings merely to enable discovery.

Validation: parse the YAML frontmatter with an actual YAML parser. The `/agents` command in an interactive session lists loaded subagents. Check the `Agent` tool's listed `subagent_type` values before claiming a saved role is active.

## Global startup file

Use `~/.claude/CLAUDE.md`. Project `CLAUDE.md` instructions load after the user file and can override it; Claude Code loads the chain at session start. [CLAUDE.md memory files](https://code.claude.com/docs/en/memory)
