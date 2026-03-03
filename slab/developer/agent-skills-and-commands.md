# Agent skills and commands

This page summarizes built-in skills and command prompts used in the Slab repository for repeatable AI workflows.

## Canonical files

- `/Users/thomaskimura/Documents/GitHub/slab/.agents/skills/`
- `/Users/thomaskimura/Documents/GitHub/slab/.cursor/skills/`
- `/Users/thomaskimura/Documents/GitHub/slab/.cursor/commands/`

## Agent skills in this repo

Under `.agents/skills/`:

- `agent-browser`: browser-driven QA workflow
- `find-skills`: helper for skill discovery
- `skill-creator`: helper for creating/updating skills

Under `.cursor/skills/`:

- `update-shopify-json`: workflow for safer Shopify JSON template updates

## Cursor command prompts

Current command files under `.cursor/commands/` include:

- `review-liquid.md`
- `review-javascript.md`
- `review-alpine.md`
- `review-accessibility.md`
- `review-performance.md`
- `review-submission.md`
- `prepare-submission.md`
- `fix-breaking-changes.md`
- `fix-accessibility-issue.md`
- `format-presets.md`
- `add-block-documentation.md`
- `add-doc.md`
- `add-comment.md`
- `update-translations.md`
- `update-schema-translations.md`

## Suggested usage pattern

- Use review commands first to identify risks.
- Use fix/format commands for scoped follow-up changes.
- Use docs/translation commands when updating schema, locales, or markdown docs.
- Keep command usage tied to changed files and target branch scope.

## Gotchas

- Command files are prompts, not executable scripts. Validate outcomes with theme check, local preview, and targeted QA.
- Skills can overlap in purpose; prefer the most specific skill/command for the current task.
