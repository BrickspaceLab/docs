# Bundled products

The bundle product template can be used to sell multiple products from a single page. This can be combined with automatic discounts for an added layer of functionality. To set this up you'll need to create a new metafield definition then assign the bundle template to a new product.

<figure><img src="https://downloads.intercomcdn.com/i/o/1199127570/6f61db4dbc02e91d09e286df/CleanShot+2024-09-30+at+16_52_17%402x.png?expires=1744682400&#x26;signature=70c912d9873f8d8e939d68c0a6f1ed1be610960c00c418497443ff59ccc57cca&#x26;req=dSEuH8h8moRYWfMW1HO4zfR48YsnIvPzChhoeb370%2Bvco%2Bgw9qRtQNn8DSCG%0A9N%2FcIqN%2FrkbflJuCsfQ%3D%0A" alt=""><figcaption></figcaption></figure>

{% stepper %}
{% step %}
**Create metafield definition**

1. Navigate to **Settings** > **Custom** **data** > **Products**
2. Click **Add definition**
3. In the name field type “Product bundle”
4. Ensure the namespace and key field is `custom.product_bundle`
5. Set the data type as "Product" then select **List** **of** **products**
6. Hit **Save**
{% endstep %}

{% step %}
**Create a bundle template**

1. In the Shopify theme editor select from the top dropdown **Products**
2. Click **Add template**
3. Enter a name
   1. This can be anything. E.g. "Bundle"
4. On the left hand side, look for **Product**
5. Under **Product**, click **Add block**
6. Choose **Bundled products**
7. Hit **Save**
{% endstep %}

{% step %}
**Create a bundle product**

1. Create a new product on Shopify
2. Add images as needed - you'll likely want to include photos showcasing all the items in your bundle. Even better if you can get photos of all the products together to really highlight the "bundle" part
3. Set a price for the product - this should be the sum of all the items in the bundle
4. **Uncheck Track quantity**. This product won't actually be purchased itself instead it will act as a landing page where the products within the bundle are purchased
5. Scroll down to **Metafields** then click **Product bundle**
6. Click **Select products** and add as many products as you'd like to include in this bundle
7. On the right-hand side under **Theme template** select **bundle** (or a different template that you've created using the "Bundled products" block)
8. Hit **Save**
{% endstep %}
{% endstepper %}
