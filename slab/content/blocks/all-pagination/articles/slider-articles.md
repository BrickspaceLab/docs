# Slider articles

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Slider](../../layout/slider/) block.

## Overview

A customizable slider component for displaying blog articles in a horizontal scrollable layout. This block iterates through articles from a selected blog and renders them as slider items with configurable layout options.

## Common use cases

* Use this block when you want to showcase blog content in a scrollable slider format
* Configure the widths carefully to ensure proper display on different devices
* When using tag filtering, ensure articles have appropriate tags assigned
* For best results, use with blog content that has consistent image dimensions

## Block settings

### Content

| Setting       | Description                       | Options             |
| ------------- | --------------------------------- | ------------------- |
| Blog          | Blog to display articles from     | Blog picker         |
| Item count    | Number of articles to display     | Number (default: 7) |
| Filter by tag | Filter articles by a specific tag | Text input          |

### Spacing

| Setting       | Description                          | Options                 |
| ------------- | ------------------------------------ | ----------------------- |
| Width mobile  | Width of each slider item on mobile  | 5 - 100 % (default: 80) |
| Width desktop | Width of each slider item on desktop | 5 - 100 % (default: 20) |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
