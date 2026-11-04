# Borders

`src/css/utilities/borders.css`

Theme-aware border width and radius utilities that read from CSS custom properties, plus standardised focus ring patterns. Use these instead of hardcoding pixel values for borders and radii so they automatically reflect merchant style settings.



## Border width

**Element**&#x20;

| Class             | Sets                                                    |
| ----------------- | ------------------------------------------------------- |
| `outline--width`  | Outline width + solid style — `--border__width-element` |
| `border--width`   | All sides — `--border__width-element`                   |
| `border--t-width` | Top only — `--border__width-element`                    |
| `border--r-width` | Right only — `--border__width-element`                  |
| `border--b-width` | Bottom only — `--border__width-element`                 |
| `border--l-width` | Left only — `--border__width-element`                   |



**Button**

| Class                    | Sets                                   |
| ------------------------ | -------------------------------------- |
| `border--button-width`   | All sides — `--border__width-button`   |
| `border--t-button-width` | Top only — `--border__width-button`    |
| `border--r-button-width` | Right only — `--border__width-button`  |
| `border--b-button-width` | Bottom only — `--border__width-button` |
| `border--l-button-width` | Left only — `--border__width-button`   |



**Input**

| Class                   | Sets                                     |
| ----------------------- | ---------------------------------------- |
| `border--input-width`   | All sides — `--size__border-input-width` |
| `border--t-input-width` | Top — `--input__border-width-top`        |
| `border--r-input-width` | Right — `--input__border-width-right`    |
| `border--b-input-width` | Bottom — `--input__border-width-bottom`  |
| `border--l-input-width` | Left — `--input__border-width-left`      |
| `border--input-padding` | Horizontal padding — `--input__padding`  |



## Border radius

| Class              | Sets                                                    |
| ------------------ | ------------------------------------------------------- |
| `border--radius`   | All corners — `--border__radius-element`                |
| `border--t-radius` | Top-left + top-right — `--border__radius-element`       |
| `border--b-radius` | Bottom-left + bottom-right — `--border__radius-element` |
| `border--l-radius` | Top-left + bottom-left — `--border__radius-element`     |
| `border--r-radius` | Top-right + bottom-right — `--border__radius-element`   |



## Focus styles

| Class                      | Style                                                                  |
| -------------------------- | ---------------------------------------------------------------------- |
| `border--focus`            | Solid outline using `--input__focus-width` and `--input__focus-border` |
| `border--focus--inset`     | 2px inset box-shadow focus ring with body-bg outline                   |
| `border--focus--outset`    | 4px outset box-shadow focus ring with body-bg outline                  |
| `border--focus--offset`    | 2px outline with `outline-offset: 2`                                   |
| `border--focus--simple`    | Inset 1px box-shadow, no outline                                       |
| `border--focus--underline` | Underline only, no outline or shadow                                   |
| `border--focus--none`      | Removes all border, outline, and shadow                                |



## Button border presets

Composite classes that apply the appropriate border widths, focus rings, and radii for buttons:

| Class                    | Applies                                           |
| ------------------------ | ------------------------------------------------- |
| `border__button`         | `border--button-width`                            |
| `border__button--focus`  | `color-br__input--focus` + `border--focus--inset` |
| `border__button--radius` | `--border__radius-button`                         |



## Input border presets

Composite classes that apply the appropriate border widths, focus rings, and radii for inputs:

| Class                      | Applies                                                    |
| -------------------------- | ---------------------------------------------------------- |
| `border__input`            | All four input border widths (top / right / bottom / left) |
| `border__input--focus`     | `border--focus--inset`                                     |
| `border__input--radius`    | `--border__radius-input`                                   |
| `border__textarea--radius` | `--border__radius-textarea`                                |



## Miscellaneous

| Class          | Effect                                                                               |
| -------------- | ------------------------------------------------------------------------------------ |
| `shadow--blur` | Diffuse drop shadow: `0px 0px 100px 10px rgb(0 0 0 / 0.3)`                           |
| `anglethrough` | Diagonal strikethrough line via a pseudo-element using `--color__background-shade-3` |
