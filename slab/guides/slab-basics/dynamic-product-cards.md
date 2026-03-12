# Dynamic product cards

Dynamic product cards let Slab load product card content from a product template instead of defining every card directly inside the section. This is useful for dynamic product areas like **Recently viewed**, where the theme decides which products to show and the `product-card` template decides how each card looks.

## How dynamic product cards work

Some Slab product sections load products at runtime, then render each result using the `product-card` product template.

* The section or block chooses which products to display.
* Slab requests the `product-card` view for each product.
* The matching section response is inserted back into the section as a finished product card.
* Any changes you make to the `product-card` template affect every dynamic card that uses that template.


## Example: recently viewed

The **Recently viewed** block uses this pattern to show products a customer has already opened.

* The block tracks recently viewed products.
* Slab fetches each product using the `product-card` template.
* The rendered result is inserted into the recently viewed grid or slider.
* This means the recently viewed block controls which products appear, while the `product-card` template controls the final card layout.


## Edit the product card template

To change these dynamic product cards, update the `product-card` product template in the theme editor.

1. Open the theme editor and navigate to a product template.
2. Open the template picker and select the `product-card` template.
3. Edit the blocks inside that template to control the card content and layout.
4. Save your changes and preview a dynamic product area like **Recently viewed**.

The `product-card` template maps to `product.product-card.json`.


## What you can change

Inside the `product-card` template, you can add, remove, or reorder blocks to change what customers see.

* Use **Product media** to control the product image area.
* Use **Rich text** to output the product title or supporting text.
* Use **Price** to show pricing.
* Use **Swatches** or **Badges** to highlight product options or labels.
* Use **Quick buy** when you want customers to start purchase actions from the card.


## Common setup pattern

Use this workflow when you want to update dynamic product cards:

* Find the dynamic product area you want to change, such as **Recently viewed**.
* Confirm that it renders products using the `product-card` template.
* Open the `product-card` product template in the theme editor.
* Update the blocks inside that template to control the final product card output.
