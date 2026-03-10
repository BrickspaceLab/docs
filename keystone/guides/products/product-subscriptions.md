# Subscription options

Shopify subscriptions can be a bit tricky to setup. This guide will walk you through different options for displaying subscription options on your product page.

***

### Built-in subscription features <a href="#h_built_in_features" id="h_built_in_features"></a>

Keystone has **built-in subscription support** that works with Shopify's native selling plan groups. The theme automatically integrates with Shopify subscription apps (like Recharge, Bold Subscriptions, etc.) through Shopify's Selling Plans API.

**What's included:**

* **Subscription Selector** - Two display layout options available in theme settings:
  * Buttons layout
  * Dropdowns layout
* **Purchase Options** - Customers can choose between:
  * One-time purchase
  * Subscription plans with recurring deliveries
* **Subscription Details Display** - Automatically shows:
  * Subscription group names
  * Individual selling plans within each group
  * Savings/discounts (e.g., "Save up to X%")
  * Delivery frequency options
  * Per-delivery pricing

**How it works:**

1. Install and configure a Shopify subscription app or set up selling plans in your Shopify admin
2. Assign subscription plans to your products
3. The theme automatically displays subscription options on product pages
4. Configure the display style in **Theme Settings** > **Product Options** > **Plan selection**

The subscription functionality is implemented in `snippets/product__options.liquid` and `snippets/product__add.liquid` for seamless integration.

***

### Using the built-in subscription options <a href="#h_10340383b3" id="h_10340383b3"></a>

We recommend using the built-in subscription options as you'll have more control over the experience and can customize this with the help of a developer.

However, this may cause complications with your product templates if you've already installed a third-party subscription widget.

* Ensure the third party subscription widget is disabled
* Ensure the product block **Options** is included on your product template

***

### Using third-party subscription options <a href="#h_0f926d6c18" id="h_0f926d6c18"></a>

Disabling the default subscription options is possible if you'd like to stick to using a third-party widget. There a few more steps here.

1. Go to **Online Store** > **Themes** > **Customize**
2. Click the top dropdown > **Products** > **Create template**
3. Label this template 'subscription'
4. On the left hand side, click into the **Product** section
5. Check **Enable default selling plan widget**
6. On the left hand side, click into the **Options** block and click **Remove block**
7. Go into your subscription app and follow instructions to install the subscription widget
8. Assign the 'subscription' product template to all products that have a subscription plan
9. Hit **Save**
