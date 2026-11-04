# Product badges

Product badges highlight key product information, helping customers quickly identify special items. Use tags or metafields to display custom badges.

#### How to Add Product Badges

**Method 1: Using Product Tags**

1. **Edit Product in Shopify**
   * Open the desired product
   * Scroll to **Tags** section
2. **Add Badge Tag**
   * Enter tag in format: `badge_YourText`
     * Example: `badge_BestSeller` or `badge_LimitedStock`
   * Click **Save**

_Note: Also works with:_

* Bulk editor
* CSV imports
* Third-party apps

**Method 2: Using Product Metafields**

1. **Create Metafield Definition**
   * Go to **Settings > Custom Data > Products**
   * Click **Add Definition**
   *   Set:

       * Name: `Product badge`
       * Namespace/key: `custom.badge`
       * Type: `Single line text`
       *

       ```
       <figure><img src="../../.gitbook/assets/image (15).png" alt="" width="287"><figcaption></figcaption></figure>
       ```
2. **Add Badge to Product**
   * Edit product
   * Scroll to **Metafields** at bottom
   * Enter badge text in **Product badge** field
   * Click **Save**

#### Best Practices

* **Keep text short:** 1-3 words (e.g., "Sale", "New", "Last Chance")
* **Make them noticeable:** Use contrasting colors
* **Be truthful:** Only add badges for real differentiators
* **Test visibility:** Check on mobile and desktop views

#### Maintenance Tips

* Review badges monthly for accuracy
* Remove expired promotions
* Keep styling consistent across products
* Consider seasonal badge updates
