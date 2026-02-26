# Age verification form


## Overview

A customizable age verification block that prevents site access until users confirm they meet the minimum required age. Supports both birthdate verification and simple confirmation methods.


## Common use cases

* Restrict access to age-sensitive content or products
* Use date-of-birth or simple confirmation verification methods
* Configure minimum age requirements for different regions


## Compatible blocks

The following blocks can be nested within this block:

* [Button](button.md)


## Block settings

### General

| Setting | Description | Options |
|---------|-------------|----------|
| Enable verification | Enables the age verification gate | Checkbox (default: false) |

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| Verification type | Type of age verification method | <p>• Full date (default)<br>• Confirmation button</p> |
| Age requirement | Minimum age required | 1 - 99 (default: 18) |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Text | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: true) |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
