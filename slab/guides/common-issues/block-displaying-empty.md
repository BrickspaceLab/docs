# Block displaying empty

Some Slab blocks need a selected Shopify object before they can render any content in the theme editor. This is common with blocks that display a **product**, **collection**, **article**, or similar resource.

If no object has been selected yet, the block may appear empty or show a warning message instead.



## Why this happens

Some blocks are designed to pull content from a specific object. Until that object is selected, the block does not have any data to display.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section=template--18647337730099__section_j6eKTX&#x26;block=template--18647337730099__section_j6eKTX__layout_flex_t9nbtF__g_flex_item_PNYPPM__g_product_card_EkNXiH&#x26;context=theme&#x26;c.png" alt=""><figcaption></figcaption></figure>

Merchants may see a warning such as `Select a product to display.` in the theme editor. This message is only shown while setting up the block and will never be shown to customers on the storefront.



## How to fix it

If you see this warning:

1. Click into the block that is displaying the warning.
2. Look for the setting that controls the content source, such as **Product**, **Collection**, or **Article**.
3. Select the object you want that block to display.

Once the object is selected, the block should begin rendering normally in the theme editor.
