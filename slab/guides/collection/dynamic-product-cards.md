# Dynamic product cards

Slab builds product cards in two different ways. Most collection and slider grids render a **Product card** block that lives on **that page’s template**. **Recently viewed** (grid and slider) loads the separate **`product-card`** product template over the network. Use the section below to find the right place to edit for the area you care about.



## Choose where to customize

### Product card blocks on page templates

Use this path for **collection pages**, **search results**, **product grids and sliders**, and **recommendations** when the theme loops products on the server.

1. Open the template for the **page** where the grid or slider appears (for example the default **Collection** or **Search** template, or a template that includes a **Section** block with a product list).
2. Select the block that drives the product list. Common editor names from the Slab schema include **Collection grid**, **Search grid**, **Product grid**, **Slider products**, and **Product recommendations** (grid and slider layouts can share that label—pick the block that matches your section).
3. Open the nested **Product card** block and edit its inner blocks (for example **Product media**, **Rich text**, **Price**).

Each template stores its own **Product card** setup. Changing the card on the collection template does **not** change **Recently viewed**, and the other way around.

Card chrome—padding, color scheme, borders, corner radius, gap between inner blocks, visibility, scroll animation—is controlled on the **Product card** block itself. See the [Product card](../../content/blocks/cards/product-card.md) reference for those settings and the full list of blocks you can nest.

### Recently viewed and the product-card template

**Recently viewed** (grid and slider) does not use the **Product card** block from your collection template. The storefront fetches each product using the **`product-card`** product template (`product.product-card.json` in theme files).

Optional: Shopify loads this with the alternate template view parameter (`?view=product-card`).

That template uses the **Product** section. The theme’s default layout is a **Container** that groups **Product media**, **Rich text** (often wired to the product title), **Price**, and **Swatches**—you can add, remove, or reorder blocks in the editor the same way as on other product templates.

Edits here apply to any feature that loads that template with the `product-card` view (including **Recently viewed**). They do **not** change cards on collection or search pages unless those pages are also loading that view (they normally are not).



## Edit the product-card template (Recently viewed)

{% stepper %}
{% step %}
### Open the template

1. Open the theme editor and go to any product template.
2. Open the template picker.
3. Select the **`product-card`** template.
{% endstep %}

{% step %}
### Update the Product section

1. Select the **Product** section.
2. Add, remove, or reorder blocks to control what each fetched card shows. The default structure uses a **Container**; you can keep that pattern or rebuild the layout using blocks the editor allows for this section (for example **Product media**, **Price**, **Buy buttons**, **Badges**, **Swatches**, **Rich text** inside **Container** or other **Theme** blocks, plus **App** blocks where supported).

The **Product** section allows a different mix of blocks than the nested list inside a **Product card** block on collection templates—for example **Buy buttons** and **Product options** are available here if you want that experience inside a fetched card.
{% endstep %}

{% step %}
### Save and preview

Save your changes, then open a page with **Recently viewed** (grid or slider) and confirm the card matches what you expect.
{% endstep %}
{% endstepper %}



## Show titles, metafields, and other product details

What appears on a card depends on **which surface** you are editing (page **Product card** block vs **`product-card`** product template). In both cases, content comes from the blocks you add—not from one combined “product card settings” panel.

| What you want | What to use |
| --- | --- |
| Formatted title or body copy | [Rich text](../../content/blocks/basics/rich-text.md) (on page cards, nested in **Product card**; on the **`product-card`** template, usually inside a **Container** or other theme block that supports it) |
| Price | [Price](../../content/blocks/products/price.md) |
| Images or video | [Product media](../../content/blocks/products/product-media.md) |
| Tags, sale, or custom labels | [Badges](../../content/blocks/products/badges.md) (including metafield-based badges) |
| Variant color or pattern chips | [Swatches](../../content/blocks/products/swatches.md) |
| Stock messaging | [Inventory availability](../../content/blocks/products/inventory-availability.md) |
| Quick add from a grid or slider card | [Quick buy button](../../content/blocks/products/quick-buy-button.md) inside the **Product card** block (see [Quick actions](quick-add-and-quick-edit.md)) |
| Full add to cart / options on the fetched **product-card** template | **Buy buttons**, **Product options**, and related blocks in the **Product** section when editing the **`product-card`** template |

### Titles and text from product data

Add or edit a **Rich text** block and connect the field to product information (for example the product title) when the editor offers that connection. The default **`product-card`** template ships with rich text using the product title. The same pattern works for many **metafields** when you connect a supported setting to a metafield you defined in Shopify admin.

### Metafields on badges

To surface custom attributes as badges, configure the **Badges** block as described in [Badges](../../content/blocks/products/badges.md).



## Related guides

* [Quick add and quick edit](quick-add-and-quick-edit.md)—**Quick buy** and **Quick edit** use the **Quick buy template** and **Quick edit template** fields under **Theme settings > Quick actions**, not the **`product-card`** view by default. You can still enter the same template suffix as your card layout if you want overlapping designs.
