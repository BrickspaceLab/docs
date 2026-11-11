---
index: 2
---

# Buy buttons

Use **Buy buttons** to let customers add the selected product to their cart. Add a **Button** inside it to change the look of the add to cart button or show the price inside the button.

## Block settings

| Setting | What it controls |
| --- | --- |
| Product | Select the product the form adds to cart. |
| Enable quantity input | Let customers choose a quantity. |
| Layout | Stack the quantity and button or place them inline. |
| Enable dynamic checkout | Show Shopify's accelerated checkout buttons where available. These buttons are hidden when the form contains product customization fields. |
| Show gift card form | Show recipient fields for gift card products. |

## Add product customization

1. Open the product template in the theme editor and select **Buy buttons**.
2. Add **Product customization**, then add an **Input field** for each choice you need. For example, use **Text** for engraving or **Select** for a list of choices.
3. Give each field a unique **Label**. The label identifies the customer's answer in the cart and on the order. For select or radio fields, separate the choices with commas in **Options**.
4. Turn on **Make this field required** on **Product customization** to require its fields before adding to cart.

The **Quick buy button** takes customers to the product page when its assigned template contains product customization. If you use a [separate quick edit template](../../../guides/collection/quick-add-and-quick-edit.md), add the same fields there with the same labels. Quick edit fills the fields with the values from the selected cart item.

## Show a quantity offer

1. Add a **Quantity discount** preset to the product template and keep **Buy buttons** in the same product section.
2. Edit each **Quantity discount option**. Set **Quantity** and **Discount**, and add a **Tag** if you want to call out an offer.
3. Create a matching automatic discount in Shopify. The block shows the offer and sets the quantity when selected. Shopify applies the discount in the cart and at checkout.

## Add purchase option cards

Use **Purchase options** to let customers select a card and add all its configured items to the cart together.

1. In the theme editor, open a product template and add **Purchase options** to the **Product** section.
2. Edit the included **Purchase option** and add more cards as needed. Set each card's **Heading** and optional **Badge**. Add a block such as **Rich text** to describe the offer.
3. Inside each card, configure a **Purchase option item** for each cart line. Choose the **Product** and set the **Quantity**, which defaults to 1. Enter a **Variant ID** to use a specific variant. Leave it blank to use the selected or first available variant.
4. For a subscription item, enter a **Selling plan ID** to use a specific plan, or a **Selling plan group ID** to use the first available plan in the group. If you enter both, the plan must belong to that group. Leave both blank for a one-time purchase when the product allows it.
5. Keep **Buy buttons** inside **Purchase options** and use its nested **Button** to customize the appearance and text. Preview each card and check that its items, quantities, and purchase plans appear in the cart as configured.
