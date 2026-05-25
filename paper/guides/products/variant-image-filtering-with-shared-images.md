# Variant image filtering with shared images

Paper’s **Only show media associated with the selected variant** setting (in the product section) filters the gallery so customers see images tied to the active variant. Merchants with large variant catalogs often also need **shared** images—lifestyle shots, size guides, or detail photos—that stay visible for every variant. This guide explains how filtering works, built-in behavior for unassigned media, and options when you need more control.

For basic setup, see [Dynamic variant images](dynamic-variant-images.md).

## How variant filtering works

When **Only show media associated with the selected variant** is enabled on **Product main** (or **Featured product**):

1. Paper groups each **image** with variants whose **featured image** matches that media file.
2. Grouped images show or hide with Alpine.js as customers change variants.
3. **Images not linked to any variant featured image are not filtered**—they remain visible for every variant selection.

Videos, 3D models, and external video media are not filtered the same way as variant-linked images.

| Setting | Location | Default |
| ------- | -------- | ------- |
| Only show media associated with the selected variant | Product section (**Product main**) | Off |

## Show variant images plus shared lifestyle shots (built-in)

To keep shared images visible while filtering variant-specific photos:

1. Enable **Only show media associated with the selected variant** on the product template.
2. In Shopify admin, open the product **Media** list.
3. Assign **featured images** only to variant-specific photos (each colorway’s hero, etc.).
4. **Do not assign** shared lifestyle, size chart, or detail images as any variant’s featured image—leave them as general product media only.
5. Order media so variant-specific images sit with their variant groups (see [Dynamic variant images](dynamic-variant-images.md)).

**Result:** Selecting a variant shows that variant’s assigned images **and** all unassigned shared images together.

{% hint style="info" %}
If a shared image disappears when switching variants, it is likely assigned as a variant featured image. Remove that assignment so the image stays in the shared pool.
{% endhint %}

## Limitations

* There is **no theme setting** to mark individual images as “always visible” while also using them as a variant featured image.
* Filtering is **all-or-nothing** per product template—you cannot enable it for some products only without separate templates.
* The setting does not support “pin these three images” independently of featured-image rules—unassigned media is the supported approach.

## Workarounds for advanced catalogs

### Use separate product templates

Create a alternate product template without filtering for products that need the full gallery always visible. Assign the template under **Products** > **Theme template** in admin.

### Custom Liquid (developer)

For rules that unassigned media cannot cover (for example pinning images by tag or metafield), a developer can customize gallery snippets (`product__gallery-grid.liquid`, `product__gallery-slider.liquid`, etc.). That is custom code—see [Support policy for modified theme code](../../../general/general/support-policy-for-modified-theme-code.md).

### Duplicate media per variant (last resort)

Duplicating the same lifestyle file under each variant’s featured image works but increases admin overhead and is harder to maintain than leaving shared files unassigned.

## Related reading

* [Dynamic variant images](dynamic-variant-images.md)
* [Use custom templates](../basics/use-custom-templates.md)
* [Add custom Liquid](../../advanced-customizations/adding-custom-liquid/README.md)
