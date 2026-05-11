---
title: "Keystone: Recently Viewed & Recommended Products Link Bug + Mobile Variant Images"
source: "Intercom conversation"
intercom_conversation_id: "215474047860594"
captured_at: "2026-05-11"
tags: [keystone, bug, recently-viewed, variant-images, mobile, troubleshooting]
product: keystone
---

# Keystone: Recently Viewed & Recommended Products Link Bug + Mobile Variant Images

## Issue 1: "Recently Viewed" and "You May Also Like" Titles Link to the Wrong Product

**Symptom:** Clicking the *title* of a product in the "Recently Viewed" or "Recommended Products" section navigates back to the product page you're already on, instead of the clicked product. Clicking the *image* works correctly.

**Status:** ⚠️ Confirmed bug in the demo store. A fix is being tracked internally (Linear issue BL-620).

**Workaround (applied by customer):** Edit the theme code directly to correct the link href in the recently-viewed and recommended product card components.

If you encounter this, [contact support](https://brickspacelab.com/pages/theme-support) to request the patch or monitor for a theme update.

---

## Issue 2: Variant Images Displaying Out of Order on Mobile

**Symptom:** On mobile, when viewing a product with variants, the cover/default photo shows first instead of the image for the currently selected variant. This pushes the correct variant image off-screen.

**Fix:**

1. In your Shopify Admin, go to **Online Store → Themes → Customize**.
2. Navigate to your **Product** section settings.
3. Enable **"Show selected variant images only"**.

This ensures only the image matching the active variant is displayed, resolving the ordering issue.

---

## Issue 3: Displaying UPC via Variant Metafields

**Question:** How do I show a UPC code under the product title?

**Answer:** Keystone doesn't have a built-in UPC toggle, but you can surface it using **variant metafields** without custom code:

1. Store your UPC in a variant metafield (e.g. `custom.upc`).
2. In **Theme Settings → Product cards**, add `custom.upc` to the **Variant metafields** field.
3. Optionally add `UPC` to the **Variant metafield labels** field to display a label alongside the value.

This prints the metafield value next to the active variant automatically.
