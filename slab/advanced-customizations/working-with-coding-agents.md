---
index: 3
---

# Work with coding agents

Start with the theme repository's `AGENTS.md`. It explains how to build and preview Slab, which project rules to read, and how to validate a change.

| Location | What it contains |
| --- | --- |
| `.agents/rules/` | Project standards for Liquid, JavaScript, accessibility, and more. Use the rules that match the files or components you are editing. |
| `.agents/skills/` | Workflows such as `edit-shopify-json` for schema-bound theme JSON and the Liquid skills for theme code. |
| `.agents/commands/` | Saved prompts for reviews, fixes, and release tasks. |

## Commands

Open the matching Markdown file under `.agents/commands/` and follow its steps. If your agent supports slash commands, you can use the command name.

#### Review commands

Run these after making changes to catch issues before committing:

| Command                 | What it audits                                           |
| ----------------------- | -------------------------------------------------------- |
| `/review-liquid`        | Liquid syntax, variable naming, file organization        |
| `/review-accessibility` | WAI-ARIA patterns, keyboard navigation, focus management |
| `/review-performance`   | Lazy loading, loop optimization, unnecessary re-renders  |
| `/review-alpine`        | Alpine.js component structure and loading strategy       |
| `/review-javascript`    | JavaScript correctness, event handling patterns          |

#### Generation and fix commands

| Command                    | What it does                                                       |
| -------------------------- | ------------------------------------------------------------------ |
| `/add-doc`                 | Adds a `{% doc %}` LiquidDoc header to a snippet or block          |
| `/add-comment`             | Adds inline comments explaining non-obvious logic                  |
| `/fix-accessibility-issue` | Diagnoses and fixes a specific accessibility problem               |
| `/fix-breaking-changes`    | Updates code for Slab API changes between versions                 |
| `/pull-upstream-updates`   | Merges `upstream/main` on a fork using the [Pull upstream updates](getting-started/pulling-upstream-updates.md) conflict policy |
| `/format-presets`          | Reformats section preset JSON to match conventions                 |
| `/prepare-submission`      | Full release workflow: build, version bump, changelog, theme check |

## Practical examples

#### "Rebuild this page to match a design"

1. Open a template file, for example `templates/index.json`
2. Attach a screenshot of the design you want
3. Prompt the agent:

```
Using the edit-shopify-json skill, update templates/index.json to match this design.
Keep the existing header and footer sections, replace the body sections with the new layout.
```

The agent will analyze the image, identify sections and blocks, and write the updated JSON.

***

#### "Add a new section from scratch"

```
Using the shopify-liquid-themes skill, create a new "Featured collection" section.
It should have a heading, a subheading, and a grid of up to 12 product cards.
The grid columns should be configurable (2, 3, or 4 columns on desktop).
```

***

#### "Audit accessibility after a change"

```
I just updated the cart drawer — run /review-accessibility on snippets/cart-drawer.liquid
and fix any issues you find.
```

***

#### "Keep translations in sync"

After adding new schema settings or user-facing strings:

```
Check the new schema translation keys in sections/hero.liquid against
locales/en.default.schema.json.
```

## Tips

* **Be specific about files.** Name the template, section, or snippet you want modified. The agent works best with a clear target file.
* **Attach images when you have them.** The `edit-shopify-json` skill is designed to accept screenshots — describing a layout in words works, but a visual reference produces faster, more accurate results.
* **Use review commands before committing.** Try `/review-liquid` and `/review-accessibility` on the files you changed.
* **Point your agent to the project rules.** Start with `AGENTS.md` if your agent does not load the repository guidance automatically.
