# Block displaying empty

Some Slab blocks need a selected Shopify object before they can render any content in the theme editor. This is common with blocks that display a **product**, **collection**, **article**, or similar resource.

If no object has been selected yet, the block may appear empty or show a warning message instead.


## Why this happens

Some blocks are designed to pull content from a specific object. Until that object is selected, the block does not have any data to display.

Merchants may see a warning such as `Select a product to display.` in the theme editor. This message is only shown while setting up the block and will never be shown to customers on the storefront.


## How to fix it

If you see this warning:

1. Click into the block that is displaying the warning.
2. Look for the setting that controls the content source, such as **Product**, **Collection**, or **Article**.
3. Select the object you want that block to display.

Once the object is selected, the block should begin rendering normally in the theme editor.


## Common example

For example, a card block may show `Select a product to display.` until a product is chosen in that block's settings.

The same behavior can apply to blocks that require a collection, article, or other supported Shopify object before they can show content.
