# Show variant metafield content

Display variant-specific metafields when a shopper selects a variant on the product page. This uses Alpine's `x-show` to conditionally render content for the active variant and can be added via a `Custom liquid` section.

{% hint style="info" %}
Replace `custom.short_description` with your metafield namespace and key. Ensure the metafield exists on each variant you want to display.
{% endhint %}

1. In the theme editor, add a `Custom liquid` section to your product template.
2. Paste the snippet below and adjust the markup/metafield as needed.
3. Save and preview. Switch variants to see content update.

```liquid
{% for variant in product.variants %}
  <div x-show="current_variant_id == {{ variant.id }}">
    {{ variant.title }}
    {% if variant.metafields.custom.short_description %}
      – {{ variant.metafields.custom.short_description }}
    {% endif %}
  </div>
{% endfor %}
```

Notes:

* `current_variant_id` is managed by the theme's Alpine state and updates on selection.
* Duplicate the inner block to output multiple metafields.
