# Show variant data in the product table

Keystone’s **Table** block on the product template can print up to three extra columns beside each variant row. Those columns read **variant metafields** (for example a UPC, size chart URL, or compliance note) from **Theme settings → Product cards**.

{% hint style="info" %}
The theme editor labels this area **Variant metafields**, while the inline help text may mention “product metafields.” The Liquid templates resolve values from each **variant’s** metafields (`namespace.key`). Create definitions on **Variants** in **Settings → Custom data** so every variant can store its own value.
{% endhint %}

## Before you start

* Add a **Table** block to the product template if you have not already. See [Product table block](product-table-block.md).
* In **Settings → Custom data → Variants** in the Shopify admin, create the metafield definitions you need (for example `custom.upc` as a single line text field).

## Map metafields in theme settings

1. Open **Online Store** > **Themes** > **Customize**.
2. Click the **Theme settings** icon (gear) in the left sidebar.
3. Open **Product cards**.
4. Scroll to the **Table details** group (the same area as SKU and inventory toggles for the table layout).
5. In **Variant metafields**, enter up to three handles separated by commas, using the `namespace.key` pattern Shopify shows in the metafield admin (for example `custom.upc, custom.gtin, custom.size_note`).
6. Optionally fill **Variant metafields labels** with the column headings merchants should see, in the same order (for example `UPC, GTIN, Size note`). Labels are optional; when omitted, the theme prints the value only.

The setting info text in the theme editor matches the synced theme source: you may list up to three comma-separated metafields and up to three optional labels.

## Verify on the storefront

1. Edit a product and enter metafield values on **each variant** that should display data.
2. Preview the product page and confirm the **Table** block is using the row layout that exposes the extra columns.
3. If a cell is blank, double-check the namespace/key spelling and that the metafield type supports storefront output (for example rich text may need different handling than plain text).

## Related guides

* [Metafields on product cards](metafields-on-product-cards.md) — explains how grid cards differ from table rows.
* [Dynamic variant images](product-variant-images.md) — when the gallery should change with the selected variant.
