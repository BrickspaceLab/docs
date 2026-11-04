# Agents

## Cursor Cloud specific instructions

### Overview

This is a **GitBook-formatted documentation repository** for Brickspace Lab's Shopify themes and apps. There is no application server or build step — development consists of editing Markdown files with optional source verification.

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

There is no linter, test suite, or build step in this repository. Quality is enforced by the Cursor rules and by verifying documentation against the synced theme source in `.src/`.
