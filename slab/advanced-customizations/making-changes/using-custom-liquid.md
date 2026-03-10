# Using custom liquid

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../support/hire-a-shopify-developer.md).
{% endhint %}

The **Custom liquid** section type lets you inject Liquid and HTML directly into any page template without editing theme source files. It is the fastest way to add a one-off snippet of dynamic or interactive content.



### When to use custom liquid

Custom liquid is a good fit when:

* You need a quick, one-off snippet that does not need to be reused across multiple pages or sections.
* The content does not require merchant-facing settings (no color pickers, text fields, or image pickers in the theme editor).
* You want to add interactivity using Alpine.js `x-data` without building a full block or section.
* You are prototyping or experimenting before committing to a more permanent solution.

If you find yourself needing the same snippet in multiple places, or if you want merchants to be able to configure the content from the theme editor, consider [creating a custom block](creating-custom-blocks.md) or [creating a custom section](creating-custom-sections.md) instead.



### How to add custom liquid

1. Open the theme editor and navigate to the page where you want to add the snippet.
2. Click **Add section** and select **Custom liquid** from the list.
3. Paste your Liquid and HTML code into the code field.
4. Save.



### Using AI to write custom liquid

AI coding agents are well-suited to writing custom liquid snippets. Slab uses [Alpine.js](https://alpinejs.dev/) for interactivity, so you can ask an agent to generate snippets that combine Liquid with Alpine's `x-data` and `x-init` directives.

A useful prompt structure:

{% code overflow="wrap" %}
```
Write a Shopify Liquid snippet using Alpine.js x-data that [describe what you want it to do]. Use utility classes from the Slab theme for styling where appropriate.
```
{% endcode %}



### Example: live clock for a timezone

The snippet below uses Alpine's `x-data` to display the current time in Toronto, updated every second. It was generated with this prompt:

{% code overflow="wrap" %}
```
Write a Shopify Liquid + Alpine.js snippet that displays the current local time in Toronto, updated every second. Use x-data and x-init.
```
{% endcode %}

```liquid
<div class="color-tx__shade-3">
  Site made with Slab / <span
    x-data="{
      time: '',
      update() {
        this.time = new Intl.DateTimeFormat('en-CA', {
          timeZone: 'America/Toronto',
          hour: 'numeric',
          minute: '2-digit',
          hour12: true
        }).format(new Date())
      }
    }"
    x-init="update(); setInterval(() => update(), 1000)"
    x-text="time"
  ></span> in Toronto
</div>
```

