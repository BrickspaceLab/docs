# Display product recommendations

Product recommendations help customers discover more products without leaving the page they are viewing. In Slab, merchants can use recommendation blocks to show either related items or complementary add-ons.

## How to set up product recommendations

1. Open your theme editor and go to a template where you want recommendations to appear (commonly product templates).
2. Add a container that supports recommendation blocks (for example a grid or slider area in your product content).
3. Add a **Product recommendations** block (grid or slider variant).
4. Set **Intent** to **Related** or **Complementary**.
5. Set **Product** if you want a fixed source product; otherwise use the current product context.
6. Set **Item count** to control how many products are shown.
7. Optional: add **Filter by tag** to narrow recommendations to one tag.
8. Choose whether to keep **Show products in cart** enabled.

### Complementary recommendations setup

If you choose **Complementary** intent, configure complementary products in Shopify's Search and Discovery app first. Slab uses that Shopify data when rendering complementary recommendations.

## Choose grid or slider recommendations

- Use a grid layout when you want recommendations to scan quickly in rows.
- Use a slider layout when you want a horizontal, swipe-friendly row on mobile.
- Slider recommendations include width controls for mobile and desktop cards.

## Suggested defaults for most stores

- Start with **Intent: Related** for automatic relevance.
- Keep **Item count** around 4 to 6 to avoid visual overload.
- Keep **Show products in cart** enabled for cross-sell workflows.
- Use **Filter by tag** only when you need tightly curated recommendations.

## What each recommendations setting controls

### Shared settings (grid and slider)

| Setting | What it controls | Options | Default |
| --- | --- | --- | --- |
| Intent | Recommendation type from Shopify. | Related, Complementary | Related |
| Product | Source product used to fetch recommendations. | Product picker | Uses current product context in presets |
| Item count | Max number of recommendation cards to render. | Number input | 5 |
| Filter by tag | Limits results to products containing a specific tag. | Text input | Blank |
| Show products in cart | Shows or hides recommended products already in the cart. | Enabled, Disabled | Enabled |
| Visibility | Where the block appears by device. | All, Mobile only, Desktop only | All |

### Slider-only settings

| Setting | What it controls | Range | Default |
| --- | --- | --- | --- |
| Width mobile | Width of each recommendation card on mobile. | 5% to 100% | 80% |
| Width desktop | Width of each recommendation card on desktop. | 5% to 100% | 20% |
