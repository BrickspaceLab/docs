# Location

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Map](README.md) block.

## Overview

A dynamic block designed to display an individual store location on a map. When clicked, it triggers a JavaScript function to fly to the specified longitude and latitude. Store details are presented within an accordion component, allowing for expandable content.

## Common use cases

- Ensure the `flyToLocation` JavaScript function is globally accessible and properly implemented to interact with the map
- Always provide accurate `latitude` and `longitude` values for precise map positioning
- Localize the store name and store details settings for multi-language storefronts
- Coordinate `color_scheme` and `border_position` settings with the overall theme design for a consistent look and feel

## Compatible blocks

The following blocks can be nested within this block:

- [Container](../containers/container.md) (for label)
- [Container](../containers/container.md) (for content)

## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Latitude | Latitude coordinate for the location | Text input (default: "43.691070") |
| Longitude | Longitude coordinate for the location | Text input (default: "-79.337015") |
| Enable internal padding | Adds padding inside the accordion | Checkbox (default: true) |
| Enable horizontal padding | Adds horizontal padding around the block | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |
| Color scheme | Controls the background color scheme | Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent (default) |
| Border color | Controls the border color | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when border position is not empty |
| Border position | Controls which sides have borders | None, Top, Bottom (default), Left, Right, Top and bottom, Left and right, All |
| Enable pre opened | Opens the accordion by default | Checkbox (default: false) |
| Enable single open | Closes other accordions when this one opens | Checkbox (default: false) |
| Visibility | Controls when the block is visible | All (default), Mobile only, Desktop only |

