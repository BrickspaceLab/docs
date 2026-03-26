# Pull upstream updates

If you forked the repo, you can pull in new Slab releases at any time:

```sh
git fetch upstream
git merge upstream/main
```

Resolve any conflicts, then run `npm install` to pick up any dependency changes. Run `npm run build` afterward to confirm the theme compiles.

## AI coding agents

The theme repo ships a Cursor command **`/pull-upstream-updates`** you can pass to an AI agent (or run yourself in Cursor). It walks through a fork-friendly merge policy—for example keeping your saved theme layout JSON while taking upstream tooling, lockfile, locales, and most other files—and pauses for your input on **`*.liquid`** conflicts instead of guessing. See [Work with coding agents](../working-with-coding-agents.md) for the full command list.

## After a large version jump

If Shopify or Slab shipped breaking template or settings changes, use **`/fix-breaking-changes`** (see [Work with coding agents](../working-with-coding-agents.md)) to migrate templates and `config/settings_data.json` when needed.
