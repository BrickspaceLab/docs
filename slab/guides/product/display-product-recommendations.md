# Display product recommendations

Product recommendations surface related or complementary items from Shopify’s recommendation system. In Slab you add them with a **Product recommendations** block inside a parent that supports that block (often a grid or slider area on product, collection, or cart templates).

## Steps

1. Open the theme editor and navigate to the template where recommendations should appear (often the default product template).
2. Select a section or block that can contain recommendation blocks (for example a product content grid or a [Slider](../../content/blocks/layout/slider/README.md) area).
3. Add **Product recommendations** and pick the **grid** or **slider** variant your layout needs.
4. Set **Intent** to **Related** or **Complementary**.
5. Leave **Product** on the default when you want recommendations based on the product being viewed; set it explicitly only if you need a fixed source product.
6. Set **Item count** to match how much room the layout has.
7. Optionally set **Filter by tag** to restrict results, and adjust **Show products in cart** if you want to hide items already in the cart.
8. Save and preview on a real product page so recommendations can load.

### Complementary recommendations

If **Intent** is **Complementary**, configure complementary product relationships in Shopify’s **Search and Discovery** app first. Slab uses that store data when rendering complementary recommendations.

## Grid or slider

- Use the **grid** variant when you want a stable row-based layout customers can scan quickly.
- Use the **slider** variant when you want a horizontal, scrollable row (especially on narrow viewports).

## Block settings reference

Shared content and visibility options are the same idea for both layouts; the slider block adds width controls per breakpoint.

* [Grid recommendations](../../content/blocks/all-pagination/products/grid-product-recommendations.md)
* [Slider recommendations](../../content/blocks/all-pagination/products/slider-product-recommendations.md)

For layout ideas and typical combinations of settings, see **Common use cases** on each block page.
