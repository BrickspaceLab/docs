# Location


## Overview

A map location block that defines a geographic point with latitude and longitude coordinates. It supports customizable spacing, color schemes, border options, and controls for pre-opened and single-open behavior.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use to define individual store locations or points of interest on an interactive map component.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Latitude | Latitude coordinate for the location | Text input |
| Longitude | Longitude coordinate for the location | Text input |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable internal padding | Adds internal padding to the block | Checkbox (default: true) |
| Enable horizontal padding | Adds horizontal padding to the block | Checkbox (default: false) |
| Enable top padding | Adds top padding to the block | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding to the block | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent (default) |
| Border | Border color for the block | &bull; Body foreground<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; None |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Position of the border on the block | &bull; None<br>&bull; Top<br>&bull; Bottom (default)<br>&bull; Left<br>&bull; Right<br>&bull; Top & bottom<br>&bull; Left & right<br>&bull; All |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Enable pre-opened | Opens this location by default when the map loads | Checkbox (default: false) |
| Enable single open | Only allows one location to be open at a time | Checkbox (default: false) |
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
