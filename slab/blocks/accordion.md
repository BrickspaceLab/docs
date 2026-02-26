# Accordion


## Overview

A collapsible accordion container that provides an expandable/collapsible content area with a header button. Uses Alpine.js for toggle functionality and includes smooth animations when enabled.


## Common use cases

* Create FAQ sections with expandable questions and answers
* Organize product details or specifications in collapsible sections
* Group related content that can be expanded on demand
* Enable pre-opened option to show content by default


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable internal padding | Adds internal padding to the accordion content | Checkbox (default: true) |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• Body<br>• Subtle (default)<br>• Strong<br>• None<br><br>Visible when border_position is not  and color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Enable pre-opened | Show the accordion open by default. | Checkbox (default: false) |
| Enable single open | Only one accordion can be open at a time. Note: only accordions with the same settings will be considered. | Checkbox (default: false) |
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
