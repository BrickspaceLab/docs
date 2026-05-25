# Configure dropdown navigation menus

Keystone’s header supports multi-level **dropdown menus** on desktop, optional **content blocks** inside dropdowns (images, promos, video), and a separate **sidebar menu** for alternative navigation layouts. This guide covers how dropdowns appear and how to achieve common menu layouts.

For sidebar vs. header-only navigation, see also [Design your menu](designing-your-menu.md).

## Prerequisites

1. In Shopify admin, go to **Content** > **Menus** and build a menu with **nested items** (parent links with child links). Flat menus show top-level links only—no dropdown.
2. In the theme editor, open the **Header** section.

## Assign the dropdown menu

1. Open **Customize**.
2. Select **Header** in the left panel.
3. Set **Dropdown menu** to your navigation menu (default is often **Main menu**).
4. Save and preview on **desktop** (dropdown hover behavior targets large screens).

| Setting | Description |
| ------- | ----------- |
| Dropdown menu | Menu used for desktop header links and nested dropdowns |
| Use top-level links as buttons | When a link has children, the parent opens the dropdown instead of navigating immediately |
| Color scheme / Color border (dropdown) | Styles the dropdown panel |

## How dropdowns behave

* **Parent links with sub-links** show a chevron and reveal a dropdown panel on hover (desktop).
* **Two levels of nesting** are supported: child links and grandchild links render in the dropdown list.
* **Content blocks** (Header section blocks) can attach promotional content to a specific parent link—set the block’s **Menu** field to match that link’s handle.

Add a **Content** block in **Header**:

1. In **Header**, click **Add block** > **Content**.
2. Set **Menu** to the parent link handle (for example `shop` for a link titled Shop).
3. Add heading, text, image, or video as needed.
4. Save.

Up to 10 content blocks can appear across dropdowns.

## Sidebar menu vs. header dropdowns

Keystone can show a persistent **sidebar menu** on desktop ( **Menu** section > **Enable sidebar menu** ) **and** header dropdown links at the same time.

| Layout goal | Configuration |
| ----------- | --------------- |
| Header dropdowns only | **Menu** > disable **Enable sidebar menu**; set **Header** > **Dropdown menu** |
| Sidebar only on desktop | Enable sidebar; minimize or hide header menu button behavior via Header settings |
| Both sidebar and header links | Enable sidebar **and** assign **Dropdown menu** in Header |

When the sidebar is open on desktop, the header **Menu** button toggles the sidebar closed so customers can access header dropdown navigation. Test both states after changing layout.

## Mobile navigation

Dropdown hover panels are desktop-oriented. On mobile, customers typically use the **menu drawer** configured in the **Menu** section. Ensure the same logical structure exists in your mobile menu blocks.

## Troubleshooting

| Issue | Check |
| ----- | ----- |
| No dropdown appears | Menu items have no child links in **Content** > **Menus** |
| Content block missing in dropdown | Block **Menu** handle matches the parent link handle exactly |
| Different layout on old theme version | [Update your theme](../basics/update-your-theme.md)—Header and Menu behavior changed across major releases |
| Expected mega-menu columns | Keystone dropdowns list nested links plus optional content blocks; multi-column mega menus may require custom development |

If you are on an outdated theme version and behavior does not match a fresh install, update to the latest Keystone release before troubleshooting further.

## Related reading

* [Design your menu](designing-your-menu.md)
* [Header section reference](../../sections/sitewide/header.md)
* [Menu drawer section reference](../../sections/sitewide/menu-drawer.md)
* [Update your theme](../basics/update-your-theme.md)
