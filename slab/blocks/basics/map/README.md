# Map

<figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable store locator block that displays a map with markers for each store location. The block supports dynamic map rendering with Mapbox and static map rendering with an image. It also includes an accordion for each store location with details and a button to fly to the store.

## Common use cases

* Display store locations with interactive maps
* Show multiple locations with detailed information
* Create location finders for retail stores
* Provide directions and location details
* Build contact pages with map integration

## Compatible blocks

The following blocks can be nested within this block:

* [Location](../location.md)

## Block settings

### Content

| Setting            | Description                                        | Options                                                             |
| ------------------ | -------------------------------------------------- | ------------------------------------------------------------------- |
| Enable dynamic map | Enables dynamic map rendering with Mapbox          | Checkbox (default: true)                                            |
| Image map          | Static map image used when dynamic map is disabled | <p>Image picker<br><br>Visible when enable dynamic map is false</p> |

### Color

| Setting      | Description                          | Options                                                                                                                                                                                    |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background color scheme | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color            | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None</p>                                                                                        |

### Style

| Setting   | Description                                 | Options                                          |
| --------- | ------------------------------------------- | ------------------------------------------------ |
| Map style | Controls the visual style of the Mapbox map | <p>• Standard<br>• Dark<br>• Light (default)</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
