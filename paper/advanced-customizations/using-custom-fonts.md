# Using custom fonts

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](/broken/pages/Fyss7M7PkIKyON7bVWSI).
{% endhint %}

We rely on [Shopify's Font Picker](https://www.shopify.ca/partners/blog/font-picker) to provide a font selection for your store. To access these settings go to Theme settings > Typography. Installing a font not available in the default selection will involve making some code customizations.



## Installing a custom font

{% stepper %}
{% step %}
**Prepare your font files**

{% hint style="info" %}
Please ensure you have a valid license to use the font you are trying to install
{% endhint %}

* Download your font in webfont file types such as `.woff2` or `.woff`
* If you don't have a webfont version of your font, you can use a generator to convert it. Font Squirrel has [a tool you can use](https://www.fontsquirrel.com/tools/webfont-generator) for this.
{% endstep %}

{% step %}
**Upload font files**

* Open your Shopify admin and navigate to **Content > Files**.
* Upload each file for your font.
{% endstep %}

{% step %}
**Edit theme code**

* Open up the theme editor and select `theme__styles.liquid` from within the snippets folder
*   Add the below code after the `{% style %}` tag. Be sure to replace `MY_FONT` with your font name and ensure the URLs are correctly linking to your uploaded font.

    <pre class="language-css" data-title="theme__styles.liquid"><code class="lang-css">@font-face { 
      font-family: "MY_FONT"; 
      src: url('{{ "MY_FONT.woff2" | file_url }}') format("woff2"),  
        url('{{ "MY_FONT.woff" | file_url }}') format("woff"); 
    }
    </code></pre>



*   From here you can include your font by updating the below code inside the same file. The variables `--type-font-body-family` , `--type-font-header-family` and `--type-font-nav-family` control the font family used for body, headings and navigation text.

    <pre class="language-css" data-title="theme__styles.liquid"><code class="lang-css">--type-font-body-family: {{ settings.type_font_body.family }}, {{ settings.type_font_body.fallback_families }};
    --type-font-body-style: {{ settings.type_font_body.style }}; 
    --type-font-body-weight: {{ settings.type_font_body.weight }}; 
    --type-font-header-family: {{ settings.type_font_heading.family }}, {{ settings.type_font_heading.fallback_families }};
    --type-font-header-style: {{ settings.type_font_heading.style }}; --type-font-header-weight: {{ settings.type_font_heading.weight }}; 
    --type-font-nav-family: {{ settings.type_font_nav.family }}, {{ settings.type_font_nav.fallback_families }};
    </code></pre>



*   The updated code should look something like this

    <pre class="language-css" data-title="theme__styles.liquid"><code class="lang-css">--type-font-body-family: 'MY_FONT';
    --type-font-body-style: {{ settings.type_font_body.style }};
    --type-font-body-weight: {{ settings.type_font_body.weight }}; 
    --type-font-header-family: 'MY_FONT'; 
    --type-font-header-style: {{ settings.type_font_heading.style }}; --type-font-header-weight: {{ settings.type_font_heading.weight }}; 
    --type-font-nav-family: 'MY_FONT';
    </code></pre>
{% endstep %}
{% endstepper %}
