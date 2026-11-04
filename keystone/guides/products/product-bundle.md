# Bundled products

The bundle product template can be used to sell multiple products from a single page. This can be combined with automatic discounts for an added layer of functionality. To set this up you'll need to create a new metafield definition then assign the bundle template to a new product.

***

### Create metafield definition <a href="#h_c88d8aca90" id="h_c88d8aca90"></a>

1. Navigate to **Settings** > **Custom data** > **Products**
2. Click **Add definition**
3. In the name field type "Product bundle"
4. Ensure the namespace and key field is `custom.product_bundle`
5. Set the data type as "Product" then select **List of products**
6. Hit **Save**

***

### Create a bundle template <a href="#h_54c57da661" id="h_54c57da661"></a>

1. In the Shopify theme editor select from the top dropdown **Products**
2. Click **Add template**
3. Enter a name
   * This can be anything. E.g. "Bundle"
4. On the left hand side, look for **Product**
5. Under **Product**, click **Add block**
6. Choose **Bundled products**
7. Hit **Save**

***

### Create a bundle product <a href="#h_cd4411e9a0" id="h_cd4411e9a0"></a>

1. Create a new product on Shopify
2. Add images as needed - you'll likely want to include photos showcasing all the items in your bundle. Even better if you can get photos of all the products together to really highlight the "bundle" part
3. Set a price for the product - this should be the sum of all the items in the bundle
4. **Uncheck Track quantity**. This product won't actually be purchased itself instead it will act as a landing page where the products within the bundle are purchased
5. Scroll down to **Metafields** then click **Product bundle**
6. Click **Select products** and add as many products as you'd like to include in this bundle
7. On the right-hand side under **Theme template** select **bundle** (or a different template that you've created using the "Bundled products" block)
8. Hit **Save**
