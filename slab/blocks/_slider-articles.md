# Slider articles

A slider component for displaying blog articles in a horizontally scrollable layout. Designed for use within the slider layout block.


## Overview

Renders articles from a selected blog as horizontally scrollable slider items with responsive width controls. Supports filtering articles by tag.


## Common use cases

Use this block to showcase blog content in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires a blog context to iterate articles and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and is not designed for standalone use.


## Block settings

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Blog | Blog to display articles from | Blog picker |
| Item count | Number of articles to display | Number input (default: 7) |
| Filter by tag | Filters articles to only show those with this tag | Text input |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Mobile width | Width of each slider item on mobile | 5 – 100 % (default: 80) |
| Desktop width | Width of each slider item on desktop | 5 – 100 % (default: 20) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
