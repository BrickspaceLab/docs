# Map


## Overview

A customizable store locator block that displays a map with markers for each store location. The block supports dynamic map rendering with Mapbox and static map rendering with an image. It also includes an accordion for each store location with details and a button to fly to the store.


## Common use cases

* Display an interactive map with location markers
* Show store locations or service areas
* Create contact pages with embedded maps


## Compatible blocks

The following blocks can be nested within this block:

* Location


## Block settings

### General

| Setting | Description | Options |
|---------|-------------|----------|
| Enable dynamic map | Enables a dynamic interactive map | Checkbox (default: true) |
| Image | This image will be used instead of the map if you disable dynamic map. | <p>Image picker<br><br>Visible when enable_dynamic_map is false</p> |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Map theme | Controls the map visual style | <p>• Standard<br>• Dark<br>• Light (default)</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
