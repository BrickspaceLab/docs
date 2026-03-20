# Overlays and popups

Slab includes four overlay block types: **Drawer**, **Sidebar**, **Popup**, and **Alert**. Use overlays when you want to show content on top of the storefront without sending customers to a new page.

Each overlay block can be connected to one of Slab's built-in overlay actions, such as **Account**, **Search**, **Menu**, **Primary cart**, or **Alternative cart**. You can also create your own custom overlays by giving the overlay a custom ID and linking a button to that same ID.



## Overlay blocks

#### Drawer

The Drawer block opens in a sliding panel and can be positioned on the left or right side, or centered at the top or bottom.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FLayout%3Ftheme_id%3D141866205235%26first_setting_id%3Dx_margin&#x26;block=template--18647337730099__section_NxEii.png" alt=""><figcaption></figcaption></figure>

**When to use Drawer**

* Use it for search, menu, cart, quick buy, or quick edit experiences that should feel tied to the edge of the screen.
* Use it when you want a larger overlay with room for both main content and an optional footer area.
* Use it when you want the page behind the overlay to pause while the drawer is open.



#### Sidebar

The Sidebar block also opens from the left or right side of the screen, but it behaves more like a side panel. In Slab's overlay logic, sidebars stay independent from the body scroll locking used by popups and drawers.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FLayout%3Ftheme_id%3D141866205235%26first_setting_id%3Dx_margin&#x26;block=template--18647337730099__section_N (1).png" alt=""><figcaption></figcaption></figure>

**When to use Sidebar**

* Use it for supplementary content that should stay lightweight and easy to dismiss.
* Use it for menu or account side panels when you want the storefront to remain scrollable.
* Use it when left or right positioning is enough and you do not need the centered top or bottom placement available in Drawer.



#### Popup

The Popup block opens as a centered modal overlay. It supports an optional **Enable full background** setting, which makes it more suitable for takeover-style experiences.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FLayout%3Ftheme_id%3D141866205235%26first_setting_id%3Dx_margin&#x26;block=template--18647337730099__section_N (2).png" alt=""><figcaption></figcaption></figure>

**When to use Popup**

* Use it for newsletter prompts, promotional messages, age verification, or focused calls to action.
* Use it when you want customers to concentrate on a single message or decision.
* Use it when a centered modal feels more natural than a slide-in panel.



#### Alert

The Alert block is the lightest overlay type. It appears in a corner of the screen and supports optional auto-close timing.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FLayout%3Ftheme_id%3D141866205235%26first_setting_id%3Dx_margin&#x26;block=template--18647337730099__section_N (4).png" alt=""><figcaption></figcaption></figure>

**When to use Alert**

* Use it for success messages, error messages, discount notices, and short promotional prompts.
* Use it when the message should be visible without taking over the full screen.
* Use it when you want the overlay to close automatically after a short delay.



## Default overlay usage

Each overlay block includes an **Overlay preset** setting. This setting assigns the block to one of Slab's built-in overlay IDs instead of using a custom ID.

For drawers and sidebars, the built-in presets are **Account**, **Search**, **Menu**, **Primary cart**, **Alternative cart**, **Quick buy**, and **Quick edit**.

For popups, the built-in presets are the same as drawers and sidebars, plus **Age verification**.

For alerts, the built-in presets are **Account**, **Search**, **Menu**, **Primary cart**, **Alternative cart**, **Age verification**, **Form response**, **Discount**, **Error**, **Quick buy**, and **Quick edit**.

Use these presets when you want a block to act as the theme's default overlay for a built-in action. For example, setting a Drawer block to **Search** connects that block to Slab's built-in search overlay action. Setting a Popup block to **Age verification** connects it to the theme's age verification overlay.

This also gives you the flexibility to control and change what overlay type is assigned to what action. For example you could upate the Menu to use a Popup instead of a Drawer.

The **Button** block can directly trigger the built-in **Account**, **Search**, **Menu**, **Primary cart**, and **Alternative cart** overlay actions, or it can trigger a custom overlay ID.



## Create a custom overlay

You are not limited to Slab's built-in overlay presets. The overlay blocks also support custom IDs, and the Button block can open those custom overlays when the IDs match.

Use a simple ID such as `newsletter-popup` or `size-guide`. Reuse that exact value in both the overlay block and the button block.

1. Add a **Drawer**, **Sidebar**, **Popup**, or **Alert** block.
2. Set **Overlay preset** to **Custom**.
3. Enter a value in **Overlay ID**.
4. Add a **Button** block where you want customers to trigger the overlay.
5. Enable **Enable custom action** on the button.
6. Set the button **Overlay preset** to **Custom**.
7. Enter the same value in **Overlay custom**.

Once both settings match, the button will open that overlay instead of linking to a URL.

