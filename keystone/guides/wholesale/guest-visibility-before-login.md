# Control guest visibility before login

Wholesale and B2B stores often need logged-out visitors to see the product catalog while hiding prices—or the opposite. Keystone separates **price** restrictions from **product** restrictions. Using the wrong tag or combining features incorrectly can hide product names when you only meant to hide prices.

This guide explains what logged-out and unapproved customers see for each setting.

## Approval basics

Restricted content is shown only to **approved customers**:

* Customers with matching **Matching tags** (when configured), or
* Any logged-in customer when **Matching tags** is empty, or
* Logged-in **B2B customers** when **Enable B2B customers** is on

See [Customer approval](customer-approval.md) for setup.

All restriction tags are **case sensitive**. Tags in theme settings must match product tags exactly.

## Three ways to restrict content

| Feature | Theme settings field | Effect on unapproved visitors |
| ------- | -------------------- | ------------------------------ |
| [Hide prices](hide-prices.md) | **Hide prices with tag** | Tagged products show **without price or add to cart**; title and image remain |
| [Hide products](hide-products.md) | **Hide products with tag** | Tagged products are **removed** from grids and search (or show a login placeholder—see below) |
| [Full site restriction](full-site-restriction.md) | **Enable full restriction** | Most of the storefront is locked; only selected homepage sections may show |

Configure these under **Theme settings** > **Account**.

## Hide prices only (keep product names visible)

Use this when guests should browse the catalog but not see pricing or purchase.

1. Open **Customize** > **Theme settings** > **Account**.
2. Set **Hide prices with tag** (for example `hide price`).
3. Leave **Hide products with tag** empty unless you also need to hide specific SKUs entirely.
4. Add the **same tag** to products that should hide prices.
5. Save.

**Result:** Unapproved visitors still see the product title, image, and card layout. Price and **Add to cart** are hidden for tagged products.

## Hide products completely

Use this for wholesale-only SKUs that should not appear in the public catalog.

1. Set **Hide products with tag** (for example `hide product`).
2. Tag restricted products in Shopify admin.
3. Choose **Restricted style**:
   * **Hidden** — product cards disappear entirely from collections and search
   * **Placeholder** — an empty card with **Login to view** appears instead of the product name and image

{% hint style="warning" %}
If product **names** disappeared for logged-out visitors, check whether products have the **Hide products with tag** tag—not just the hide-price tag. Also check **Restricted style**: **Placeholder** replaces the full card with a login prompt, which can look like missing product names.
{% endhint %}

## Full site restriction

When **Enable full restriction** is on, unapproved visitors cannot access product pages, collections, blog posts, or search results. You can still show selected homepage sections (welcome banner, sign-up form). See [Full site restriction](full-site-restriction.md).

Do not enable full restriction if you want a public catalog with hidden prices only.

## Common misconfigurations

| Goal | Configure | Avoid |
| ---- | --------- | ----- |
| Public catalog, hidden prices | **Hide prices with tag** only | **Hide products with tag** on the same products |
| Wholesale-only SKU | **Hide products with tag** | Using hide-price tag alone (product still visible) |
| Login-only store | **Enable full restriction** | Expecting collection pages to remain public |
| Show “login to view” placeholders | **Restricted style** = **Placeholder** | **Hidden** when you want a visible login cue |

## Test before launch

1. Open the storefront in a private window (logged out).
2. Browse a collection with tagged and untagged products.
3. Log in as a test wholesale customer with approval tags.
4. Confirm prices, titles, and add-to-cart match your policy.

## Related reading

* [Hide prices](hide-prices.md)
* [Hide products](hide-products.md)
* [Full site restriction](full-site-restriction.md)
* [Customer approval](customer-approval.md)
* [Wholesale overview](README.md)
