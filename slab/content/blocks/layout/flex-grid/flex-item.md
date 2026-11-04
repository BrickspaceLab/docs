# Flex item

## Overview

A flexible container item designed to be used within layout\_\_flex.liquid for creating customizable layouts. Supports fit, fill, or custom responsive widths, alignment controls, spacing, optional sticky positioning, and optional load or scroll animations.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Use with layout\_\_flex.liquid to create flexible grid-like layouts
* Choose **Width** **Fill** so a column grows, **Fit** for natural width, or **Custom** with mobile and desktop percentages
* Turn on **Show advanced settings** to adjust device visibility, sticky behavior, or entrance motion
* Adjust gap size to maintain consistent spacing between nested elements

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

### General

| Setting                | Description                                                                 | Options                   |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals device visibility, sticky layout, sticky position, and load or scroll animations | Checkbox (default: false) |

### Spacing

| Setting                 | Description                               | Options                                                                                           |
| ----------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Enable padding          | Adds padding around the flex item content | Checkbox (default: false)                                                                         |
| Enable vertical spacing | Adds vertical padding (top and bottom)    | Checkbox (default: true)                                                                          |
| Gap size                | Spacing between child blocks              | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p>                         |

### Color

| Setting             | Description                          | Options                                                                                                                                                                                                                                                      |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset surface pair | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Enable inheritance** is off                                                                                                                                                                       |
| Color scheme        | Background and text                  | Color scheme picker<br><br>Visible when type is **Custom** and **Enable inheritance** is off                                                                                                                                                                   |
| Color scheme        | Background and text                  | <p>• Body background<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent (default)</p><br><br>Visible when type is **Base** and **Enable inheritance** is off                                                                     |
| Color border        | Border color                         | <p>• Subtle (default)<br>• Strong<br>• None</p><br><br>Visible when **Border position** is not **None**, type is **Base**, and **Enable inheritance** is off                                                                                               |
| Enable inheritance  | Inherit colors from a parent block   | Checkbox (default: false)                                                                                                                                                                                                                                    |

### Style

| Setting         | Description                   | Options                                                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting              | Description                                    | Options                                                                                                                                                          |
| -------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Width                | How the item sizes in the flex row             | <p>• Fit (content width)<br>• Fill (grow to use free space)<br>• Custom (default) — use mobile and desktop sliders</p>                                            |
| Width mobile         | Width on small screens                         | <p>5–100 %, step 5 (default: 80 %)<br><br>Visible when **Width** is **Custom**</p>                                                                                |
| Width desktop        | Width on large screens                         | <p>5–100 %, step 5 (default: 40 %)<br><br>Visible when **Width** is **Custom**</p>                                                                                |
| Vertical alignment   | Aligns nested content vertically in the item   | <p>• Top<br>• Middle<br>• Bottom (default)</p>                                                                                                                    |
| Enable sticky layout | Enables sticky positioning for this item       | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                             |
| Sticky position      | Edge the sticky item pins to                   | <p>• None (default)<br>• Top<br>• Bottom</p><br><br>Visible when **Show advanced settings** and **Enable sticky layout** are on</p>                               |

### Display

| Setting          | Description                          | Options                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Visibility       | Device visibility                    | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on                                                                                                                     |
| Load animation   | Animation when the block first loads | <p>• None (default)<br>• Fade<br>• Fade up<br>• Offset fade<br>• Offset fade up</p><br><br>Visible when **Show advanced settings** is on and **Scroll animation** is **None**                                                  |
| Scroll animation | Animation tied to scroll position    | <p>• None (default)<br>• Fade<br>• Fade up<br>• Fade down<br>• Slide left<br>• Slide right<br>• Zoom</p><br><br>Visible when **Show advanced settings** is on and **Load animation** is **None**                                 |
