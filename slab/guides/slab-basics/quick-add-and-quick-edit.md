---
hidden: true
---

# Quick add and quick edit

Quick add lets customers open a product form from a product card or other merchandising area without leaving the current page. In Slab, the editor labels this feature as **Quick buy**. **Quick edit** uses the same pattern for items already in the cart, so customers can update their selection from an overlay instead of returning to the product page.

Both experiences work in two parts:

* A block or action opens the overlay.
* A matching product template controls the content rendered inside that overlay.


## Quick buy button

Use the **Quick buy button** block anywhere you want to trigger quick add, such as inside a **Product card**.

* For single-variant products, the button can add the item directly to cart.
* For products with multiple variants, it opens the quick add overlay.
* Use this block when you want customers to start the quick add flow.


## Quick buy content

Use the **Quick buy content** block inside the overlay that should display your quick add form.

* This block renders the template selected in **Theme settings > Quick actions > Quick buy template**.
* Add it inside a **Popup**, **Drawer**, or other overlay block depending on how you want quick add to appear.
* The content customers see comes from the selected product template, not from the product card itself.


## Quick edit content

Use the **Quick edit content** block inside the overlay used for editing cart items.

* This block renders the template selected in **Theme settings > Quick actions > Quick edit template**.
* Add it inside the overlay where customers should edit an existing cart item.
* This is useful when customers need to change variants, subscriptions, or other product options after adding an item to cart.


## How to edit quick add and quick edit

To change what customers see in quick add or quick edit, update the global quick action setting first, then edit the matching product template.

1. Open **Theme settings > Quick actions**.
2. Set **Quick buy template** for quick add and **Quick edit template** for quick edit.
3. Enter the product template suffix you want the overlay to use.
4. Leave the field blank to use the default product template.

For example:

* Enter `product-card` to use `product.product-card.json`.
* Enter `quick-edit` to use `product.quick-edit.json`.
* Leave the field blank to use `product.json`.


## Update the matching product template

After choosing the template in **Quick actions**, open that same product template in the theme editor and update its blocks.

This is where you control the actual quick add or quick edit content, such as:

* **Product options**.
* **Product buy**.
* **Product price**.
* **Product media**.
* **Rich text**.
* **Product subscription**.

Any blocks you add, remove, or reorder in that product template will appear inside the quick add or quick edit overlay.


## Common setup pattern

Use this workflow when building or updating either experience:

* Add a **Quick buy button** where customers should start quick add.
* Add **Quick buy content** or **Quick edit content** inside the overlay block that should display the form.
* Choose the correct template in **Theme settings > Quick actions**.
* Edit that matching product template to control the final overlay content.
