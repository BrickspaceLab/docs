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
| Threshold | The minimum amount customers need to reach before the bar is complete. Enter a number only (no currency symbol). | Set `100` to show a $100 goal. |
| Calculation | Which cart amount is used for progress: subtotal or total. | Use **Subtotal** to compare against the original subtotal amount. |
| Success message | The message shown when the threshold is reached. | `You unlocked free shipping.` |

## How the progress amount is calculated

- **Subtotal** uses the cart `original_total_price`.
- **Total** uses the cart `total_price`.
- The bar fills as customers add products, then switches to the success message once the goal is reached.

## Message behavior

- The in-progress line uses Keystone locale text keys (`info.cart_bar_pre_text` and `info.cart_bar_text`) and automatically inserts the remaining amount between them.
- The **Success message** field controls only the completed-state message when customers pass the threshold.

## Where to edit progress bar text

- **Completed message**: In the theme editor, open **Cart drawer > Progress bar** and edit **Success message**.
- **In-progress text**: In Shopify admin, open **Online Store > Themes > ... > Edit default theme content**, then search for the cart bar text strings (for example, `You're` and `away from free shipping`) and update them.
