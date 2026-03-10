---
description: Kaleidoscope demo files
---

# Kaleidoscope

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
            "content": "<p>Make announcements or share a promotion.</p>"
          }
        }
      },
      "block_order": [
        "announcement_z8GqMR"
      ],
      "disabled": true,
      "custom_css": [],
      "settings": {
        "announcement_delay": 15,
        "color_scheme": "color__bg-tertiary color__tertiary",
        "layout_alignment": "center",
        "enable_margin": true,
        "visibility": ""
      }
    }
  }
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
        "menu_RjKi3r": {
          "type": "menu",
          "settings": {
            "menu": "footer"
          }
        },
        "menu_A8h9q6": {
          "type": "menu",
          "settings": {
            "menu": "footer-menu-2"
          }
        },
        "menu_beJm9E": {
          "type": "menu",
          "settings": {
            "menu": "account"
          }
        },
        "menu_C9maBx": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "menu_EgxNVF": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "menu_4tpM7t": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "content_zz6r94": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>Net 60 Payments</p><h6>Buy now, pay later</h6><p></p><p>24/7 Support</p><h6>Order with confidence</h6><h6></h6><p>Free Shipping</p><h6>On domestic orders</h6><p></p><p>Easy Re-Order</p><h6>Save time and money</h6>",
            "button_label": "",
            "button_url": "",
            "logo_desktop_height": 30,
            "logo_mobile_height": 20
          }
        }
      },
      "block_order": [
        "menu_RjKi3r",
        "menu_A8h9q6",
        "menu_beJm9E",
        "menu_C9maBx",
        "menu_EgxNVF",
        "menu_4tpM7t",
        "content_zz6r94"
      ]
    }
  }
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
  }
}
```

</details>

### Template files

<details>

<summary>templates/index.json</summary>

```json
{
  "sections": {
    "banner_alternative_dzQqhb": {
      "type": "banner-alternative",
      "blocks": {
        "content_EnhnNY": {
          "type": "content",
          "settings": {
            "heading": "Keep competitive with the premium wholesale home goods resource",
            "content": "",
            "url": "",
            "show_entire_image": false,
            "show_video_background_mobile": true,
            "button_label": "Sign Up",
            "button_url": "https://shopify.com/92083781912/account?locale=en",
            "color_button": "btn",
            "secondary_button_label": "",
            "secondary_button_url": "",
            "secondary_color_button": "btn",
            "color_scheme": "color__bg-secondary color__secondary",
            "color_text": "",
            "enable_gradient": false,
            "enable_background_overlay": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "justify-start"
          }
        },
        "content_pwTqaQ": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "url": "",
            "image_background_desktop": "shopify://shop_images/pexels-ron-lach-10117817.jpg",
            "show_entire_image": false,
            "show_video_background_mobile": true,
            "button_label": "",
            "button_url": "",
            "color_button": "btn",
            "secondary_button_label": "",
            "secondary_button_url": "",
            "secondary_color_button": "btn btn--neutral",
            "color_scheme": "color__bg-overlay-3 color__text",
            "color_text": "",
            "enable_gradient": false,
            "enable_background_overlay": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "justify-start"
          }
        }
      },
      "block_order": [
        "content_EnhnNY",
        "content_pwTqaQ"
      ],
      "settings": {
        "layout_y_spacing": "min-h-[250px] md:min-h-[350px]",
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "enable_margin": true,
        "enable_max_width": true,
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
        "color_scheme": "color__bg-body color__text",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "enable_background_overlay": false,
        "style_border": "border--b-width",
        "layout_y_alignment": "items-end",
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
        "enable_expand_filters": false,
        "enable_layout_toggle": true,
        "enable_margin": true,
        "enable_sort": true,
        "enable_filter": true,
        "show_details_button": false,
        "show_variant_table": true,
        "products_per_page": 20
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
    "main": {
      "type": "product__main",
      "blocks": {
        "title": {
          "type": "title",
          "settings": {}
        },
        "price": {
          "type": "price",
          "settings": {}
        },
        "description": {
          "type": "description",
          "settings": {}
        },
        "options": {
          "type": "options",
          "settings": {}
        },
        "add": {
          "type": "add",
          "settings": {}
        }
      },
      "block_order": [
        "title",
        "price",
        "description",
        "options",
        "add"
      ],
      "settings": {
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "enable_margin": true,
        "visibility": ""
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
        },
        "content_kUNtpA": {
          "type": "content",
          "settings": {
            "content": ""
          }
        }
      },
      "block_order": [
        "heading_Bb4XW8",
        "content_kUNtpA"
      ],
      "settings": {
        "url": "",
        "show_image": false,
        "show_entire_image": false,
        "show_video_background_mobile": true,
        "layout_y_spacing": "min-h-[100px] md:min-h-[150px]",
        "color_scheme": "color__bg-body color__text",
        "color_text": "color__text",
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
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "style_border": "",
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
    }
  }
}
```

</details>
