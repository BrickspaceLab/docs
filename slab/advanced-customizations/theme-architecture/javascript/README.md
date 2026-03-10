# JavaScript

Interactivity is handled by Alpine.js. Components are defined inline in Liquid templates with `x-data`.



## Entry point

`src/entrypoints/theme.ts` is the single JavaScript entry point compiled by Vite. It imports `src/javascript/app.ts` to assemble the global `window.app()` factory, registers Alpine.js plugins (`AsyncAlpine`, `@alpinejs/focus`, `@alpinejs/intersect`, `@alpinejs/persist`), and starts Alpine.



## Global Alpine components

`layout/theme.liquid` sets `x-data="app()"` on `<body>`, making every method in `app()` available to all child Alpine components via `$root` or direct call.

`app()` is assembled in `src/javascript/app.ts` by spreading four core modules: `products` (variant selection, option availability, URL sync, recently viewed, quick-buy fetching), `cart` (add/change/edit/remove items, discount codes, cart notes, cart overlay routing), `utils` (overlays, image loading, scroll tracking, clipboard, audio, event dispatching, string utilities), and `shopify` (`formatMoney()` for price formatting, also assigned to `window.Shopify.formatMoney`).



## Global Alpine stores

`theme__scripts.liquid` registers all global Alpine stores inside an `alpine:init` listener. These stores are the single source of truth for shared state across the theme.

The `config` store holds theme-wide settings seeded from Liquid, including scroll state, sidebar visibility, login state, body scrolling toggles, audio settings, and URLs. The `cart` store holds live cart state refreshed after every mutation. The `overlays` store tracks the open/closed status and type of every overlay registered at render time. Supporting stores (`feedback`, `search`, `filter`, `pagination`, `recentProducts`) handle transient UI messages, predictive search state, collection filter state, infinite scroll state, and persisted recently-viewed products respectively.



## Product data

Product sections build their `x-data` object using `{% render 'helper__product-object' %}` captured into an inline JS object literal on the product container. This exposes the full Shopify product JSON, the currently selected options and variant, selling plan data, quantity, calculated price, and availability flags directly to the Alpine component.

The main entry method is `initProduct()` (called via `x-init`). It attaches the form submit handler, reads the URL for a variant pre-selection, and calls `handleProductFormChange()` to sync all display state with the initial selection.



## Section-specific components

Heavier, page-specific components live in `src/javascript/components/`. They are loaded on-demand via `async-alpine` using `x-load` on the element:

```liquid
<div x-data="slider({{ section.settings.autoplay_delay }})" x-load="visible">
```

Each file exports a default function whose name matches the filename (e.g. `slider.ts` exports `slider()`). See `.cursor/rules/alpine.mdc` for the full component authoring guide.



{% content-ref url="events.md" %}
[events.md](events.md)
{% endcontent-ref %}
