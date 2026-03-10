# Sibling products

Paper supports two methods to display products as swatch options. This is helpful if you want to split one product into seperate listing but maintain visibility for each option. When this is setup customers will see sibling products as options so they can easily select different options or colors.&#x20;



### Using the Combined listing app <a href="#h_2bcf225838" id="h_2bcf225838"></a>

The app can be used to link multiple product together. Visit the Shopify help center to [learn more about this feature](https://www.shopify.com/enterprise/blog/combined-listings?utm_campaign=winter24edition\&utm_channel=W24-editions-website\&utm_content=W24E\&utm_medium=W24E-page\&utm_source=editions).



### Using the Linked products block <a href="#h_cca672d346" id="h_cca672d346"></a>

If you have multiple versions of one product split into different product listing it may be hard for customers to find the option they want. Using the “Linked products” block you can display additional products as options on your product page.

<div align="left"><figure><img src="https://downloads.intercomcdn.com/i/o/1199113876/d52e9df88e7df4162b8d1a2a/CleanShot+2024-09-30+at+16_38_29%402x.png?expires=1744682400&#x26;signature=77329ecf2a86c61fe8b5aa4a8c3ee774ca76885856f5adea859b17cd9de91d47&#x26;req=dSEuH8h%2FnolYX%2FMW1HO4zbKV%2FaqpEaFXxYnS4Ar%2FPaaCkex3r0CyKkqc2esv%0AFKm0Q3gjxu03JLwRdz0%3D%0A" alt=""><figcaption></figcaption></figure></div>

{% stepper %}
{% step %}
**Enable the product block**

1. Go ton Online Store > Themes > Customize
2. Navigate to the product template then click "Add block" within the "Product" section
3. Move the block and add a label
   1. It's usually best to display the "Linked products" block above the "Buy buttons"
   2. Try adding a label that describes the additional linked products. If the additional products are variants of different color you could update the label to "Color".
4. Hit **Save**
{% endstep %}

{% step %}
**Create metafield definition**

1. Navigate to **Settings** > **Custom** **data** > **Products**
2. Click **Add definition**
3. In the name field type “Linked collection"
4. Ensure the namespace and key field is `custom.linked_collection`
5. Set the data type as "Collection"
6. Hit **Save**
{% endstep %}

{% step %}
**Update metafield**

1. Navigate to the product you’d like to update
2. Scroll to the bottom and select a collection for the metafield
3. Click **Save**
{% endstep %}
{% endstepper %}
