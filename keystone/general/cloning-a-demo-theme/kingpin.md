---
description: Kingpin demo files
---

# Kingpin

{% hint style="info" %}
💡 Tip: Duplicate your theme before making code changes. This will ensure you have a backup to revert to if needed.
{% endhint %}

If you want to get a head start on your theme design this guide will help you copy the existing layout and settings from our demo stores.

{% stepper %}
{% step %}
#### Open up theme editor

In Shopify select Online store then click **Edit code** for the theme you'd like update.
{% endstep %}

{% step %}
#### Duplicate theme

It's always a good idea to have a backup.
{% endstep %}

{% step %}
#### Copy changes

Copy the below files and replace your existing file.
{% endstep %}
{% endstepper %}

### Section files

<details>

<summary>sections/header-group.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "type": "header",
  "name": "Header group",
  "sections": {
    "theme_announcement": {
      "type": "theme__announcement",
      "blocks": {
        "announcement_z8GqMR": {
          "type": "announcement",
          "settings": {
            "content": "<p>Same Day Delivery</p>"
          }
        }
      },
      "block_order": [
        "announcement_z8GqMR"
      ],
      "custom_css": [],
      "settings": {
        "announcement_delay": 15,
        "color_scheme": "color__bg-secondary color__secondary",
        "layout_alignment": "center",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "theme_header": {
      "type": "theme__header",
      "blocks": {
        "button_XnBygi": {
          "type": "button",
          "settings": {
            "button_label": "Shop now",
            "button_url": "",
            "color_button": "btn"
          }
        }
      },
      "block_order": [
        "button_XnBygi"
      ],
      "custom_css": [],
      "settings": {
        "dropdown_links": "",
        "logo_default": "shopify://shop_images/keystoneparts.png",
        "logo_desktop_height": 26,
        "logo_mobile_height": 14,
        "enable_logo_on_desktop": false,
        "bar_default_color_scheme": "color__bg-body color__text",
        "bar_default_color_border": "color__border-divider-1",
        "bar_button_search_type": "desktop",
        "bar_button_cart_type": "text",
        "bar_button_login_type": "text",
        "bar_button_menu_type_desktop": "icon",
        "bar_button_menu_type_mobile": "icon",
        "bar_capitilization": "",
        "bar_font": "type__body",
        "bar_link_as_button": true,
        "enable_margin": true,
        "dropdown_color_scheme": "color__bg-body !color__text",
        "dropdown_color_border": "color__border-divider-1",
        "visibility": ""
      }
    }
  },
  "order": [
    "theme_announcement",
    "theme_header"
  ]
}
```

</details>

<details>

<summary>sections/footer-group.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "type": "footer",
  "name": "Footer group",
  "sections": {
    "liquid_qhQNCW": {
      "type": "liquid",
      "settings": {
        "liquid": "<script>\n  window.intercomSettings = {\n    api_base: \"https://api-iam.intercom.io\",\n    app_id: \"fnubgeik\",\n  };\n</script>\n\n\n<script>\n  // We pre-filled your app ID in the widget URL: 'https://widget.intercom.io/widget/fnubgeik'\n  (function(){var w=window;var ic=w.Intercom;if(typeof ic===\"function\"){ic('reattach_activator');ic('update',w.intercomSettings);}else{var d=document;var i=function(){i.c(arguments);};i.q=[];i.c=function(args){i.q.push(args);};w.Intercom=i;var l=function(){var s=d.createElement('script');s.type='text/javascript';s.async=true;s.src='https://widget.intercom.io/widget/fnubgeik';var x=d.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);};if(document.readyState==='complete'){l();}else if(w.attachEvent){w.attachEvent('onload',l);}else{w.addEventListener('load',l,false);}}})();\n</script>",
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "content_grid_R999P7": {
      "type": "content-grid",
      "blocks": {
        "content_B7ePAr": {
          "type": "content",
          "settings": {
            "heading": "Apply For An Account",
            "content": "<p>Become a member and receive wholesale pricing</p>",
            "button_label": "Apply Now",
            "url": "shopify://pages/apply-for-contractor-account",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 100,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__text",
            "color_border": "",
            "color_button": "btn--small btn--outline",
            "enable_gradient": false,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "content_LhnGTe": {
          "type": "content",
          "settings": {
            "heading": "Same Day Delivery",
            "content": "<p>Place your order before 11am for same day delivery</p>",
            "button_label": "Lean More",
            "url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 100,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__text",
            "color_border": "",
            "color_button": "btn--small btn--outline",
            "enable_gradient": false,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "content_8JEeTW": {
          "type": "content",
          "settings": {
            "heading": "Read Our Guides",
            "content": "<p>Learn more about our products and how to use them</p>",
            "button_label": "Guides",
            "url": "shopify://blogs/news",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 100,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__text",
            "color_border": "",
            "color_button": "btn--small btn--outline",
            "enable_gradient": false,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "content_QmyzQ6": {
          "type": "content",
          "settings": {
            "heading": "24/7 Support",
            "content": "<p>Our team is able to help you at anytime</p>",
            "button_label": "Contact Us",
            "url": "shopify://pages/contact",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 100,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__text",
            "color_border": "",
            "color_button": "btn--small btn--outline",
            "enable_gradient": false,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "content_B7ePAr",
        "content_LhnGTe",
        "content_8JEeTW",
        "content_QmyzQ6"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 50,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-shade-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--t-width",
        "layout_row_desktop": 4,
        "layout_row_mobile": 1,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "theme_footer": {
      "type": "theme__footer",
      "custom_css": [],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 0,
        "main_color_scheme": "color__bg-shade-1 color__text",
        "main_color_border": "!color__border-transparent",
        "main_color_button": "btn--small btn--secondary",
        "main_layout_x_alignment": "justify-start",
        "sub_color_scheme": "color__bg-shade-1 color__text",
        "sub_color_border": "!color__border-transparent",
        "sub_links": "footer",
        "sub_show_account_link": true,
        "sub_show_localization": true,
        "sub_show_payment_icons": true,
        "sub_enable_follow_on_shop": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "liquid_qhQNCW",
    "content_grid_R999P7",
    "theme_footer"
  ]
}
```

</details>

<details>

<summary>sections/overlay-group.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "type": "custom.overlay",
  "name": "Overlay group",
  "sections": {
    "theme_tooltip": {
      "type": "theme__tooltip",
      "blocks": {
        "71c48f59-2e6d-4190-8942-3924132a07ee": {
          "type": "newsletter",
          "settings": {
            "content": "<p>Tell customers why they should subscribe to your newsletter.</p>",
            "button_label": "Subscribe",
            "disclaimer": "",
            "success": "<p>Success! You've been subscribed.</p>"
          }
        }
      },
      "block_order": [
        "71c48f59-2e6d-4190-8942-3924132a07ee"
      ],
      "disabled": true,
      "settings": {
        "button_label": "Sign up",
        "button_icon": "",
        "color_button": "btn btn--secondary",
        "placement": "bottom-0 right-0",
        "visibility": ""
      }
    },
    "theme_scrollup": {
      "type": "theme__scroll-up",
      "settings": {
        "scroll_up_style": "text",
        "button_color": "btn btn--secondary",
        "visibility": "hidden md:block"
      }
    },
    "theme_age-verification": {
      "type": "theme__age-verification",
      "disabled": true,
      "settings": {
        "age_verification_style": "full_date",
        "age_limit": 1,
        "heading": "Verify your age",
        "content": "<p>Please confirm that you are over the age of 18 to proceed.</p>"
      }
    }
  },
  "order": [
    "theme_tooltip",
    "theme_scrollup",
    "theme_age-verification"
  ]
}
```

</details>

### Template files

<details>

<summary>templates/index.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "signup_CkHT9k": {
      "type": "signup",
      "blocks": {
        "content_zC9eY6": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "",
            "url": "",
            "image_background": "shopify://shop_images/pexels-koolshooters-8946878.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 700,
            "enable_padding": false,
            "color_scheme": "color__bg-shade-2 color__text",
            "color_text": "!color__text",
            "color_border": "",
            "color_button": "btn--small btn--plain",
            "enable_gradient": false,
            "layout_width_desktop": 9,
            "layout_width_mobile": 12,
            "layout_y_alignment": "justify-end",
            "layout_x_alignment": "justify",
            "text_position": "above"
          }
        },
        "form_JngpU9": {
          "type": "form",
          "settings": {
            "heading": "Wholesale Login",
            "content": "",
            "default_form": "login",
            "layout_width_desktop": 6,
            "layout_width_mobile": 12,
            "layout_x_alignment": ""
          }
        },
        "field_NPXRbN": {
          "type": "field",
          "settings": {
            "input_label": "Company Name",
            "input_placeholder": "Enter a company name",
            "input_type": "input",
            "enable_required_field": true
          }
        }
      },
      "block_order": [
        "content_zC9eY6",
        "form_JngpU9",
        "field_NPXRbN"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-shade-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--tertiary",
        "style_border": "",
        "layout_y_alignment": "items-start",
        "layout_x_alignment": "justify-start",
        "enable_margin": false,
        "visibility": ""
      }
    },
    "product_grid_FmKwVT": {
      "type": "product-grid",
      "settings": {
        "collection": "best-sellers",
        "products_count": 4,
        "heading": "Best Sellers",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 150,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_row_desktop": 4,
        "layout_row_mobile": 1,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "content_grid_rmM7gD": {
      "type": "content-grid",
      "blocks": {
        "content_KxV9jC": {
          "type": "content",
          "settings": {
            "heading": "Skin Care",
            "content": "",
            "button_label": "",
            "url": "shopify://collections/skincare",
            "image_background": "shopify://shop_images/pexels-koolshooters-8946947_1_f204f5b2-58a5-46b5-a97f-93764a4df752.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 440,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__light",
            "color_border": "outline--width color__outline-divider-1",
            "color_button": "btn--small btn--outline",
            "enable_gradient": true,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "content_bLpbd7": {
          "type": "content",
          "settings": {
            "heading": "Hair Care",
            "content": "",
            "button_label": "",
            "url": "shopify://collections/hair-care",
            "image_background": "shopify://shop_images/pexels-karolina-grabowska-5241037_1_1ab4a54f-541e-4c99-ad39-6615f2e19827.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 460,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__light",
            "color_border": "outline--width color__outline-divider-1",
            "color_button": "btn--small btn--outline",
            "enable_gradient": true,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "content_KxV9jC",
        "content_bLpbd7"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_row_desktop": 2,
        "layout_row_mobile": 1,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "signup_CkHT9k",
    "product_grid_FmKwVT",
    "content_grid_rmM7gD"
  ]
}
```

</details>

<details>

<summary>templates/collection.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "1639417635d5f561bb": {
      "type": "collection__banner",
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "image_source": "show_none",
        "image": "",
        "enable_autoplay": true,
        "enable_mute_toggle": true,
        "enable_loop": true,
        "spacing_top": 100,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn--small btn--tertiary",
        "style_border": "",
        "layout_width": 9,
        "layout_y_alignment": "items-start",
        "layout_x_alignment": "justify-start",
        "show_page_title": true,
        "show_page_description": true,
        "enable_margin": true,
        "visibility": ""
      }
    },
    "1637764550a7d7d2b3": {
      "type": "collection__main",
      "settings": {
        "spacing_top": 20,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "layout_row_desktop": 4,
        "layout_row_tablet": 3,
        "layout_row_mobile": 2,
        "enable_filter_sticky": true,
        "enable_filter_horizontal": true,
        "enable_filter_category_visible": false,
        "enable_filter_category_collapse": false,
        "enable_filter_count": true,
        "enable_filter_active": true,
        "enable_filter_button_uppercase": true,
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "1639417635d5f561bb",
    "1637764550a7d7d2b3"
  ]
}
```

</details>

<details>

<summary>templates/product.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "1638995507af787164": {
      "type": "product__main",
      "blocks": {
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5": {
          "type": "title",
          "settings": {
            "content": "",
            "spacing_top": 20,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right",
            "savings_badge": "none",
            "enable_badges": true,
            "enable_type": false,
            "enable_vendor": false,
            "enable_sku": false
          }
        },
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22": {
          "type": "price",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width",
            "position": "right"
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "btn--plain",
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width",
            "position": "right",
            "layout_x_alignment": "left",
            "enable_accordion": false,
            "enable_open": true
          }
        },
        "pickup_MN8xAw": {
          "type": "pickup",
          "settings": {
            "spacing_top": 10,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right"
          }
        },
        "table_YKc7BL": {
          "type": "table",
          "settings": {
            "spacing_top": 10,
            "spacing_bottom": 10,
            "color_border": "color__border-divider-1",
            "style_border": ""
          }
        }
      },
      "block_order": [
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5",
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22",
        "123fd04c-91f3-4248-a65a-614e2f64fdeb",
        "pickup_MN8xAw",
        "table_YKc7BL"
      ],
      "settings": {
        "enable_default_variant": true,
        "enable_default_plans": true,
        "enable_default_selling_plan_widget": true,
        "media_gallery_style": "slider",
        "media_slider_size_desktop": 100,
        "media_slider_size_mobile": 100,
        "media_gallery_position": "left",
        "enable_alt": true,
        "enable_variant_images": false,
        "enable_zoom": true,
        "zoom_level": "scale-[1.5]",
        "media_color_scheme": "color__bg-overlay-1 color__text",
        "media_border": "outline--width color__outline-divider-1",
        "media_ratio": "aspect-[1/1]",
        "media_object_sizing": "contain",
        "enable_ratio": true,
        "spacing_top": 10,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body",
        "layout_column_width": 40,
        "enable_margin": true
      }
    },
    "1649436653425ff0fe": {
      "type": "recommendations-slider",
      "settings": {
        "intent": "related",
        "products_count": 10,
        "heading": "You may also like",
        "content": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "style_size": "md:w-[25%] w-8/12",
        "card_width_mobile": 8,
        "card_width_desktop": 3,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "1649436645dda33170": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "card_width_mobile": 8,
        "card_width_desktop": 3,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "1638995507af787164",
    "1649436653425ff0fe",
    "1649436645dda33170"
  ]
}
```

</details>

<details>

<summary>templates/page.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "main": {
      "type": "page__main"
    }
  },
  "order": [
    "main"
  ]
}
```

</details>

<details>

<summary>templates/blog.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "1639002214a22c9d49": {
      "type": "banner",
      "blocks": {
        "16390022140b4cb49c-0": {
          "type": "heading",
          "settings": {
            "heading": "{{ blog.title }}",
            "heading_size": "type__h1"
          }
        }
      },
      "block_order": [
        "16390022140b4cb49c-0"
      ],
      "settings": {
        "spacing_top": 50,
        "spacing_bottom": 50,
        "layout_image_height": "",
        "default_image_ratio": "",
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "layout_width": 6,
        "layout_y_alignment": "items-start",
        "layout_x_alignment": "justify-start",
        "image_source": "none",
        "image": "",
        "enable_autoplay": true,
        "enable_mute_toggle": true,
        "enable_loop": true,
        "show_overlay": false,
        "color_text": "!color__text",
        "color_button": "btn",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "1639071353ef4d21a7": {
      "type": "blog__main",
      "settings": {
        "layout": "grid",
        "layout_row_desktop": 3,
        "layout_row_mobile": 1,
        "spacing_top": 50,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "1639002214a22c9d49",
    "1639071353ef4d21a7"
  ]
}
```

</details>

<details>

<summary>templates/article.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "1638993982c4b842f5": {
      "type": "article__banner",
      "settings": {
        "spacing_top": 100,
        "spacing_bottom": 50,
        "layout_image_height": 480,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "color_button": "btn",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "1638994039e866359e": {
      "type": "article__main",
      "blocks": {
        "16389940393df01a3b-0": {
          "type": "featured_image",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "enable_margin": false,
            "image_aspect_ratio": "aspect-[16/9]",
            "image_object_fit": "cover",
            "enable_image_caption": true
          }
        },
        "16389940393df01a3b-1": {
          "type": "title",
          "settings": {
            "blog_show_date": true,
            "blog_show_author": true,
            "spacing_top": 30,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "enable_margin": false
          }
        },
        "16389940393df01a3b-2": {
          "type": "share",
          "settings": {
            "share_label": "Share",
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "layout_x_alignment": "",
            "enable_margin": false,
            "share_facebook": true,
            "share_twitter": true,
            "share_pinterest": true
          }
        },
        "16389940393df01a3b-3": {
          "type": "content",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "enable_margin": false
          }
        },
        "next-previous": {
          "type": "next-previous",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "enable_margin": false
          }
        }
      },
      "block_order": [
        "16389940393df01a3b-0",
        "16389940393df01a3b-1",
        "16389940393df01a3b-2",
        "16389940393df01a3b-3",
        "next-previous"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "layout_width": 10,
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "1638993982c4b842f5",
    "1638994039e866359e"
  ]
}
```

</details>

<details>

<summary>templates/list-collections.json</summary>

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "1639071459d43b5c7c": {
      "type": "banner",
      "blocks": {
        "16390714595c4ccd8e-0": {
          "type": "heading",
          "settings": {
            "heading": "Collections",
            "heading_size": "type__h1"
          }
        }
      },
      "block_order": [
        "16390714595c4ccd8e-0"
      ],
      "settings": {
        "spacing_top": 50,
        "spacing_bottom": 50,
        "layout_image_height": 560,
        "default_image_ratio": "16/9",
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "layout_width": 6,
        "layout_y_alignment": "items-start",
        "layout_x_alignment": "justify-start",
        "image_source": "none",
        "image": "",
        "enable_autoplay": true,
        "enable_mute_toggle": true,
        "enable_loop": true,
        "show_overlay": false,
        "color_text": "!color__text",
        "color_button": "btn",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "163907145957ac0a6b": {
      "type": "list-collections__main",
      "settings": {
        "layout_row_desktop": 3,
        "layout_row_mobile": 1,
        "spacing_top": 50,
        "spacing_bottom": 100,
        "layout_sort": "alphabetical",
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "1639071459d43b5c7c",
    "163907145957ac0a6b"
  ]
}
```

</details>
