---
index: 8
---

# Automate with Flow

Use Shopify Flow to alert staff about wholesale applications, tag orders for review, or follow up when inventory runs low.

***

### What is Shopify Flow

Shopify Flow is free on Basic, Grow, Advanced, and Plus. Some actions have additional plan requirements. For example, **Send HTTP request** requires Grow, Advanced, or Plus. [Shopify Flow plan requirements](https://help.shopify.com/en/manual/shopify-flow).

***

### Wholesale automation examples

#### Review wholesale applications

Have your application form add a request tag such as `wholesale-request`. Use the steps below to notify staff when it arrives. After reviewing the application, staff can add Keystone’s approval tag to the customer.

#### Tiered pricing based on order history

When an order is paid, Flow can check the customer's total spend and add a tier tag. A [pricing app](wholesale-pricing-apps.md) must have a rule for that tag to change the price. Shopify B2B catalogs apply according to the company location purchasing the order.

#### Inventory alerts for wholesale products

**Trigger:** Wholesale product inventory drops below threshold\
**Action:** Send email notification to store owner

Stay on top of popular wholesale items before they run out.

#### Order approval workflow

**Trigger:** Large order is placed (over certain amount)\
**Action:** Tag order for manual review and notify staff

Ensure high-value wholesale orders are reviewed before fulfillment.

#### Post-purchase follow-ups

**Trigger:** Wholesale order is fulfilled\
**Action:** Send thank you email or request for reorder

Maintain relationships with wholesale customers automatically.

***

### Getting started with Flow

1. Install [Shopify Flow](https://apps.shopify.com/flow) from the Shopify App Store
2. Open the Flow app from your Shopify admin
3. Click **Create workflow**
4. Choose the [**Customer tags added** trigger](https://help.shopify.com/en/manual/shopify-flow/reference/triggers/customer-tags-added).
5. Check whether the tags added in this event include `wholesale-request`.
6. Add **Send internal email** and enter the address of the person who reviews applications.
7. Turn on the workflow and submit the wholesale application using a test customer who does not already have the request tag. Check that the form added `wholesale-request`, the workflow ran, and the reviewer received the email.

***

### Flow with Keystone features

Flow works seamlessly with Keystone's wholesale features:

* Use a separate approval tag for [Keystone customer approval](customer-approval.md) so a submitted application can wait for review.
* Tag products to trigger [hide products](hide-products.md) or [hide prices](hide-prices.md)
* Monitor orders that meet [minimum order amounts](minimum-order-amount.md)
* Check how your [wholesale pricing](wholesale-pricing-apps.md) is assigned before using a customer tag for a price tier.

***

### Important notes

* Always test workflows with test customers before enabling them
* You can view workflow history to troubleshoot automation issues

{% hint style="info" %}
Start with simple workflows and add complexity as you become comfortable with Flow. Even basic automations can save hours of manual work each week.
{% endhint %}

***

### Learn more

* [Shopify Flow Documentation](https://help.shopify.com/en/manual/shopify-flow)
* [Flow Template Library](https://help.shopify.com/en/manual/shopify-flow/templates)
* [Building Custom Workflows](https://help.shopify.com/en/manual/shopify-flow/create-workflow)
