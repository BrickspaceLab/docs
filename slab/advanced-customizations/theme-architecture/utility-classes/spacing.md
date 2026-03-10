# Spacing

`src/css/utilities/spacing.css`

Layout-gap and section-overlap utilities that read from merchant layout settings. Use these instead of hardcoded spacing values so spacing automatically reflects the merchant's layout gap and overlap settings.

## Section layout

| Class               | Sets                                                                                          |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `section-overlap`   | Negative top margin + matching top padding to overlap the preceding section. Responsive: uses `--layout__desktop-overlap` on desktop and `--layout__mobile-overlap` on mobile. |
| `spacing--font-base`| `min-height` equal to base line-height (`--type__base * 1.625`)                               |

## Padding

| Class           | Sets                      |
| --------------- | ------------------------- |
| `padding--gap`  | All sides — `--layout__gap` |
| `padding--t-gap`| Top — `--layout__gap`     |
| `padding--r-gap`| Right — `--layout__gap`   |
| `padding--b-gap`| Bottom — `--layout__gap`  |
| `padding--l-gap`| Left — `--layout__gap`    |

## Margin

| Class          | Sets                      |
| -------------- | ------------------------- |
| `margin--gap`  | All sides — `--layout__gap` |
| `margin--t-gap`| Top — `--layout__gap`     |
| `margin--r-gap`| Right — `--layout__gap`   |
| `margin--b-gap`| Bottom — `--layout__gap`  |
| `margin--l-gap`| Left — `--layout__gap`    |
