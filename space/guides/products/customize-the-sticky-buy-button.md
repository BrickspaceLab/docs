# Customize the sticky buy button

Space’s **Fixed buy buttons** block adds a sticky add-to-cart bar on product pages. The theme editor exposes colors, position, and scroll behavior. Changes to button labels, price in the button, or mobile layout beyond those settings require editing the **`product__stickyadd.liquid`** snippet.

For editor setup, see [Fixed buy buttons](fixed-buy-buttons.md).

## What you can change in the theme editor

Add the block on **Product main** (or **Featured product**):

1. **Customize** > open a product template > select the product section.
2. **Add block** > **Fixed buy buttons**.
3. Configure:
   * **Color scheme**, **Color border**, **Color button**
   * **Horizontal position** — Left, Right, Center, or Full
   * **Show after scrolling** — bar appears only after scrolling past the main add-to-cart form
   * **Optional text** — rich text above the button (desktop)

Only one **Fixed buy buttons** block is allowed per product section.

## What requires code changes

The sticky bar markup lives in:

```
snippets/product__stickyadd.liquid
```

Common merchant requests that need snippet or developer work:

| Request | Editor support | Code location |
| ------- | -------------- | ------------- |
| Change add-to-cart button text globally | Partial — use product metafield `custom.button_text` for per-product text | Snippet button labels |
| Show price inside the sticky button | Not in editor | `product__stickyadd.liquid` |
| Full-width mobile layout tweaks | **Full** position only in editor | Snippet CSS classes |
| Replace variant dropdown with swatches | Not in editor | Snippet + product options blocks |

{% hint style="warning" %}
Editing `product__stickyadd.liquid` counts as **modified theme code**. Keep a backup duplicate and review [Support policy for modified theme code](../../../general/general/support-policy-for-modified-theme-code.md) before requesting theme support on customized files.
{% endhint %}

## Locate the snippet

1. Go to **Online Store** > **Themes**.
2. On your theme, open **…** > **Edit code**.
3. Open **Snippets** > `product__stickyadd.liquid`.

The snippet is rendered from `product__main.liquid` when a **stickyadd** block is present:

```liquid
{% render 'product__stickyadd', block: block %}
```

## Safe customization practices

1. **Duplicate the theme** before editing snippets.
2. **Change one element at a time** (button text, layout class, optional price output).
3. **Test on mobile and desktop** — position classes differ by breakpoint (`md:` prefixes).
4. **Document changes** so you can merge them after [updating the theme](../basics/update-your-theme.md).

### Example: show price next to the button (developer)

A developer can output the selected variant price inside the sticky bar using existing Alpine.js state (`current_variant_id`) and Paper/Space price snippets. Exact Liquid depends on your Space version—compare with `product__add.liquid` for patterns used on the main product form.

We do not publish copy-paste code here because Space updates can change variable names. Hire a Shopify developer if you are not comfortable editing Liquid.

## Sticky bar and other fixed elements

Fixed elements (sticky header, cookie banners, chat widgets) can overlap the buy bar. If content is obscured, adjust **Horizontal position**, disable **Show after scrolling** temporarily to debug, or reduce third-party widget z-index via app settings.

## Related reading

* [Fixed buy buttons](fixed-buy-buttons.md)
* [Preserve customizations when updating themes](../../../general/general/preserve-customizations-when-updating-themes.md)
* [Add custom Liquid](../../advanced-customizations/adding-custom-liquid/README.md)
* [Hire a Shopify developer](../../../general/support/hire-a-shopify-developer.md)
