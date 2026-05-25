# Show variant count on product cards

Keystone can display how many variants a product has (for example “3 options”) on collection grids, sliders, and other product cards. The **Show variant count** setting is global—it applies to all products that use product cards, including single-variant products.

## Enable the setting

1. Open **Online Store** > **Themes** > **Customize**.
2. Open **Theme settings** (gear icon).
3. Go to **Product cards**.
4. Enable **Show variant count**.
5. Click **Save**.

| Setting | Location | Default |
| ------- | -------- | ------- |
| Show variant count | **Theme settings** > **Product cards** | Off |

## What customers see

When enabled, product cards show a line such as **3 options** next to variant or SKU details. The count uses the product’s total variant count (`product.variants_count`) and the theme’s **options** label.

### Single-variant products

Keystone does **not** hide the variant count for products with only one variant. A single-variant product may show **1 options**, which can look redundant next to products that have multiple sizes or colors.

There is no per-product toggle for this setting. Options if the label is unwanted on single-variant items:

* **Turn off Show variant count** globally if most of your catalog is single-variant.
* **Use product tags and custom CSS** (developer task) to hide the count on specific cards—this requires custom code and falls under [modified-code support limits](../../general/support-policy.md).
* **Leave it on** if the count helps B2B buyers quickly scan configurable vs. simple SKUs across a large catalog.

## Relationship to other product card settings

**Show variant count** is independent of:

* **Show SKU** — displays the first variant’s SKU
* **Show swatches** — color or option swatches on the card
* **Quick add** — add-to-cart from collection pages

You can enable any combination in **Theme settings** > **Product cards**.

## Related reading

* [Metafields on product cards](metafields-on-product-cards.md)
* [Show variant data in the product table](show-variant-data-in-product-tables.md)
* [Dynamic variant images](product-variant-images.md)
