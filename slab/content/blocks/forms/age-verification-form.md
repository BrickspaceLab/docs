# Age verification

<figure><img src="../../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable age verification block that prevents site access until users confirm they meet the minimum required age. Supports both birthdate verification and simple confirmation methods. Uses localStorage to remember verified users between sessions.

## Common use cases

* Comply with age restrictions for products like alcohol, tobacco, or adult content
* Set appropriate age requirements based on your products and local regulations
* Use date verification method for stricter compliance needs
* Add custom button styling to match your theme design
* Remember verified users between sessions to improve user experience

## Compatible blocks

The following blocks can be nested within this block:

* [Button](../basics/button.md)

## Block settings

### Content

| Setting                 | Description                             | Options                                   |
| ----------------------- | --------------------------------------- | ----------------------------------------- |
| Enable age verification | Enables the age verification form       | Checkbox (default: false)                 |
| Age verification type   | Method used to verify age               | <p>• Date (default)<br>• Confirmation</p> |
| Age requirement         | Minimum age required to access the site | 1 - 99 (default: 18)                      |

### Spacing

| Setting                   | Description                             | Options                   |
| ------------------------- | --------------------------------------- | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the form | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the form        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the form     | Checkbox (default: false) |

### Color

| Setting    | Description             | Options                                                                                                                                                                                                                                                      |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color text | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
