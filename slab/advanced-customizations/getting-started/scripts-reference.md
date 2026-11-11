---
index: 0
---

# Scripts reference

Use these scripts during local development, builds, and testing.

| Script                | Description                                         |
| --------------------- | --------------------------------------------------- |
| `npm run dev`         | Watch and upload to a worktree-owned unpublished Shopify theme    |
| `npm run dev:hmr` | Run Vite hot reload through an HTTPS tunnel. |
| `npm run dev:pull` | Pull editor settings after stopping the development watcher. |
| `npm run dev:cleanup` | Preview which worktree-owned theme cleanup would remove. |
| `npm run build`       | Build sections and Vite assets for production       |
| `npm run theme-check` | Run Shopify theme check (output to `check.md`)      |
| `npm run json-check`  | Run JSON-focused theme check (output to `check.md`) |
| `npm run test`        | Run end-to-end browser tests                        |
| `npm run test:headed` | Run e2e tests with visible browser window           |

For browser tests, set `TEST_URL` to the actual local or Shopify-hosted preview URL. See [Install from GitHub](../../getting-started/installing-slab/installing-from-github.md) for both preview paths.
