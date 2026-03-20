---
hidden: true
---

# Menus

Your menu helps customers move through the storefront quickly. In Slab, most stores use a dropdown menu for desktop and a menu page inside the mobile drawer.

## How to set up your menu

1. In Shopify admin, go to **Content > Menus** and build your main navigation structure first.
2. Go to **Online Store > Themes > Customize**.
3. Open the **Header** group and select the **Theme header** section.
4. In your desktop navigation area, add or select a **Menu dropdown** block.
5. Choose your navigation in the **Menu** setting.
6. For mobile navigation, open the **Overlay** group and select the menu drawer content, then edit the **Menu page** block.
7. Use the same **Menu** setting there so desktop and mobile stay in sync.

## Suggested setup order

* Set up your menu structure in **Content > Menus** before styling.
* Configure desktop behavior first in **Menu dropdown**.
* Configure mobile behavior in **Menu page**.
* Turn on dropdown icons for clearer navigation when links have children.
* Test both desktop and mobile navigation before publishing.

## Menu dropdown settings to adjust first

Use these settings in the **Menu dropdown** block for desktop navigation.

| Setting                          | What it controls                                                                   | Default     |
| -------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| Menu                             | Which Shopify menu is rendered.                                                    | `main-menu` |
| Enable click to open             | Opens parent items with a click instead of hover/focus behavior.                   | Off         |
| Enable dropdown icons            | Shows chevrons when a parent item has child links.                                 | On          |
| Dropdown layout                  | Arranges dropdown content as stacked columns or inline rows.                       | Stacked     |
| Menu columns                     | Comma-separated parent menu items that should open as full-width dropdown columns. | Empty       |
| Dropdown enable internal padding | Adds internal spacing in dropdown content.                                         | On          |
| Dropdown gap size                | Controls spacing between dropdown items.                                           | Default     |
| Visibility                       | Shows block on all devices, mobile only, or desktop only.                          | All         |

## Menu page settings for mobile drawer

Use these settings in the **Menu page** block for mobile navigation overlays.

| Setting                 | What it controls                                          | Default     |
| ----------------------- | --------------------------------------------------------- | ----------- |
| Menu                    | Which Shopify menu is rendered in the drawer/page menu.   | `main-menu` |
| Enable internal padding | Adds inner spacing in the menu page panel.                | On          |
| Enable dropdown icons   | Shows chevrons on parent links with child items.          | On          |
| Gap size                | Controls spacing between menu rows.                       | Default     |
| Visibility              | Shows block on all devices, mobile only, or desktop only. | All         |
