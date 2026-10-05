---
published: false
---

# Syncing source repos

Run this command from the repo root:

```bash
npm run sync
```

What it does:

- Downloads latest default-branch snapshots for:
  - `brickspacelab/slab`
  - `brickspacelab/paper`
  - `brickspacelab/space`
  - `brickspacelab/keystone`
- Refreshes each repo into `.src/<repo>`.
- Stores snapshots without git history so docs tooling and AI can reference real source files.

Notes:

- `.src/` is ignored by git in this repo.
- Re-running `npm run sync` replaces existing snapshots with fresh upstream content.

## Publishing with Knowing

Knowing imports every Markdown file in the selected repository branch. Public articles and folder landing pages use flat frontmatter:

```yaml
title: Getting started
published: true
index: 0
```

Put these fields between leading `---` delimiters. Keep `published: false` on `AGENTS.md`, this tooling guide, GitBook `SUMMARY.md` files, and GitBook include snippets so they do not become public pages. Other existing GitBook frontmatter can stay in place.

The root `README.md` supplies the Support homepage. Each documentation folder has a published `README.md` whose title names the folder and whose index orders it among siblings. Knowing displays that landing content followed by its child pages and folders, without a duplicate README entry. Article indexes also apply among siblings; lower indexes appear first.

Keep titles, folder nesting and sibling indexes aligned with the live help site's navigation when adding or moving pages. Use repository-relative links to Markdown files or folder READMEs, and update links and GitBook summaries when a path moves. Catalog's changelog lives in `catalog/changelog.md`.
