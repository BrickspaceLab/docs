---
description: Knit demo files
---

# Knit

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
            "content": "<p>Become a Member, Save 15% on Bulk Orders<\/p>"
          }
        }
      },
      "block_order": [
        "announcement_z8GqMR"
      ],
      "disabled": true,
      "custom_css": [

      ],
      "settings": {
        "announcement_delay": 0,
        "color_scheme": "color__bg-neutral color__text",
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
      "custom_css": [

      ],
      "settings": {
        "dropdown_links": "",
        "logo_default": "shopify:\/\/shop_images\/keystone.png",
        "logo_desktop_height": 26,
        "logo_mobile_height": 20,
        "enable_logo_on_desktop": false,
        "bar_default_color_scheme": "color__bg-body color__text",
        "bar_default_color_border": "color__border-divider-1",
        "bar_button_search_type": "desktop",
        "bar_button_cart_type": "icon",
        "bar_button_login_type": "icon",
        "bar_button_menu_type": "icon",
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
    "liquid_KiVA6c": {
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
    "theme_footer": {
      "type": "theme__footer",
      "blocks": {
        "content_HmMemC": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>Basics, Made in Canada</p>",
            "button_label": "",
            "button_url": "",
            "logo": "shopify://shop_images/keystone.png",
            "logo_desktop_height": 30,
            "logo_mobile_height": 20
          }
        },
        "menu_qQMxVQ": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "menu_TDUbCe": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "menu_RjKi3r": {
          "type": "menu",
          "settings": {
            "menu": "customer-assistance"
          }
        },
        "menu_A8h9q6": {
          "type": "menu",
          "settings": {
            "menu": "wholesale"
          }
        },
        "menu_TGUWBQ": {
          "type": "menu",
          "settings": {
            "menu": "about-us"
          }
        }
      },
      "block_order": [
        "content_HmMemC",
        "menu_qQMxVQ",
        "menu_TDUbCe",
        "menu_RjKi3r",
        "menu_A8h9q6",
        "menu_TGUWBQ"
      ],
      "custom_css": [

      ],
      "settings": {
        "spacing_top": 50,
        "spacing_bottom": 100,
        "main_color_scheme": "color__bg-body color__text",
        "main_color_border": "color__border-divider-1",
        "main_color_button": "btn--small btn--secondary",
        "main_layout_x_alignment": "justify-between",
        "sub_color_scheme": "color__bg-body color__text",
        "sub_color_border": "color__border-divider-1",
        "sub_links": "",
        "sub_show_account_link": true,
        "sub_show_localization": true,
        "sub_show_payment_icons": true,
        "sub_enable_follow_on_shop": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "liquid_KiVA6c",
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
        "form_dwTApN": {
          "type": "form",
          "settings": {}
        }
      },
      "block_order": [
        "form_dwTApN"
      ],
      "settings": {
        "button_label": "Have a question?",
        "button_icon": "",
        "color_button": "btn btn--secondary",
        "placement": "bottom-0 left-0",
        "visibility": ""
      }
    },
    "theme_scrollup": {
      "type": "theme__scroll-up",
      "disabled": true,
      "settings": {
        "scroll_up_style": "text",
        "button_color": "btn btn--tertiary",
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
    "slideshow_hyKHix": {
      "type": "slideshow",
      "blocks": {
        "content_mdMUbJ": {
          "type": "content",
          "settings": {
            "heading": "Comfort and Quality",
            "content": "<p>Breathable, lightweight and comfortable.</p>",
            "url": "",
            "image_background_desktop": "shopify://shop_images/pexels-shvetsa-4611660.jpg",
            "image_background_mobile": "shopify://shop_images/tees.png",
            "show_entire_image": false,
            "show_video_background_mobile": true,
            "button_label": "Shop All",
            "button_url": "shopify://collections/all",
            "color_button": "btn btn--secondary",
            "secondary_button_label": "",
            "secondary_button_url": "",
            "secondary_color_button": "btn btn--neutral",
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_text": "!color__light",
            "enable_gradient": true,
            "enable_background_overlay": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "justify-center text-center"
          }
        },
        "content_z7p4xg": {
          "type": "content",
          "settings": {
            "heading": "Ease of Movement",
            "content": "<p>The perfect lounge and exercise shorts</p>",
            "url": "",
            "image_background_desktop": "shopify://shop_images/ease_of_movement.png",
            "show_entire_image": false,
            "show_video_background_mobile": true,
            "button_label": "Shop Shorts",
            "button_url": "shopify://collections/shorts",
            "color_button": "btn btn--secondary",
            "secondary_button_label": "",
            "secondary_button_url": "",
            "secondary_color_button": "btn btn--neutral",
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__light",
            "enable_gradient": true,
            "enable_background_overlay": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "justify-center text-center"
          }
        },
        "content_tLCyqn": {
          "type": "content",
          "settings": {
            "heading": "Cozy Corner",
            "content": "<p>Cuddle up with our newest sweaters</p>",
            "url": "",
            "image_background_desktop": "shopify://shop_images/pexels-shvetsa-6283543_long.png",
            "show_entire_image": false,
            "show_video_background_mobile": true,
            "button_label": "Shop Turtle Necks",
            "button_url": "shopify://products/turtle-neck",
            "color_button": "btn",
            "secondary_button_label": "",
            "secondary_button_url": "",
            "secondary_color_button": "btn btn--neutral",
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_text": "!color__light",
            "enable_gradient": true,
            "enable_background_overlay": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "justify-center text-center"
          }
        }
      },
      "block_order": [
        "content_mdMUbJ",
        "content_z7p4xg",
        "content_tLCyqn"
      ],
      "custom_css": [
        "h1 {font-size: 40px; line-height: 1;}",
        "@media (min-width: 768px) {h1 {font-size: 70px; line-height: 1; }}"
      ],
      "settings": {
        "auto_scroll_delay": 0,
        "layout_y_spacing": "min-h-[450px] md:min-h-[550px]",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "enable_margin": true,
        "enable_border_margin": false,
        "enable_max_width": true,
        "visibility": ""
      }
    },
    "navigation_links_6yqBpp": {
      "type": "navigation-links",
      "blocks": {
        "link_QxDBiV": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/tankssss.png",
            "heading": "Tanks",
            "url": "shopify://collections/tanks"
          }
        },
        "link_ih96WP": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/tshirts.png",
            "heading": "T-Shirts",
            "url": "shopify://collections/t-shirts"
          }
        },
        "link_HrU33T": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/fwfa.png",
            "heading": "Sweaters",
            "url": "shopify://collections/sweater"
          }
        },
        "link_AQXMWz": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/dresspink.png",
            "heading": "Dresses",
            "url": "shopify://collections/dresses"
          }
        },
        "link_TFBPzX": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/shawts.png",
            "heading": "Shorts",
            "url": "shopify://collections/shorts"
          }
        },
        "link_TJ7TL3": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/puffer_jacke.png",
            "heading": "Jackets",
            "url": "shopify://collections/jackets"
          }
        },
        "link_JaybUG": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/dadcappurpe.png",
            "heading": "Hats",
            "url": "shopify://collections/hats"
          }
        },
        "link_PbPUXc": {
          "type": "link",
          "settings": {
            "image": "shopify://shop_images/acess.png",
            "heading": "Accessories",
            "url": "shopify://collections/accessories"
          }
        }
      },
      "block_order": [
        "link_QxDBiV",
        "link_ih96WP",
        "link_HrU33T",
        "link_AQXMWz",
        "link_TFBPzX",
        "link_TJ7TL3",
        "link_JaybUG",
        "link_PbPUXc"
      ],
      "settings": {
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-shade-1 color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "style_size": "100",
        "style_container": "grid",
        "layout_x_alignment": "justify-center items-start",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "featured_table_X9Ragq": {
      "type": "featured-table",
      "settings": {
        "product": "matte-water-bottle",
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": "",
        "show_details_button": false
      }
    },
    "product_grid_FmKwVT": {
      "type": "product-grid",
      "settings": {
        "collection": "best-sellers",
        "products_count": 10,
        "heading": "Best Sellers",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--tertiary",
        "style_border": "border--b-width",
        "layout_row_desktop": 5,
        "layout_row_mobile": 2,
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "collection_grid_NBUdtA": {
      "type": "collection-grid",
      "settings": {
        "collection": [
          "accessories",
          "dresses",
          "jackets",
          "shorts",
          "sweater",
          "tops"
        ],
        "heading": "Shop our Categories",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_row_desktop": 2,
        "layout_row_mobile": 1,
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "product_grid_gmp6Xa": {
      "type": "product-grid",
      "settings": {
        "collection": "accessories",
        "products_count": 5,
        "heading": "Accessories",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_row_desktop": 5,
        "layout_row_mobile": 1,
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "signup_RYiFDP": {
      "type": "signup",
      "blocks": {
        "form_hwPNp4": {
          "type": "form",
          "settings": {
            "heading": "Become a Member",
            "content": "<p>Save 15% on bulk orders when you become a member</p>",
            "default_form": "signup",
            "layout_width_desktop": 6,
            "layout_width_mobile": 12,
            "layout_x_alignment": ""
          }
        },
        "content_f4yeGw": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "",
            "url": "",
            "image_background": "shopify://shop_images/pexels-polina-tankilevitch-6739059.jpg",
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
            "layout_width_desktop": 6,
            "layout_width_mobile": 12,
            "layout_y_alignment": "justify-start",
            "layout_x_alignment": "left",
            "text_position": "above"
          }
        }
      },
      "block_order": [
        "form_hwPNp4",
        "content_f4yeGw"
      ],
      "settings": {
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_y_alignment": "items-start",
        "layout_x_alignment": "justify-center",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "article_grid_awjHBU": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 4,
        "heading": "Our Blog",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_row_desktop": 2,
        "layout_row_mobile": 1,
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "store_locator_VmiMYL": {
      "type": "store-locator",
      "blocks": {
        "store_dAcRTR": {
          "type": "store",
          "settings": {
            "store_name": "Toronto",
            "store_details": "<p><strong>100 Queen St. W. Toronto, ON M5H 2N2<br/>416-921-4718</strong></p><p>M: 8-5<br/>T: 8-5<br/>W: 8-5<br/>T: 8-5<br/>F: 8-4<br/>S: 11-2<br/>S: Closed</p><p></p>",
            "latitude": "43.651070",
            "longitude": "-79.347015"
          }
        },
        "store_hfNrzT": {
          "type": "store",
          "settings": {
            "store_name": "Halifax",
            "store_details": "<p><strong>841 Argyle St, Halifax, NS B3J 3A5<br/>719-391-3917</strong></p><p>M: 8-5<br/>T: 8-5<br/>W: 8-5<br/>T: 8-5<br/>F: 8-4<br/>S: 11-2<br/>S: Closed</p>",
            "latitude": "44.6490",
            "longitude": "-63.5754"
          }
        },
        "store_rBMiWm": {
          "type": "store",
          "settings": {
            "store_name": "Vancouver",
            "store_details": "<p><strong>453 W 12th Ave, Vancouver, BC V5Y 1V4<br/>827-193-1836</strong></p><p>M: 8-5<br/>T: 8-5<br/>W: 8-5<br/>T: 8-5<br/>F: 8-4<br/>S: 11-2<br/>S: Closed</p>",
            "latitude": "49.2608",
            "longitude": "-123.1140"
          }
        }
      },
      "block_order": [
        "store_dAcRTR",
        "store_hfNrzT",
        "store_rBMiWm"
      ],
      "settings": {
        "enable_dynamic_map": true,
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "map_style": "mapbox://styles/mapbox/light-v11",
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "accordions_DeLW8x": {
      "type": "accordions",
      "blocks": {
        "content_L4ynUA": {
          "type": "content",
          "settings": {
            "heading": "Do I have to be a member to purchase?",
            "content": "<p>No, however we do have bulk discounts for wholesale customers</p>",
            "icon": "",
            "color_scheme": "minimal",
            "enable_open": true
          }
        },
        "content_gBTKE8": {
          "type": "content",
          "settings": {
            "heading": "Where do you ship from?",
            "content": "<p>We have two warehouses located on the east and west coast of Canada</p>",
            "icon": "",
            "color_scheme": "minimal",
            "enable_open": false
          }
        },
        "content_RPzJtL": {
          "type": "content",
          "settings": {
            "heading": "Do you have an order minimum?",
            "content": "<p>No order minimums are required for shipping</p>",
            "icon": "",
            "color_scheme": "minimal",
            "enable_open": false
          }
        }
      },
      "block_order": [
        "content_L4ynUA",
        "content_gBTKE8",
        "content_RPzJtL"
      ],
      "settings": {
        "heading": "FAQS",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "heading_font": "type__body type--base",
        "style_border": "border--b-width",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "newsletter_eLb8FF": {
      "type": "newsletter",
      "settings": {
        "heading": "Newsletter",
        "content": "<p>Subscribe to our newsletter and we'll send you exclusive content about new product launches and offers.</p>",
        "disclaimer": "<p>We won't spam you and we'll never sell your data.</p>",
        "success": "<p>Success! You've been subscribed to our newsletter. </p>",
        "subscribe_label": "Subscribe",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "slideshow_hyKHix",
    "navigation_links_6yqBpp",
    "featured_table_X9Ragq",
    "product_grid_FmKwVT",
    "collection_grid_NBUdtA",
    "product_grid_gmp6Xa",
    "signup_RYiFDP",
    "article_grid_awjHBU",
    "store_locator_VmiMYL",
    "accordions_DeLW8x",
    "newsletter_eLb8FF"
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
    "banner": {
      "type": "collection__banner",
      "settings": {
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "border--b-width",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "enable_margin": true,
        "enable_max_width": true,
        "visibility": "",
        "enable_description": true,
        "enable_image": false
      }
    },
    "grid": {
      "type": "collection__main",
      "settings": {
        "spacing_top": 30,
        "spacing_bottom": 30,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "layout_row_desktop": 4,
        "layout_row_mobile": 2,
        "filter_placement": "side",
        "layout_type": "grid",
        "enable_expand_filters": true,
        "enable_layout_toggle": true,
        "enable_margin": true,
        "enable_sort": true,
        "enable_filter": true,
        "products_per_page": 10
      }
    }
  },
  "order": [
    "banner",
    "grid"
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
            "content": "<p>Made in Canada</p>",
            "spacing_top": 20,
            "spacing_bottom": 0,
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
            "spacing_bottom": 0,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right"
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "spacing_top": 5,
            "spacing_bottom": 5,
            "color_scheme": "btn--plain",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right",
            "layout_x_alignment": "left",
            "enable_accordion": false,
            "enable_open": true
          }
        },
        "options_aR9LwQ": {
          "type": "options",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right"
          }
        },
        "add_NtYMdg": {
          "type": "add",
          "settings": {
            "content": "",
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-transparent",
            "color_border": "color__border-divider-1",
            "color_button": "btn",
            "style_border": "",
            "position": "right",
            "enable_quantity": false,
            "enable_dynamic_checkout": false,
            "enable_gift_card_recipient": false
          }
        },
        "pickup_MN8xAw": {
          "type": "pickup",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 20,
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
        "options_aR9LwQ",
        "add_NtYMdg",
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
        "media_color_scheme": "color__bg-body color__text",
        "media_border": "outline--width color__outline-divider-1",
        "media_ratio": "aspect-[1/1]",
        "media_object_sizing": "cover",
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
        "style_border": "",
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
      "type": "page__main",
      "settings": {
      }
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
    "banner_9R7hhk": {
      "type": "banner",
      "blocks": {
        "heading_Bb4XW8": {
          "type": "heading",
          "settings": {
            "content": "{{ blog.title }}"
          }
        }
      },
      "block_order": [
        "heading_Bb4XW8"
      ],
      "settings": {
        "url": "shopify://collections/all",
        "show_image": false,
        "show_entire_image": false,
        "show_video_background_mobile": true,
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "border--b-width",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_margin": true,
        "enable_border_margin": false,
        "enable_max_width": true,
        "visibility": ""
      }
    },
    "main": {
      "type": "blog__main",
      "settings": {
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "layout_row_desktop": 2,
        "layout_row_mobile": 1,
        "enable_margin": true,
        "items_per_page": 6,
        "visibility": ""
      }
    }
  },
  "order": [
    "banner_9R7hhk",
    "main"
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
    "article_banner_48nKa3": {
      "type": "article__banner",
      "settings": {
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-body color__text",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_margin": true,
        "enable_max_width": true,
        "visibility": "",
        "enable_author": true,
        "enable_date": true,
        "enable_tags": false,
        "enable_image": false
      }
    },
    "content_grid_qxE9Ym": {
      "type": "content-grid",
      "blocks": {
        "content_nVDTGP": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p><\/p><p>{{ article.title }}<\/p>",
            "button_label": "",
            "url": "",
            "image_background": "{{ article.image }}",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_minimum_height": 500,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "",
            "color_text": "color__light",
            "color_button": "btn--small btn--outline",
            "enable_gradient": true,
            "layout_y_alignment": "justify-end",
            "layout_x_alignment": "left",
            "text_position": "below",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "content_nVDTGP"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body",
        "color_text": "",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_row_desktop": 1,
        "layout_row_mobile": 1,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "main": {
      "type": "article__main",
      "blocks": {
        "6d44e560-358d-4232-8708-502806610136": {
          "type": "breadcrumb",
          "settings": {
            "spacing_top": 50,
            "spacing_bottom": 10,
            "color_border": "color__border-divider-1",
            "style_border": "",
            "layout_x_alignment": "text-left"
          }
        },
        "table_pj9eVt": {
          "type": "table",
          "settings": {
            "spacing_top": 50,
            "spacing_bottom": 10,
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "right"
          }
        },
        "f7c49961-aaf7-41df-8711-43d3d5753948": {
          "type": "article",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 50,
            "color_border": "color__border-divider-1",
            "style_border": "",
            "layout_x_alignment": "justify-start"
          }
        },
        "797ba560-2717-42ee-a1dc-547f7f40f214": {
          "type": "share",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 50,
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width",
            "layout_x_alignment": "justify-start",
            "position": "left"
          }
        },
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2": {
          "type": "comment",
          "settings": {
            "spacing_top": 50,
            "spacing_bottom": 50,
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width",
            "layout_x_alignment": "justify-start",
            "position": "left"
          }
        },
        "recent_articles_GWGD9F": {
          "type": "recent_articles",
          "settings": {
            "articles_count": 2,
            "spacing_top": 50,
            "spacing_bottom": 50,
            "layout_row_desktop": 2,
            "layout_row_mobile": 1,
            "position": "left"
          }
        }
      },
      "block_order": [
        "6d44e560-358d-4232-8708-502806610136",
        "table_pj9eVt",
        "f7c49961-aaf7-41df-8711-43d3d5753948",
        "797ba560-2717-42ee-a1dc-547f7f40f214",
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2",
        "recent_articles_GWGD9F"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_text": "",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": true,
        "visibility": ""
      }
    }
  },
  "order": [
    "article_banner_48nKa3",
    "content_grid_qxE9Ym",
    "main"
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
    "165583830739141e89": {
      "type": "banner",
      "blocks": {
        "82dc43ff-a8dd-484c-a794-1064d07c5d26": {
          "type": "heading",
          "settings": {
            "content": "Collections"
          }
        }
      },
      "block_order": [
        "82dc43ff-a8dd-484c-a794-1064d07c5d26"
      ],
      "settings": {
        "url": "",
        "show_image": false,
        "show_entire_image": false,
        "show_video_background_mobile": true,
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-body color__text",
        "color_text": "",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "border--b-width",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_margin": true,
        "enable_border_margin": false,
        "enable_max_width": true,
        "visibility": ""
      }
    },
    "main": {
      "type": "list-collections__main",
      "settings": {
        "spacing_top": 30,
        "spacing_bottom": 30,
        "color_scheme": "color__bg-body",
        "color_text": "",
        "layout_row_desktop": 2,
        "layout_row_mobile": 1,
        "enable_margin": true,
        "items_per_page": 12
      }
    }
  },
  "order": [
    "165583830739141e89",
    "main"
  ]
} 
```

</details>

