# Start with Paper when you are new to Shopify

Paper is a Shopify Online Store 2.0 theme. If your background is in stacks such as ASP.NET, Ruby on Rails, or Laravel, the biggest mental shift is that **merchants** customize almost everything in the **theme editor**, while **Liquid** templates render HTML on Shopify’s servers instead of your own application server.

## What Shopify owns versus what you own

* **Shopify** hosts the storefront, checkout, cart, customer accounts, and the admin where merchants manage products, collections, and settings.
* **Themes** are a bundle of Liquid files, JSON templates, CSS, and JavaScript that Shopify serves when someone visits a URL on the storefront.
* **Apps** extend the admin or inject blocks into the theme. They are not npm packages inside the theme by default.

You do not SSH into a server to deploy Paper. You upload or connect the theme through the Shopify admin or Shopify GitHub integration, then publish when ready.

## What Liquid is (and is not)

* Liquid is a **templating language**, not a general-purpose programming language. It loops over objects Shopify provides (for example `product`, `collection`, `cart`).
* Business logic that must stay secret belongs in a **private app** or Shopify Function, not in theme JavaScript exposed to the browser.
* Paper’s sections and blocks map closely to what you see in **Online Store** > **Themes** > **Customize**. That is intentional so merchants can iterate without deployments.

## Where Paper’s documentation lives

* **Product walkthroughs:** continue with [Theme basics](theme-basics.md) inside this Paper hub for editor-first setup tasks.
* **Deep dives:** browse the GitBook sidebar for **Guides**, **Sections**, and **Advanced customizations** once you know which surface you are changing.
* **Cross-theme articles:** the [Brickspace general hub](../../general/README.md) covers licensing, support policy, and comparisons between Paper, Space, Keystone, and Slab.

## Purchasing and installing Paper

Buy Paper through the [Shopify Theme Store](https://themes.shopify.com/) listing for Brickspace Lab. After purchase, the theme appears in **Online Store** > **Themes** > **Theme library**. Duplicate it before large experiments so you always have a clean rollback.

## Suggested learning order

1. Skim Shopify’s [Themes overview](https://shopify.dev/docs/storefronts/themes) and [Liquid introduction](https://shopify.dev/docs/api/liquid).
2. Follow [Theme basics](theme-basics.md) to configure global settings in Paper.
3. Read [Use custom templates](../guides/basics/use-custom-templates.md) when you need alternate layouts for specific collections or products.
4. Open [Add custom Liquid](../advanced-customizations/adding-custom-liquid/README.md) only after you are comfortable making backups and working in **Edit code**.

## When to hire help

Brickspace support answers questions about built-in features. It does not replace a Shopify Partner for bespoke app integration or large refactors. The general hub lists [Hire a Shopify developer](../../general/support/hire-a-shopify-developer.md) if you need a retained developer.
