# Grid articles

## Overview

A blog article grid block that displays articles from a selected blog. Supports filtering by tag and customizable display settings including item count and device visibility.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Use this block when you want to display a specific blog's articles in a grid layout
* Set an appropriate item\_count to control the number of articles shown
* Use the tag filter to display a subset of articles that match a specific tag

## Compatible blocks

The following blocks can be nested within this block:

* [Article card](../../cards/article-card.md)

## Block settings

### Content

| Setting       | Description                              | Options                   |
| ------------- | ---------------------------------------- | ------------------------- |
| Blog          | Select the blog to display articles from | Blog picker               |
| Item count    | Maximum number of articles to display    | Number input (default: 8) |
| Filter by tag | Filter articles by a specific tag        | Text input                |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
