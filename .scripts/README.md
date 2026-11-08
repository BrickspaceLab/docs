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

## Check Knowing documentation

Run `npm run check` before opening a documentation PR. It validates published page metadata, local links and assets, supported block structure, and the captured live-page inventory without network access. Requires Python 3.9 or later. The migration evidence and open content suggestions are in `../.migration/README.md`.
