# Progress tier

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Progress bar](./) block.

## Overview

A block that displays a cart progress tier message when a specific threshold is reached. Used to show messages like "You've unlocked free shipping" when the cart total meets or exceeds the threshold amount.

## Common use cases

* Display free shipping notifications when cart threshold is met
* Show tier-based incentives or rewards
* Provide visual feedback for cart value milestones

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../../layout/container.md)

## Block settings

| Setting                | Description                               | Options               |
| ---------------------- | ----------------------------------------- | --------------------- |
| Label                  | Text to display when threshold is reached | Text input            |
| Progress bar threshold | Cart value threshold (in dollars)         | Number (default: 100) |
