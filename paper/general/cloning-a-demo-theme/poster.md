---
description: >-
  Copy and paste the contents from the below files into your theme to duplicate
  the theme.
---

# Poster

<details>

<summary>sections/header-group.json</summary>

```
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
            "content": "<p>Get free <a href=\"https:\/\/paperthemedemo2.myshopify.com\/\" title=\"\/\">shipping<\/a> on all orders over $35<\/p>"
          }
        },
        "493bfb93-68fd-473f-bc87-57abeae993ce": {
          "type": "text",
          "settings": {
            "content": "<p>Get a free sticker pack this week. Ends 2\/10.<\/p>"
          }
        }
      },
      "block_order": [
        "f2232503-8685-46db-aaf1-b796c5ea14f9",
        "493bfb93-68fd-473f-bc87-57abeae993ce"
      ],
      "settings": {
        "color_scheme": "color__bg-secondary color__secondary",
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
            "menu": "wallets",
            "url": "shopify:\/\/collections\/vertical-wallet",
            "heading": "Vertical Wallets",
            "content": "<p>The original minimal wallet<\/p>",
            "image": "shopify:\/\/shop_images\/vertical1.png"
          }
        },
        "55fbebf4-5325-42e7-866b-9f1b13b21f9f": {
          "type": "Content",
          "settings": {
            "menu": "wallets",
            "url": "shopify:\/\/collections\/bifold-wallet",
            "heading": "Bifold Wallets",
            "content": "<p>RFID technology protects your data<\/p>",
            "image": "shopify:\/\/shop_images\/bifold1.png"
          }
        },
        "f30e82ca-d488-4b4e-bb74-0b648774a526": {
          "type": "Content",
          "settings": {
            "menu": "wallets",
            "url": "shopify:\/\/collections\/phone-case-wallet",
            "heading": "Phone Wallets",
            "content": "<p>New cases, colors and sizes - available now<\/p>",
            "image": "shopify:\/\/shop_images\/phonecase1.png"
          }
        },
        "359ae4cc-66fa-4a4e-9832-9b2ff0329c9c": {
          "type": "Content",
          "settings": {
            "menu": "accessories",
            "url": "shopify:\/\/collections\/accessories",
            "heading": "Shop all Accessories",
            "content": "<p>Hold it all together<\/p>",
            "image": "shopify:\/\/shop_images\/accessories1.png"
          }
        },
        "f4df18d8-be07-4916-8a08-eaddb29823d5": {
          "type": "Content",
          "settings": {
            "menu": "bags",
            "url": "shopify:\/\/collections\/crossbody-bag",
            "heading": "Crossbody Bags",
            "content": "<p>Our crossbody bags are perfect for running around<\/p>",
            "image": "shopify:\/\/shop_images\/bag_831dfd04-5f8c-4316-b48f-fd126ae43a58.png"
          }
        },
        "75d64df5-8343-4298-b204-e14145ec982b": {
          "type": "Content",
          "settings": {
            "menu": "bags",
            "url": "shopify:\/\/collections\/tote",
            "heading": "Tote Bags",
            "content": "<p>Perfect for errands, the beach and everything inbetween<\/p>",
            "image": "shopify:\/\/shop_images\/tote_5c3497f4-d080-48a8-9f69-03b6229a8ac5.png"
          }
        }
      },
      "block_order": [
        "e561cffb-e23b-4a10-8382-4959a1b99bf2",
        "55fbebf4-5325-42e7-866b-9f1b13b21f9f",
        "f30e82ca-d488-4b4e-bb74-0b648774a526",
        "359ae4cc-66fa-4a4e-9832-9b2ff0329c9c",
        "f4df18d8-be07-4916-8a08-eaddb29823d5",
        "75d64df5-8343-4298-b204-e14145ec982b"
      ],
      "settings": {
        "dropdown_links": "main-menu",
        "search_links": "search-recomendations",
        "logo_light": "shopify:\/\/shop_images\/paper.png",
        "logo_desktop_height": 20,
        "logo_mobile_height": 16,
        "bar_color_scheme": "color__bg-body color__text",
        "bar_color_border": "color__border-divider-1",
        "bar_layout_desktop": "left-below",
        "bar_button_cart_type": "text",
        "bar_button_search_type": "icon",
        "bar_button_login_type": "none",
        "bar_button_menu_type": "text",
        "enable_search": true,
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

<summary>sections/footer-group.json</summary>

```
{
  "type": "footer",
  "name": "Footer group",
  "sections": {
    "49ac83c2-2f4d-49bf-ad2c-0a114d4de224": {
      "type": "icon-grid",
      "blocks": {
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-0": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/box-heart-solid.png",
            "icon_height": "h-8",
            "heading": "Free shipping",
            "content": "<p>Enjoy free shipping for your orders over $35.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-1": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/Frame_1_a6067915-9d6d-4e91-b11d-f01db44bc7ee.png",
            "icon_height": "h-8",
            "heading": "Hassle free returns",
            "content": "<p>We have a no-hassle <a href=\"https:\/\/paperthemedemo2.myshopify.com\/policies\/refund-policy\" title=\"Refund Policy\">return policy <\/a>for all orders.<\/p>",
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-row",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1"
          }
        },
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-2": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/badge-dollar-solid.png",
            "icon_height": "h-8",
            "heading": "Buy 2 Get 10%",
            "content": "<p>Buy two or more items and get 10% off your order.<\/p>",
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
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-0",
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-1",
        "sections--16744960131305__49ac83c2-2f4d-49bf-ad2c-0a114d4de224-16805368055bcc2cd0-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 40,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "visibility": ""
      }
    },
    "theme_footer": {
      "type": "theme__footer",
      "blocks": {
        "760fb357-5f92-47ad-a5a0-8e80918c9217": {
          "type": "logo",
          "settings": {
            "logo_light": "shopify:\/\/shop_images\/paper.png",
            "logo_desktop_height": 20,
            "logo_mobile_height": 16
          }
        },
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321": {
          "type": "newsletter",
          "settings": {
            "heading": "",
            "content": "<p>Join our newsletter to stay in the loop for all our latest sales and product drops<\/p>",
            "button": "Join",
            "disclaimer": "<p>By signing up you agree to our terms and conditions<\/p>",
            "success": "<p>Success! You’ve been subscribed.<\/p>"
          }
        },
        "4bad3d67-ba1d-41ab-b096-3d8c47a3e2e4": {
          "type": "menu",
          "settings": {
            "menu": ""
          }
        },
        "5dc22179-9717-40d2-9d83-4532c904e6d1": {
          "type": "menu",
          "settings": {
            "menu": "footer-3"
          }
        },
        "150805eb-9862-49dd-b0c2-0111162d6fce": {
          "type": "menu",
          "settings": {
            "menu": "footer-2"
          }
        },
        "6ad6b950-210d-4cf8-b231-62c67db4980e": {
          "type": "menu",
          "settings": {
            "menu": "footer"
          }
        }
      },
      "block_order": [
        "760fb357-5f92-47ad-a5a0-8e80918c9217",
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321",
        "4bad3d67-ba1d-41ab-b096-3d8c47a3e2e4",
        "5dc22179-9717-40d2-9d83-4532c904e6d1",
        "150805eb-9862-49dd-b0c2-0111162d6fce",
        "6ad6b950-210d-4cf8-b231-62c67db4980e"
      ],
      "settings": {
        "main_color_scheme": "color__bg-body color__text",
        "main_color_border": "color__border-divider-1",
        "main_color_button": "btn btn--secondary",
        "sub_color_scheme": "color__bg-body color__text",
        "sub_color_border": "!color__border-transparent",
        "sub_color_button": "btn btn--plain",
        "sub_links": "legal",
        "sub_enable_payment_icons": true,
        "visibility": ""
      }
    }
  },
  "order": [
    "49ac83c2-2f4d-49bf-ad2c-0a114d4de224",
    "theme_footer"
  ]
}
```

</details>

<details>

<summary>sections/overlay-group.json</summary>

```
{
  "type": "custom.overlay",
  "name": "Overlay group",
  "sections": {
    "theme_scrollup": {
      "type": "theme__scrollup",
      "disabled": true,
      "settings": {
        "enable_back_to_top": false,
        "scroll_up_style": "icon",
        "button_color": "btn",
        "visibility": ""
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

<summary>templates/index.json</summary>

```
{
  "sections": {
    "6762bdff-42b8-40c0-b357-2fdd9fdf777e": {
      "type": "navigation-slider",
      "blocks": {
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-0": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/wallet5.png",
            "heading": "Wallets",
            "url": "shopify:\/\/collections\/wallets"
          }
        },
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-1": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/306124882_811081790343809_3640385817232118395_n.jpg",
            "heading": "Accessories",
            "url": "shopify:\/\/collections\/accessories"
          }
        },
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-2": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/tote_1.png",
            "heading": "Bags",
            "url": "shopify:\/\/collections\/bags"
          }
        },
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-3": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/bags8.png",
            "heading": "Best selling",
            "url": "shopify:\/\/collections\/crossbody-bag"
          }
        },
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-4": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/289653776_552922956448269_6363512142412118467_n_1.png",
            "heading": "Blog",
            "url": "shopify:\/\/blogs\/news"
          }
        }
      },
      "block_order": [
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-0",
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-1",
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-2",
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-3",
        "template--16671743672553__6762bdff-42b8-40c0-b357-2fdd9fdf777e-1672778398776fe59f-4"
      ],
      "settings": {
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "visibility": "md:hidden"
      }
    },
    "1655754078b117ff84": {
      "type": "banner",
      "blocks": {
        "2f1af8c8-7de9-4132-b03d-8970abb75617": {
          "type": "heading",
          "settings": {
            "content": "Carry on"
          }
        },
        "eb0c9326-733b-4104-9e5b-f94482618684": {
          "type": "buttons",
          "settings": {
            "button_color": "btn btn--secondary",
            "button_label": "Shop All",
            "button_url": "shopify:\/\/collections\/all",
            "secondary_button_color": "btn btn--neutral",
            "secondary_button_label": "Button label",
            "secondary_button_url": ""
          }
        },
        "29af8de7-1a36-45f5-a516-b9a9f2afe042": {
          "type": "content",
          "settings": {
            "content": "<p>Moving you forward with style<\/p>"
          }
        }
      },
      "block_order": [
        "2f1af8c8-7de9-4132-b03d-8970abb75617",
        "eb0c9326-733b-4104-9e5b-f94482618684",
        "29af8de7-1a36-45f5-a516-b9a9f2afe042"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_1.png",
        "image_background_mobile": "shopify:\/\/shop_images\/235364082_830616680923777_5629114582486314207_n.webp",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[550px] max-h-[75vh] md:min-h-[60vh]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "visibility": ""
      }
    },
    "fef36a2d-1869-475a-8901-cf95571729f2": {
      "type": "content-grid",
      "blocks": {
        "template--16747560009961__fef36a2d-1869-475a-8901-cf95571729f2-1683312329deba14d8-0": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>\"One of the best new products this year\"<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Frame_17.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": false,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-start content-start",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "e015a7b1-1691-4090-82b7-e8ed97f648e8": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>\"The best thing for your friends birthday gift\"<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Frame_20.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": false,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-start content-start",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "18e5ffff-0f54-4601-874b-334e216ecbb2": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>\"I can't stop obsessig over my new wallet\"<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Frame_18.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": false,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-start content-start",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "5ae3fcb6-5b03-4c99-9f97-8741858e1345": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>\"Honestly these are the last wallets you'll ever need\"<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Frame_19.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": false,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-start content-start",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "024a230a-1f1d-4c65-9ac4-6277f843702b": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "<p>\"You have to check this out - it's just too good\"<\/p>",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/Frame_21.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": false,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "!color__border-transparent",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-start content-start",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        }
      },
      "block_order": [
        "template--16747560009961__fef36a2d-1869-475a-8901-cf95571729f2-1683312329deba14d8-0",
        "e015a7b1-1691-4090-82b7-e8ed97f648e8",
        "18e5ffff-0f54-4601-874b-334e216ecbb2",
        "5ae3fcb6-5b03-4c99-9f97-8741858e1345",
        "024a230a-1f1d-4c65-9ac4-6277f843702b"
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
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-5",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "visibility": ""
      }
    },
    "1656607690f9c46d91": {
      "type": "content-grid",
      "blocks": {
        "16566076905ecb39eb-0": {
          "type": "content",
          "settings": {
            "heading": "Keep it together",
            "content": "<p>Never lose your balm again with the new Lip Balm Holder <\/p>",
            "button_label": "Shop Accessories",
            "button_url": "shopify:\/\/collections\/accessories",
            "image_featured": "shopify:\/\/shop_images\/Frame_7.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body",
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
        "fae440e8-e78f-49f7-b442-2b8663df4674": {
          "type": "content",
          "settings": {
            "heading": "Bag it up",
            "content": "<p>Carry all of your essentials in one place with the Crossbody Bag<\/p>",
            "button_label": "Shop Crossbody",
            "button_url": "shopify:\/\/collections\/crossbody-bag",
            "image_featured": "shopify:\/\/shop_images\/Frame_5.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body color__text",
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
        "2861ed85-6d25-4c7a-9637-78a6f8fe5366": {
          "type": "content",
          "settings": {
            "heading": "Your info on lock",
            "content": "<p>Built-in RFID blocking technology to keep theifs away<\/p>",
            "button_label": "Shop Vertical Wallets",
            "button_url": "shopify:\/\/collections\/accessories",
            "image_featured": "shopify:\/\/shop_images\/Frame_4.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        }
      },
      "block_order": [
        "16566076905ecb39eb-0",
        "fae440e8-e78f-49f7-b442-2b8663df4674",
        "2861ed85-6d25-4c7a-9637-78a6f8fe5366"
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
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "165660746705ac5016": {
      "type": "collection-grid",
      "blocks": {
        "1656607467815d12d1-0": {
          "type": "collection",
          "settings": {
            "collection": "wallets"
          }
        },
        "dd2998f7-0335-4552-b342-e1d5e4728d8f": {
          "type": "collection",
          "settings": {
            "collection": "accessories"
          }
        },
        "defe7d05-dbe9-4585-aa07-eb59b6434eb6": {
          "type": "collection",
          "settings": {
            "collection": "bags"
          }
        },
        "1656607467815d12d1-1": {
          "type": "card",
          "settings": {
            "heading": "All Categories",
            "content": "<p>Not sure where to start? Shop from our entire collection.<\/p>",
            "button_label": "Shop Now",
            "button_url": "shopify:\/\/collections"
          }
        }
      },
      "block_order": [
        "1656607467815d12d1-0",
        "dd2998f7-0335-4552-b342-e1d5e4728d8f",
        "defe7d05-dbe9-4585-aa07-eb59b6434eb6",
        "1656607467815d12d1-1"
      ],
      "settings": {
        "heading": "Everything in one place",
        "content": "",
        "button_label": "View All Categories",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": "",
        "enable_collection_size_count": true
      }
    },
    "16566133035a6b63bc": {
      "type": "product-grid",
      "blocks": {
        "cf9d4593-9b93-4855-991f-f0fdd1bf3224": {
          "type": "card",
          "settings": {
            "heading": "Best Sellers",
            "content": "<p>A collection of our best selling items throughout the years<\/p>",
            "button_label": "Shop Now",
            "button_url": "shopify:\/\/collections\/staff-picks"
          }
        }
      },
      "block_order": [
        "cf9d4593-9b93-4855-991f-f0fdd1bf3224"
      ],
      "settings": {
        "collection": "staff-picks",
        "products_count": 7,
        "heading": "Best Sellers",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "c9923c64-6d70-4fbd-926a-5dffe2191a50": {
      "type": "featured-product",
      "blocks": {
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-0": {
          "type": "title",
          "settings": {
            "spacing_top": 15,
            "spacing_bottom": 5,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_thumbnails_product_type": false,
            "enable_thumbnails_vendor": false,
            "content": ""
          }
        },
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-1": {
          "type": "price",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "e4f97c6f-5129-4a5e-ab3e-db9ef68d826f": {
          "type": "text",
          "settings": {
            "spacing_top": 15,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "content": "<p>⟶ Keyring for attaching things<\/p><p>⟶ Inner zip pouch<\/p><p>⟶ Easy grab-and-go storage<\/p>"
          }
        },
        "f7bc08c3-f020-4206-8994-e31cb6bea41d": {
          "type": "options",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "style_border": ""
          }
        },
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-2": {
          "type": "add",
          "settings": {
            "spacing_top": 15,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "enable_quantity": false,
            "enable_dynamic_checkout": false,
            "content": "<p>Free shipping · Easy returns · Guranteed amazing<\/p>"
          }
        },
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-3": {
          "type": "description",
          "settings": {
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_open": true
          }
        }
      },
      "block_order": [
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-0",
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-1",
        "e4f97c6f-5129-4a5e-ab3e-db9ef68d826f",
        "f7bc08c3-f020-4206-8994-e31cb6bea41d",
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-2",
        "template--16649499607273__c9923c64-6d70-4fbd-926a-5dffe2191a50-16705129669c5ed52a-3"
      ],
      "settings": {
        "product": "carry-on-tote-bag",
        "enable_default_variant": true,
        "media_gallery_style": "thumbnail-slider",
        "enable_zoom": true,
        "enable_alt": false,
        "enable_variant_images": false,
        "media_color_scheme": "color__bg-overlay-1 color__text",
        "media_ratio": "aspect-[2\/3] aspect-w-2 aspect-h-3",
        "media_object-sizing": "cover",
        "enable_ratio": true,
        "show_product_badges": true,
        "spacing_top": 0,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "layout_gallery_size": "w-full md:w-2\/3",
        "visibility": ""
      }
    },
    "3be5e723-af3b-412d-a53f-a9adf8b34a9a": {
      "type": "product-featured",
      "settings": {
        "collection": "elastic-wallet",
        "products_count": 3,
        "heading": "Elastic Wallets",
        "content": "",
        "button_label": "Shop All",
        "button_url": "shopify:\/\/collections\/elastic-wallet",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "00c3caf4-5af0-417d-b143-468d067633be": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 2,
        "heading": "Get outside",
        "content": "<p>Read our blog to get inspired for your next outdoor adventure<\/p>",
        "button_label": "Read All",
        "button_url": "shopify:\/\/blogs\/news",
        "enable_author": false,
        "enable_summary": true,
        "enable_date": true,
        "enable_tags": false,
        "spacing_top": 100,
        "spacing_bottom": 40,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-2",
        "row_size_mobile": "grid grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "49e8c338-4b80-49c0-9957-0150e3e6b94d": {
      "type": "video",
      "settings": {
        "image_background": "shopify:\/\/shop_images\/ezgif-4-a28350dd59_94889762-75ac-400b-a063-9539adb47ba0.gif",
        "video_background": "shopify:\/\/files\/videos\/Woven_for_Originality-vimeo-323032222-http-1080p-sub-1.0-28.0.mp4.mp4",
        "auto_play": true,
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "20dc02d2-40e7-49f5-af7d-170e6d82410e": {
      "type": "accordions",
      "blocks": {
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-0": {
          "type": "content",
          "settings": {
            "title": "How do I get free shipping?",
            "content": "<p>Free shipping will automatically be applied to all domestic orders over $35. Simplfy add over $35 to your cart and you will see the discount while checking out.<\/p>"
          }
        },
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-1": {
          "type": "content",
          "settings": {
            "title": "How much do I need to spend to get free shipping?",
            "content": "<p>Shipping is free for orders over $35. For all other domestic orders shipping is $10. International shipping is $20.<\/p>"
          }
        },
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-2": {
          "type": "content",
          "settings": {
            "title": "How long does shipping take?",
            "content": "<p>We typically ship orders out within 1-2 business days of ordering. From there shipping may take 3-5 business days. For international orders shipping can take between 7-14 business days.<\/p>"
          }
        }
      },
      "block_order": [
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-0",
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-1",
        "template--16649499607273__20dc02d2-40e7-49f5-af7d-170e6d82410e-1670512679e0f985cf-2"
      ],
      "settings": {
        "heading": "FAQs",
        "content": "",
        "button_label": "Read more",
        "button_url": "shopify:\/\/pages\/faqs",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "border--t-width",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "176811aa-201e-4ae5-a7ee-8d50999866a2": {
      "type": "content-slider",
      "blocks": {
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-0": {
          "type": "content",
          "settings": {
            "heading": "Sponsored creators",
            "content": "<p><a href=\"\/pages\/contact\" title=\"Contact\">Learn more<\/a><\/p>",
            "image_background": "shopify:\/\/shop_images\/289653776_552922956448269_6363512142412118467_n_1.png",
            "button_label": "",
            "button_url": "",
            "spacing_top": 160,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__light",
            "color_button": "btn btn--secondary",
            "enable_gradient": true,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 8,
            "layout_mobile_width": 10
          }
        },
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-1": {
          "type": "content",
          "settings": {
            "heading": "Join the team",
            "content": "<p><a href=\"\/pages\/contact\" title=\"Contact\">See careers<\/a><\/p>",
            "image_background": "shopify:\/\/shop_images\/281490640_180424071004945_5203116822781132846_n.webp",
            "button_label": "",
            "button_url": "",
            "spacing_top": 160,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-overlay-1 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__light",
            "color_button": "btn btn--secondary",
            "enable_gradient": true,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 8,
            "layout_mobile_width": 10
          }
        },
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-2": {
          "type": "content",
          "settings": {
            "heading": "Community events",
            "content": "<p><a href=\"\/pages\/contact\" title=\"Contact\">Get tickets<\/a><\/p>",
            "image_background": "shopify:\/\/shop_images\/156673844_2798533807067229_3390704918855172837_n_acb062db-70fe-4857-83d8-30b159db7a60.webp",
            "button_label": "",
            "button_url": "",
            "spacing_top": 160,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__light",
            "color_button": "btn btn--secondary",
            "enable_gradient": true,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 8,
            "layout_mobile_width": 10
          }
        }
      },
      "block_order": [
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-0",
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-1",
        "template--16652076941545__176811aa-201e-4ae5-a7ee-8d50999866a2-167073839650e62910-2"
      ],
      "settings": {
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
    }
  },
  "order": [
    "6762bdff-42b8-40c0-b357-2fdd9fdf777e",
    "1655754078b117ff84",
    "fef36a2d-1869-475a-8901-cf95571729f2",
    "1656607690f9c46d91",
    "165660746705ac5016",
    "16566133035a6b63bc",
    "c9923c64-6d70-4fbd-926a-5dffe2191a50",
    "3be5e723-af3b-412d-a53f-a9adf8b34a9a",
    "00c3caf4-5af0-417d-b143-468d067633be",
    "49e8c338-4b80-49c0-9957-0150e3e6b94d",
    "20dc02d2-40e7-49f5-af7d-170e6d82410e",
    "176811aa-201e-4ae5-a7ee-8d50999866a2"
  ]
}
```

</details>

<details>

<summary>templates/collection.json</summary>

```
{
  "sections": {
    "banner": {
      "type": "collection__banner",
      "settings": {
        "color_scheme": "color__bg-secondar",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "border--b-width",
        "layout_y_spacing": "min-h-[300px] md:min-h-[300px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "visibility": "",
        "enable_description": true,
        "enable_image": true
      }
    },
    "grid": {
      "type": "collection__main",
      "blocks": {
        "dd463a6a-8261-41de-bc19-aaa61419805c": {
          "type": "content",
          "settings": {
            "url": "",
            "heading": "Free shipping",
            "content": "<p>Spend over $35 and recieve free shipping.<\/p>",
            "button_label": "",
            "index": 3,
            "background_color_scheme": "color__bg-overlay-1 color__text",
            "column_size": "col-span-2"
          }
        },
        "2c8aad49-b136-4f65-935a-7368b8cc5bb3": {
          "type": "newsletter",
          "settings": {
            "image_background": "shopify:\/\/shop_images\/bags8.png",
            "heading": "Over $100 of monthly prizes",
            "content": "<p>Enter to win our monthly prize pack.<\/p>",
            "button_label": "Enter to win",
            "disclaimer": "",
            "success": "<p>Thanks for subscribing<\/p>",
            "index": 11,
            "background_color_scheme": "color__bg-overlay-1 color__text",
            "column_size": "col-span-2"
          }
        }
      },
      "block_order": [
        "dd463a6a-8261-41de-bc19-aaa61419805c",
        "2c8aad49-b136-4f65-935a-7368b8cc5bb3"
      ],
      "settings": {
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "enable_sort": true,
        "enable_filter": true,
        "products_per_page": 16
      }
    },
    "recent": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "<p><\/p>",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--t-width",
        "visibility": ""
      }
    },
    "f2831a72-a2a6-49e9-a4a9-335345cd5944": {
      "type": "text",
      "settings": {
        "heading": "",
        "content": "<p>Our premium minimal wallets are designed for people who value simplicity and functionality. These wallets are made from high-quality materials and have a sleek, slim design that makes them easy to carry in your pocket or bag. They have just the right amount of space for your cards, cash, and other essentials, without being bulky or cumbersome. Our premium minimal wallets come in a variety of colors and styles to suit your personal preferences, and they are the perfect choice for anyone who wants a stylish, functional wallet that will last for years to come.<\/p>",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-neutral color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "",
        "visibility": ""
      }
    }
  },
  "order": [
    "banner",
    "grid",
    "recent",
    "f2831a72-a2a6-49e9-a4a9-335345cd5944"
  ]
}
```

</details>

<details>

<summary>templates/list-collections.json</summary>

```
{
  "sections": {
    "main": {
      "type": "list-collections__main",
      "blocks": {
        "a66c5d26-9bba-4a8c-8079-98c20b6df3db": {
          "type": "newsletter",
          "settings": {
            "heading": "",
            "content": "<p>Join our newsletter to stay in the loop for all our latest sales and product drops<\/p>",
            "button_label": "Join",
            "disclaimer": "",
            "success": "<p>Success!<\/p>",
            "index": 10,
            "background_color_scheme": "color__bg-body color__text",
            "column_size": "md:col-span-2"
          }
        }
      },
      "block_order": [
        "a66c5d26-9bba-4a8c-8079-98c20b6df3db"
      ],
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "enable_collection_size_count": true,
        "items_per_page": 14
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

<summary>templates/product.json</summary>

```
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
            "style_border": ""
          }
        },
        "89816093-eb0c-4b16-8952-2862b463454a": {
          "type": "rating",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": ""
          }
        },
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5": {
          "type": "title",
          "settings": {
            "content": "<p>⟶ High quality materials<\/p><p>⟶ Slim-profile design<\/p><p>⟶ 30-day satisfaction guarantee<\/p>",
            "spacing_top": 10,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--t-width",
            "enable_thumbnails_product_type": false,
            "enable_thumbnails_vendor": false,
            "enable_sku": false
          }
        },
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22": {
          "type": "price",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "3c821cec-15b4-40fa-bd51-0072523601e3": {
          "type": "popup",
          "settings": {
            "option": "size",
            "title": "Guide ↗",
            "page": "sizing-chart",
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "style_border": ""
          }
        },
        "cdf38c91-7aae-472a-bd36-8b9d32859233": {
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
            "content": "<p>Free shipping · Easy returns · Guranteed amazing<\/p>",
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_quantity": false,
            "enable_dynamic_checkout": false
          }
        },
        "9f1692ea-ccb9-4e4c-9c83-7a6ae53392aa": {
          "type": "inventory",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "threshold": 99999
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "enable_open": true
          }
        },
        "1af8dc66-c25a-46e1-8c34-7d902b4ab936": {
          "type": "accordion",
          "settings": {
            "title": "Shipping and returns",
            "content": "<p>We have a no-hassle shipping and return policy. All items are shipped the next day.<\/p><p>If you want to make a return just use the enclosed return label and you'll receive a store credit. <\/p>",
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "enable_open": false
          }
        },
        "5dc0f396-3058-4aef-abb5-fa7cf986b096": {
          "type": "upsell",
          "settings": {
            "title": "Pairs well with",
            "products_count": 3,
            "intent": "related",
            "color_scheme": "color__bg-overlay-1 color__text",
            "style_border": "",
            "enable_open": true
          }
        },
        "848f5aea-f7ad-4974-a5fb-020776e3e523": {
          "type": "stickyadd",
          "settings": {
            "content": "<p>Free shipping · Easy returns · Guranteed amazing<\/p>",
            "color_scheme": "color__bg-body color__text",
            "on_scroll": true
          }
        }
      },
      "block_order": [
        "bef9bd40-2a8e-45c2-ae54-59c9ef6f0e26",
        "89816093-eb0c-4b16-8952-2862b463454a",
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5",
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22",
        "3c821cec-15b4-40fa-bd51-0072523601e3",
        "cdf38c91-7aae-472a-bd36-8b9d32859233",
        "b78b560b-e1c2-428d-ad73-fb5f8aac6d53",
        "9f1692ea-ccb9-4e4c-9c83-7a6ae53392aa",
        "123fd04c-91f3-4248-a65a-614e2f64fdeb",
        "1af8dc66-c25a-46e1-8c34-7d902b4ab936",
        "5dc0f396-3058-4aef-abb5-fa7cf986b096",
        "848f5aea-f7ad-4974-a5fb-020776e3e523"
      ],
      "settings": {
        "enable_default_variant": false,
        "media_gallery_style": "grid",
        "image_border": "color__border-divider-1",
        "enable_zoom": true,
        "enable_alt": false,
        "enable_variant_images": false,
        "media_color_scheme": "color__bg-overlay-1 color__text",
        "media_ratio": "aspect-[1\/1] aspect-w-1 aspect-h-1",
        "media_object-sizing": "contain",
        "enable_ratio": true,
        "show_product_badges": true,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-divider-1",
        "layout_gallery_size": "w-full md:w-2\/3"
      }
    },
    "1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19": {
      "type": "content-grid",
      "blocks": {
        "template--16616281997545__1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19-1666905576ce0d7535-0": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/306124882_811081790343809_3640385817232118395_n.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body color__text",
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
        "template--16616281997545__1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19-1666905576ce0d7535-1": {
          "type": "content",
          "settings": {
            "heading": "30-day satisfaction guarantee",
            "content": "<p>All our products are backed by our 30-day satisfaction guarantee. If you aren't 100% happy with your order just let us know.<\/p>",
            "button_label": "Learn more",
            "button_url": "shopify:\/\/pages\/faqs",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "enable_padding": true,
            "color_scheme": "color__bg-body color__text",
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
        "template--16616281997545__1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19-1666905576ce0d7535-0",
        "template--16616281997545__1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19-1666905576ce0d7535-1"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "Button label",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 40,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn",
        "style_border": "border--t-width",
        "row_size_desktop": "md:grid-cols-2",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
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
        "button_label": "Help center",
        "button_url": "shopify:\/\/pages\/faqs",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width border--t-width",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "1649436645dda33170": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "<p><\/p>",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "visibility": ""
      }
    },
    "1649436653425ff0fe": {
      "type": "recommendations-slider",
      "settings": {
        "intent": "related",
        "products_count": 10,
        "heading": "You may also like",
        "content": "<p><\/p>",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
        "visibility": ""
      }
    },
    "1666327913b6639152": {
      "type": "apps",
      "blocks": {
        "e76bf002-82e1-46d5-8dbb-21d03d9acb8d": {
          "type": "shopify:\/\/apps\/product-reviews\/blocks\/reviews\/bae150af-8da8-48b2-9867-398188115e5f",
          "settings": {
          }
        }
      },
      "block_order": [
        "e76bf002-82e1-46d5-8dbb-21d03d9acb8d"
      ],
      "settings": {
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--t-width",
        "layout_padding": true
      }
    }
  },
  "order": [
    "1638995507af787164",
    "1a8aa4b5-2ae5-4b2d-aa4d-afb883fdeb19",
    "165592515341576314",
    "1649436645dda33170",
    "1649436653425ff0fe",
    "1666327913b6639152"
  ]
}
```

</details>

<details>

<summary>templates/page.about.json</summary>

```
{
  "sections": {
    "16566208525aa0565e": {
      "type": "banner",
      "blocks": {
        "cb4e549d-5450-4826-9be6-7285406c65d9": {
          "type": "heading",
          "settings": {
            "content": "About"
          }
        }
      },
      "block_order": [
        "cb4e549d-5450-4826-9be6-7285406c65d9"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Hero.png",
        "image_background_mobile": "shopify:\/\/shop_images\/244686508_428454605370496_8678587370165260132_n.webp",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center"
      }
    },
    "16566209831b6db755": {
      "type": "content-grid",
      "blocks": {
        "1656620983a0362b67-0": {
          "type": "content",
          "settings": {
            "heading": "Carry On",
            "content": "<p>We want to bring your uniqueness, creativity and style to every product.<\/p>",
            "button_label": "",
            "button_url": "",
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "1656620983a0362b67-1": {
          "type": "content",
          "settings": {
            "heading": "Careers",
            "content": "<p>Interested in joining our team? We're hiring for a variety of rolls -<a href=\"\/pages\/careers\" title=\"Careers\"> apply here<\/a>.<\/p>",
            "button_label": "",
            "button_url": "",
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-neutral color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "1656620983a0362b67-2": {
          "type": "content",
          "settings": {
            "heading": "Our Story",
            "content": "<p>From humble beginings we've come along way to get to where we are now. With thounsands of reviews and supportive customers we're here for you everyday.<\/p>",
            "button_label": "",
            "button_url": "",
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-secondary color__secondary",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-2",
            "enable_padding": true
          }
        }
      },
      "block_order": [
        "1656620983a0362b67-0",
        "1656620983a0362b67-1",
        "1656620983a0362b67-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 0,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "justify-between"
      }
    },
    "1661972038e94070cb": {
      "type": "content-slider",
      "blocks": {
        "166197203787690a9b-0": {
          "type": "content",
          "settings": {
            "heading": "Kelis Kaleopa'a",
            "content": "<p>Pro Surfer<\/p>",
            "image_featured": "shopify:\/\/shop_images\/kelis_451f740a-4e62-4af4-985e-19.jpg",
            "button_label": "",
            "button_url": "",
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 4,
            "layout_mobile_width": 8,
            "enable_padding": true
          }
        },
        "166197203787690a9b-1": {
          "type": "content",
          "settings": {
            "heading": "Carson Hancock",
            "content": "<p>Pro skater<\/p>",
            "image_featured": "shopify:\/\/shop_images\/carson-hancock.jpg",
            "button_label": "",
            "button_url": "",
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 4,
            "layout_mobile_width": 8,
            "enable_padding": true
          }
        },
        "166197203787690a9b-2": {
          "type": "content",
          "settings": {
            "heading": "Brooklinn Khoury",
            "content": "<p>Pro Skater<\/p>",
            "image_featured": "shopify:\/\/shop_images\/brooke_2895eda5-2dd5-4532-b97c-6f71472632d4.webp",
            "button_label": "",
            "button_url": "",
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 4,
            "layout_mobile_width": 8,
            "enable_padding": true
          }
        },
        "aa979e6d-e311-4c89-8c8c-5b74d3285959": {
          "type": "content",
          "settings": {
            "heading": "Kevin Schulz",
            "content": "<p>Pro Surfer<\/p>",
            "image_featured": "shopify:\/\/shop_images\/kevin_806d4658-06ba-4ddb-9892-83429f702447.jpg",
            "button_label": "",
            "button_url": "",
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_desktop_width": 4,
            "layout_mobile_width": 8,
            "enable_padding": true
          }
        }
      },
      "block_order": [
        "166197203787690a9b-0",
        "166197203787690a9b-1",
        "166197203787690a9b-2",
        "aa979e6d-e311-4c89-8c8c-5b74d3285959"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 40,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-selected-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "layout_x_alignment": "justify-between"
      }
    },
    "692180fe-e387-4689-90f0-2afb625cce8e": {
      "type": "banner",
      "settings": {
        "video_background": "shopify:\/\/files\/videos\/Woven_for_Originality-vimeo-323032222-http-1080p-sub-1.0-28.0.mp4.mp4",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "style_border": "",
        "layout_y_spacing": "min-h-[250px] md:min-h-[350px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start"
      }
    }
  },
  "order": [
    "16566208525aa0565e",
    "16566209831b6db755",
    "1661972038e94070cb",
    "692180fe-e387-4689-90f0-2afb625cce8e"
  ]
}
```

</details>

<details>

<summary>templates/blog.json</summary>

```
{
  "sections": {
    "16558222329618bae3": {
      "type": "banner",
      "blocks": {
        "b29c55bb-3717-452a-964b-9e03170e0f92": {
          "type": "heading",
          "settings": {
            "content": "Blog"
          }
        }
      },
      "block_order": [
        "b29c55bb-3717-452a-964b-9e03170e0f92"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Screen_Shot_2022-05-25_at_2.13.21_PM_1024x1024_ac7af594-aa82-4924-b54c-dacd6d8e1d87.webp",
        "image_background_mobile": "shopify:\/\/shop_images\/Screen_Shot_2022-05-25_at_2.13.21_PM_1024x1024_ac7af594-aa82-4924-b54c-dacd6d8e1d87.webp",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-center text-center",
        "visibility": ""
      }
    },
    "main": {
      "type": "blog__main",
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-2",
        "row_size_mobile": "grid grid-cols-1",
        "enable_author": true,
        "enable_summary": false,
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

<summary>templates/article.json</summary>

```
{
  "sections": {
    "banner": {
      "type": "article__banner",
      "settings": {
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "border--b-width",
        "layout_y_spacing": "min-h-[350px] md:min-h-[450px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "enable_author": false,
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
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width"
          }
        },
        "821a01e2-b9bf-45dc-b208-835bf9ac938c": {
          "type": "content",
          "settings": {
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width"
          }
        },
        "797ba560-2717-42ee-a1dc-547f7f40f214": {
          "type": "share",
          "settings": {
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width"
          }
        },
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2": {
          "type": "comment",
          "settings": {
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
