---
hidden: true
---

# Using custom CSS

Custom CSS can be applied to your Shopify theme by using the built-in [custom CSS](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/add-css) feature in your theme editor.&#x20;

Custom CSS can be used in a variety of ways and is the perfect option for minor customizations. Here are a few guides for commonly requested customizations.

<details open>

<summary>Change the background color for a section</summary>

1. Navigate to the section you want to edit.
2. In the settings panel scroll to the bottom and open **Custom CSS**.
3. Alternatively, if you want to apply this change across your entire store front navigate to **Theme settings > Custom CSS**
4. Paste the following code in the input field and update the color value to any hex color code.

section { background-color: #000000; }

</details>

<details open>

<summary>Change the color of section section headings</summary>

1. Navigate to the section you want to edit.
2. In the settings panel scroll to the bottom and open **Custom CSS**.
3. Alternatively, if you want to apply this change across your entire store front navigate to **Theme settings > Custom CSS**
4. Paste the following code in the input field and update the color value to any hex color code. E.g. `#000000` could be changed to `#ffffff`.

h3 { color: #000000; }

</details>

<details open>

<summary>Change the color of a button</summary>

1. Navigate to the section you want to edit.
2. In the settings panel scroll to the bottom and open **Custom CSS**.
3. Alternatively, if you want to apply this change across your entire store front navigate to **Theme settings > Custom CSS**
4. Paste the following code in the input field and update the color value to any hex color code.
   * In the below example, `#000000` can be replaced to change the background of the button, `#ffffff` can be replaced to change the text color of the bottom

.btn { background: #000000; border: #000000; color: #ffffff; }

</details>

<details open>

<summary>Adjust the size of a button</summary>

1. Navigate to the section you want to edit.
2. In the settings panel scroll to the bottom and open **Custom CSS**.
3. Alternatively, if you want to apply this change across your entire store front navigate to **Theme settings > Custom CSS**
4. Paste in the following code. Adjust any of the values to change the button as needed

.btn { font-size: 24px; padding: 10px 30px; }

</details>
