# Display linked products

Linked products let customers move between related items (for example colors or styles) without leaving the product page. Slab uses the **Product sibling options** block for this.

## Steps

1. In Shopify admin, create a product metafield definition for **`custom.linked_collection`** (collection reference).
2. For each product that should show siblings, set that metafield to a collection that contains the related products.
3. Open **Online Store > Themes > Customize** and load a product template.
4. In the **Main product** section, add **Product sibling options** where you want the links to appear.
5. In the block settings, confirm **Product** matches the product you are editing (or pick one while testing).
6. Choose **Swatch selection**: **Buttons** for a small set of siblings, or **Dropdowns** when there are many.
7. Save the theme, then open a product that has **`custom.linked_collection`** set and confirm the options appear on the storefront.

## How it works

- The block reads related products from `product.metafields.custom.linked_collection`.
- Nothing renders on the storefront until that metafield points to a collection with products.
- In the theme editor, you may see a setup hint when the metafield is empty.

## Block settings reference

All options—swatches, labels, grid layout, spacing, colors, button size, and visibility—are documented on the [Product sibling options](../../content/blocks/products/sibling-options.md) block page.

## Troubleshooting

- Confirm each product has **`custom.linked_collection`** filled in.
- Confirm the linked collection contains the products you expect.
- Confirm the block is on the product template customers actually use.
- If the block never appears, check **Visibility** on the block (device limits can hide it).
