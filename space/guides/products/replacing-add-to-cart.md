# Replacing “Add to cart”

The “Add to cart” text can be customized for each product using metafields. This is useful if you want to change the wording for specific products. For example, you could use this to display “Pre-order” for one product.

{% stepper %}
{% step %}
#### Create metafield definition <a href="#h_18d27d70b1" id="h_18d27d70b1"></a>

1. Navigate to **Settings** > **Custom** **data** > **Products**
2. Click **Add definition**
3. In the name field type “**Button text**”
4. Ensure the namespace and key field is `custom.button_text`
{% endstep %}

{% step %}
#### Update metafield <a href="#h_da3430396b" id="h_da3430396b"></a>

1. Navigate to the product you’d like to update
2. Scroll to the bottom and enter in text for the “Button text” metafield
3. Click **Save**
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Metafields can also be updated using the bulk editor
{% endhint %}
