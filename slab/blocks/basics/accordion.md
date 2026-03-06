# Accordion

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

## Overview

A collapsible accordion container that provides an expandable/collapsible content area with a header button. Uses Alpine.js for toggle functionality and includes smooth animations when enabled.

## Common use cases

* Create FAQ sections with expandable questions and answers
* Organize product details or specifications in collapsible sections
* Group related content that can be expanded on demand
* Enable pre-opened option to show content by default

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../containers/container.md) (for accordion label)
* [Container](../containers/container.md) (for accordion content)

## Block settings

### Spacing

| Setting                   | Description                                    | Options                   |
| ------------------------- | ---------------------------------------------- | ------------------------- |
| Enable internal padding   | Adds internal padding to the accordion content | Checkbox (default: true)  |
| Enable horizontal padding | Adds horizontal padding around the accordion   | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the accordion          | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the accordion       | Checkbox (default: false) |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank</p>                                       |

### Style

| Setting         | Description                   | Options                                                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Display

| Setting            | Description                                         | Options                                                   |
| ------------------ | --------------------------------------------------- | --------------------------------------------------------- |
| Enable pre opened  | Opens the accordion by default                      | Checkbox (default: false)                                 |
| Enable single open | Allows only one accordion item to be open at a time | Checkbox (default: false)                                 |
| Visibility         | Controls when the block is visible                  | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
