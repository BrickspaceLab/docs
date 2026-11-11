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
| `npm run theme-check-core` | Run Shopify Theme Check and write the results to `check.md`. |
| `npm run theme-check-schema` | Check JSON and translations and write the results to `check.md`. |
| `npm run test`        | Run the browser journeys. |
| `npm run test:headed` | Run the browser journeys in a visible window. |

The browser journeys use Claude Code. Sign in with `claude auth login` and install Chromium with `npx e2e-web install chromium`.

* For Shopify data, set `STORE_DOMAIN` and run `npm run dev`. Wait for `READY` before running the tests in another terminal.
* For demo data, start the local renderer on port `9292` and leave `STORE_DOMAIN` empty.

See [Install from GitHub](../../getting-started/installing-slab/installing-from-github.md) for both preview paths.
