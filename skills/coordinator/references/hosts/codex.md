# Coordinator host note: Codex

Use this reference for Coordinator’s Codex routes, skill locations, agent roles and startup configuration.

## Skill sources

- Expand short path aliases through the session's skill-roots table.
- Codex discovers user-level skills in `~/.agents/skills`; symlinked skill folders are supported. Follow active catalog paths and inspect compatibility aliases under the configured Codex home (often `~/.codex/skills`) when present. Resolve and deduplicate by real path. [Skill locations](https://learn.chatgpt.com/docs/build-skills)
- System helpers normally live under `<Codex home>/skills/.system/<name>/SKILL.md`. Use the active catalog's source for namespaced plugin skills; do not hard-code plugin versions or edit managed caches.
- User-owned chats are Codex chats: never create one without an explicit request.

## Route names

| Generic route | Codex skill or tool |
|---|---|
| Documents, PDFs, presentations, spreadsheets, visualizations | Documents/PDF, Presentations, Spreadsheets or Visualize; connected Google files: the matching Google Drive skill; a live Excel session: Excel Live Control |
| Website, page or ChatGPT Pages/Spaces, ChatGPT pet | `sites`, `pages` or `work-pets` |
| Bitmap image or reusable artifact template | `imagegen` or `template-creator:template-creator` |
| New reusable skill | `skill-creator` |
| Skill installation, plugin management | `skill-installer`; `plugin-management:plugin-management` |
| Product/configuration/API questions | `openai-docs` |
| Project Manager role | native custom-role selection when the delegation tool exposes it |

## Agent roles (capability-creation)

Inspect the installed CLI version/help and only relevant agent/config keys or files. Never print the full user config, tokens or credential stores. Check current official guidance through `openai-docs` when installed behavior is unclear or the schema has changed.

Current documentation supports standalone personal agents in `~/.codex/agents/*.toml` and project agents in `.codex/agents/*.toml`. Each defines `name`, `description` and `developer_instructions`; `name` determines the role, not the filename. Avoid built-in names unless intentionally replacing one. Optional model/effort values override inherited values; omit them unless specifically needed and authorized. Agents inherit parent permissions, provider and MCP servers; sandbox/approval overrides in a role do not replace those controls. Supported capability toggles can reduce tool availability. [Custom agents and inheritance](https://learn.chatgpt.com/docs/agent-configuration/subagents)

Minimal example, to adapt to an evidenced role rather than install automatically:

```toml
name = "evidence_checker"
description = "Check material claims against supplied sources without editing or publishing."
developer_instructions = """
Review only the assigned artifact and relevant evidence.
Distinguish observations, assumptions and unresolved questions.
Return source-backed findings, limitations and the next needed decision.
Do not edit files, publish, or take the proposed operational action.
"""
```

The configuration reference also documents `[agents.<name>]` declarations with `description` and `config_file`; relative `config_file` paths resolve from the declaring config. Do not mix registration and standalone formats or assume an arbitrary TOML file is discovered. Scalar `[agents]` settings are reserved names. Preserve existing registrations. [Agent configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

Prefer the standalone format so a new role does not require changing global defaults. Project configuration depends on trust and can be skipped in an untrusted project; do not change trust settings merely to enable discovery. [Configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic)

Validation: parse TOML with an actual TOML parser and validate against a schema for the correct file type; the root `config.toml` schema is not automatically a standalone-agent schema. [Published root configuration schema](https://learn.chatgpt.com/docs/config-schema.json) For the inspected local CLI, `app-server --print-startup-config --strict-config` validates startup configuration without launching the server; avoid displaying its full output. Check the delegation tool's schema for an `agent_type`/role selector before claiming a saved role is active.

## Global startup file

Use the active Codex-home `AGENTS.md` (default `~/.codex`). Global discovery uses `AGENTS.override.md` before `AGENTS.md`; another configured Codex home is a separate scope. [AGENTS.md discovery and precedence](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
