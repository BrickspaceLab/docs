# Hide out of stock options

Use Custom CSS to hide variant options that are out of stock. This removes values that appear with a strikethrough and disabled options in dropdowns.

***

### When to use this customization

This CSS customization is useful when you want to completely hide unavailable options from customers. However, many themes now include built-in settings to control how unavailable options are displayed. **Check your theme's Product Options settings first** before applying this custom code.

***

### Add custom CSS

{% stepper %}
{% step %}
Go to **Online Store** > **Themes** > **Customize**
{% endstep %}

{% step %}
Open **Theme settings** > **Custom CSS**
{% endstep %}

{% step %}
Paste the following code:

```css
/* Hide out-of-stock variants with strikethrough */
.strikethrough,
.linethrough {
  display: none !important;
}

/* For dropdown options that are disabled */
select option:disabled {
  display: none !important;
}
```
{% endstep %}

{% step %}
Click **Save**
{% endstep %}
{% endstepper %}

***

### How it works

This code targets:

* **Strikethrough variants** - Options marked with `.strikethrough` or `.linethrough` classes (typically button-style selectors)
* **Disabled dropdown options** - Options marked as `:disabled` in dropdown selectors

***

### Important notes

* This applies to all products on your store
* Customers won't see that these options exist
* Some themes have built-in settings for this - check **Theme Settings > Product Options** first
* Test thoroughly on different product pages before going live

{% hint style="info" %}
Many modern themes include **"Unavailable indication"** settings that let you hide unavailable options without custom code. Check your theme's documentation for native options.
{% endhint %}

