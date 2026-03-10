# Hide prices

Hiding prices is useful for wholesale or B2B stores where you want to prevent unauthorized visitors from seeing product pricing. Products with the restriction tag will not display prices or an **Add to Cart** button to customers who aren't logged in or approved.

***

### Setup <a href="#setup" id="setup"></a>

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Account**
4. In the **Hide prices tag** field, enter a tag (e.g., `hide price`)
5. Click **Save**

***

### Add tags to products <a href="#add-tags" id="add-tags"></a>

1. In your Shopify admin, go to **Products**
2. Select the product you want to restrict
3. In the **Tags** section, add the exact tag you configured (e.g., `hide price`)
4. Click **Save**

***

### Important notes <a href="#notes" id="notes"></a>

{% hint style="warning" %}
**Restriction tags are case sensitive!**

Tags must match exactly between the theme settings and your products. For example, if you set `Hide Price` in theme settings, the product tag must also be `Hide Price`—`hide price` or `HIDE PRICE` won't work.
{% endhint %}

* Unauthorized visitors will see the product but not the price or add to cart button
* Approved customers must be logged in to see prices
* Learn how to [approve customers](customer-approval.md) to grant access
