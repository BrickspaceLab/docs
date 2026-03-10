# Table

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible container component that provides customizable table layout options for child blocks. Allows merchants to add multiple table items with customizable columns. Supports responsive display with mobile-friendly layout and column highlighting features.

## Common use cases

* Create comparison tables for products or features
* Display specification tables with multiple columns
* Show pricing comparison tables
* Organize data in a structured tabular format
* Highlight specific columns for emphasis
* Use for product feature comparisons or specification sheets

## Compatible blocks

The following blocks can be nested within this block:

* [Table row](table-row/)

## Block settings

### Content

| Setting         | Description                                                                      | Options    |
| --------------- | -------------------------------------------------------------------------------- | ---------- |
| Column headings | Comma-separated list of column headings (e.g., "Feature, Our Brand, Competitor") | Text input |

### Color

| Setting                 | Description                                                | Options                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Color scheme            | Controls the background and text colors                    | <p>• Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default)</p>                                                     |
| Enable column highlight | Highlights a specific column with a different color scheme | Checkbox (default: false)                                                                                                                                                                                                                      |
| Color column scheme     | Color scheme for the highlighted column                    | <p>• Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary (default)<br>• Blur<br>• Transparent<br><br>Visible when enable column highlight is true</p> |
| Highlighted column      | Column number to highlight (1-based index)                 | <p>0 - 10 (default: 2)<br><br>Visible when enable column highlight is true</p>                                                                                                                                                                 |

### Spacing

| Setting                   | Description                              | Options                   |
| ------------------------- | ---------------------------------------- | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the table | Checkbox (default: false) |
| Top spacing               | Padding space at the top of the table    | 0 - 300 px (default: 0)   |
| Bottom spacing            | Padding space at the bottom of the table | 0 - 300 px (default: 0)   |

### Style

| Setting     | Description                       | Options                                                                                                                                                           |
| ----------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Font family for table header text | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type--</p>                                                          |
| Font size   | Font size for table header text   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Layout

| Setting       | Description                                                   | Options                                                      |
| ------------- | ------------------------------------------------------------- | ------------------------------------------------------------ |
| Table layout  | Controls how table columns are sized                          | <p>• Auto<br>• Fixed (default)<br>• Custom</p>               |
| Column widths | Comma-separated list of column widths (e.g., "30%, 40%, 30%") | <p>Text input<br><br>Visible when table layout is custom</p> |

### Display

| Setting          | Description                        | Options                                                                                                    |
| ---------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Adds scroll-triggered animations   | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
