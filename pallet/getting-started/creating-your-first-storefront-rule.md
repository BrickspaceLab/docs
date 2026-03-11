# Create your first storefront rule

## Pricing Rules

Pricing rules are the heart of Pallet. They define which customers receive which discounts based on their tags. This guide will walk you through creating, managing, and optimizing your pricing rules.

A pricing rule is a discount configuration that automatically applies to customers with a specific tag. Each rule consists of:

* **Customer Tag**: The tag that identifies which customers receive the discount (e.g., "wholesale", "vip", "tier-1")
* **Discount Percentage**: The percentage discount to apply (1-100%)
* **Status**: Whether the rule is active or inactive

#### Example

**Rule:** Wholesale customers get 20% off

* Customer Tag: `wholesale`
* Discount Percentage: `20`
* Status: `Active`

When a customer tagged "wholesale" logs in and browses your store, all prices will display 20% lower than the regular price.



{% stepper %}
{% step %}
### Navigate to the Rules Page

* Open your Shopify admin
* Click **Apps** in the left sidebar
* Select **Pallet**
* Click **Rules** in the navigation (if not already there)
{% endstep %}

{% step %}
### Start Creating a Rule

* Click the **Create rule** button in the top right
* You'll see the rule creation form with two main sections: **Audience** and **Discount**
{% endstep %}

{% step %}
### Configure the Audience

The Audience section defines which customers will receive this discount.

**Customer Tag**

* Enter the exact tag that identifies your customer segment
* Tags are case-insensitive (e.g., "Wholesale" and "wholesale" are the same)
* Common examples:
  * `wholesale` - For wholesale buyers
  * `vip` - For VIP members
  * `tier-1`, `tier-2`, `tier-3` - For tiered pricing
  * `distributor` - For distributors
  * `retail` - For retail partners
{% endstep %}

{% step %}
### Set the Discount

**Discount Percentage**

* Enter a number between 1 and 100
* This represents the percentage off the regular price
* Examples:
  * `15` = 15% off (customer pays 85% of original price)
  * `30` = 30% off (customer pays 70% of original price)
  * `50` = 50% off (customer pays 50% of original price)
{% endstep %}

{% step %}
### Save the Rule

1. Review your settings
2. Click **Create rule**
3. The rule is now active (if status is set to Active)

Your pricing rule is now live! Customers with the matching tag will see discounted prices when they log in.
{% endstep %}
{% endstepper %}
