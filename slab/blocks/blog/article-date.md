# Article date


## Overview

A configurable block that renders the published date of the nearest article using the 'abbreviated_date' format; supports alignment, typography, color, spacing, max width, visibility, and custom size controls via block settings; intended for use inside article cards, article templates, or blog listings; uses Tailwind utility classes and respects Theme Editor preview constraints.


## Common use cases

- Place near other article metadata (author, tags) for consistent hierarchy
- Prefer the default or smaller type sizes for subtle metadata
- Use custom size sparingly; favor predefined sizes for consistency
- Consider enabling max width to maintain readability in wide layouts


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the date | Checkbox (default: false) |
| Enable top padding | Adds top padding around the date | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the date | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Text color | Controls the text color | • Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for the date | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--' |
| Font size | Controls the font size of the date | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment | • Left (default)<br>• Center<br>• Right |
| Enable max width | Limits the maximum width of the date text | Checkbox (default: true) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
