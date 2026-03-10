# Working with coding agents

Slab ships with first-class support for AI-assisted development. The repo includes skills, rules, and commands that give any coding agent (Cursor, Claude, GitHub Copilot, etc.) the context it needs to write correct Shopify Liquid code, maintain consistency across the theme, and perform tasks that would otherwise require manual file editing.



## What's included

| Type         | Location            | Purpose                                        |
| ------------ | ------------------- | ---------------------------------------------- |
| **Skills**   | `.agents/skills/`   | Step-by-step workflows for specialized tasks   |
| **Rules**    | `.cursor/rules/`    | Always-on coding standards loaded into context |
| **Commands** | `.cursor/commands/` | Saved prompts for reviews, fixes, and docs     |



## Skills

Skills are focused instruction sets that tell the agent exactly how to approach a task. They are loaded on demand when you ask the agent to do something that matches the skill's description.

#### `update-shopify-json` — Edit templates with text or images

This is the most powerful skill in the repo. It lets you describe a page layout in plain text **or drop in a screenshot**, and the agent will produce valid Shopify JSON template output — no manual block hunting or schema reading required.

**How it works:**

1. You describe what you want (or share an image of a design)
2. The agent reads your prompt or analyzes the image to identify layout type, columns, content blocks, and spacing
3. It searches `/blocks` for the right block types, reads their schemas to check settings and nesting rules
4. It compiles a valid JSON structure you can paste directly into a template file

**Example prompts:**

```
Add a 3-column grid to the homepage with an image and a button in each column.
```

```
[attaches screenshot of a competitor's hero section]
Recreate this layout using Slab blocks.
```

```
Add a full-width slider section below the hero with 4 slides, each containing a heading and a link.
```

This output is valid Shopify JSON and can be pasted into any template file under `templates/`.

***

#### `shopify-liquid-themes` — Generate sections, blocks, and snippets

Generates Shopify Liquid code with correct schema JSON, LiquidDoc headers, translation keys, and CSS/JS patterns. Use this when building new components from scratch.

**Example prompts:**

```
Create a new testimonials section with a heading and up to 6 quote blocks.
```

```
Add a new block type to the hero section for a video background.
```

```
Write a snippet for a reusable price display that handles sale prices correctly.
```

The skill knows all 33 Shopify schema setting types, the `{% doc %}` tag format, translation key conventions, and when to use `{% stylesheet %}` vs `{% style %}` vs inline styles.

***

#### `liquid-theme-a11y` — Accessibility patterns

Provides WCAG 2.2 compliant component patterns for every common e-commerce UI element. Use this when building new components or fixing accessibility issues.

**Example prompts:**

```
Make the cart drawer accessible — it needs focus trapping and proper ARIA attributes.
```

```
Fix the product filters form so it works with a screen reader.
```

```
Review this carousel block and tell me what accessibility issues it has.
```

Covers: product cards, carousels, modals, cart drawers, forms, filters, price display, tabs, accordions, dropdowns, and tooltips.

***

#### `liquid-theme-standards` — CSS, JS, and HTML conventions

Enforces BEM naming, design tokens, CSS custom properties, progressive enhancement, and Web Component patterns. Use when writing or reviewing CSS and JavaScript in Liquid files.



## Rules

Rules are always-on guidance loaded automatically into the agent's context. They enforce consistency without you having to ask.

| Rule file              | What it covers                                                             |
| ---------------------- | -------------------------------------------------------------------------- |
| `liquid.mdc`           | Liquid syntax, file organization, variable naming, single top-level blocks |
| `snippets.mdc`         | Parameter defaults, color class splitting, LiquidDoc                       |
| `alpine.mdc`           | Alpine.js component structure, loading strategies, state management        |
| `blocks.mdc`           | Block patterns, nesting, schema structure                                  |
| `schemas.mdc`          | Setting organization and schema field ordering                             |
| `colors.mdc`           | Color system, CSS variables, color scheme utilities                        |
| `css.mdc`              | Custom CSS conventions when Tailwind is insufficient                       |
| `javascript.mdc`       | JS patterns, module structure, event handling                              |
| `tailwind.mdc`         | Tailwind CSS v4 utility class usage                                        |
| `naming-standards.mdc` | File prefixes, variable naming, BEM class names                            |
| `locales.mdc`          | Translation key structure, `t:` prefix usage                               |
| `html.mdc`             | HTML element choice, attribute ordering                                    |

These rules mean the agent will automatically follow Slab conventions without you specifying them. For example, it will use the right snippet naming prefixes, keep schema translations in `t:` format, and avoid hardcoding color values.



## Commands

Commands are saved prompts you can invoke with a `/` slash in Cursor's chat. Each one loads the relevant rules and runs a focused audit or generation task.

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

| Command                       | What it does                                                       |
| ----------------------------- | ------------------------------------------------------------------ |
| `/add-doc`                    | Adds a `{% doc %}` LiquidDoc header to a snippet or block          |
| `/add-block-documentation`    | Documents all settings in a block's schema                         |
| `/add-comment`                | Adds inline comments explaining non-obvious logic                  |
| `/fix-accessibility-issue`    | Diagnoses and fixes a specific accessibility problem               |
| `/fix-breaking-changes`       | Updates code for Slab API changes between versions                 |
| `/update-translations`        | Adds missing translation keys to locale files                      |
| `/update-schema-translations` | Syncs schema translation keys across locale files                  |
| `/format-presets`             | Reformats section preset JSON to match conventions                 |
| `/prepare-submission`         | Full release workflow: build, version bump, changelog, theme check |



## Practical examples

#### "Rebuild this page to match a design"

1. Open a template file, for example `templates/index.json`
2. Attach a screenshot of the design you want
3. Prompt the agent:

```
Using the update-shopify-json skill, update templates/index.json to match this design.
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
Run /update-schema-translations on sections/hero.liquid —
make sure all new t: keys exist in locales/en.default.schema.json.
```



## Tips

* **Be specific about files.** Name the template, section, or snippet you want modified. The agent works best with a clear target file.
* **Attach images when you have them.** The `update-shopify-json` skill is designed to accept screenshots — describing a layout in words works, but a visual reference produces faster, more accurate results.
* **Use review commands before committing.** Running `/review-liquid` and `/review-accessibility` on changed files catches most issues in seconds.
* **Rules are always active.** You do not need to tell the agent to follow Slab conventions — the rules load automatically. Focus your prompts on what you want, not how to write it.
