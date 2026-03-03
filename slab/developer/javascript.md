# JavaScript

Slab JavaScript is Alpine-first: core behavior is composed into a single global app object, then consumed by `x-data` components across theme templates.

## Canonical files

- `/Users/thomaskimura/Documents/GitHub/slab/src/entrypoints/main.js`
- `/Users/thomaskimura/Documents/GitHub/slab/src/javascript/app.ts`
- `/Users/thomaskimura/Documents/GitHub/slab/src/javascript/core/utils.ts`
- `/Users/thomaskimura/Documents/GitHub/slab/src/javascript/core/cart.ts`
- `/Users/thomaskimura/Documents/GitHub/slab/src/javascript/core/products.ts`
- `/Users/thomaskimura/Documents/GitHub/slab/layout/theme.liquid`
- `/Users/thomaskimura/Documents/GitHub/slab/snippets/theme__scripts.liquid`

## Runtime structure

- `main.js` initializes Alpine, registers plugins, sets async component loading, and starts Alpine.
- `app.ts` composes core modules into `window.app()`.
- `theme.liquid` binds root HTML with `x-data="app()"` and root `x-init` lifecycle calls.
- `theme__scripts.liquid` seeds Alpine stores (`config`, `cart`, `filter`, `search`, `feedback`, `overlays`).

## Events used across the theme

Custom event dispatch happens through `utils.dispatchEvent(...)`, then listeners react in components and blocks.

Common events from cart flows:

- `cart:change`
- `cart:error`

These are dispatched during add/update/change/note/discount operations in `core/cart.ts`.

## Alpine component strategy

- Async components load from `src/javascript/components/*.ts` via `AsyncAlpine`.
- Product and collection features rely on Alpine store state plus `x-data` payloads from Liquid snippets.
- Overlay interactions are centralized in `utils.ts` (`openOverlay`, `closeOverlay`, `toggleOverlay`, `closeAllOverlays`).

## Working with product interactions

- `core/products.ts` handles variant selection, option state, URL sync, selling plan calculations, and dynamic template fetch/injection.
- Product templates pass structured product data through `helper__product-object.liquid`.
- Keep server-rendered Liquid data and client-side TypeScript assumptions aligned when adding new fields.

## Recommended approach for JavaScript changes

1. Add shared behavior to `core/*` modules first.
2. Expose needed methods through `window.app()` composition in `app.ts`.
3. Keep Alpine store shape consistent with `theme__scripts.liquid`.
4. Use custom events for cross-component communication rather than tight coupling.

## Gotchas

- Repo docs include mixed statements about Playwright status; check actual scripts/workflows before changing testing docs.
- Store key naming can vary (`camelCase` vs `snake_case` expectations in some formatting helpers). Validate fallbacks before refactors.
