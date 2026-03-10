---
description: >-
  Copy and paste the contents from the below files into your theme to duplicate
  the theme.
---

# Pastel

## Theme Configuration Files

<details>

<summary><strong>sections/header-group.json</strong></summary>

```json
{
  "type": "header",
  "name": "Header group",
  "sections": {
    "theme_announcement": {
      "type": "theme__announcement",
      "blocks": {
        "f2232503-8685-46db-aaf1-b796c5ea14f9": {
          "type": "text",
          "settings": {
            "content": "<p>Get free <a href=\"\/\" title=\"\/\">shipping<\/a> on all orders over $50 <\/p>"
          }
        },
        "493bfb93-68fd-473f-bc87-57abeae993ce": {
          "type": "text",
          "settings": {
            "content": "<p>We donate $1 from every purchase<\/p>"
          }
        }
      },
      "block_order": [
        "f2232503-8685-46db-aaf1-b796c5ea14f9",
        "493bfb93-68fd-473f-bc87-57abeae993ce"
      ],
      "settings": {
        "color_scheme": "color__bg-neutral color__text",
        "layout_alignment": "left",
        "visibility": "",
        "show_account_link": true
      }
    },
    "theme_header": {
      "type": "theme__header",
      "blocks": {
        "e561cffb-e23b-4a10-8382-4959a1b99bf2": {
          "type": "Content",
          "settings": {
            "menu": "trending",
            "url": "shopify:\/\/collections\/bestsellers",
            "heading": "Bestsellers",
            "content": "",
            "image": "shopify:\/\/shop_images\/Group_13.png"
          }
        },
        "0f91aafe-7946-4571-bcf4-fde2cd2d2073": {
          "type": "Content",
          "settings": {
            "menu": "tone",
            "url": "shopify:\/\/collections\/portrait",
            "heading": "Perfect Portraits",
            "content": "",
            "image": "shopify:\/\/shop_images\/Frame_8_fb094ac1-6c08-44cb-83c0-e079ef89dd72.png"
          }
        }
      },
      "block_order": [
        "e561cffb-e23b-4a10-8382-4959a1b99bf2",
        "0f91aafe-7946-4571-bcf4-fde2cd2d2073"
      ],
      "settings": {
        "dropdown_links": "main-menu",
        "search_links": "",
        "logo_light": "shopify:\/\/shop_images\/paper.png",
        "logo_desktop_height": 25,
        "logo_mobile_height": 20,
        "bar_color_scheme": "color__bg-body color__text",
        "bar_color_border": "color__border-divider-1",
        "bar_layout_desktop": "left-inline",
        "bar_button_cart_type": "icon",
        "bar_button_search_type": "icon",
        "bar_button_login_type": "none",
        "bar_button_menu_type": "icon",
        "enable_search": false,
        "dropdown_color_scheme": "color__bg-body color__text",
        "dropdown_color_border": "color__border-divider-1",
        "search_color_scheme": "color__bg-body color__text",
        "search_color_border": "!color__border-transparent",
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

<summary><strong>sections/footer-group.json</strong></summary>

```json
{
  "type": "footer",
  "name": "Footer group",
  "sections": {
    "theme_footer": {
      "type": "theme__footer",
      "blocks": {
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321": {
          "type": "newsletter",
          "settings": {
            "heading": "Save 10%",
            "content": "<p>Keep up to date on new launches and  save 10%<\/p>",
            "button": "Sign up",
            "disclaimer": "",
            "success": "<p>Thanks for subscribing<\/p>"
          }
        },
        "42816038-4f81-4035-b672-7356ee99aa30": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "35777b7a-9356-4cac-87c2-7e9d9c3fb65b": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "150805eb-9862-49dd-b0c2-0111162d6fce": {
          "type": "menu",
          "settings": {
            "menu": "footer"
          }
        },
        "6ad6b950-210d-4cf8-b231-62c67db4980e": {
          "type": "menu",
          "settings": {
            "menu": "footer-menu-2"
          }
        }
      },
      "block_order": [
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321",
        "42816038-4f81-4035-b672-7356ee99aa30",
        "35777b7a-9356-4cac-87c2-7e9d9c3fb65b",
        "150805eb-9862-49dd-b0c2-0111162d6fce",
        "6ad6b950-210d-4cf8-b231-62c67db4980e"
      ],
      "settings": {
        "main_color_scheme": "color__bg-overlay-1 color__text",
        "main_color_border": "color__border-divider-1",
        "main_color_button": "btn btn--secondary",
        "sub_color_scheme": "color__bg-overlay-1 color__text",
        "sub_color_border": "color__border-divider-1",
        "sub_color_button": "btn btn--secondary",
        "sub_links": "subfooter",
        "sub_enable_payment_icons": true,
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

<summary><strong>sections/overlay-group.json</strong></summary>

```json
{
  "type": "custom.overlay",
  "name": "Overlay group",
  "sections": {
    "theme_scrollup": {
      "type": "theme__scrollup",
      "settings": {
        "scroll_up_style": "text",
        "button_color": "btn btn--secondary",
        "enable_back_to_top": true
      }
    },
    "theme_age-verification": {
      "type": "theme__age-verification",
      "settings": {
        "enable_age_verification": false,
        "age_verification_style": "full_date",
        "age_limit": 18,
        "heading": "Verify your age",
        "content": "<p>Please confirm that you are over the age of 18 to proceed.<\/p>"
      }
    }
  },
  "order": [
    "theme_scrollup",
    "theme_age-verification"
  ]
}
```

</details>

<details>

<summary><strong>templates/index.json</strong></summary>

```json
{
  "sections": {
    "1655754078b117ff84": {
      "type": "banner",
      "blocks": {
        "e058d283-e8cf-412f-be81-1928168a3702": {
          "type": "heading",
          "settings": {
            "content": "Bring Your Home to Life With Stunning Art"
          }
        },
        "8fa83b17-954f-4497-9154-f1d0b7b9902d": {
          "type": "buttons",
          "settings": {
            "button_color": "btn",
            "button_label": "Shop Summer",
            "button_url": "shopify:\/\/collections\/all",
            "secondary_button_color": "btn btn--neutral",
            "secondary_button_label": "Learn more",
            "secondary_button_url": "shopify:\/\/pages\/about"
          }
        },
        "094a4e0a-43ef-4079-b95b-3ea8595faf92": {
          "type": "content",
          "settings": {
            "content": "<p>★★★★★ Over 1000+ 5 star reviews<\/p>"
          }
        }
      },
      "block_order": [
        "e058d283-e8cf-412f-be81-1928168a3702",
        "8fa83b17-954f-4497-9154-f1d0b7b9902d",
        "094a4e0a-43ef-4079-b95b-3ea8595faf92"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_10_2.png",
        "image_background_mobile": "shopify:\/\/shop_images\/templegardens_9467a049-6725-4125-ba94-fa407c22de05.png",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[650px] max-h-[85vh] md:min-h-[80vh]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "visibility": ""
      }
    },
    "1ef1d73d-faf8-4792-aed8-77d37b4b0041": {
      "type": "icon-grid",
      "blocks": {
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-0": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/box.png",
            "icon_height": "h-8",
            "heading": "Free shipping",
            "content": "<p>Spend over $50 to recieve free shipping on all orders. <a href=\"\/\" title=\"\/\">Learn more<\/a><\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-1": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/badge.png",
            "icon_height": "h-8",
            "heading": "Art for all",
            "content": "<p>For every purchase, we donate $2 to a local art program.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-2": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/leaf.png",
            "icon_height": "h-8",
            "heading": "Carbon neutral",
            "content": "<p>We offset all of our carbon emissions, from the factory to the delivery truck.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-0",
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-1",
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "165582633503d90b9c": {
      "type": "content-grid",
      "blocks": {
        "16558263356d045fa0-0": {
          "type": "content",
          "settings": {
            "heading": "Portrait",
            "content": "<p>Perfect for vertical spaces<\/p>",
            "button_label": "Shop portrait",
            "button_url": "shopify:\/\/collections\/portrait",
            "image_featured": "shopify:\/\/shop_images\/portrait.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "16558263356d045fa0-1": {
          "type": "content",
          "settings": {
            "heading": "Landscape",
            "content": "<p>The best use of space above a couch or bed<\/p>",
            "button_label": "Shop landscape",
            "button_url": "shopify:\/\/collections\/landscape",
            "image_featured": "shopify:\/\/shop_images\/landscape2_e951c571-1268-4f9a-8bc2-b99e2d3b0cda.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "16558263356d045fa0-2": {
          "type": "content",
          "settings": {
            "heading": "Square",
            "content": "<p>Great for a geometiric gallery wall<\/p>",
            "button_label": "Shop square",
            "button_url": "shopify:\/\/collections\/square",
            "image_featured": "shopify:\/\/shop_images\/square.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        }
      },
      "block_order": [
        "16558263356d045fa0-0",
        "16558263356d045fa0-1",
        "16558263356d045fa0-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "165643793121f4937c": {
      "type": "product-grid",
      "settings": {
        "collection": "bestsellers",
        "products_count": 8,
        "heading": "Bestsellers",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "145b431c-42e9-4c42-b16c-b2298604c0a0": {
      "type": "collection-slider",
      "blocks": {
        "template--16113693065415__145b431c-42e9-4c42-b16c-b2298604c0a0-167053155112f2f9a0-0": {
          "type": "collection",
          "settings": {
            "collection": "abstract"
          }
        },
        "4ce42a94-56c3-4ed3-9392-2bd7a756cea9": {
          "type": "collection",
          "settings": {
            "collection": "flowers"
          }
        },
        "1438767c-97bc-45e0-b43f-3a3f98a879d1": {
          "type": "collection",
          "settings": {
            "collection": "fruit"
          }
        },
        "b0a851cb-7144-48f1-a83a-5dd5866f677f": {
          "type": "collection",
          "settings": {
            "collection": "mountains"
          }
        },
        "1784e3e4-acab-4efa-9f1f-4e60029a6129": {
          "type": "collection",
          "settings": {
            "collection": "trees"
          }
        },
        "7a3822e8-2167-4c1c-8880-1de83e0fd814": {
          "type": "collection",
          "settings": {
            "collection": "water"
          }
        }
      },
      "block_order": [
        "template--16113693065415__145b431c-42e9-4c42-b16c-b2298604c0a0-167053155112f2f9a0-0",
        "4ce42a94-56c3-4ed3-9392-2bd7a756cea9",
        "1438767c-97bc-45e0-b43f-3a3f98a879d1",
        "b0a851cb-7144-48f1-a83a-5dd5866f677f",
        "1784e3e4-acab-4efa-9f1f-4e60029a6129",
        "7a3822e8-2167-4c1c-8880-1de83e0fd814"
      ],
      "settings": {
        "heading": "Shop by subject",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "justify-between",
        "visibility": "",
        "enable_collection_size_count": false
      }
    },
    "165600667888cb4e6d": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 3,
        "heading": "Our blog",
        "content": "<p>Read more from our founder and the team behind our award winning products<\/p>",
        "button_label": "More blog posts",
        "button_url": "shopify:\/\/blogs\/news",
        "enable_author": true,
        "enable_summary": true,
        "enable_date": false,
        "enable_tags": false,
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "f43f1aab-5408-4ae1-b17a-c026ccf63e02": {
      "type": "logo-list",
      "blocks": {
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-0": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/housee.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-1": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/splash_911897a6-2dd0-41af-9c42-4d56865b3678.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-2": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/interiors_canada.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-3": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/apartment_life_394422c1-10ca-4691-9ef8-8ab146edaf8d.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-0",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-1",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-2",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-3"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    }
  },
  "order": [
    "1655754078b117ff84",
    "1ef1d73d-faf8-4792-aed8-77d37b4b0041",
    "165582633503d90b9c",
    "165643793121f4937c",
    "145b431c-42e9-4c42-b16c-b2298604c0a0",
    "165600667888cb4e6d",
    "f43f1aab-5408-4ae1-b17a-c026ccf63e02"
  ]
}
```

</details>

<details>

<summary><strong>templates/collection.json</strong></summary>

```json
{
  "sections": {
    "1655754078b117ff84": {
      "type": "banner",
      "blocks": {
        "e058d283-e8cf-412f-be81-1928168a3702": {
          "type": "heading",
          "settings": {
            "content": "Bring Your Home to Life With Stunning Art"
          }
        },
        "8fa83b17-954f-4497-9154-f1d0b7b9902d": {
          "type": "buttons",
          "settings": {
            "button_color": "btn",
            "button_label": "Shop Summer",
            "button_url": "shopify:\/\/collections\/all",
            "secondary_button_color": "btn btn--neutral",
            "secondary_button_label": "Learn more",
            "secondary_button_url": "shopify:\/\/pages\/about"
          }
        },
        "094a4e0a-43ef-4079-b95b-3ea8595faf92": {
          "type": "content",
          "settings": {
            "content": "<p>★★★★★ Over 1000+ 5 star reviews<\/p>"
          }
        }
      },
      "block_order": [
        "e058d283-e8cf-412f-be81-1928168a3702",
        "8fa83b17-954f-4497-9154-f1d0b7b9902d",
        "094a4e0a-43ef-4079-b95b-3ea8595faf92"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_10_2.png",
        "image_background_mobile": "shopify:\/\/shop_images\/templegardens_9467a049-6725-4125-ba94-fa407c22de05.png",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[650px] max-h-[85vh] md:min-h-[80vh]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "visibility": ""
      }
    },
    "1ef1d73d-faf8-4792-aed8-77d37b4b0041": {
      "type": "icon-grid",
      "blocks": {
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-0": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/box.png",
            "icon_height": "h-8",
            "heading": "Free shipping",
            "content": "<p>Spend over $50 to recieve free shipping on all orders. <a href=\"\/\" title=\"\/\">Learn more<\/a><\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-1": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/badge.png",
            "icon_height": "h-8",
            "heading": "Art for all",
            "content": "<p>For every purchase, we donate $2 to a local art program.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-2": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/leaf.png",
            "icon_height": "h-8",
            "heading": "Carbon neutral",
            "content": "<p>We offset all of our carbon emissions, from the factory to the delivery truck.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-0",
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-1",
        "template--16133769691335__1ef1d73d-faf8-4792-aed8-77d37b4b0041-1672853062b6aaccb5-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "165582633503d90b9c": {
      "type": "content-grid",
      "blocks": {
        "16558263356d045fa0-0": {
          "type": "content",
          "settings": {
            "heading": "Portrait",
            "content": "<p>Perfect for vertical spaces<\/p>",
            "button_label": "Shop portrait",
            "button_url": "shopify:\/\/collections\/portrait",
            "image_featured": "shopify:\/\/shop_images\/portrait.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "16558263356d045fa0-1": {
          "type": "content",
          "settings": {
            "heading": "Landscape",
            "content": "<p>The best use of space above a couch or bed<\/p>",
            "button_label": "Shop landscape",
            "button_url": "shopify:\/\/collections\/landscape",
            "image_featured": "shopify:\/\/shop_images\/landscape2_e951c571-1268-4f9a-8bc2-b99e2d3b0cda.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "16558263356d045fa0-2": {
          "type": "content",
          "settings": {
            "heading": "Square",
            "content": "<p>Great for a geometiric gallery wall<\/p>",
            "button_label": "Shop square",
            "button_url": "shopify:\/\/collections\/square",
            "image_featured": "shopify:\/\/shop_images\/square.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        }
      },
      "block_order": [
        "16558263356d045fa0-0",
        "16558263356d045fa0-1",
        "16558263356d045fa0-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "165643793121f4937c": {
      "type": "product-grid",
      "settings": {
        "collection": "bestsellers",
        "products_count": 8,
        "heading": "Bestsellers",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "145b431c-42e9-4c42-b16c-b2298604c0a0": {
      "type": "collection-slider",
      "blocks": {
        "template--16113693065415__145b431c-42e9-4c42-b16c-b2298604c0a0-167053155112f2f9a0-0": {
          "type": "collection",
          "settings": {
            "collection": "abstract"
          }
        },
        "4ce42a94-56c3-4ed3-9392-2bd7a756cea9": {
          "type": "collection",
          "settings": {
            "collection": "flowers"
          }
        },
        "1438767c-97bc-45e0-b43f-3a3f98a879d1": {
          "type": "collection",
          "settings": {
            "collection": "fruit"
          }
        },
        "b0a851cb-7144-48f1-a83a-5dd5866f677f": {
          "type": "collection",
          "settings": {
            "collection": "mountains"
          }
        },
        "1784e3e4-acab-4efa-9f1f-4e60029a6129": {
          "type": "collection",
          "settings": {
            "collection": "trees"
          }
        },
        "7a3822e8-2167-4c1c-8880-1de83e0fd814": {
          "type": "collection",
          "settings": {
            "collection": "water"
          }
        }
      },
      "block_order": [
        "template--16113693065415__145b431c-42e9-4c42-b16c-b2298604c0a0-167053155112f2f9a0-0",
        "4ce42a94-56c3-4ed3-9392-2bd7a756cea9",
        "1438767c-97bc-45e0-b43f-3a3f98a879d1",
        "b0a851cb-7144-48f1-a83a-5dd5866f677f",
        "1784e3e4-acab-4efa-9f1f-4e60029a6129",
        "7a3822e8-2167-4c1c-8880-1de83e0fd814"
      ],
      "settings": {
        "heading": "Shop by subject",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "justify-between",
        "visibility": "",
        "enable_collection_size_count": false
      }
    },
    "165600667888cb4e6d": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 3,
        "heading": "Our blog",
        "content": "<p>Read more from our founder and the team behind our award winning products<\/p>",
        "button_label": "More blog posts",
        "button_url": "shopify:\/\/blogs\/news",
        "enable_author": true,
        "enable_summary": true,
        "enable_date": false,
        "enable_tags": false,
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "f43f1aab-5408-4ae1-b17a-c026ccf63e02": {
      "type": "logo-list",
      "blocks": {
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-0": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/housee.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-1": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/splash_911897a6-2dd0-41af-9c42-4d56865b3678.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-2": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/interiors_canada.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-3": {
          "type": "logo",
          "settings": {
            "logo": "shopify:\/\/shop_images\/apartment_life_394422c1-10ca-4691-9ef8-8ab146edaf8d.png",
            "logo_height": "max-h-[64px]",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "!color__border-transparent",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        }
      },
      "block_order": [
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-0",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-1",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-2",
        "template--16133769691335__f43f1aab-5408-4ae1-b17a-c026ccf63e02-16729402970e3eb2e3-3"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    }
  },
  "order": [
    "1655754078b117ff84",
    "1ef1d73d-faf8-4792-aed8-77d37b4b0041",
    "165582633503d90b9c",
    "165643793121f4937c",
    "145b431c-42e9-4c42-b16c-b2298604c0a0",
    "165600667888cb4e6d",
    "f43f1aab-5408-4ae1-b17a-c026ccf63e02"
  ]
}
```

</details>

<details>

<summary><strong>templates/list-collections.json</strong></summary>

```json
{
  "sections": {
    "165583830739141e89": {
      "type": "banner",
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_11.png",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[250px] md:min-h-[300px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "visibility": ""
      }
    },
    "main": {
      "type": "list-collections__main",
      "blocks": {
        "2c8aad49-b136-4f65-935a-7368b8cc5bb3": {
          "type": "newsletter",
          "settings": {
            "heading": "Block heading",
            "content": "<p>Keep up to date on new launches and save 10%<\/p>",
            "button_label": "Get 10% off",
            "disclaimer": "",
            "success": "<p>You have been succesfully subscribed.<\/p>",
            "index": 6,
            "background_color_scheme": "color__bg-neutral color__text",
            "column_size": "col-span-2"
          }
        }
      },
      "block_order": [
        "2c8aad49-b136-4f65-935a-7368b8cc5bb3"
      ],
      "settings": {
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "enable_collection_size_count": true,
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

<summary><strong>templates/product.json</strong></summary>

```json
{
  "sections": {
    "1638995507af787164": {
      "type": "product__main",
      "blocks": {
        "bef9bd40-2a8e-45c2-ae54-59c9ef6f0e26": {
          "type": "breadcrumb",
          "settings": {
            "spacing_top": 10,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5": {
          "type": "title",
          "settings": {
            "content": "",
            "spacing_top": 20,
            "spacing_bottom": 5,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_thumbnails_product_type": false,
            "enable_thumbnails_vendor": false,
            "enable_sku": false
          }
        },
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22": {
          "type": "price",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "a6a19617-9e36-4efe-94e9-a750d0c775de": {
          "type": "options",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "style_border": ""
          }
        },
        "b78b560b-e1c2-428d-ad73-fb5f8aac6d53": {
          "type": "add",
          "settings": {
            "content": "<p>Free shipping over $50 · Easy returns <\/p>",
            "spacing_top": 20,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_quantity": false,
            "enable_dynamic_checkout": false,
            "enable_gift_card_recipient": false
          }
        },
        "3c821cec-15b4-40fa-bd51-0072523601e3": {
          "type": "popup",
          "settings": {
            "option": "",
            "title": "Need Help?",
            "page": "need-help",
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "enable_open": false
          }
        },
        "1af8dc66-c25a-46e1-8c34-7d902b4ab936": {
          "type": "accordion",
          "settings": {
            "title": "Shipping and returns",
            "content": "<p>We have a no-hassle shipping and return policy. All items are shipped the next day.<\/p><p>If you want to make a return just use the enclosed return label and you'll receive a store credit. <\/p>",
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_open": false
          }
        },
        "285b75fe-59d8-47bf-a70f-ff9e3d5f8ebe": {
          "type": "upsell",
          "settings": {
            "title": "You may also like",
            "products_count": 2,
            "intent": "related",
            "color_scheme": "color__bg-overlay-1 color__text",
            "style_border": "",
            "enable_open": true
          }
        },
        "848f5aea-f7ad-4974-a5fb-020776e3e523": {
          "type": "stickyadd",
          "settings": {
            "content": "<p>Free shipping over $50 · Easy returns<\/p>",
            "color_scheme": "color__bg-overlay-1 color__text",
            "on_scroll": true
          }
        }
      },
      "block_order": [
        "bef9bd40-2a8e-45c2-ae54-59c9ef6f0e26",
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5",
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22",
        "a6a19617-9e36-4efe-94e9-a750d0c775de",
        "b78b560b-e1c2-428d-ad73-fb5f8aac6d53",
        "3c821cec-15b4-40fa-bd51-0072523601e3",
        "123fd04c-91f3-4248-a65a-614e2f64fdeb",
        "1af8dc66-c25a-46e1-8c34-7d902b4ab936",
        "285b75fe-59d8-47bf-a70f-ff9e3d5f8ebe",
        "848f5aea-f7ad-4974-a5fb-020776e3e523"
      ],
      "settings": {
        "enable_default_variant": true,
        "spacing_top": 0,
        "spacing_bottom": 0,
        "media_gallery_style": "slider",
        "image_border": "!color__border-transparent",
        "enable_zoom": true,
        "enable_alt": true,
        "enable_variant_images": false,
        "media_color_scheme": "color__bg-overlay-1 color__text",
        "media_ratio": "aspect-[2\/3] aspect-w-2 aspect-h-3",
        "media_object-sizing": "cover",
        "enable_ratio": true,
        "show_product_badges": true,
        "color_scheme": "color__bg-body color__text",
        "color_border": "!color__border-transparent",
        "layout_gallery_size": "w-full md:w-2\/3"
      }
    },
    "f07b2ee0-f9bb-4fdd-a9b3-e4242646430d": {
      "type": "testimonials",
      "blocks": {
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-2": {
          "type": "testimonial",
          "settings": {
            "content": "<p>I am extremely satisfied with my purchase and would highly recommend this art print to anyone looking to add some visual interest to their home. The quality of the paper and the overall aesthetic of the print are top-notch.<\/p>",
            "title": "<p>Sarah D.<\/p>",
            "avatar": "shopify:\/\/shop_images\/lorem-face-5198_9efe2d86-5556-464f-9bee-f6aa1746dd12.jpg"
          }
        },
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-1": {
          "type": "testimonial",
          "settings": {
            "content": "<p>I really appreciate the fact that the art print looks just as good in my living room as it does online. It's not always easy to gauge how a piece of art will look in your home, but this one exceeded my expectations.<\/p>",
            "title": "<p>Ryder G.<\/p>",
            "avatar": "shopify:\/\/shop_images\/lorem-face-2274.jpg"
          }
        },
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-0": {
          "type": "testimonial",
          "settings": {
            "content": "<p>I am extremely impressed with the quality of the paper it is printed on. The colors are vibrant and the resolution is crystal clear, making the image pop off the page.<\/p>",
            "title": "<p>Trey R.<\/p>",
            "avatar": "shopify:\/\/shop_images\/lorem-face-6270.jpg"
          }
        }
      },
      "block_order": [
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-2",
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-1",
        "template--16113693229255__f07b2ee0-f9bb-4fdd-a9b3-e4242646430d-16705324589c0602ea-0"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--t-width",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "16663285032715217b": {
      "type": "apps",
      "blocks": {
        "7fa87443-1d33-4f71-9df3-eea1030b8925": {
          "type": "shopify:\/\/apps\/product-reviews\/blocks\/reviews\/bae150af-8da8-48b2-9867-398188115e5f",
          "settings": {
          }
        }
      },
      "block_order": [
        "7fa87443-1d33-4f71-9df3-eea1030b8925"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "layout_padding": true
      }
    },
    "165592515341576314": {
      "type": "accordions",
      "blocks": {
        "165592515344a810fb-0": {
          "type": "content",
          "settings": {
            "title": "How do I get free shipping?",
            "content": "<p>Free shipping will automatically be applied to all domestic orders over $75. Simplfy add over $75 to your cart and you will see the discount while checking out.<\/p>"
          }
        },
        "165592515344a810fb-1": {
          "type": "content",
          "settings": {
            "title": "How much is shipping?",
            "content": "<p>Shipping is free for orders over $75. For all other domestic orders shipping is $10. International shipping is $20.<\/p>"
          }
        },
        "165592515344a810fb-2": {
          "type": "content",
          "settings": {
            "title": "How long does shipping take?",
            "content": "<p>We typically ship orders out within 1-2 business days of ordering. From there shipping may take 3-5 business days. For international orders shipping can take between 7-14 business days.<\/p>"
          }
        }
      },
      "block_order": [
        "165592515344a810fb-0",
        "165592515344a810fb-1",
        "165592515344a810fb-2"
      ],
      "settings": {
        "heading": "FAQs",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "1649436653425ff0fe": {
      "type": "recommendations-slider",
      "settings": {
        "intent": "related",
        "products_count": 10,
        "heading": "Check these out",
        "content": "",
        "spacing_top": 60,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "visibility": ""
      }
    },
    "1649436645dda33170": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "",
        "spacing_top": 60,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "visibility": ""
      }
    }
  },
  "order": [
    "1638995507af787164",
    "f07b2ee0-f9bb-4fdd-a9b3-e4242646430d",
    "16663285032715217b",
    "165592515341576314",
    "1649436653425ff0fe",
    "1649436645dda33170"
  ]
}
```

</details>

<details>

<summary><strong>templates/page.about.json</strong></summary>

```json
{
  "sections": {
    "16584345007aaf78db": {
      "type": "banner",
      "blocks": {
        "da8826b7-2320-452c-b3e6-79a85aee7fae": {
          "type": "heading",
          "settings": {
            "content": "About"
          }
        }
      },
      "block_order": [
        "da8826b7-2320-452c-b3e6-79a85aee7fae"
      ],
      "settings": {
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": false,
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "color__dark",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "style_border": "",
        "layout_y_spacing": "min-h-[250px] md:min-h-[350px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "visibility": ""
      }
    },
    "1658952564faef90a2": {
      "type": "content-grid",
      "blocks": {
        "1658952564d627444e-2": {
          "type": "content",
          "settings": {
            "heading": "Our story",
            "content": "<p>For so long, fine art was only for the wealthy. We wanted to bring that art and beauty into everyone's home.<\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "1658952564d627444e-0": {
          "type": "content",
          "settings": {
            "heading": "Our pieces",
            "content": "<p>We work with 1000s of local artist and provide a fair payment for all submitted artworks. <\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Group_2_copy_8c36516c-ca86-45d3-8638-c2f060088f70.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-neutral",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "1658952564d627444e-1": {
          "type": "content",
          "settings": {
            "heading": "Our team",
            "content": "<p>We are art-obsessed designers who want to bring luxury to everyone's spaces. With a rich and diverse background we're able to select some truly unique pieces.<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Screen_Shot_2023-01-04_at_12.16.27_PM.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-2",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "8dd5be61-5483-409d-ad6c-4066507b9a39": {
          "type": "content",
          "settings": {
            "heading": "Art for all",
            "content": "<p>For every purchase, we donate $2 to a local art program. These programs are fundemental in supporting the arts for underprivledged youth. <\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "2c829151-8695-4ad8-bd5b-1682cf3f4100": {
          "type": "content",
          "settings": {
            "heading": "Carbon neutral",
            "content": "<p>Sustainably is very important to us, from the factory, to the delivery van, we offset all of our carbon emissions.<\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-neutral color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        }
      },
      "block_order": [
        "1658952564d627444e-2",
        "1658952564d627444e-0",
        "1658952564d627444e-1",
        "8dd5be61-5483-409d-ad6c-4066507b9a39",
        "2c829151-8695-4ad8-bd5b-1682cf3f4100"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "0d3ff79e-69d7-4630-83c5-92d360b74445": {
      "type": "video",
      "settings": {
        "image_background": "shopify:\/\/shop_images\/ezgif-4-71e37fc503_df573092-b844-4d86-a9fa-17df46e333d5.gif",
        "video_background": "shopify:\/\/files\/videos\/production_ID_4067800.mp4.mp4",
        "auto_play": true,
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "16590236924b857f7a": {
      "type": "newsletter",
      "blocks": {
        "1659023692537da5b0-1": {
          "type": "image",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/bedroom.png",
            "layout_desktop_width": 8,
            "layout_mobile_width": 12
          }
        },
        "1659023692537da5b0-0": {
          "type": "newsletter",
          "settings": {
            "heading": "Stay connected!",
            "content": "<p>Enjoy 10% off your first purchase when you join our email newsletter. Community members also get first access to offers and new releases. <\/p>",
            "button_label": "Get 10% off",
            "disclaimer": "<p>Subscribers will receive promotional conent from us on a weekly basis. <\/p>",
            "success": "<p>Success! You've been subscribed. Use code <strong>TAKE10<\/strong> for 10% off.<\/p>",
            "layout_desktop_width": 4,
            "layout_mobile_width": 12,
            "layout_x_alignment": "justify-between"
          }
        }
      },
      "block_order": [
        "1659023692537da5b0-1",
        "1659023692537da5b0-0"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn",
        "style_border": "",
        "layout_alignment": "items-start",
        "visibility": ""
      }
    }
  },
  "order": [
    "16584345007aaf78db",
    "1658952564faef90a2",
    "0d3ff79e-69d7-4630-83c5-92d360b74445",
    "16590236924b857f7a"
  ]
}
```

</details>

<details>

<summary><strong>templates/blog.json</strong></summary>

```json
{
  "sections": {
    "16558222329618bae3": {
      "type": "banner",
      "blocks": {
        "0900543e-2663-4b6a-9ca2-725ca001255b": {
          "type": "heading",
          "settings": {
            "content": "Our Blog"
          }
        }
      },
      "block_order": [
        "0900543e-2663-4b6a-9ca2-725ca001255b"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_14.png",
        "image_background_mobile": "shopify:\/\/shop_images\/Group_14.png",
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start"
      }
    },
    "main": {
      "type": "blog__main",
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-1",
        "enable_author": true,
        "enable_summary": true,
        "enable_date": true,
        "enable_tags": false,
        "items_per_page": 6
      }
    }
  },
  "order": [
    "16558222329618bae3",
    "main"
  ]
}
```

</details>

<details>

<summary><strong>templates/article.json</strong></summary>

```json
{
  "sections": {
    "banner": {
      "type": "article__banner",
      "settings": {
        "color_scheme": "color__bg-neutral color__text",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "border--b-width",
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "visibility": "",
        "enable_author": true,
        "enable_date": true,
        "enable_tags": true,
        "enable_image": true
      }
    },
    "main": {
      "type": "article__main",
      "blocks": {
        "6d44e560-358d-4232-8708-502806610136": {
          "type": "breadcrumb",
          "settings": {
            "spacing_top": 10,
            "spacing_bottom": 10,
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width"
          }
        },
        "821a01e2-b9bf-45dc-b208-835bf9ac938c": {
          "type": "content",
          "settings": {
            "spacing_top": 50,
            "spacing_bottom": 50,
            "color_border": "color__border-divider-1",
            "style_border": ""
          }
        },
        "797ba560-2717-42ee-a1dc-547f7f40f214": {
          "type": "share",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 50,
            "color_border": "color__border-divider-1",
            "style_border": ""
          }
        },
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2": {
          "type": "comment",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_border": "color__border-divider-1",
            "style_border": ""
          }
        }
      },
      "block_order": [
        "6d44e560-358d-4232-8708-502806610136",
        "821a01e2-b9bf-45dc-b208-835bf9ac938c",
        "797ba560-2717-42ee-a1dc-547f7f40f214",
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-body color__text"
      }
    }
  },
  "order": [
    "banner",
    "main"
  ]
}
```

</details>
