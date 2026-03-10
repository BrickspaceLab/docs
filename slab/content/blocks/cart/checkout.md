# Checkout

<figure><img src="../../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

## Overview

A checkout container block that displays a form with checkout button, only visible when cart has items. Handles checkout redirection and supports Alpine.js for interactivity. Uses localStorage to remember verified users between sessions.

## Common use cases

* Display checkout button in cart drawers or cart pages
* Redirect customers to checkout when form is submitted
* Customize checkout button styling and behavior
* Show checkout form only when cart contains items
* Use with button blocks for checkout functionality

## Compatible blocks

The following blocks can be nested within this block:

* [Button](../basics/button.md)

## Block settings

### Spacing

| Setting                   | Description                                      | Options                   |
| ------------------------- | ------------------------------------------------ | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the checkout form | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the checkout form        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the checkout form     | Checkbox (default: false) |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
