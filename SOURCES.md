# Skill sources and dependencies

Initially imported on 2026-11-03 and synchronized on 2026-11-16 from the
maintainer's active installed skills. This is a curated
backup of reusable instructions, not a dump of installed packages or runtime
state. The maintainer confirmed authorship of `work-detective`.

## Custom skills

| Skill | Active source at synchronization | Declared version/license |
| --- | --- | --- |
| coordinator | `~/.agents/skills/coordinator` | 1.3; no license declared |
| slack-message-drafter | `~/.agents/skills/slack-message-drafter` | No version or license declared |
| skill-improver | `~/.agents/skills/skill-improver` | No version or license declared |
| mad-senior | `~/.agents/skills/mad-senior` | 1.3; no license declared |
| development-orchestrator | `~/.agents/skills/development-orchestrator` | 2.2.0; MIT; bundled LICENSE retained with a non-personal contributor attribution |
| development-supporter | `~/.agents/skills/development-supporter` | 4.1; Apache-2.0 declared in frontmatter |
| jira-ticket-supporter | `~/.agents/skills/jira-ticket-supporter` | No version or license declared |
| requirement-collector | `~/.agents/skills/requirement-collector` | No version or license declared |
| progress-summary | `~/.agents/skills/progress-summary` | No version or license declared |
| project-manager | `~/.agents/skills/project-manager` | No version or license declared |
| work-detective | `~/.agents/skills/work-detective` | No version or license declared |

The selected custom sources now live in `~/.agents/skills`. Both Codex and
Claude personal aliases resolve to those same real directories; each source
was compared once. Repository copies are adapted only for Codex, with one
physical folder per skill and Codex references where needed. Installed sources,
symlinks and private runtime state are not migrated by this synchronization.

## Required third-party skills

| Skill | Required by | Source and license |
| --- | --- | --- |
| ponytail | coordinator implementation routing | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/84740e3d344b69b4a133201fa519eb37a62a2b2a/skills/ponytail), active installed plugin 5.2.0, commit `84740e3d344b69b4a133201fa519eb37a62a2b2a`; MIT, copyright DietrichGebert; license copied from the same bundled plugin snapshot |
| ponytail-review | coordinator; development-orchestrator; development-supporter; mad-senior | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/84740e3d344b69b4a133201fa519eb37a62a2b2a/skills/ponytail-review), active installed plugin 5.2.0, commit `84740e3d344b69b4a133201fa519eb37a62a2b2a`; MIT, copyright DietrichGebert |
| skill-creator | coordinator, when a reusable capability is needed; skill-improver also uses it when available | OpenAI Codex installed system snapshot at `~/.codex/skills/.system/skill-creator`; Apache-2.0 text retained; exact upstream revision not recorded |
| openai-docs | coordinator, when Codex configuration or client support needs verification during capability creation | OpenAI Codex installed system snapshot at `~/.codex/skills/.system/openai-docs`; Apache-2.0 text retained; exact upstream revision not recorded |
| find-skills | development-orchestrator, when discovery needs an additional capability | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills), locally installed snapshot; MIT, copyright Vercel, Inc. |

Only these five required skill folders are bundled, with their supplied license
files. Ponytail hooks, commands, optional audit/debt/help skills, and plugin runtime are not required
by the review skill and are excluded. Four third-party SKILL.md files remain
verbatim snapshots. Find Skills has a documented Codex-only installation
adaptation; its upstream provenance and license remain intact.

The local Skills CLI lock records `find-skills` from `vercel-labs/skills`, path
`skills/find-skills/SKILL.md`, installed/updated 2026-10-16, with folder hash
`76a98a285cb0434f3d39e1a873823556330e398b`. This is a folder hash, **not** a Git
commit. The original upstream SKILL.md SHA-256 is
`c00eeea0e13e74fe4a9d84ba0a8542205a1b736d65f13134fe1a6647eb14976f`. Its exact upstream commit was not recorded. The upstream
MIT license was retrieved on 2026-11-03; upstream HEAD at retrieval was
`7a5e920bead4b1039a6d6df5d7e1163b7b09423a`, not an asserted skill snapshot revision.

The Codex-adapted Find Skills entrypoint SHA-256 is
`5109c4994c9d566890bbde9153c796a72da53c40817643f89cbfbdfd82bc8a31`. Only its installation/update instructions and installation example
were changed; license and upstream discovery guidance are retained.

No repository-wide license is imposed. Each supplied license applies to its
own material; absence of a license is not a new redistribution grant.

## Dependency closure

- `coordinator` routes development through `development-orchestrator`, and other
  work through the matching retained specialist. Its risk-based reviews use
  `mad-senior` and `ponytail-review`. Capability creation conditionally requires
  `skill-creator`, and `openai-docs` for uncertain Codex client/configuration facts.
- `development-orchestrator` routes into `development-supporter`,
  `jira-ticket-supporter`, and `requirement-collector`, uses `ponytail-review` and
  `mad-senior` for applicable risks, and conditionally uses `find-skills`.
- `development-supporter` uses `ponytail-review` and `mad-senior` for applicable
  risks. Version 4.1 no longer requires the orchestrator's shared review-loop file.
- `skill-improver` uses `skill-creator` when available, with direct validation
  fallback. `mad-senior` routes executable-code questions to `ponytail-review`.
- `progress-summary` requires sibling `work-detective`.
- `coordinator` routes current-work refreshers to `project-manager`, which uses
  `jira-ticket-supporter` and the sibling `work-detective` session helper. Its
  journal is private user state, not a bundled resource.
- The remaining skills introduce no further required named skill dependency.
  Optional host document/spreadsheet/browser, plugin discovery and API-key
  capabilities are not vendored. In particular, OpenAI Docs uses
  `openai-platform-api-key` only when available. Executables, services, network
  access, and PyYAML are prerequisites, not skills.

## Synchronization evidence

On 2026-11-16, synchronized the eleven custom skills from the unified shared
source, including the new `project-manager`. Retained the five required
third-party dependencies. Repository workflows are adapted only for Codex,
with Codex metadata as sidecars. Other-host execution references are excluded.
The installer now targets only Codex’s documented `~/.agents/skills` location;
it leaves other products’ existing installations untouched. Codex discovery
guidance was verified through the official README link.

Refreshed `openai-docs/SKILL.md` and `agents/openai.yaml` verbatim from the
installed system snapshot. Its exact upstream revision remains unknown.
`skill-creator` remains identical to the installed snapshot. The installed
`find-skills` adds a machine-specific move/link instruction; the repository
omits that local migration instruction and adapts installation guidance to target
Codex explicitly. Discovery examples and upstream attribution remain intact.


On 2026-11-10, refreshed the retained custom workflows from active installed
sources and added the custom `slack-message-drafter`. Coordinator’s implementation
route now requires the standalone `ponytail` skill, so that skill is bundled
with the existing plugin license. The four existing third-party snapshots still
match their installed sources. At that synchronization, the collection had ten custom skills and five
required dependencies. General catalog routes (including optional Ponytail
audit/debt commands and document/browser tools) do not require bundling every
optional task capability. Private state and installed originals remain excluded.


The 2026-11-06 comparison covered all six existing custom skills and the two
retained third-party snapshots. Development Orchestrator 2.2.0, Development
Supporter 4.1, and Jira Ticket Supporter's Epic conventions were refreshed.
Requirement Collector, Progress Summary, Work Detective, Ponytail Review, and
Find Skills needed no content refresh after existing packaging adaptations.
Coordinator, Skill Improver, and Mad Senior are new custom additions.

The two new system dependencies were copied from their active installed
folders. No source Git revision was recorded there, so these are identified by
installed snapshot rather than an invented upstream commit. Current bundled
entrypoint SHA-256 (OpenAI Docs refreshed 2026-11-16):

| Snapshot | SKILL.md SHA-256 |
| --- | --- |
| skill-creator | `6656e54755638e8efcf275a472b9672eaa8a9a1b9e59dc210e275b03b59e1e66` |
| openai-docs | `208bb19dcdfa7cdcae5e6766ff3fd6bf7268d235c12a426869c8151a33e5c3ab` |

Ponytail retains its upstream `argument-hint` frontmatter. The bundled generic
validator does not recognize that field; YAML parsing and the source comparison
verify it without modifying the upstream manifest.

Their necessary references, scripts, UI metadata, icons and supplied license
texts remain together; no entire system-skill collection or vendor plugin was
copied. The collection targets Codex; retained third-party provenance and
research sources do not establish support for execution in other products.

## Packaging changes

- Personal-information exclusion is the highest-priority repository policy.
  Internal teams supply their own authorized identity, account and project
  context; repository copies do not inherit the maintainer’s personal setup.

- Imported Work Detective’s read-only local session helper from the shared source
  (source SHA-256 `7654b7db6d4c56c8e9da37b038f765b57f55fdba8d5c13376760f1915baaf374`).
  Adapted the repository copy to honor `CODEX_HOME`, select a versioned history
  database read-only, identify exported transcript formats from their contents,
  and report unavailable sources, unsupported schemas and missing transcripts.
  Added synthetic fixture tests; source text remains filtered/truncated and
  local history does not establish remote/account-wide coverage.
- Reconciled repository policies against all five earlier project conversations,
  preserving the final decisions on personal-repository PR delivery, separate
  merge/fork authority, global installation, source ownership and privacy.
  Historical transcripts, ticket defaults and one-time approvals are not bundled.

- Adapted unified local sources to Codex-only repository workflows. Removed
  other-host execution routes and Claude-specific agent/browser/skill APIs.
  Kept authorized Claude history as evidence readable from Codex, not a host
  requirement. Installed multi-product originals remain untouched.
- Restricted the installer to Codex and updated its temporary-profile tests.
  Find Skills routes authorized installations through Codex’s available installer
  or verified Codex-specific CLI options, avoiding multi-agent default installs.
- Added Project Manager with a host-independent private journal under
  `$XDG_STATE_HOME/project-manager/`, falling back to
  `~/.local/state/project-manager/`. No journal or work evidence is bundled.
- Generalized the team’s ticket-context repository requirement to resolve the
  current user’s authorized repository and its README before use. No private
  organization repository or historical ticket content is bundled.
- Refreshed Codex-specific dependency guidance while retaining standalone skill
  names alongside plugin namespaces and the exclusive Jira writer boundary.


- The 2026-11-06 package retained the original six custom workflows and added
  three; later synchronizations added Slack Message Drafter and Project Manager.
  Each keeps its required supporting files together.
- Removed maintainer names and author metadata, named audience/colleagues,
  concrete timezone, personal email-provider and involvement preferences, and
  historical approval claims. Examples now use fictional projects and roles.
- Jira assignee/reporter and reporting audience/timezone are resolved from the
  current user. The estimation formula is a suggested method, not inherited
  approval; current team conventions take precedence.
- Kept the custom MIT license terms with a generic contributor attribution;
  third-party copyright notices remain unchanged.
- Made custom callers of Ponytail Review accept the standalone `ponytail-review` name
  as well as the original plugin namespace, without changing review behavior.
- Replaced progress-summary's concrete Mac home path with sibling resolution.
- Replaced its real historical weekly report with a fictional style example.
- Excluded Jira's saved project/account/approval memory. Updated its skill to
  read/write private user state under `$XDG_STATE_HOME/jira-ticket-supporter/`,
  or `~/.local/state/jira-ticket-supporter/` when unset. The README explains
  migration of existing memory; installed private records were not changed.
- Generalized Jira Epic conventions by removing the private source link, real
  project names and ticket keys; preserved the required summary syntax and
  blank Fix behavior.
- Removed author metadata from new custom copies, preserving source versions,
  workflow gates, invocation policies and necessary supporting references.
- Excluded OS files, bytecode, caches, and generated/runtime state.

These changes make the backup portable and suitable for the existing public
repository while preserving workflow structure and approval boundaries. Identity
and team-specific choices now come from the current user.

## Deliberate exclusions

The live inventory of
[Momentum Standard Skills](https://github.com/MomentumMPS/standards-momentum-skills/tree/main/skills)
was checked on 2026-11-16. Its five skills remain maintained there:

- momentum-architecture-audit
- momentum-audit-skill-creator
- momentum-ci-cd-audit
- momentum-security-audit
- momentum-stack-audit

`pptx-generator`, optional Ponytail skills, other Codex system skills, and bundled
vendor plugins are installed third-party material without a required dependency
from this collection. They are excluded. Re-evaluate this list when dependencies
change; a new local installation alone is not reason to add it.
