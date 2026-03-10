# Filter

## Overview

A comprehensive filtering system for collection and search pages that provides customers with sorting options and advanced filtering capabilities. The block supports multiple filter types including boolean filters, list filters, and price range sliders with an accordion-style interface for organized presentation.

## Common use cases

* Ensure JavaScript functions (handleFilterChange, handleFilterDeleteAll, handlePriceFilterChange) are implemented for full functionality
* Configure border styling and internal padding based on your theme's design system
* Use appropriate gap sizes to maintain visual hierarchy between filter groups
* Test price range filters with your currency formatting and decimal handling
* Consider the number of filter options when deciding on swatch vs standard presentation
* Place this block in collection and search templates for optimal filtering experience

## Block settings

### Content

| Setting        | Description                                | Options                  |
| -------------- | ------------------------------------------ | ------------------------ |
| Enable filters | Enable or disable the filter functionality | Checkbox (default: true) |
| Enable sorting | Enable or disable sorting options          | Checkbox (default: true) |

### Filter container

| Setting                   | Description                                              | Options                                                                                                                                                                                                    |
| ------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Layout                    | Controls the filter container layout                     | <p>• Stacked (default)<br>• Inline</p>                                                                                                                                                                     |
| Top spacing               | Spacing above the filter container                       | 0 - 30 px (default: 0)                                                                                                                                                                                     |
| Bottom spacing            | Spacing below the filter container                       | 0 - 30 px (default: 0)                                                                                                                                                                                     |
| Enable horizontal padding | Adds horizontal padding around the container             | Checkbox (default: false)                                                                                                                                                                                  |
| Enable internal padding   | Adds internal padding to filter items                    | <p>Checkbox (default: false)<br><br>Visible when container layout is "stacked"</p>                                                                                                                         |
| Gap size                  | Spacing between filter items                             | <p>• None (default)<br>• Default<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p>                                                                                                                               |
| Button color              | Color scheme for filter buttons in inline layout         | <p>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link<br><br>Visible when container layout is "inline"</p> |
| Button size               | Size of filter buttons in inline layout                  | <p>• Extra small<br>• Small (default)<br>• Standard<br>• Large<br><br>Visible when container layout is "inline"</p>                                                                                        |
| Border color              | Color of borders around the filter container             | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when container border position is not empty and container layout is "stacked"</p>           |
| Border position           | Position of borders on the filter container              | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All<br><br>Visible when container layout is "stacked"</p>                                       |
| Open filters              | Comma-separated list of filter labels to open by default | <p>Text input<br><br>Visible when container layout is "stacked"</p>                                                                                                                                        |

### Filter items

| Setting              | Description                                                            | Options                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter limit         | Maximum number of filter options to display before showing "Show more" | Number input (default: 10)                                                                                                                            |
| Layout               | Controls the layout of filter items                                    | <p>• Stacked (default)<br>• Grid</p>                                                                                                                  |
| Desktop rows         | Number of columns per row on desktop                                   | <p>1 - 4 (default: 2)<br><br>Visible when items layout is "grid"</p>                                                                                  |
| Mobile rows          | Number of columns per row on mobile                                    | <p>1 - 4 (default: 1)<br><br>Visible when items layout is "grid"</p>                                                                                  |
| Show filter count    | Display the count of items for each filter option                      | Checkbox (default: true)                                                                                                                              |
| Show filter swatches | Display color/image swatches for filter options                        | Checkbox (default: true)                                                                                                                              |
| Swatch size          | Size of color/image swatches                                           | <p>8 - 256 px (default: 16)<br><br>Visible when show filter swatches is true</p>                                                                      |
| Swatch radius        | Border radius for color/image swatches                                 | <p>• None<br>• Default<br>• SM<br>• MD<br>• LG<br>• XL<br>• 2XL<br>• Full (default)<br><br>Visible when show filter swatches is true</p>              |
| Border color         | Color of borders around filter items                                   | <p>• Body<br>• Subtle<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None (default)<br><br>Visible when container layout is "stacked"</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
