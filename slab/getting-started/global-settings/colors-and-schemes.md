# Colors

Slab color styling starts in **Theme settings > Colors**. Merchants pick a small set of global colors, then Slab generates additional color tokens (such as accents, shades, neutral, and plain) that sections and blocks can use through color scheme settings.



## How to change theme colors

{% stepper %}
{% step %}
### Configure base colors

* Open **Theme settings > Colors**.
* Select and edit your base colors such as Background, Foreground, Error, Success, Mobile bar, and Overlay background.
{% endstep %}

{% step %}
### Configure color schemes

* Open **Theme settings > Colors**.
* Under **Schemes**, edit **Scheme 1** and **Scheme 2** first.
* Click **Add Scheme** if you need more brand variations.
* For each scheme, set all six fields: background, foreground, border, hover background, hover foreground, and hover border.
{% endstep %}

{% step %}
### Apply colors to your sections and blocks

* Open the theme editor and select the block or section you'd like to edit
* Find the color settings and select **Base** or **Custom** for the **Type** option
* Selecting **Base** will show generated base colors such as Accents and Shades.&#x20;
* Selecting **Custom** will let you choose any color scheme
{% endstep %}
{% endstepper %}



### Generated color options

After you choose your global colors, Slab automatically creates extra color variations so sections and blocks stay visually consistent.

* **Accent 1/2/3:** Layered overlay tones used for depth and emphasis.
* **Shade 1/2/3:** Lighter or darker background steps for subtle contrast.
* **Main:** The main emphasis style for a component, based on the body foreground color.&#x20;
* **Plain:** A softer, low-emphasis surface based on the body background.
* If your body background is light, Slab creates darker overlays and shade tones.
* If your body background is dark, Slab creates lighter overlays and shade tones.



## Color settings



### Base

These settings define your store's base color system.

| Setting    | What it controls                                                                |
| ---------- | ------------------------------------------------------------------------------- |
| Background | Main storefront background and the base used for generated shade/overlay tones. |
| Foreground | Default text color and default border contrast for base surfaces.               |



### Schemes

In **Theme settings > Colors > Schemes**, you can edit **Scheme 1**, **Scheme 2**, and add as many additional schemes as needed.

Each scheme has the same six color fields:

| Setting          | How it is applied                                                     |
| ---------------- | --------------------------------------------------------------------- |
| Background       | Main background color for any section or block using that scheme.     |
| Foreground       | Text/icon color used on top of that scheme background.                |
| Border           | Default border color for elements using that scheme.                  |
| Hover background | Hover background for buttons and interactive elements in that scheme. |
| Hover foreground | Hover text/icon color for interactive elements in that scheme.        |
| Hover border     | Hover border color for interactive elements in that scheme.           |

Important: editing a scheme updates every section and block that uses that scheme.



### Utility

These settings control utility and supporting colors.

| Setting            | What it controls                               |
| ------------------ | ---------------------------------------------- |
| Error              | Error surfaces and error feedback color.       |
| Success            | Success surfaces and success feedback color.   |
| Mobile bar         | Browser UI color on supported mobile browsers. |
| Overlay background | Background shown behind overlays and popups.   |
