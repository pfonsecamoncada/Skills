# Repository instructions

## Highest priority: personal information and internal reuse

Never include the maintainer’s personal information in repository skill content
or bundled resources. This requirement takes precedence over copying an
installed source verbatim. Remove personal names and author metadata, emails,
usernames, account identifiers, concrete home paths, private links, named
colleagues/audiences, personal defaults, real work examples, saved approvals,
credentials, transcripts and runtime memory from repository copies. Preserve
required third-party copyright and license notices.

Adapt the skills for reusable internal team use: obtain identity, organization,
accounts, projects, audience, timezone, repositories and permissions from the
current authorized environment. Use fictional examples and portable paths; do
not make the maintainer’s private setup the team default. Keep required private
runtime state outside the checkout and installed skill folders.

Apply these changes only to repository copies. Preserve the installed originals
and their personal configuration unless installation or migration is explicitly
requested. Before every publication, inspect the complete included file set for
personal information and private state, including metadata, examples, scripts
and assets. Resolve any finding before publication and report validation limits.

## Codex-only adaptation

Repository skills are adapted only for Codex. Shared local skill folders are
source artifacts, not a promise of multi-product support in this repository.
Translate their workflows to Codex's available tools, skill discovery, agent
roles and permission model. Exclude other products' execution instructions,
host adapters and installation targets. Keep the installed shared sources
unchanged. Current explicit Codex-only scope overrides older multi-product
setup guidance recovered from previous conversations.

A workflow running in Codex may read authorized evidence from other products,
such as Claude conversation history. Treat those as data sources, not alternate
execution hosts or assumed tools. Preserve useful source coverage without
requiring Claude-specific tools to run the workflow.

## Scope and ownership

The canonical public repository is `pfonsecamoncada/Skills`, owned by its
maintainer. `MomentumMPS/momentum-skills` is a separate fork, not the default
publication target; `MomentumMPS/standards-momentum-skills` is the separate
standards collection. Preserve repository ownership, visibility and existing
maintainer access. Transfers, renames, fork synchronization and permission
changes require authorization for that specific action.

This repository backs up the maintainer's custom skills that are not maintained
in `MomentumMPS/standards-momentum-skills`. Compare that repository's actual
inventory before adding or moving a skill; do not classify solely by its name.
Do not duplicate its audit/audit-authoring skills here; verify the live inventory
rather than relying on a fixed count.

Include a third-party skill only when a retained custom skill requires it,
including a conditional workflow dependency. Record the consuming skill,
upstream source, known revision, license, and local modifications in SOURCES.md.
Follow dependencies transitively. Generic optional host capabilities (browser,
document, or spreadsheet support) do not justify copying entire vendor plugins.
Do not treat local installation as evidence of the maintainer's authorship.

External executables and services are prerequisites, not vendored skills.
Document required tools (such as Git, gh, acli, Python, and Node.js) and guide
their installation only when the selected workflow needs them. Do not bundle
binaries, package caches, credentials, or an entire plugin for one skill.
Suggest optional capabilities when relevant rather than installing them all.

## Layout

- Keep one flat `skills/<skill-name>/` collection for custom skills and required
  third-party dependencies. Mark ownership in the README and SOURCES tables.
- Keep each SKILL.md and its necessary references, scripts, assets, and optional
  agent metadata together. Preserve folder names used by dependency links.
- Keep repository documentation and the installer at the root. Add directories
  only for a real resource need; no per-product copies, category trees, generated
  bundles, or duplicated installation guides.
- Back up real files, not links into one machine's installed skill directories.
- Maintain one Codex-adapted copy per skill in this repository. Resolve installed
  aliases and deduplicate by real path before comparing or copying. Codex
  workflow instructions belong in SKILL.md with supporting references inside the
  skill. Optional Codex metadata belongs in agents/openai.yaml. Do not add
  alternate-host copies or adapters.

## Installation and portability

Document and support global user-level installation for Codex only, across projects.
Use home-relative or resolved paths, never one person's concrete home path.
The installer links repository skills only into Codex’s documented user-level
`~/.agents/skills` location. Verify official documentation before changing
Codex discovery guidance. Do not create or modify other products’ installation
roots, or add redundant Codex copies to mirror local source aliases. Do not
silently overwrite or remove existing installations. Preserve conflict checks,
dry-run behavior, repeatable installation and working paths containing spaces.
Document setup, update, backup, removal and the Windows/WSL limitations in README.

Keep required skills as siblings. Resolve supporting resources relative to the
skill's real directory. Allow standalone dependency names as well as a plugin
namespace when applicable. Do not assume a tool, connector, account, or plugin
exists in every Codex session. Preserve invocation policies and workflow gates.

## Backups and changes

Read installed skills as source artifacts when backing them up; copying a
workflow does not activate it or authorize its Jira, messaging, or deployment
actions. Prefer the active, user-selected version when copies differ. Preserve
installed originals unless the user requests installation or migration.

Publish reusable workflows without the maintainer's personal information or
private defaults. Resolve identity, accounts, audience, timezone, and team
preferences from the current user's context. Keep private runtime memory, account
identifiers, credentials, approval records, and real work evidence out of this
public repository. Use fictional examples and user-state directories outside
the checkout for mutable memory. Apply sanitization only to repository copies;
never remove personal data from the maintainer's installed originals. Record
packaging and portability changes in SOURCES.md.

Do not apply a blanket license to third-party or unlicensed skills. Preserve
existing notices and obtain actual provenance rather than inventing authorship,
versions, or permission. Add only dependencies required by the retained skills.
Disclose existing license gaps without inventing a license or presenting the
whole collection as freely licensed. A synchronization does not itself require
a relicensing decision.

Before delivery, verify the skill inventory, dependency closure, frontmatter,
local references, absence of private state, and `git diff --check`. Run installer
tests when installation behavior changes. Test in temporary directories, never
by replacing the user's installed skills. Report actual validation limits.

Keep README.md and SOURCES.md aligned with the final collection, including
ownership, exact counts, required consumers, upstream revisions (or explicitly
unknown revisions), licenses, local adaptations and deliberate exclusions.
Verify installed source hashes after synchronization to substantiate preservation.
Review changed executable behavior with Ponytail Review and consequential
privacy, scope or publication claims with Mad Senior when those risks apply;
reuse adequate reviews instead of adding repetitive approval gates.

## Synchronization and delivery

For a request referring to earlier project conversations, read the complete
relevant conversations, including corrections, later decisions and outcomes;
paginate as needed. Titles and summaries are retrieval aids, not sufficient
requirements evidence. Apply current corrections over superseded instructions.
Reconcile durable requirements into these policies and
README/SOURCES as appropriate. Keep private transcripts and work evidence out
of the repository. Do not promote a one-time action, superseded direction or
old approval into permanent authority.

When publication is authorized, use a feature branch in the personal repository
and open a PR into its main branch. Never push synchronization changes directly
to main or substitute the Momentum fork as the PR target. Verify the saved PR's
base/head repository, branches and commit. Leave merging to an explicit merge
instruction; approval for an earlier PR does not authorize a later merge.
After an authorized merge, verify the merge and fast-forward the local checkout
without discarding unrelated edits. Fork synchronization remains a separate,
explicitly authorized action.

Report the actual artifact/PR, changes, inventory, checks, review coverage,
installed-original preservation and remaining limitations. A delivered PR may
finish a PR-delivery request; it does not establish merge, deployment, acceptance
or Jira closure. Preserve the requested endpoint and continue authorized work.

## Coordination and Jira ownership

Use the available Coordinator skill as the primary session entry point unless
the user chooses otherwise. Keep small requests simple; delegate substantial
separable work with bounded ownership and capacity. Skill maintenance belongs
to Skill Improver; executable development and Git delivery go through Development
Orchestrator. Subagents keep their assigned roles and do not restart Coordinator.
Unavailable tooling is a precise limitation, not a reason to invent capabilities.

Use an explicitly supplied work ticket and record the work in Jira when requested;
do not infer a new ticket mandate from a past ticket-creation request. All Jira
operations and every acli invocation use Jira Ticket Supporter from the active
catalog or resolved shared skill source. It alone prepares, executes and verifies
authorized Jira mutations. Other skills hand it facts and the requested delta;
they never write through another CLI, script, API, browser or connector. Reads,
implementation, comments, transitions and closure retain their own authorization
scope. Other acli products remain read-only even when Jira Ticket Supporter is
active. Do not copy private Jira defaults or approval memory into these policies.

When using a skill, start each user-facing commentary/final message with one
bold label on its own line: **[SKILL NAME · PURPOSE]**. Use uppercase names with
spaces and no plugin prefix. Label the task owner, attribute supporting roles
when relevant, and distinguish a skill switch from a separate agent. Keep these
labels out of published tickets, source artifacts and tool calls.

## Conversation titles

When title tools are available, update only the current chat unless a bounded
batch rename was explicitly requested. Titles describe the requested outcome
and last verified state, never runtime idleness or the ticket status alone.

- Begin with exactly one status: `[OPEN]` for unfinished work that can continue;
  `[WAITING]` for a verified answer, approval, access or external dependency;
  `[PAUSED]` only when the user explicitly defers; `[DONE]` only when the requested
  outcome is verified and no required work remains.
- One ticket: `[STATUS] KEY-123: Short faithful topic`, derived from its real
  summary or trusted conversation. Multiple tickets:
  `[STATUS] [2 TICKETS][KEY-123 & KEY-456]: Shared topic`. Preserve every key and
  the count; use an unambiguous shared-prefix form when needed to fit.
- Without a specific work ticket: `[STATUS] [NO-TICKET] Subject — Specific task`.
  Incidental ticket mentions do not require adopting a ticket title.
- Keep the subject core stable and distinctive words early. Every WAITING title
  includes its verified dependency, such as `— Your QA approval` or `— CI results`.
  Never guess the responsible person or assume the dependency cleared.
- Reassess at start/resume, scope or dependency changes, explicit pause and before
  ending. Reopen DONE for additional work; replace NO-TICKET when scope adopts a
  real ticket. Use explicit dates for dated recaps. Verify the saved title and
  detect truncation; shorten wording before losing status, keys or dependency.
- For authorized historical batches, inspect requests, steering and outcomes;
  age, archive state and title alone do not prove completion. Preserve placement,
  record old/new titles, verify saves, and leave ambiguous classification unresolved.
  Do not message or resume chats merely to enforce titles. Titles are last-known
  state, not background monitoring.

## Jira authentication

Follow the current host's sandbox and approval rules. If a sandbox prevents
access to the authenticated CLI session or network, retry in an authorized
execution context before asking for login. All Jira write authorization
requirements still apply.
