---
description: Kettle demo files
---

# Kettle

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
            "content": "<p>Your Cafe One Stop Shop</p>"
          }
        }
      },
      "block_order": [
        "announcement_z8GqMR"
      ],
      "custom_css": [],
      "settings": {
        "announcement_delay": 0,
        "color_scheme": "color__bg-tertiary color__tertiary",
        "layout_alignment": "left",
        "enable_margin": true,
        "visibility": ""
      }
    },
    "theme_header": {
      "type": "theme__header",
      "custom_css": [],
      "settings": {
        "dropdown_links": "main-menu",
        "logo_default": "shopify://shop_images/keystone_1.png",
        "logo_desktop_height": 50,
        "logo_mobile_height": 20,
        "enable_logo_on_desktop": true,
        "bar_default_color_scheme": "color__bg-secondary color__secondary",
        "bar_default_color_border": "color__border-divider-1",
        "bar_button_search_type": "always",
        "bar_button_cart_type": "icon",
        "bar_button_login_type": "icon",
        "bar_button_menu_type_desktop": "none",
        "bar_button_menu_type_mobile": "icon",
        "bar_capitilization": "",
        "bar_font": "type__body",
        "bar_link_as_button": true,
        "enable_margin": true,
        "dropdown_color_scheme": "color__bg-neutral !color__text",
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
{
  "type": "footer",
  "name": "Footer group",
  "sections": {
    "theme_footer": {
      "type": "theme__footer",
      "blocks": {
        "newsletter_3tHc8z": {
          "type": "newsletter",
          "settings": {
            "heading": "Newsletter",
            "content": "",
            "button": "Subscribe",
            "disclaimer": "",
            "success": "<p>Success! You've been subscribed.</p>"
          }
        },
        "menu_4kpwpK": {
          "type": "menu",
          "settings": {
            "menu": "footer"
          }
        },
        "menu_xEP7aW": {
          "type": "menu",
          "settings": {
            "menu": "footer-2"
          }
        },
        "menu_RjKi3r": {
          "type": "menu",
          "settings": {
            "menu": "footer-3"
          }
        },
        "menu_A8h9q6": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "content_9CcQHh": {
          "type": "content",
          "disabled": true,
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "",
            "button_url": "",
            "logo": "shopify://shop_images/cuppa.png",
            "logo_desktop_height": 70,
            "logo_mobile_height": 50
          }
        }
      },
      "block_order": [
        "newsletter_3tHc8z",
        "menu_4kpwpK",
        "menu_xEP7aW",
        "menu_RjKi3r",
        "menu_A8h9q6",
        "content_9CcQHh"
      ],
      "custom_css": [],
      "settings": {
        "spacing_top": 150,
        "spacing_bottom": 100,
        "main_color_scheme": "color__bg-secondary color__secondary",
        "main_color_border": "color__border-divider-1",
        "main_color_button": "btn--small btn--tertiary",
        "main_layout_x_alignment": "justify-between",
        "sub_color_scheme": "color__bg-secondary color__secondary",
        "sub_color_border": "color__border-divider-1",
        "sub_links": "",
        "sub_show_account_link": false,
        "sub_show_localization": false,
        "sub_show_payment_icons": true,
        "sub_enable_follow_on_shop": false,
        "visibility": ""
      }
    }
  },
  "order": [
    "theme_footer"
  ]
}
```

</details>

<details>

<summary>sections/overlay-group.json</summary>

```json
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
            "content": "<p>Sign up and save 10%</p>",
            "button_label": "Subscribe",
            "disclaimer": "",
            "success": "<p>Success! You've been subscribed.</p>"
          }
        }
      },
      "block_order": [
        "71c48f59-2e6d-4190-8942-3924132a07ee"
      ],
      "settings": {
        "button_label": "Save 10%",
        "button_icon": "bell",
        "color_button": "btn",
        "placement": "bottom-0 left-0",
        "visibility": ""
      }
    },
    "theme_scrollup": {
      "type": "theme__scroll-up",
      "disabled": true,
      "settings": {
        "scroll_up_style": "text",
        "button_color": "btn btn--plain",
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
{
  "sections": {
    "banner_PqnEwq": {
      "type": "banner",
      "blocks": {
        "content_qFhqrQ": {
          "type": "content",
          "settings": {
            "content": "<p>★★★★★ Over 10000+ 5 star reviews</p>"
          }
        },
        "heading_K4cPPH": {
          "type": "heading",
          "settings": {
            "content": "Your favorite barista's favorite coffee supplier"
          }
        }
      },
      "block_order": [
        "content_qFhqrQ",
        "heading_K4cPPH"
      ],
      "settings": {
        "url": "",
        "show_image": false,
        "show_entire_image": false,
        "show_video_background_mobile": false,
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "color_scheme": "color__bg-secondary color__secondary",
        "color_text": "color__dark",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_margin": true,
        "enable_border_margin": false,
        "enable_max_width": true,
        "visibility": ""
      }
    },
    "marquee_jLHmD7": {
      "type": "marquee",
      "blocks": {
        "content_fRWqk8": {
          "type": "content",
          "settings": {
            "content": "<p>One-Stop Cafe Shop</p>",
            "layout_x_alignment": "text-center"
          }
        },
        "content_wVGXTe": {
          "type": "content",
          "settings": {
            "content": "<p>Worldwide Flavours</p>",
            "layout_x_alignment": "text-center"
          }
        },
        "content_EWUr4j": {
          "type": "content",
          "settings": {
            "content": "<p>Roasted in Canada</p>",
            "layout_x_alignment": "text-center"
          }
        },
        "content_eWVFMm": {
          "type": "content",
          "settings": {
            "content": "<p>Compostable Supplies</p>",
            "layout_x_alignment": "text-center"
          }
        }
      },
      "block_order": [
        "content_fRWqk8",
        "content_wVGXTe",
        "content_EWUr4j",
        "content_eWVFMm"
      ],
      "settings": {
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-tertiary color__tertiary",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": false,
        "use_reverse_animation": false,
        "animation_speed": 190,
        "visibility": ""
      }
    },
    "product_table_cryWpb": {
      "type": "product-table",
      "settings": {
        "collection": "coffee",
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 50,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-selected-1",
        "color_button": "btn btn--neutral",
        "style_border": "",
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": "",
        "show_details_button": true,
        "show_variant_table": true
      }
    },
    "hotspot_HfDtfJ": {
      "type": "hotspot",
      "blocks": {
        "link_PNTbch": {
          "type": "link",
          "settings": {
            "title": "Coffee",
            "url": "shopify://collections/coffee",
            "layout_y_alignment": 32,
            "layout_x_alignment": 58
          }
        },
        "link_K7YMPA": {
          "type": "link",
          "settings": {
            "title": "Coffee Makers",
            "url": "shopify://collections/coffee-makers",
            "layout_y_alignment": 79,
            "layout_x_alignment": 25
          }
        },
        "link_mc9WFe": {
          "type": "link",
          "settings": {
            "title": "Kettles",
            "url": "shopify://collections/kettles",
            "layout_y_alignment": 65,
            "layout_x_alignment": 29
          }
        },
        "link_ppbYBp": {
          "type": "link",
          "settings": {
            "title": "Drinkware",
            "url": "shopify://collections/drinkware",
            "layout_y_alignment": 79,
            "layout_x_alignment": 58
          }
        }
      },
      "block_order": [
        "link_PNTbch",
        "link_K7YMPA",
        "link_mc9WFe",
        "link_ppbYBp"
      ],
      "settings": {
        "image_background_desktop": "shopify://shop_images/kewl_053ecfe5-b2fe-4606-8946-cbc62caf9756.png",
        "show_entire_image": false,
        "layout_y_spacing": "min-h-[450px] md:min-h-[550px]",
        "color_scheme": "color__bg-overlay-3 color__text",
        "color_text": "",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_margin": true,
        "enable_max_width": true,
        "visibility": ""
      }
    },
    "product_grid_FmKwVT": {
      "type": "product-grid",
      "settings": {
        "collection": "tea",
        "products_count": 10,
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 50,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_row_desktop": 5,
        "layout_row_mobile": 1,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    },
    "collection_grid_ehAAXh": {
      "type": "collection-grid",
      "settings": {
        "collection": [
          "barista-tools",
          "cafe-tools",
          "coffee",
          "coffee-makers",
          "kettles",
          "sauce",
          "syrups",
          "tea",
          "drinkware",
          "grinders"
        ],
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 50,
        "spacing_bottom": 50,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_row_desktop": 5,
        "layout_row_mobile": 2,
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": false,
        "visibility": ""
      }
    }
  }
}
```

</details>

<details>

<summary>templates/collection.json</summary>

```json
{
  "sections": {
    "banner": {
      "type": "collection__banner",
      "settings": {
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-tertiary color__tertiary",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "",
        "layout_y_alignment": "items-center",
        "layout_x_alignment": "justify-start",
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
        "spacing_top": 20,
        "spacing_bottom": 20,
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
        "show_details_button": false,
        "show_variant_table": true,
        "products_per_page": 12
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

<summary>templates/list-collections.json</summary>

```json
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

<details>

<summary>templates/product.json</summary>

```json
{
  "sections": {
    "1638995507af787164": {
      "type": "product__main",
      "blocks": {
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5": {
          "type": "title",
          "settings": {
            "content": "<p>✔ 100% satisfaction guarantee</p><p>✔ Made locally in Canada</p>",
            "spacing_top": 20,
            "spacing_bottom": 20,
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
            "style_border": "border--b-width",
            "position": "right",
            "enable_quantity": false,
            "enable_dynamic_checkout": true,
            "enable_gift_card_recipient": false
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "btn--plain",
            "color_border": "color__border-divider-1",
            "style_border": "",
            "position": "left",
            "layout_x_alignment": "left",
            "enable_accordion": false,
            "enable_open": true
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
        "options_aR9LwQ",
        "add_NtYMdg",
        "123fd04c-91f3-4248-a65a-614e2f64fdeb",
        "pickup_MN8xAw",
        "table_YKc7BL"
      ],
      "settings": {
        "enable_default_variant": true,
        "enable_default_plans": true,
        "enable_default_selling_plan_widget": true,
        "media_gallery_style": "slider",
        "media_slider_size_desktop": 70,
        "media_slider_size_mobile": 80,
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
    "165592515341576314": {
      "type": "accordions",
      "blocks": {
        "165592515344a810fb-0": {
          "type": "content",
          "settings": {
            "heading": "Do you offer free shipping?",
            "content": "<p>Free shipping will automatically be applied to all domestic orders over $250. Simply add over $250 to your cart and you will see the discount while checking out.</p>",
            "icon": "",
            "color_scheme": "minimal",
            "enable_open": true
          }
        },
        "content_yTp6eq": {
          "type": "content",
          "settings": {
            "heading": "Do you sell directly to customers?",
            "content": "<p>No, we only ship wholesale orders.</p>",
            "icon": "",
            "color_scheme": "minimal",
            "enable_open": false
          }
        }
      },
      "block_order": [
        "165592515344a810fb-0",
        "content_yTp6eq"
      ],
      "settings": {
        "heading": "FAQs",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 200,
        "spacing_bottom": 200,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "heading_font": "type__body type--base",
        "style_border": "border--b-width border--t-width",
        "layout_x_alignment": "justify-between",
        "enable_margin": true,
        "enable_split": true,
        "visibility": ""
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
    "165592515341576314",
    "1649436653425ff0fe",
    "1649436645dda33170"
  ]
}
```

</details>

<details>

<summary>templates/page.json</summary>

```json
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
        "style_border": "",
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
