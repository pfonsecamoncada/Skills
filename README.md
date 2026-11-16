# Skills

Codex skills for coordination, development, requirements, ticket creation,
review, and work reporting. Maintained in
[pfonsecamoncada/Skills](https://github.com/pfonsecamoncada/Skills).
Skills maintained in
[Momentum Standard Skills](https://github.com/MomentumMPS/standards-momentum-skills)
belong there and are excluded here. Third-party skills are included only when
one of these custom skills depends on them.

The repository copies are adapted **only for Codex**, for internal team use.
Repository skills must never contain the maintainer’s personal information or private working state. Each
team supplies its own identities, accounts, projects, audience and preferences
through current authorized context. Privacy takes priority over verbatim source
copying; installed originals retain their own personal configuration.

## Collection

| Skill | Ownership | Purpose |
| --- | --- | --- |
| [coordinator](skills/coordinator) | Custom | Coordinate the overall outcome across specialist skills and bounded agents. |
| [project-manager](skills/project-manager) | Custom | Recover pending work and keep a private continuity journal across Codex sessions. |
| [skill-improver](skills/skill-improver) | Custom | Review and improve skill intent, strategy, and instructions. |
| [mad-senior](skills/mad-senior) | Custom | Review consequential non-code decisions and evidence. |
| [development-orchestrator](skills/development-orchestrator) | Custom | Coordinate skills, reviews, approvals, and delivery. |
| [development-supporter](skills/development-supporter) | Custom | Resolve Jira work through code, branch setup, or a no-code outcome. |
| [jira-ticket-supporter](skills/jira-ticket-supporter) | Custom | Draft and create Jira tickets with reusable templates and verified context. |
| [requirement-collector](skills/requirement-collector) | Custom | Consolidate requirements and prepare approved ticket drafts. |
| [progress-summary](skills/progress-summary) | Custom | Write a weekly spoken leadership update from work evidence. |
| [slack-message-drafter](skills/slack-message-drafter) | Custom | Draft Slack messages using the current user’s evidenced voice. |
| [work-detective](skills/work-detective) | Custom | Reconstruct work across connected sources with supporting evidence. |
| [ponytail](skills/ponytail) | Third-party dependency | Apply the smallest complete implementation in development workflows. |
| [ponytail-review](skills/ponytail-review) | Third-party dependency | Review proposals and results for the development workflows. |
| [find-skills](skills/find-skills) | Third-party dependency | Discover missing capabilities for development-orchestrator. |
| [skill-creator](skills/skill-creator) | Third-party dependency | Author and validate capabilities when Coordinator needs them. |
| [openai-docs](skills/openai-docs) | Third-party dependency | Verify Codex configuration and client guidance for capability creation. |

Everything lives directly under `skills/<skill-name>/`. Each folder is the
Codex-adapted copy. Workflow instructions stay in `SKILL.md`, supporting
references stay with the owning skill, and optional Codex UI metadata stays in
`agents/openai.yaml`.
There are no separate product copies or category directories.
[SOURCES.md](SOURCES.md) records origins, dependencies, exclusions, and packaging
changes. [AGENTS.md](AGENTS.md) defines how to maintain this repository.

## Install globally

Here, **global means user-level: available across all local projects for your
operating-system account**. Never install this collection into an individual
project. Installation does not require administrator access or `sudo`.

The installer uses Codex’s documented user-level `~/.agents/skills/` location.
See [OpenAI skill locations](https://learn.chatgpt.com/docs/build-skills). It creates
no installation links for other products. Other software may independently
scan that shared directory; this collection supports execution only in Codex.

### macOS and Linux

Requires Git and Python 3. Keep the clone in a permanent location under your
home directory. For example:

```sh
mkdir -p "$HOME/.local/share"
git clone https://github.com/pfonsecamoncada/Skills.git "$HOME/.local/share/agent-skills"
cd "$HOME/.local/share/agent-skills"
python3 install.py --dry-run
python3 install.py
```

If you already have a clone, run the last two commands from that clone instead.
The installer links each complete skill folder into `~/.agents/skills`,
pointing to the physical files in this clone. Dependencies are included
automatically. Keep the clone in place; no additional `~/.codex/skills` copy is needed.

Existing links to this clone are accepted on reruns. An existing directory,
different link, or broken link with the same name stops installation before any
links are created. Compare its contents with this repository and preserve local
edits before moving it to a backup location **outside all skill discovery
folders**. Do not use force-overwrite commands. Retry after resolving the
reported conflicts. A later filesystem/permission failure can leave some links
installed; correct that error and rerun safely.

When migrating an older `jira-ticket-supporter`, keep its
`references/project-memory.json` private. Move that file to
`~/.local/state/jira-ticket-supporter/project-memory.json`, or the equivalent
location under your configured `XDG_STATE_HOME`, before retiring the old skill.
Do not overwrite existing state; reconcile both sets of entries if necessary.

Check for older duplicate Codex installations in `~/.codex/skills/` and enabled
plugins. The installer does not remove them or manage other products’ existing
installations. Keep one active source for each skill after comparing any local differences;
duplicate copies can produce duplicate or conflicting skill choices.

### Windows

For tools running inside WSL, use the Linux instructions inside that WSL user
account. For native Windows tools, clone into a permanent directory under your
Windows user profile and run:

```powershell
py -3 install.py --dry-run
py -3 install.py
```

Native Windows symlinks require suitable permissions (commonly Developer Mode).
If symlinks are unavailable, copy each complete `skills/<skill-name>` directory
into `%USERPROFILE%\.agents\skills\` after checking for conflicts.
Keep all sixteen folders together so relative dependency references resolve.
Copies must be updated manually; symlinks keep one source in the clone.

### Verify and use

Start a fresh Codex session, open an unrelated project, and ask it to
list the available skills. Confirm the eleven custom skills and five dependencies
appear. For example: "Use requirement-collector to organize these requirements."
Invoke a skill with `$skill-name` in Codex.

The installer supplies instructions and supporting files, not service access.
Jira workflows require authenticated `acli`; repository delivery requires Git
and `gh`; discovery through `find-skills` uses Node.js/npm. Work research needs
the relevant connectors or permitted browser/desktop tools. Check the selected
skill's prerequisites and use the capabilities exposed by the current Codex session.
Skill validation uses Python 3 with PyYAML; the OpenAI Docs helpers use Node.js
and network access. Install these only when their selected workflow needs them.
Installing a skill does not install connectors or authorize external writes.

When a required tool is missing, ask your assistant to help install it from its
official source and verify it before continuing that workflow. Install optional
tools only when needed. This repository bundles the five required third-party
skill folders, not their entire upstream packages, command-line tools, or
binaries. Their licenses and sources are recorded in SOURCES.md.

Project Manager stores its journal outside the checkout in private user state,
shared across Codex sessions. Jira memory and the development skill inventory
also belong in private user state. None is created by this installer. Work Detective’s
optional Python helper reads authorized local Claude/Codex session stores; its
local coverage is not a substitute for unavailable remote chat history.
Claude history is an evidence source read from Codex, not an execution target.

The skills resolve identity, assignee, audience, timezone, and service choices
from the current user's context. No maintainer account, personal reporting
preferences, or private project memory is bundled.
`agents/openai.yaml` is optional Codex metadata; the portable entrypoint is
`SKILL.md`.

User-level files apply to local sessions. They are not automatically installed
into remote machines, cloud agents, or other operating-system accounts.

## Update, back up, and remove

From the permanent clone, run `git pull --ff-only`, review the changes, and run
`python3 install.py` again to link newly added skills. Existing links immediately
see updated files. Preserve local edits before pulling; do not reset them away.
If a skill is removed from the repository, remove its obsolete user-level links
after checking their targets.

For installations linked to this clone, changes through an installed symlink
also change the repository. When backing up separately maintained installed
skills, compare their active sources and apply privacy and portability changes
only to repository copies. Review `git diff` before committing and pushing backups. Do not copy entire installed-skill or plugin-cache directories
into the repository.

For separately maintained installations, resolve `~/.agents/skills` and any
catalog aliases before comparing sources. When aliases resolve to the same
folder, compare it once. Adapt the repository copy to Codex while preserving
its intended workflow and privacy rules. Leave shared installed originals intact.

To uninstall, remove only the per-skill symlinks that point into this clone from
`~/.agents/skills/`. Keep other products’ installations, unrelated skills and private
runtime state. Remove the clone only after its links are gone and any edits are
backed up. For copy-based installs, compare and back up local edits before
removing those specific copied folders.

## Maintenance checks

```sh
python3 -m unittest -v test_install.py
python3 -m unittest discover -s skills/work-detective/scripts -p 'test_*.py' -v
git diff --check
```

The installer and session-helper tests use temporary directories and do not
touch installed skills or real chat history. Also check each changed skill's frontmatter, local references, dependency
closure, and provenance. Keep runtime memory, credentials, work reports, and
machine-specific absolute paths out of backups. Existing per-skill licenses are
preserved; see [SOURCES.md](SOURCES.md) for license scope.
