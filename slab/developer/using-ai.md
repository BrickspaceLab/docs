# Using AI

Slab is set up to use AI-assisted workflows for implementation, review, and documentation with project-specific rules and command prompts.

## Canonical files

- `/Users/thomaskimura/Documents/GitHub/slab/AGENTS.md`
- `/Users/thomaskimura/Documents/GitHub/slab/.cursor/rules/`
- `/Users/thomaskimura/Documents/GitHub/slab/.cursor/commands/`

## How AI guidance is organized

- `.cursor/rules/`: coding standards for Liquid, JavaScript, Alpine, CSS, naming, localization, performance, and accessibility
- `.cursor/commands/`: reusable prompts for common tasks like reviews, docs generation, formatting, and submission preparation
- `AGENTS.md`: repo-specific instructions and runtime caveats for agents

## Recommended workflow

1. Start from a focused command (for example `/review-liquid` or `/review-javascript`).
2. Apply fixes against changed files only.
3. Re-run a targeted review command for validation.
4. Use `/prepare-submission` before release-related handoff.

## High-value review commands

- `/review-liquid`
- `/review-javascript`
- `/review-alpine`
- `/review-accessibility`
- `/review-performance`
- `/review-submission`

## Writing better prompts in this repo

- Reference exact files and components instead of broad requests.
- Ask for rule-based checks tied to `.cursor/rules`.
- Keep scope narrow (single bug, single component, or single workflow).
- Request concrete outputs (diff-ready edits, checklist, or risk findings).

## Gotchas

- Rules and workflow docs evolve quickly; verify the latest behavior in `.cursor/rules`, `.cursor/commands`, and `.github/workflows`.
- Some historical docs mention local-only review flows; current repo state also includes automated review in GitHub Actions.
