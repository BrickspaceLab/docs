# Popups, drawers and overlays

Slab includes four overlay block types: **Drawer**, **Sidebar**, **Popup**, and **Alert**. Use overlays when you want to show content on top of the storefront without sending customers to a new page.

Each overlay block can be connected to one of Slab's built-in overlay actions, such as **Account**, **Search**, **Menu**, **Primary cart**, or **Alternative cart**. You can also create your own custom overlays by giving the overlay a custom ID and linking a button to that same ID.


## Overlay types

### Drawer

The Drawer block opens in a sliding panel and can be positioned on the left or right side, or centered at the top or bottom.

**When to use Drawer**

* Use it for search, menu, cart, quick buy, or quick edit experiences that should feel tied to the edge of the screen.
* Use it when you want a larger overlay with room for both main content and an optional footer area.
* Use it when you want the page behind the overlay to pause while the drawer is open.


### Sidebar

The Sidebar block also opens from the left or right side of the screen, but it behaves more like a side panel. In Slab's overlay logic, sidebars stay independent from the body scroll locking used by popups and drawers.

**When to use Sidebar**

* Use it for supplementary content that should stay lightweight and easy to dismiss.
* Use it for menu or account side panels when you want the storefront to remain scrollable.
* Use it when left or right positioning is enough and you do not need the centered top or bottom placement available in Drawer.


### Popup

The Popup block opens as a centered modal overlay. It supports an optional **Enable full background** setting, which makes it more suitable for takeover-style experiences.

**When to use Popup**

* Use it for newsletter prompts, promotional messages, age verification, or focused calls to action.
* Use it when you want customers to concentrate on a single message or decision.
* Use it when a centered modal feels more natural than a slide-in panel.


### Alert

The Alert block is the lightest overlay type. It appears in a corner of the screen and supports optional auto-close timing.

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

The **Button** block can directly trigger the built-in **Account**, **Search**, **Menu**, **Primary cart**, and **Alternative cart** overlay actions, or it can trigger a custom overlay ID.


## Choosing the right overlay

Use **Drawer** when the overlay should feel like an extension of the page layout.

Use **Sidebar** when you want a lighter side panel and want to keep storefront scrolling available.

Use **Popup** when the message needs stronger focus in the center of the screen.

Use **Alert** when the message should be brief, contextual, and easy to dismiss.


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


## How custom overlay IDs work

In Slab's source code, each overlay block checks whether **Overlay preset** is set to `custom`. If it is, the block uses the value from **Overlay ID** as the overlay's internal ID. The Button block uses its **Overlay custom** value to call the theme's `toggleOverlay(...)` function with that same ID.

That is why the two values must match exactly. If the IDs do not match, the button will not know which overlay to open.


## Common examples

### Create a custom newsletter popup

Use a **Popup** block with **Overlay preset** set to **Custom** and **Overlay ID** set to `newsletter-popup`. Then add a **Button** block, enable **Enable custom action**, choose **Custom** for the button overlay preset, and enter `newsletter-popup` in **Overlay custom**.


### Create a custom size guide drawer

Use a **Drawer** block with **Overlay preset** set to **Custom** and **Overlay ID** set to `size-guide`. Then connect a **Button** block to the same `size-guide` value.


### Show short feedback after an action

Use an **Alert** block when you want to show a brief message such as a discount notice, form response, or error message. If the message should disappear automatically, enable **Enable auto close** and choose an **Auto close duration**.
