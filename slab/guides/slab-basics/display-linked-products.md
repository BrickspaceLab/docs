# Display linked products

Linked products help customers switch between related items (for example colors, materials, or similar styles) without leaving the product flow. In Slab, this is handled by the **Product sibling options** block.

## How to display linked products

1. In Shopify admin, set up a product metafield definition for **`custom.linked_collection`**.
2. For each product, assign a collection that contains the related products you want to show as linked options.
3. Go to **Online Store > Themes > Customize** and open your product template.
4. In the **Main product** section, add the **Product sibling options** block where you want linked products to appear.
5. Confirm the block **Product** setting is set to the current product context (or pick a product for testing).
6. Choose **Swatch selection** as **Buttons** or **Dropdowns**.
7. Save, then test a product that has a populated linked collection.

## How it works in Slab

- The block reads related products from `product.metafields.custom.linked_collection`.
- Linked options appear only when that collection has products.
- If the product has no linked collection, the block shows a setup message in the editor.

## Settings to adjust first

| Setting | What it controls | Default |
| --- | --- | --- |
| Swatch selection | Shows linked products as button/swatch choices or as a dropdown list. | Buttons |
| Show swatch | Uses each linked product featured image as a visual swatch. | On |
| Show tooltip | Shows product title tooltip when swatches are shown without labels (buttons mode). | On |
| Show labels | Shows product titles next to swatches (buttons mode). | Off |
| Swatch size | Controls swatch image size. | 16 px |
| Swatch radius | Controls swatch corner style. | Full |
| Enable grid layout | Displays linked options in a grid instead of flex wrap (buttons mode). | Off |
| Row desktop / Row mobile | Number of grid columns when grid layout is enabled. | 4 / 2 |
| Button size | Size for linked-product buttons/dropdown trigger. | Small |

## Troubleshooting checklist

- Confirm each product has `custom.linked_collection` populated.
- Confirm the linked collection contains actual products.
- Confirm the block is added to the active product template.
- Confirm the block visibility setting is not limited to another device.
