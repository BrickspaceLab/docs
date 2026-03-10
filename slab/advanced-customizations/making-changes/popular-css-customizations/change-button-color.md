# Change button color

This guide shows how to override the background and text color of buttons using the theme editor's built-in custom CSS field.

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../../support/hire-a-shopify-developer.md).
{% endhint %}

1. In the theme editor, navigate to the section you want to edit.
2. In the settings panel, scroll to the bottom and expand **Custom CSS**.
3. To apply the change across your entire storefront instead, navigate to **Theme settings > Custom CSS**.
4. Paste the following code into the input field and update the color values as needed.
   - Replace the first `#000000` to change the button background color.
   - Replace the second `#000000` to change the button border color.
   - Replace `#ffffff` to change the button text color.

```css
.btn { background: #000000; border: #000000; color: #ffffff; }
```
