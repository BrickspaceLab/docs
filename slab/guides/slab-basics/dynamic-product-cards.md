# Dynamic product cards

Dynamic product cards let Slab load product card content from a product template instead of defining every card directly inside the section. This is useful for dynamic product areas like **Recently viewed**, where the theme decides which products to show and the `product-card` template decides how each card looks.



## How it works

Some Slab product sections load products at runtime, then render each result using the `product-card` product template.

* The section or block chooses which products to display.
* Slab requests the `product-card` view for each product.
* The matching section response is inserted back into the section as a finished product card.
* Any changes you make to the `product-card` template affect every dynamic card that uses that template.



## Edit the product card template

To change these dynamic product cards, update the `product-card` product template in the theme editor.

{% stepper %}
{% step %}
### Open the template

1. Open the theme editor and navigate to a product template.
2. Open the template picker.
3. Select the `product-card` template.
{% endstep %}

{% step %}
### Update the blocks

Edit the blocks inside that template to control the card content and layout.

You can add, remove, or reorder blocks depending on what the card should show.
{% endstep %}

{% step %}
### Save and preview

Save your changes.

Preview a dynamic product area like **Recently viewed** to confirm the result.

The `product-card` template maps to `product.product-card.json`.
{% endstep %}
{% endstepper %}
