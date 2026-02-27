# Product media


## Overview

A versatile product media block that renders product images or videos with extensive customization options. Features include hover effects with secondary media, aspect ratio control, flexible padding and spacing, comprehensive color schemes, and responsive visibility settings. The block automatically detects and handles both image and video media types from the product's media collection.


## Common use cases

- Display product images on product pages and product cards
- Show product videos with autoplay and loop functionality
- Enable hover effects to show secondary product images
- Control aspect ratios for consistent product image display
- Use object-fit settings to control how images fill their containers
- Configure appropriate padding based on the block's container context


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display media for | Product picker |
| Show second image on hover | Displays the second product image when hovering over the first | Checkbox (default: true) |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the media | Checkbox (default: false) |
| Enable top padding | Adds top padding around the media | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the media | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background color scheme | • Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |
| Enable aspect ratio | Forces the media to maintain a specific aspect ratio | Checkbox (default: false) |
| Show entire image | Uses object-contain instead of object-cover to show full image | Checkbox (default: true)<br><br>Visible when enable aspect ratio is true |
| Aspect ratio | The aspect ratio to maintain | • Square<br>• Landscape<br>• Portrait<br>• None<br><br>Visible when enable aspect ratio is true |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
