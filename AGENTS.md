---
published: false
---

# Agents

## Cursor Cloud specific instructions

### Overview

This is a **Knowing-compatible Markdown documentation repository** for Brickspace Lab's Shopify themes and apps. There is no application server or build step. Development consists of editing Markdown and verifying theme claims against source. Run `npm run check` to validate publication metadata, page coverage, links, assets, and supported block structure. See `.migration/README.md` for migration evidence and remaining acceptance checks.

### Products documented

| Directory | Product | Type |
|---|---|---|
| `general/` | General / Support Hub | Cross-product support & dev guides |
| `paper/` | Paper theme | Shopify theme (large catalog storefronts) |
| `space/` | Space theme | Shopify theme (visual impact storefronts) |
| `slab/` | Slab theme | Shopify theme (fully modular) |
| `keystone/` | Keystone theme | Shopify theme (B2B / wholesale) |
| `pallet/` | Pallet app | Shopify app (B2B pricing groups) |

### Theme source sync

Before writing or editing theme documentation, run `npm run sync` to pull the latest theme source code into `.src/`. This clones the private repos `brickspacelab/slab`, `brickspacelab/paper`, `brickspacelab/space`, and `brickspacelab/keystone` via HTTPS. The sync requires:

- **`rsync`** — installed by the update script.
- **`BRICKSPACE_GITHUB_TOKEN`** — a GitHub Personal Access Token (classic or fine-grained) with read access to the private BrickspaceLab theme repos. Must be added as a Cursor secret. The update script configures git to use this token automatically for `brickspacelab/*` repos.

If `npm run sync` fails with "Repository not found", the token is missing or lacks the required permissions.

### Cursor rules

The `.cursor/rules/` directory contains three rule files that apply automatically based on file globs:

- `theme-docs.mdc` — enforces source-of-truth verification against `.src/<theme>/` schema and locale files.
- `changelog.mdc` — standards for changelog entries.
- `formatting.mdc` — markdown formatting conventions.

### Source verification workflow

Schema settings use translated labels like `"label": "t:general.settings.dropdown_menu.label"`. Resolve these by looking up the key path in `.src/<theme>/locales/en.default.schema.json`. For example, the key `t:general.settings.dropdown_menu.label` resolves via `general` → `settings` → `dropdown_menu` → `label` in that JSON file. Always verify setting names, defaults, ranges, and options against the schema before documenting them.

### Lint / test / build

There is no application build or test suite. Run `npm run check` for documentation validation. Verify feature claims against the synced theme source in `.src/` and follow the writing rules.

## Knowing publication

- Keep a root `README.md` for the Brickspace Lab homepage and folder `README.md` files for navigation labels.
- Use flat Knowing frontmatter. The integer `index` orders pages and folders among siblings.
- Set `published: false` on contributor instructions, GitBook `SUMMARY.md` files, includes, and migration reports. Every regular Markdown file is otherwise a page.
- Use relative repository paths ending in `.md` for internal page links, including `README.md` for folders.
- Knowing supports the existing GitBook-style hints, steppers, tabs, content references, updates, HTML cards, and details. Preserve them; remove GitBook-only action buttons and layout metadata.
- Keep Catalog product documentation in the separate `catalog-docs` repository. Shared company legal policies may remain here.
- Opening or merging a PR is not a request to publish a Knowing release, change DNS, or replace the live help center.
