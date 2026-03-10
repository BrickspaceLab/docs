# Fixed buy buttons

The Fixed Buy Buttons feature adds a sticky add-to-cart bar that stays visible on product pages, making it easy for customers to purchase even when they've scrolled away from the main product form. This helps reduce friction and can improve conversion rates, especially on mobile devices.

## How to setup

***

{% stepper %}
{% step %}
**Navigate to Product Template**

1. Go to **Online Store** > **Themes** > **Customize**
2. Open any product template (e.g., Default Product)
3. Click on the product section
{% endstep %}

{% step %}
**Add the Block**

1. Click **Add block** within the Product section
2. Select **Fixed buy buttons** from the block list

{% hint style="info" %}
Only one fixed buy button block can be added per product page.
{% endhint %}
{% endstep %}

{% step %}
**Configure Settings**

The block will automatically appear at the bottom of your screen when customers scroll down the page. Configure the settings to match your store's design and needs.
{% endstep %}

{% step %}
Hit **Save**
{% endstep %}
{% endstepper %}

## Key features

***

### Smart visibility

* **Show after scrolling**: Enable this option to make the bar appear only after customers scroll past the main add-to-cart button
* Automatically hides when the main product form is in view to avoid redundancy

### Positioning options

Choose from 4 position options to match your design:

* **Left**: Fixed card on bottom-left (desktop), full-width bar (mobile)
* **Right**: Fixed card on bottom-right (desktop), full-width bar (mobile)
* **Center**: Centered bar constrained to content width
* **Full Width**: Spans entire viewport width (most prominent option)

### Variant selection

* For products with variants: Shows a dropdown selector displaying the currently selected variant
* Clicking the variant selector scrolls back to the main options area
* Shows contextual button states:
  * "Choose options" when no variant is selected
  * "Sold out" when selected variant is unavailable
  * "Unavailable" when variant doesn't exist
  * "Add to cart" when ready to purchase

### Custom content

* Add optional rich text content (e.g., product title, promotional messages)
* Example: "Free shipping on orders over $50" or "Lifetime warranty included"
* Content appears on desktop only to save mobile screen space

### Full customization

**Color Schemes:**

* 12 color scheme options including body, neutral, accent colors, and transparent

**Button Styles:**

* 9 button style options: Primary, Secondary, Tertiary, Neutral, Plain, Outline, Inverted Outline, Link styles

**Border Options:**

* Subtle border, strong border, or no border

**Button Text:**

* Supports custom button text via product metafields (`custom.button_text`)

### Responsive design

* **Mobile**: Full-width bar at bottom of screen
* **Desktop**: Positioned card with rounded corners and shadow (except "Full" position)
* Maximum width of 500px for left/right positions on desktop

### Loading states

* Animated loading spinner during cart submission
* Visual feedback prevents duplicate submissions

## Best practices

***

{% hint style="success" %}
**Enable "Show after scrolling"** for a cleaner experience that doesn't distract from the main product content
{% endhint %}

{% hint style="success" %}
**Use "Full" position** for maximum visibility and conversions on mobile
{% endhint %}

{% hint style="success" %}
**Use "Left" or "Right" positions** for a more subtle, premium feel on desktop
{% endhint %}

{% hint style="success" %}
**Add promotional text** in the content field to reinforce value propositions (e.g., "Free returns", "2-year warranty")
{% endhint %}

{% hint style="success" %}
**Match button style** to your primary CTA buttons for brand consistency
{% endhint %}

{% hint style="success" %}
**Test on mobile devices** to ensure the bar doesn't obstruct important content
{% endhint %}

## Common use cases

***

* **Long product descriptions**: Keep the buy button accessible when customers scroll through detailed specs
* **High-converting products**: Ensure the CTA is always visible for your best sellers
* **Mobile optimization**: Reduce scrolling friction on mobile devices
* **Promotional campaigns**: Highlight limited-time offers or free shipping thresholds

## Technical notes

***

Works seamlessly with products that have:

* Single variants
* Multiple variants
* Selling plans/subscriptions
* Custom button text metafields

Automatically integrates with your cart system (no additional configuration needed).
