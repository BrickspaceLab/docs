# Progress bar

## Overview

A simple horizontal progress bar block driven by a **Value** between 0 and 100. Use it for static milestones, campaign progress, or connect **Value** to a product or page metafield so the fill updates per product or context. This block is separate from the [cart progress bar](../cart/progress-bar/README.md), which calculates progress from cart totals and tiers.

## Common use cases

* Show completion toward a goal (for example fundraising or a multi-step story)
* Pair **Value** with a metafield for per-product readiness or capacity
* Match bar height and colors to surrounding sections

## Compatible blocks

This block does not accept nested blocks.

## Block settings

### General

| Setting                | Description                                              | Options                    |
| ---------------------- | -------------------------------------------------------- | -------------------------- |
| Show advanced settings | Reveals device visibility for the block                  | Checkbox (default: false)  |

### Content

| Setting | Description                                      | Options                                                                 |
| ------- | ------------------------------------------------ | ----------------------------------------------------------------------- |
| Value   | Fill level for the bar (clamped between 0–100)   | Text (default: 50). Use a number or a dynamic source such as a metafield |

### Spacing

| Setting                   | Description                               | Options                                                                      |
| ------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------- |
| Enable horizontal padding | Adds horizontal padding around the bar    | Checkbox (default: false)                                                    |
| Enable top padding        | Adds top padding above the bar            | Checkbox (default: false)                                                    |
| Enable bottom padding     | Adds bottom padding below the bar         | Checkbox (default: false)                                                    |
| Gap size                  | Space between the bar and other flex items | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting        | Description                         | Options                                                                                                                                                                                                                                                      |
| -------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type           | Use theme base colors or a custom scheme for the fill | <p>• Custom<br>• Base (default)</p>                                                                                                                                                                                                                          |
| Bar (custom)   | Color scheme for the filled portion | Color scheme picker<br><br>Visible when type is **Custom**                                                                                                                                                                                                    |
| Bar (base)     | Base color token for the fill       | <p>• Body background<br>• Body foreground (default)<br>• Accent 1–3<br>• Shade 1–3</p><br><br>Visible when type is **Base**                                                                                                                                  |

### Layout

| Setting     | Description   | Options                          |
| ----------- | ------------- | -------------------------------- |
| Height      | Bar thickness | 2–24 px, step 2 (default: 8 px) |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Device visibility for the block    | <p>• All devices (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |
