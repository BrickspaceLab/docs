# JavaScript

Interactivity is handled by Alpine.js. Components are defined inline in Liquid templates with `x-data`.



## Entry point

This file is the single JavaScript entry point compiled by Vite. It:

1. Imports `src/javascript/app.ts`, which assembles the global `window.app()` factory.
2. Imports and registers Alpine.js plugins (`AsyncAlpine`, `@alpinejs/focus`, `@alpinejs/intersect`, `@alpinejs/persist`).
3. Registers the async component alias so `x-load` can fetch components from `src/javascript/components/`.
4. Starts Alpine.



## Global Alpine components

`layout/theme.liquid` sets `x-data="app()"` on `<body>`. This makes every method in `app()` available to all child Alpine components via `$root` or direct call.

`app()` is assembled in `src/javascript/app.ts` by spreading four core modules:

| Module     | File                              | Responsibility                                                                                                                                                                        |
| ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `products` | `src/javascript/core/products.ts` | Variant selection, option availability, URL sync, selling plan savings, pickup refresh, recently viewed, quick-buy/edit template fetching                                             |
| `cart`     | `src/javascript/core/cart.ts`     | Add/change/edit/remove cart items, discount codes, cart notes, shared cart parsing, cart overlay routing                                                                              |
| `utils`    | `src/javascript/core/utils.ts`    | Overlay open/close/toggle, image load animation, scroll tracking, clipboard, audio playback, event dispatching, string utilities (`handleize`, `encodeToBase64`)                      |
| `Shopify`  | `src/javascript/core/shopify.ts`  | `formatMoney()` — reads price format and currency toggles from `Alpine.store('config')` and formats a cent value into a display string; also assigned to `window.Shopify.formatMoney` |



## Global Alpine stores

`theme__scripts.liquid` is rendered in `layout/theme.liquid` and registers all global Alpine stores inside an `alpine:init` listener. These stores are the single source of truth for shared state:

| Store            | Key properties                                                                         | Purpose                                                                                                                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config`         | `header`, `audio`, `behavior`, `prices`, `states`, `toggles`, `urls`                   | Theme-wide configuration seeded from Liquid settings. `states` tracks scroll position, sidebar visibility, login state, etc. `toggles` controls body scrolling, audio, and currency display. |
| `cart`           | `items`, `itemCount`, `totalPrice`, `loading`, `note`, `editVariantId`, `editQuantity` | Live cart state, refreshed after every mutation via `updateCart()`.                                                                                                                          |
| `overlays`       | keyed by overlay ID                                                                    | Each key holds `{ status, type, position, disableAutoClose }`. Overlays are registered by their snippet at render time.                                                                      |
| `feedback`       | `error.message`, `form.message/status`, `discount.code/text`                           | Transient UI messages for error drawers, form responses, and discount alerts.                                                                                                                |
| `search`         | `term`, `results`, `loading`, `hasSearched`, `resources`, `params`                     | Predictive search state.                                                                                                                                                                     |
| `filter`         | `sortBy`, `minPrice`, `maxPrice`, `min`, `max`                                         | Collection filter and price range state.                                                                                                                                                     |
| `pagination`     | `loading`, `currentPage`, `totalPages`, `pageType`, `section`                          | Infinite scroll / paginate state.                                                                                                                                                            |
| `recentProducts` | `products`, `loadedCount`                                                              | Recently viewed products, persisted in `localStorage`.                                                                                                                                       |



## Product data

Product sections (e.g. `main__product.liquid`) build their `x-data` object using `{% render 'helper__product-object' %}` inside a `{% capture %}`. The rendered output is an inline JS object literal injected directly into the `x-data` attribute of the product container.

Key variables exposed by the product `x-data` object:

| Variable                        | Type         | Purpose                                                                                    |
| ------------------------------- | ------------ | ------------------------------------------------------------------------------------------ |
| `product`                       | object       | Full Shopify product JSON (URL-encoded then parsed client-side to avoid XSS)               |
| `handle`                        | string       | Product handle                                                                             |
| `options`                       | array        | Array of option name strings                                                               |
| `option1`, `option2`, `option3` | string       | Currently selected option values (base64-encoded)                                          |
| `unavailableOption1/2/3`        | array        | Option values unavailable given the current selection                                      |
| `neverAvailableOption1/2/3`     | array        | Option values with no available variant regardless of other selections                     |
| `selectedVariant`               | object\|null | The currently matched variant object                                                       |
| `variantId`                     | number       | ID of the selected variant                                                                 |
| `variantFeaturedImageId`        | number\|null | Featured image ID of the selected variant (used to sync gallery)                           |
| `variantSellingPlanId`          | number\|null | Selected selling plan ID                                                                   |
| `variantSellingPlanSavingsText` | string\|null | Formatted savings label (e.g. "Save 10%")                                                  |
| `sellingPlans`                  | object       | Map of selling plan ID → plan data (sourced from `selling_plan_groups`, not capped at 250) |
| `quantity`                      | number       | Current quantity selection                                                                 |
| `calculatedPrice`               | number       | `selectedVariant.price × quantity`, adjusted for selling plan                              |
| `productLoading`                | boolean      | True while variant data is being fetched                                                   |
| `allOptionsSelected`            | boolean      | True when every option position has a selection                                            |
| `enableDefaultVariant`          | boolean      | When false, reads `?variant=` from the URL instead of pre-selecting                        |
| `isQuickBuy`                    | boolean      | Set by `refreshQuickFlags()` when rendered inside a quick-buy overlay                      |
| `isQuickEdit`                   | boolean      | Set by `refreshQuickFlags()` when rendered inside a quick-edit overlay                     |

The main entry method is `initProduct()` (called via `x-init`). It runs `attachForm()`, reads the URL for a variant pre-selection, and calls `handleProductFormChange()`.



## Section specific components

Heavier, page-specific components live in `src/javascript/components/`. They are loaded on-demand via `async-alpine` using `x-load` on the element:

```liquid
<div x-data="slider({{ section.settings.autoplay_delay }})" x-load="visible">
```

Each file exports a default function whose name matches the filename (e.g. `slider.ts` exports `slider()`). See `.cursor/rules/alpine.mdc` for the full component authoring guide.
