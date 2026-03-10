# Using custom icons

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../support/hire-a-shopify-developer.md).
{% endhint %}

The theme includes 60+ icons available through the [Icon block](../../../content/blocks/basics/icon.md). If you need an icon that is not part of the default set, you have two options: add a custom icon via code, or use the Image block to display any image as an icon.

### Option 1: Add a custom icon via code

{% stepper %}
{% step %}
**Prepare your SVG file**

* Obtain or create the icon you want to add in SVG format.
* Optimize the SVG to remove unnecessary attributes and reduce file size. [SVGOMG](https://jakearchibald.github.io/svgomg/) is a free tool you can use for this.
{% endstep %}

{% step %}
**Upload the SVG file**

* Open your Shopify admin and navigate to **Content > Files**.
* Upload your `.svg` file.
* Once uploaded, copy the file URL provided by Shopify.
{% endstep %}

{% step %}
**Edit theme code**

* Open the theme editor and navigate to **Actions > Edit code**.
* Locate the `theme__icons.liquid` snippet inside the **Snippets** folder.
* Find the `{% case icon %}` block and add a new entry for your icon. Replace `my-custom-icon` with the name you want to use and update the `src` with the file URL copied in the previous step.
* Save the file. Your custom icon will now be available for selection in the Icon block picker.
{% endstep %}
{% endstepper %}

### Option 2: Use the Image block (no code required)

If you only need to display a single custom icon without modifying theme code, the [Image block](../../../content/blocks/basics/icon.md) is a simpler alternative.

* Add an **Image** block to any section in the theme editor.
* Use the image picker to upload your icon file (`.png`, `.svg`, `.webp`, etc.).
* Adjust the **Width** setting to control the display size of the icon.

Refer to the [Image block documentation](../../../content/blocks/basics/image.md) for a full list of available settings including spacing, color scheme, alignment, and border options.
