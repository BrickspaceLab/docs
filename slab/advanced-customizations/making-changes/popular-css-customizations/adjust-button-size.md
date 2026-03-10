# Adjust button size

This guide shows how to change the font size and padding of buttons using the theme editor's built-in custom CSS field.

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../../support/hire-a-shopify-developer.md).
{% endhint %}

1. In the theme editor, navigate to the section you want to edit.
2. In the settings panel, scroll to the bottom and expand **Custom CSS**.
3. To apply the change across your entire storefront instead, navigate to **Theme settings > Custom CSS**.
4. Paste the following code into the input field and adjust the values as needed.
   - `font-size` controls the text size inside the button.
   - `padding` controls the space inside the button. The first value sets the top and bottom padding, the second sets the left and right padding.

```css
.btn { font-size: 24px; padding: 10px 30px; }
```
