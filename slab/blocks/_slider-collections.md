# Slider collections

A slider component for displaying collections in a horizontally scrollable layout. Designed for use within the slider layout block.


## Overview

Renders collections from a merchant-selected collection list as horizontally scrollable slider items with responsive width controls. Falls back to all collections in the theme editor when no collection list is selected.


## Common use cases

Use this block to showcase collections in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires a collection list selection and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and is not designed for standalone use.


## Block settings

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Collection list | Collections to display in the slider | Collection list picker |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Mobile width | Width of each slider item on mobile | 5 – 100 % (default: 80) |
| Desktop width | Width of each slider item on desktop | 5 – 100 % (default: 20) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
