# Typography

`src/css/utilities/typography.css`

Use these instead of hardcoding font families, weights, or sizes. All classes read CSS custom properties set from merchant theme settings, so they adapt automatically to font selections.

## Font family and style

| Class                | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| `type__body`         | Body font family, weight, style, and line-height |
| `type__heading`      | Default heading font family, weight, and style  |
| `type__subheading`   | Subheading font family, weight, and style       |
| `type__accent`       | Accent font family, weight, and style           |
| `type__button-style` | Button font family, weight, and capitalization  |
| `type__button-size`  | Button line-height and letter-spacing           |

## Heading styles and sizes

Apply `type__heading-N-style` and `type__heading-N-size` independently so font style and size can be mixed as needed:

| Class                    | Purpose                    |
| ------------------------ | -------------------------- |
| `type__heading-1-style`  | H1 font family and style   |
| `type__heading-1-size`   | H1 font size               |
| `type__heading-2-style`  | H2 font family and style   |
| `type__heading-2-size`   | H2 font size               |
| `type__heading-3-style`  | H3 font family and style   |
| `type__heading-3-size`   | H3 font size               |
| `type__heading-4-style`  | H4 font family and style   |
| `type__heading-4-size`   | H4 font size               |
| `type__heading-5-style`  | H5 font family and style   |
| `type__heading-5-size`   | H5 font size               |
| `type__heading-6-style`  | H6 font family and style   |
| `type__heading-6-size`   | H6 font size               |

## Font sizes

Theme-relative sizes that scale with the merchant's base font setting:

| Class           | Purpose                     |
| --------------- | --------------------------- |
| `type--smaller` | Smaller than base           |
| `type--small`   | Small                       |
| `type--base`    | Base (default) size         |
| `type--big`     | Larger than base            |
| `type--bigger`  | Largest relative size       |
