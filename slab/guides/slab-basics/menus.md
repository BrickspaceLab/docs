# Menus

Slab separates **desktop navigation** (dropdown menus in the header) from the **menu overlay** (the panel that opens when customers tap the menu control on smaller screens or when a button is set to open the menu). You build the link structure in the Shopify admin, then style behavior and layout in the theme editor.

For how overlay blocks connect to theme actions, see [Overlays and popups](popups-drawers-and-overlays.md). For flex layouts often used next to menus in the header, see [Grid layouts](build-grid-layouts.md).



## Menu dropdown (header navigation)

The **Menu dropdown** block drives the main horizontal navigation with hover or click dropdowns, nested links, and optional featured content beside links.

**When to use Menu dropdown**

* When you want parent links with dropdown panels on desktop (and visibility can be limited to desktop if you rely on the overlay menu on mobile).
* When you need full-width “mega menu” style panels for specific top-level items.
* When you want to add extra blocks (promotions, products, and so on) inside a specific dropdown via **Menu item** child blocks.



## Menu overlay (drawer, sidebar, or popup)

The storefront **menu** action opens whichever overlay block is assigned the **Menu overlay** preset in **Overlay group**. The default theme content often uses a **Drawer** block (commonly named **Menu drawer**) with a **Menu page** or **Menu** block inside it.

**When to use the overlay menu**

* Primary navigation on viewports where the header menu is hidden.
* A full-screen or side-panel menu experience independent from the header bar.



## Swap the menu to a different overlay type

Only one overlay block should use the **Menu overlay** preset at a time.

{% stepper %}
{% step %}
### Open Overlay group

* In the theme editor, open **Overlay group**.
{% endstep %}

{% step %}
### Add the new overlay block

* Add a **Drawer**, **Sidebar**, or **Popup** block, or duplicate an existing overlay block and adjust it.
{% endstep %}

{% step %}
### Assign the menu action

* On the new block, set **Overlay** to **Menu overlay**.
{% endstep %}

{% step %}
### Move your menu content

* Move or rebuild the inner blocks (for example **Menu page**, **Menu**, search, and utilities) so customers still see the links you expect.
{% endstep %}

{% step %}
### Retire the old menu overlay

* On the previous menu overlay block, set **Overlay** to **Custom** with a unique ID you will not use, or remove that block so it no longer competes for the same action.
{% endstep %}
{% endstepper %}

Menu controls in the header use the same **Menu overlay** action. On a **Button** block, turn on **Enable custom action**, set **Overlay** to **Menu overlay**, so the button opens the overlay you configured above.



## Customize menus and dropdowns

{% stepper %}
{% step %}
### Build your link structure

* In the Shopify admin, go to **Online Store > Navigation** and edit the menu you will assign to the block (often the main menu).
* Parent items become top-level links; nested items appear in dropdowns (up to three levels: parent, child, grandchild).
{% endstep %}

{% step %}
### Assign the menu in the theme editor

* Open **Header group**, select the **Menu dropdown** block, and choose the same menu under **Menu**.
{% endstep %}

{% step %}
### Tune the Menu dropdown block

* Under **Parent links**, **Child links**, and **Grandchild links**, adjust typography for each level.
* Turn **Enable dropdown icons** off if you do not want chevrons on items that have children.
* Turn **Enable click to open** on so parents with children act as buttons that open the dropdown instead of navigating to the parent URL (info text in the theme explains this behavior).
* Under **Dropdown**, choose **Layout** **Stacked** or **Inline** for how child groups arrange, and use **Gap size** for spacing in that layout.
* Under **Dropdown colors**, set scheme, border, and divider styling, or use **Enable inheritance** so the dropdown follows surrounding color context.
{% endstep %}

{% step %}
### Add optional images next to links

* For child or grandchild links, you can show a small round image when a theme asset exists named `navigation_[link-handle].jpg` (the handle is derived from the link title), matching the pattern used in the **Menu** block.
{% endstep %}

{% step %}
### Add featured content to one top-level item

* Inside **Menu dropdown**, add a **Menu item** block.
* Set **Menu key** to the exact parent menu item title that should show that content when its dropdown is open (the theme matches a handleized form of the title).
* Add blocks inside **Menu item** as needed; those blocks appear only for the matching top-level item.
{% endstep %}
{% endstepper %}



## Full width dropdowns

For top-level items that should span the viewport like a mega menu, use the **Full width dropdown** setting on the **Menu dropdown** block.

{% stepper %}
{% step %}
### List the parent items

* In **Full width dropdown**, enter a **comma-separated** list of **parent** link titles as they appear in **Online Store > Navigation**, for example: `Best sellers, Sale, New arrivals`.
{% endstep %}

{% step %}
### Adjust horizontal spacing (optional)

* When **Full width dropdown** is not empty, **Enable margin** appears. Turn it on so spacing around the wide panel can follow **Theme settings > Layout** horizontal margins, or turn it off if you prefer edge-to-edge width.
{% endstep %}
{% endstepper %}

**Enable internal padding** on the dropdown applies to non-full-width dropdowns; full-width panels use wider edge padding in the theme.

Full-width dropdowns still respect a maximum height with scrolling when content is tall, so long lists remain usable on smaller screens.



## Menu dropdown: dropdown and layout settings

| Setting | What it controls |
| ------- | ---------------- |
| Layout (dropdown) | **Stacked** or **Inline** arrangement of child link groups in the panel. Default **Stacked**. |
| Enable internal padding | Adds padding inside the dropdown content when the panel is not full width. Default on. |
| Enable margin | When **Full width dropdown** has values, applies horizontal margin from theme layout settings. Default on. |
| Gap size (dropdown) | Spacing inside the dropdown panel; how it applies depends on **Layout** (stacked or inline) and whether the panel is full width. |
| Full width dropdown | Comma-separated parent link titles that use a full viewport-width panel. |
| Enable click to open | Parents with children become toggle buttons; dropdown closes on outside click. Default off (hover/focus behavior). |
| Horizontal alignment | Aligns the row of parent links: **Left**, **Center**, or **Right**. |
