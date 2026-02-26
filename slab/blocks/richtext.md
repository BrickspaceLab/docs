# Rich text

A flexible rich text content block that allows for formatted text content with customizable text color, alignment, and responsive visibility options.


## Overview

The Rich text block renders formatted HTML content created in the Shopify theme editor's rich text editor. It supports responsive visibility controls, text alignment, color theming, and custom font sizing.


## Common use cases

- Adding descriptive paragraphs, headings, or lists beneath a product image or banner
- Displaying editorial copy with a brand-specific font family and size
- Showing mobile-only or desktop-only variations of the same content
- Applying a scroll-triggered entrance animation to text for visual interest
- Constraining long-form copy to a readable max-width within wide layout containers


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Content | Rich text content displayed in the block | Richtext input |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds left and right padding to the text | Checkbox (default: false) |
| Enable top padding | Adds top padding to the text | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding to the text | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Selects between a base theme color or a custom color scheme | Custom, Base (default). Visible when Enable inheritance is off |
| Text | Sets the text color using a custom color scheme picker | Color scheme picker. Visible when Type is Custom and Enable inheritance is off |
| Text | Sets the text color from a predefined list of theme colors | Default (default), Alternative, Link, Error, Success, Shade 1, Shade 2, Shade 3. Visible when Type is Base and Enable inheritance is off |
| Enable inheritance | Inherits text color from the nearest parent block with a set scheme | Checkbox (default: false). Info: Colors will be inherited from the closest parent block that has a set scheme. |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Sets the typeface applied to all text in the block | Standard (default), Heading, Subheading, Accent. Visible when Font size is a body size or Custom |
| Font size | Controls the base text size using a preset scale or heading styles | Smaller, Small, Default (default), Big, Bigger, Heading 1, Heading 2, Heading 3, Heading 4, Heading 5, Heading 6, Custom |
| Size | Sets a custom font size in pixels | 4 – 200 px (default: 16). Visible when Font size is Custom |
| Line height | Sets a custom line height as a percentage | 100 – 300 % (default: 150). Visible when Font size is Custom |
| Letter spacing | Sets a custom letter spacing in rem units | -3 – 3 rem (default: 0). Visible when Font size is Custom |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls text and flex alignment within the block | Left (default), Center, Justify, Right |
| Enable max width | Constrains the text to a readable prose width | Checkbox (default: true) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls which devices the block is shown on | Show on all devices (default), Show on mobile only, Show on desktop only |
| Scroll animation | Controls how the block appears when scrolled into view | None (default), Fade, Slide up, Slide down, Slide left, Slide right, Zoom |
