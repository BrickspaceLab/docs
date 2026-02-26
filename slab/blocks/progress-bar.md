# Progress bar


## Overview

A configurable progress bar block for use in theme sections.


## Common use cases

* Display cart progress tiers that incentivize customers to reach spending thresholds
* Show free shipping progress indicators
* Create tiered discount progress bars


## Compatible blocks

The following blocks can be nested within this block:

* Progress tier


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| Progress bar calculation | Choose to calculate the progress bar based on subtotal or total. | <p>• Subtotal<br>• Total (default)</p> |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |
| Enable internal padding | Adds internal padding to the progress bar content | Checkbox (default: true) |
| Gap size | Spacing between content blocks within the container | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Bar | Select a custom progress bar color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Container | Select a custom container color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Bar | Controls the progress bar color | <p>• Body<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Container | Controls the container background color | <p>• Body<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1 (default)<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Text | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when border_position is not  and color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: true) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Font family | Controls the font family | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type--</p> |
| Font size | Controls the font size | <p>• Smaller<br>• Small (default)<br>• Default<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All</p> |

### Layout

| Setting | Description | Options |
|---------|-------------|----------|
| Horizontal alignment | Controls horizontal alignment | <p>• Left (default)<br>• Center<br>• Justify<br>• Right</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
