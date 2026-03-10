# Discount popups

Customize the popup message that appears when customers apply automatic discounts by adding      `?dt=Custom+text` to your discount URL.

#### How to Set Up a Custom Discount Popup

1. **Find the Discount in Shopify**
   * Navigate to your Shopify admin
   * Select the discount you want to share
2. **Get the Shareable Link**
   * Click **Promote** > **Get a shareable link**
   * Copy the generated link
3. **Add Custom Message**
   * Append `?dt=Your+message+here` to the end of the URL
   * Replace spaces with `+` and special characters with URL codes
     * Example: `%25` for %
4. **Example URLs**
   * Basic example:\
     `https://yourstore.myshopify.com/discount/SAVE10?dt=Save+10%25+storewide`
   * With redirect option:\
     `https://yourstore.myshopify.com/discount/SAVE10?redirect=%2Fcollections%2Fwallets&dt=Save+10%25+storewide`

#### Important Notes

* Works with automatic discounts only
* Message appears in the discount application popup
* Use `+` for spaces in your custom text
* Encode special characters properly (e.g., %25 for %)
