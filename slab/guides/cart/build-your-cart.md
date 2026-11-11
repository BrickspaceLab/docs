---
index: 0
---

# Build your cart

Add cart blocks to your cart page or the [overlay](../slab-basics/popups-drawers-and-overlays.md) you use as a cart. Start with [Cart results](../../content/blocks/cart/cart-results.md) and [Checkout](../../content/blocks/cart/checkout.md).

## Add an automatic cart upgrade

1. Add **Cart upgrade** to the cart layout.
2. Choose a **Product**. Leave **Variant ID** blank to use its first variant, or enter the ID of the variant to add.
3. Set the **Minimum amount**. Slab checks item prices before discounts and excludes upgrade products.
4. To require a matching item, enter a **Required product tag**.

Slab adds one upgrade item when the conditions match and removes the automatically added item when they stop matching. The item uses its catalog price. Set up a separate Shopify discount if you want it to be free or discounted.

## Let customers change subscription frequency

Add **Cart frequency** near **Checkout** to let customers switch their subscriptions to a frequency supported by every subscription item in the cart. One-time purchases stay as they are.

When this control is available and the cart has mixed frequencies, customers must choose a common frequency before continuing through Slab's checkout button. If no common frequency is available, customers need to edit a subscription to continue.
