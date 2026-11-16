# Create or improve a capability when it adds durable value

Use this reference for explicit capability requests and opportunities identified during Coordinator's normal routing, execution or completion checks. Relevant reusable local skill/agent authoring is covered by the user's Coordinator policy; it does not authorize unrelated installations, expanded account access or weakened controls. Honor narrower task instructions and the normal filesystem approval mechanism.

## Choose the smallest useful change

- **Reuse:** an existing skill or focused worker brief is sufficient and there is no concrete durable benefit to authoring. Keep one-off details in the assignment.
- **Improve:** an existing maintained skill owns the workflow, but its instructions cause avoidable rework, miss an accepted recurring preference, or omit reusable knowledge established by the task. Route to `skill-improver` with the observed behavior and source evidence. Distinguish an instruction defect from execution that ignored adequate instructions; the latter may need a corrected handoff, not more rules.
- **Create:** no suitable skill owns a reusable workflow, and preserving its non-obvious method would materially help future work or repeated parts of the current assignment. Route to `skill-creator` from the active Codex catalog or the bundled standalone skill. Successful ad hoc work can establish this opportunity; inability to complete the task is not required, nor is an arbitrary number of prior occurrences.
- **Specialize an agent:** use a narrowly scoped Codex agent TOML role only when stable role instructions/capability settings add value beyond a skill. Prefer references to installed skills over copying workflows. A role definition is not an extra permission grant.

For authoring, give the selected owner the evidence, intended requests and benefit, nearby exclusions, existing owner/candidate overlap, maintained destination, constraints, authorization and representative validation cases. Resolve aliases and inspect current changes before editing. Default to user-maintained skills; for a managed skill, prepare a concrete proposal at its maintained source rather than patching a plugin cache or creating a shadow copy. Missing authoring tools need an explicit fallback or limitation, not a claim that authoring ran.

Keep this work bounded and scheduled: complete it directly when small, delegate an independent change when capacity permits, or queue it after the main dependency. Do not introduce recursive maintenance of the authoring skills or a collection-wide audit. If the evidence is weak, the benefit is speculative or scope excludes maintenance, reuse current capabilities. Defer a selected worthwhile change only for a concrete scope, priority, access or unresolved decision constraint; state what is prepared and what remains.

Inspect and validate the changed capability before using it: follow its owner's structural and behavioral checks, preserve a reviewable diff, verify installed content, and exercise representative safe scenarios where useful. Keep authoring separate from live execution. Report the changed capability and benefit, or the specific deferral; do not equate a proposed change, saved file or scenario walkthrough with verified runtime use.

## Agent role format: verify the installed client first

Read [the Codex configuration reference](hosts/codex.md) for role format, location, discovery and validation. Check the installed Codex client and active delegation schema before writing a role; a TOML file on disk is not proof that the current runtime discovers it.

## Preserve configuration and authority

Before writing, inspect the maintained destination and existing changes. Prepare a narrow diff, preserve unrelated content, avoid name collisions and use the normal filesystem permission mechanism. Do not add model overrides, change global concurrency/defaults, broaden tools, modify provider/MCP credentials, or relax sandbox/approval settings to make the role work. Such changes are a separate concrete decision, not an implication of creating a worker.

Generated skills and agent roles must preserve the Jira write boundary: `acli` is read-only outside `jira-ticket-supporter`; Jira mutations are handed to that owner for preparation, execution and read-back. Do not generate a competing writer, alternate-client fallback or payload for another skill to execute.

A textual read-only instruction is a behavioral constraint, not a new sandbox. Keep the parent session's actual permissions appropriate to the task. A specialized role cannot approve its own critical actions, expand its assignment, or delegate recursively without the coordinator's bounded authorization.

## Validate, then verify availability honestly

1. Parse the role file with an actual parser for its format, check the required fields, unique name, referenced skill paths and only supported keys.
2. Inspect the installed CLI's validation/help facilities before using them (host note). A listing or config check is not proof that a named agent has been selected.
3. Walk through an intended task, an adjacent task that should not use the capability, and a failure/permission case. Use safe temporary fixtures. Check that the agent preserves scope, produces usable evidence, reports blockers and cannot authorize its own external actions. Run executable helpers only when needed and within the test authorization.
4. Check the active delegation tool's schema/catalog for named-role selection (host note). A task label is not proof of a role selection. If the runtime exposes no custom-role selector, use a normal worker with the validated instructions in its brief, explicitly describing that as prompt-based delegation rather than claiming the saved role is active.
5. Verify discovery in a fresh supported session when necessary. Do not promise hot reload, change an already-running worker's configuration by editing a file, or launch a paid model test solely to manufacture activation evidence. Report separately: files saved, syntax/instructions checked, discovery verified, and actual role execution verified.

The current collaboration tool surface may differ from the public CLI. Inspect the live tool contract every time; do not invent an agent-type, role, or configuration-file parameter it does not expose.

## Global Coordinator startup guidance

For the user's explicit preference to start new sessions with Coordinator, add a concise instruction to the active Codex home's global instruction file (host note), preserving existing preferences. Later project instructions can override earlier guidance. Codex builds this chain per session, so verify in a fresh session rather than promising an existing chat reload.

Apply that startup instruction to the primary/root agent only. A delegated worker must retain its assigned specialist role; it must not bootstrap another Coordinator merely because it inherits global instructions. A root can read and follow Coordinator without spawning a duplicate root agent. Respect explicit current user exclusions, higher-priority instructions and unavailable delegation tools.

This is a local Codex startup convention, not a guarantee that remote or already-running sessions load the file. Preserve existing global overrides rather than deleting them to force activation. Verification should inspect loaded instruction sources or a fresh-session response without changing model, permission or account settings.

Recheck current Codex support before future agent or configuration changes.
