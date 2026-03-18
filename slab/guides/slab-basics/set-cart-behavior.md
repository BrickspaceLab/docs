# Set cart behavior

Cart behavior controls where customers go after they interact with cart actions in your storefront. In Slab, merchants can set different behavior for desktop, mobile, and cart button clicks.

## How to set up cart behavior

1. Open **Theme settings > Cart**.
2. Set **Desktop cart behavior** for add-to-cart actions on desktop screens.
3. Set **Mobile cart behavior** for add-to-cart actions on mobile screens.
4. Set **Cart button behavior** for cart icon/button clicks in your storefront.
5. Optional: set **Minimum order amount** if your store requires an order minimum.
6. Save and test on both desktop and mobile viewports.

## How Slab applies these settings

- **Desktop cart behavior** is used after cart updates on desktop.
- **Mobile cart behavior** is used after cart updates on mobile.
- **Cart button behavior** is used when customers click a cart button or cart icon.
- If a cart overlay is already open, Slab does not open a second cart overlay on update.

## Suggested defaults for most stores

- Use **Open primary cart overlay** for desktop to keep shoppers on-page.
- Use **Open alternative cart overlay** on mobile if your mobile flow is built around that overlay.
- Keep **Cart button behavior** aligned with your main overlay choice.
- Only use redirect options when your store relies on the full cart or checkout page flow.

## Cart behavior settings reference

| Setting | What it controls | Options | Default |
| --- | --- | --- | --- |
| Desktop cart behavior | What happens after cart updates on desktop. | Open primary cart overlay, Open alternative cart overlay, Redirect to cart, Redirect to checkout | Open primary cart overlay |
| Mobile cart behavior | What happens after cart updates on mobile. | Open primary cart overlay, Open alternative cart overlay, Redirect to cart, Redirect to checkout | Open alternative cart overlay |
| Cart button behavior | What happens when customers click cart buttons/icons. | Open primary cart overlay, Open alternative cart overlay, Go to cart, Go to checkout | Open primary cart overlay |
| Minimum order amount | Minimum order value required before checkout. Enter value without currency symbol or decimal point. Example: enter `10000` for `$100.00`. | Number input | Blank (no minimum) |
