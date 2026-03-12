# Build grid layouts

Slab offers two main layout blocks for arranging content: **Default grid** and **Flex grid**. Each suits different layout needs. This guide covers both blocks and when to use them.

## Default grid

The Default grid block creates a responsive grid of equal-width columns. Use it for product grids, image galleries, card layouts, or any content that benefits from a uniform grid structure.

### When to use Default grid

- Display multiple blocks in rows and columns
- Use specialized blocks like Grid products, Grid articles, Grid collections, Grid gallery, Grid recommendations, or Grid recent
- Build custom layouts with [Grid item](../../content/blocks/layout/default-grid/grid-item.md) blocks
- Support app blocks and all theme blocks as children

### Key settings

| Setting | Description | Default |
|---------|-------------|---------|
| Desktop row size | Number of columns on desktop | 5 (range: 1–8) |
| Mobile row size | Number of columns on mobile | 2 (range: 1–3) |
| Gap size | Spacing between grid items | Default (None, XS, SM, MD, LG, XL) |
| Top spacing | Padding at top of container | 0–300 px |
| Bottom spacing | Padding at bottom of container | 0–300 px |
| Enable horizontal padding | Adds horizontal padding around the container | Off |

The Default grid also supports color scheme, border, visibility, and scroll animation settings.

### Grid item

For custom content inside a Default grid, add [Grid item](../../content/blocks/layout/default-grid/grid-item.md) blocks. Grid item supports:

- **Row span** — Extend a block across 1–6 rows
- **Column span** — Extend a block across 1–6 columns on desktop
- **Vertical alignment** — Top, Middle, or Bottom
- Color scheme, border, padding, and gap controls

## Flex grid

The Flex grid block arranges child blocks in a row or column with flexible alignment and spacing. Use it for side-by-side layouts, stacked sections, hero layouts, or any content that needs flexible widths and alignment.

### When to use Flex grid

- Create row or column layouts with configurable alignment
- Use horizontal direction for side-by-side content
- Use vertical direction for stacked content
- Control item widths with percentage-based or fill options

Flex grid only accepts [Flex item](../../content/blocks/layout/flex-grid/flex-item.md) blocks as direct children. Add your content (images, text, cards, etc.) inside Flex item blocks.

### Key settings

| Setting | Description | Default |
|---------|-------------|---------|
| Direction | Horizontal or Vertical | Horizontal |
| Horizontal alignment (row) | When direction is horizontal: Left, Center, Right, Between | Left |
| Vertical alignment (row) | When direction is horizontal: Start, Middle, End, Between, Stretch | Stretch |
| Vertical alignment (column) | When direction is vertical: Start, Middle, End, Between | Start |
| Horizontal alignment (column) | When direction is vertical: Left, Center, Right, Between, Stretch | Stretch |
| Enable block wrap | Allow flex items to wrap to the next line | On |
| Gap size | Spacing between flex items | Default (None, XS, SM, MD, LG, XL) |
| Top spacing / Bottom spacing | Padding at top and bottom | 0–300 px |
| Enable horizontal padding | Adds horizontal padding around the container | Off |

### Flex item

[Flex item](../../content/blocks/layout/flex-grid/flex-item.md) is the only block that can be added directly inside Flex grid. It supports:

- **Mobile width** — 5–100% (default: 80%). Visible when Enable width fill and Enable default width are off
- **Desktop width** — 5–100% (default: 40%). Same visibility condition
- **Enable width fill** — Makes the item grow to fill remaining space
- **Enable default width** — Uses automatic width based on content
- **Enable sticky layout** — Keeps the item visible while scrolling (Top or Bottom)
- **Vertical alignment** — Top, Middle, or Bottom
- Color scheme, border, padding, gap, and visibility controls

## Grid vs Flex comparison

| Use case | Default grid | Flex grid |
|----------|--------------|-----------|
| Product grids, image galleries | Yes | No (use Flex items with images or cards for custom layouts) |
| Equal-width columns | Yes (via row count) | Yes (via width fill or default width) |
| Unequal-width columns | Via column span on Grid item | Yes (via width %) |
| Row vs column direction | Fixed grid | Horizontal or vertical |
| Sticky content | No | Yes (Flex item) |
| Specialized blocks (products, articles, etc.) | Yes | No |
| Direct children | Grid item, specialized blocks, all theme blocks, app blocks | Flex item only |

## Common layouts

Step-by-step instructions for building common layouts will be added here.
