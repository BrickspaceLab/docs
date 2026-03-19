# Configure cart drawer progress bar

Use the cart drawer progress bar to show customers how close they are to a cart goal, such as free shipping.

## Where to configure it

1. Open **Online Store > Themes** in Shopify admin.
2. Click **Customize** on your Keystone theme.
3. In the theme editor, open the **Cart drawer** section.
4. Click **Add block** and select **Progress bar**.
5. Save your changes.

## Progress bar settings explained

| Setting | What it controls | Example |
| --- | --- | --- |
| Threshold | The cart amount customers need to reach before the bar is complete. | Set `100` to show a goal of $100. |
| Calculation | Which cart value is used to measure progress: subtotal or total. | Use subtotal to ignore shipping and taxes. |
| Success message | The message shown when the threshold is reached. | `You unlocked free shipping.` |

## How the progress amount is calculated

- **Subtotal** uses line items after product discounts and before shipping and taxes.
- **Total** uses the final cart amount that includes extra charges like shipping and taxes.
- The bar fills as customers add products, then switches to the success message once the goal is reached.

## Message examples

- `You are {{ amount }} away from free shipping.`
- `Add {{ amount }} more to unlock a free gift.`
- `Nice work - your cart qualified for free shipping.`

If you use dynamic amount text in your message, confirm your store translation or app logic supports the same placeholder format.

## Recommended testing

1. Add products below the threshold and confirm the remaining amount updates.
2. Add enough products to cross the threshold and confirm the success message appears.
3. Remove an item and confirm the bar returns to the in-progress state.
4. Check behavior on both desktop and mobile cart drawer layouts.
