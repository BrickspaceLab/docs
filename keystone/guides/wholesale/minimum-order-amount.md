# Minimum order amount

Setting a minimum order amount prevents customers from checking out unless their cart meets a specified subtotal. This is useful for wholesale stores that require minimum purchase quantities or order values.

***

### Setup minimum order <a href="#setup" id="setup"></a>

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Cart**
4. Find the **Minimum Order Amount** field
5. Enter the minimum amount in cents (e.g., `10000` for $100.00)
6. Click **Save**

***

### How it works <a href="#how-it-works" id="how-it-works"></a>

When a minimum order amount is set:

* The checkout button is disabled if the cart subtotal is below the minimum
* A message displays informing customers of the minimum required
* Customers can continue shopping to meet the minimum
* Once the minimum is met, the checkout button becomes active

***

### Examples <a href="#examples" id="examples"></a>

| Minimum Amount | Enter in Field |
| -------------- | -------------- |
| $50.00         | `5000`         |
| $100.00        | `10000`        |
| $250.00        | `25000`        |
| $500.00        | `50000`        |

***

### Remove minimum order <a href="#remove" id="remove"></a>

To allow orders of any amount:

1. Go to **Theme Settings** > **Cart**
2. Clear the **Minimum Order Amount** field (leave it blank)
3. Click **Save**

***

### Important notes <a href="#notes" id="notes"></a>

* The minimum is based on the cart subtotal before taxes and shipping
* The minimum applies to all customers unless using custom code
* Discounts are applied before checking the minimum
* The amount must be entered in cents (multiply dollars by 100)

{% hint style="info" %}
For more advanced minimum order rules (e.g., different minimums for different customer groups), consider using Shopify Functions or a wholesale app.
{% endhint %}
