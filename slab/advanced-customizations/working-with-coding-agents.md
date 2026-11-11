---
index: 3
---

# Work with coding agents

Start with the theme repository's `AGENTS.md`. It explains how to build and preview Slab, which project rules to read, and how to validate a change.

| Location | What it contains |
| --- | --- |
| `.agents/rules/` | Project standards for Liquid, JavaScript, accessibility, and more. Use the rules that match the files or components you are editing. |
| `.agents/skills/` | Guides for Liquid, accessibility, and code review. |
| `.agents/commands/` | Saved prompts for reviews, fixes, and release tasks. |

## Commands

Open the matching Markdown file under `.agents/commands/` and follow its steps. If your agent supports slash commands, you can use the command name.

| Command | What it does |
| --- | --- |
| `/review-rules` | Reviews changes against the project rules and review skills. |
| `/test-preview` | Checks the Shopify preview for a pull request. |
| `/review-submission` | Validates a theme release before submission. |
| `/add-doc` | Adds a `{% doc %}` LiquidDoc header to a snippet or block. |
| `/add-comment` | Adds inline comments explaining non-obvious logic. |
| `/pull-upstream-updates` | Merges `upstream/main` on a fork using the [Pull upstream updates](getting-started/pulling-upstream-updates.md) conflict policy. |

## Practical examples

#### "Rebuild this page to match a design"

1. Open a template file, for example `templates/index.json`
2. Attach a screenshot of the design you want
3. Prompt the agent:

```
Read the template and block rules before updating templates/index.json to match this design.
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
I just updated the cart drawer. Review it against the cart drawer accessibility rule
and verify keyboard navigation in the preview.
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
* **Attach images when you have them.** Describe the layout in words if you don't have an image.
* **Use review commands before committing.** Run `/review-rules` on the files you changed.
* **Point your agent to the project rules.** Start with `AGENTS.md` if your agent does not load the repository guidance automatically.
