# Project setup

This guide covers the fastest way to run Slab locally and understand the core scripts used during development.

## Canonical files

- `/Users/thomaskimura/Documents/GitHub/slab/README.md`
- `/Users/thomaskimura/Documents/GitHub/slab/package.json`
- `/Users/thomaskimura/Documents/GitHub/slab/AGENTS.md`

## Requirements

- Node.js 18+ and npm
- Shopify CLI 3+
- Access to a development Shopify store

## Initial setup

1. Clone Slab locally:
   ```sh
   git clone git@github.com:BrickspaceLab/slab.git
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Create `.env` from `.env.example`.
4. Authenticate Shopify CLI:
   ```sh
   shopify auth login --store your-store.myshopify.com
   ```

## Start local development

Run:

```sh
npm run dev
```

This starts three processes in parallel:

- `vite dev`
- `shopify theme dev --store ...`
- `node src/scripts/section-builder.js --watch`

## Common scripts

- `npm run dev`: full local dev loop
- `npm run build`: build sections and Vite assets
- `npm run theme-check`: Shopify Theme Check (writes to `check.md`)
- `npm run json-check`: JSON-focused Theme Check
- `npm run test:e2e`: Playwright tests

## Environment variables

Common local variables:

- `SHOPIFY_CLI_THEME_TOKEN`: Theme Access app token for Shopify CLI auth
- `SHOP_PASSWORD`: storefront password for protected development stores

If your store is password-protected, you may need to run Shopify CLI manually with `--store-password`.

## Gotchas

- The Vite dev URL is not the full storefront preview. Use the Shopify preview URL from `shopify theme dev`.
- Theme checks can take several minutes on larger changesets.
- Repo docs contain mixed guidance about Playwright and CI; verify current behavior from `package.json` and `.github/workflows/`.
