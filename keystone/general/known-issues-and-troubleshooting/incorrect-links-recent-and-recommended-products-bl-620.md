# Incorrect links in Recent slider and recommended products (BL-620)

**Tracking:** Internal ticket **BL-620** covers incorrect product URLs inside dynamic sliders on product templates.

## Summary

Under certain conditions, tiles inside the **Recent slider** and **Recommendations** slider sections (for example “Recently viewed” or “You may also like”) can link to the **wrong** product detail page. The issue has been observed on the public Keystone demo storefront and can mislead customers who are comparing items.

## Affected areas

* **Recent slider** section (`recent-slider` in the theme source).
* **Recommendations** slider section (`recommendations-slider` in the theme source), including complementary or related product intents configured in the section settings.

Standard Liquid sections that loop over collection products (such as **Featured collection**) are not part of this bug pattern.

## Workarounds until a fix ships

* Remove or hide the affected sections on templates where incorrect links are unacceptable (for example high-traffic PDPs during a launch).
* Use **device-specific visibility** if only one breakpoint misbehaves in your tests.
* Replace the dynamic slider temporarily with a manually curated **Featured collection** or **Product slider** section when you must guarantee link targets.

## Staying up to date

Watch the [Keystone changelog](../../changelog.md) and your theme library notifications for a release that references BL-620 or these sections. After upgrading, re-test the same product template in a private browsing window.

## Related documentation

* [Recently viewed](../../sections/products-and-collections/recently-viewed.md) — section overview and settings.
* [Dynamic variant images](../../guides/products/product-variant-images.md) — separate topic from BL-620, but often reviewed in the same support conversations.
