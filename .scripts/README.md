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
