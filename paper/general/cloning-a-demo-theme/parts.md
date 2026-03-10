---
description: >-
  Copy and paste the contents from the below files into your theme to duplicate
  the theme.
---

# Parts

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
        "f2232503-8685-46db-aaf1-b796c5ea14f9": {
          "type": "text",
          "settings": {
            "content": "<p>Price freeze on all fasteners from now until 10\/11<\/p>"
          }
        }
      },
      "block_order": [
        "f2232503-8685-46db-aaf1-b796c5ea14f9"
      ],
      "settings": {
        "color_scheme": "color__bg-primary color__primary",
        "layout_alignment": "left",
        "visibility": "",
        "show_account_link": false
      }
    },
    "theme_header": {
      "type": "theme__header",
      "settings": {
        "dropdown_links": "main-menu",
        "search_links": "",
        "logo_light": "shopify:\/\/shop_images\/Parts_2_2a56d383-6576-437a-bd29-1c2b61dbf357.png",
        "logo_desktop_height": 30,
        "logo_mobile_height": 28,
        "bar_color_scheme": "color__bg-secondary color__secondary",
        "bar_color_border": "!color__border-transparent",
        "bar_layout_desktop": "left-below",
        "bar_button_cart_type": "icon",
        "bar_button_search_type": "icon",
        "bar_button_login_type": "icon",
        "bar_button_menu_type": "icon",
        "enable_search": true,
        "dropdown_color_scheme": "color__bg-body color__text",
        "dropdown_color_border": "color__border-divider-1",
        "search_color_scheme": "color__bg-body color__text",
        "search_color_border": "color__border-divider-1",
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
        "959314c0-5d60-4e09-8e67-c702220d02f1": {
          "type": "logo",
          "settings": {
            "logo_light": "shopify:\/\/shop_images\/Parts_2_2a56d383-6576-437a-bd29-1c2b61dbf357.png",
            "logo_desktop_height": 30,
            "logo_mobile_height": 20
          }
        },
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321": {
          "type": "newsletter",
          "settings": {
            "heading": "Newsletter",
            "content": "<p>Tell customers why they should subscribe to your newsletter.<\/p>",
            "button": "Subscribe",
            "disclaimer": "<p>Include an additional disclaimer to clarify how you will use a subscribers email.<\/p>",
            "success": "<p>Success! You've been subscribed.<\/p>"
          }
        },
        "6ad6b950-210d-4cf8-b231-62c67db4980e": {
          "type": "menu",
          "settings": {
            "menu": "footer"
          }
        },
        "150805eb-9862-49dd-b0c2-0111162d6fce": {
          "type": "menu",
          "settings": {
            "menu": "footer-menu-2"
          }
        },
        "5dc22179-9717-40d2-9d83-4532c904e6d1": {
          "type": "menu",
          "settings": {
            "menu": "footer-menu-3"
          }
        }
      },
      "block_order": [
        "959314c0-5d60-4e09-8e67-c702220d02f1",
        "78204a1a-1009-4f50-a9c8-4a9f0b2af321",
        "6ad6b950-210d-4cf8-b231-62c67db4980e",
        "150805eb-9862-49dd-b0c2-0111162d6fce",
        "5dc22179-9717-40d2-9d83-4532c904e6d1"
      ],
      "settings": {
        "main_color_scheme": "color__bg-secondary color__secondary",
        "main_color_border": "color__border-divider-1",
        "main_color_button": "btn",
        "sub_color_scheme": "color__bg-secondary color__secondary",
        "sub_color_border": "color__border-divider-1",
        "sub_color_button": "btn btn--plain",
        "sub_links": "sub-footer",
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

<summary>sections/overlay-group.json</summary>

```json
{
  "type": "custom.overlay",
  "name": "Overlay group",
  "sections": {
    "theme_scrollup": {
      "type": "theme__scrollup",
      "settings": {
        "enable_back_to_top": true,
        "scroll_up_style": "text",
        "button_color": "btn btn--plain",
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

```json
{
  "sections": {
    "1658853151e8c4f7dd": {
      "type": "banner",
      "blocks": {
        "1ef5fee1-7b9c-4d85-aa48-5c2d33af8bb9": {
          "type": "heading",
          "settings": {
            "content": "UP TO 40% OFF TOP BRAND POWER TOOLS"
          }
        },
        "a21647d7-a0f8-4425-a411-712f67becd88": {
          "type": "content",
          "settings": {
            "content": "<p>★★★★★ 4.8 rated - over 4,000+ reviews<\/p>"
          }
        },
        "c65d362c-aa3c-468a-a95e-7bff77c8e56c": {
          "type": "buttons",
          "settings": {
            "button_color": "btn",
            "button_label": "Shop Tools",
            "button_url": "shopify:\/\/collections\/tools",
            "secondary_button_color": "btn btn--plain",
            "secondary_button_label": "Contact Us",
            "secondary_button_url": "shopify:\/\/pages\/contact"
          }
        }
      },
      "block_order": [
        "1ef5fee1-7b9c-4d85-aa48-5c2d33af8bb9",
        "a21647d7-a0f8-4425-a411-712f67becd88",
        "c65d362c-aa3c-468a-a95e-7bff77c8e56c"
      ],
      "settings": {
        "image_background_desktop": "shopify:\/\/shop_images\/Group_1_7.png",
        "image_background_mobile": "shopify:\/\/shop_images\/Group_1_7.png",
        "video_background": "shopify:\/\/files\/videos\/production ID_4957770.mp4",
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": false,
        "color_scheme": "color__bg-body color__text",
        "color_text": "color__light",
        "color_border": "color__border-divider-1",
        "enable_gradient": true,
        "style_border": "",
        "layout_y_spacing": "min-h-[550px] max-h-[75vh] md:min-h-[60vh]",
        "layout_y_alignment": "items-center",
        "layout_x_alignment": "justify-center text-center",
        "visibility": ""
      }
    },
    "7c42deb3-6a19-4a7b-8346-5924594a4f25": {
      "type": "navigation-slider",
      "blocks": {
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-0": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_1_c6efcb65-d816-42ea-ba1c-96eb87868cd4.png",
            "heading": "Contour",
            "url": "shopify:\/\/collections\/contour"
          }
        },
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-1": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_2.png",
            "heading": "Ed-E Sun",
            "url": "shopify:\/\/collections\/ed-e-sun"
          }
        },
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-2": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_3.png",
            "heading": "Fasteners",
            "url": "shopify:\/\/collections\/fasteners-1"
          }
        },
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-3": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_4.png",
            "heading": "Floorintine",
            "url": "shopify:\/\/collections\/floorintine"
          }
        },
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-4": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_5.png",
            "heading": "Flushed",
            "url": "shopify:\/\/collections\/flushed"
          }
        },
        "6b5a1449-de4a-49c7-bac4-d9b68ddb82ea": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_6.png",
            "heading": "Form",
            "url": "shopify:\/\/collections\/form"
          }
        },
        "6ec70f40-837b-4f85-ac26-7e9f3785eb4d": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_7.png",
            "heading": "La Obra",
            "url": "shopify:\/\/collections\/la-obra"
          }
        },
        "c7086a21-b671-4e24-8432-973c9be40938": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_8.png",
            "heading": "Monument",
            "url": "shopify:\/\/collections\/monument"
          }
        },
        "73c82e19-304d-4eb0-801d-cb226c5aa19c": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_9.png",
            "heading": "Pipetech",
            "url": "shopify:\/\/collections\/pipetech"
          }
        },
        "d1bde515-1385-4d87-be57-a4ece11c1fce": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_10.png",
            "heading": "Terrace",
            "url": "shopify:\/\/collections\/terrace"
          }
        },
        "6ea89d8b-f09c-48d6-a04d-b13104d6094d": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_11.png",
            "heading": "Thunder Electric",
            "url": "shopify:\/\/collections\/thunder-electric"
          }
        },
        "8b1b577a-c425-40bd-b33a-c41b2bb06459": {
          "type": "slide",
          "settings": {
            "image_featured": "shopify:\/\/shop_images\/Frame_12.png",
            "heading": "System",
            "url": "shopify:\/\/collections\/system"
          }
        }
      },
      "block_order": [
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-0",
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-1",
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-2",
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-3",
        "template--17169339908369__7c42deb3-6a19-4a7b-8346-5924594a4f25-1671560411ad23cca8-4",
        "6b5a1449-de4a-49c7-bac4-d9b68ddb82ea",
        "6ec70f40-837b-4f85-ac26-7e9f3785eb4d",
        "c7086a21-b671-4e24-8432-973c9be40938",
        "73c82e19-304d-4eb0-801d-cb226c5aa19c",
        "d1bde515-1385-4d87-be57-a4ece11c1fce",
        "6ea89d8b-f09c-48d6-a04d-b13104d6094d",
        "8b1b577a-c425-40bd-b33a-c41b2bb06459"
      ],
      "settings": {
        "spacing_top": 5,
        "spacing_bottom": 5,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "visibility": "md:hidden"
      }
    },
    "47a456e2-05f6-45f1-95a7-b479fe45aac5": {
      "type": "content-grid",
      "blocks": {
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-0": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Tools",
            "button_url": "shopify:\/\/collections\/tools",
            "image_featured": "shopify:\/\/shop_images\/Frame_1_727723af-ea93-4075-be1d-6ecfea47b680.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-1": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Fasteners",
            "button_url": "shopify:\/\/collections\/fasteners-1",
            "image_featured": "shopify:\/\/shop_images\/Frame_2_9494ffbd-79ca-4fa8-b04c-a20c7433c0f9.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-2": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Electrical",
            "button_url": "shopify:\/\/collections\/electrical",
            "image_featured": "shopify:\/\/shop_images\/Frame_3_dc4a8a38-fbcf-4c89-a308-7847db15bd30.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "4ef13374-85cb-4ce4-84b4-039d4e8cb9ed": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Garden",
            "button_url": "shopify:\/\/collections\/garden",
            "image_featured": "shopify:\/\/shop_images\/Frame_4_85bf2f0e-e340-4f83-a252-d6d48d11bdd1.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "1a18c39b-dee0-4bdc-9656-329e5581149a": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Flooring",
            "button_url": "shopify:\/\/collections\/flooring",
            "image_featured": "shopify:\/\/shop_images\/Frame_6_09df0a73-a555-42a4-8427-105f45d25c23.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "d51a6d7f-1456-480f-88fa-287383c5a828": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Plumbing",
            "button_url": "shopify:\/\/collections\/plumbing",
            "image_featured": "shopify:\/\/shop_images\/Frame_5_558da449-6601-4703-b438-d120f8a3c2df.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "003628d3-3683-42fd-8e2f-2195a2e01f9d": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Lumber",
            "button_url": "shopify:\/\/collections\/lumber",
            "image_featured": "shopify:\/\/shop_images\/Frame_7_9193bba1-ba22-4461-a584-4ffaee29b5b5.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "e16b69c5-896b-4cb8-bd9e-e644628db621": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "Sale",
            "button_url": "shopify:\/\/collections\/sale",
            "image_featured": "shopify:\/\/shop_images\/Frame_8_efd96402-bb4c-42be-94c2-c350ef55d755.png",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "text-center justify-center",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        }
      },
      "block_order": [
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-0",
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-1",
        "template--17169339908369__47a456e2-05f6-45f1-95a7-b479fe45aac5-167185676051561857-2",
        "4ef13374-85cb-4ce4-84b4-039d4e8cb9ed",
        "1a18c39b-dee0-4bdc-9656-329e5581149a",
        "d51a6d7f-1456-480f-88fa-287383c5a828",
        "003628d3-3683-42fd-8e2f-2195a2e01f9d",
        "e16b69c5-896b-4cb8-bd9e-e644628db621"
      ],
      "settings": {
        "heading": "Shop by department",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "text-center justify-center flex-col items-center",
        "visibility": ""
      }
    },
    "a5996071-c096-4edd-a711-173b623c54a5": {
      "type": "product-grid",
      "blocks": {
        "template--16732988277009__a5996071-c096-4edd-a711-173b623c54a5-1666979337f6268656-0": {
          "type": "card",
          "settings": {
            "heading": "40% Tools",
            "content": "<p>Take up to 40% off our best selling tools.<\/p>",
            "button_label": "Shop Sale",
            "button_url": "shopify:\/\/collections\/sale"
          }
        }
      },
      "block_order": [
        "template--16732988277009__a5996071-c096-4edd-a711-173b623c54a5-1666979337f6268656-0"
      ],
      "settings": {
        "collection": "sale",
        "products_count": 7,
        "heading": "Deals of the week",
        "content": "<p>Take up to 40% off our best selling products this week.<\/p>",
        "button_label": "Shop Sale",
        "button_url": "shopify:\/\/collections\/sale",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn",
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "76fe60da-009f-44ae-8dc1-4912caebe748": {
      "type": "featured-product",
      "blocks": {
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-0": {
          "type": "title",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_thumbnails_product_type": false,
            "enable_thumbnails_vendor": false,
            "content": ""
          }
        },
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-1": {
          "type": "price",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-2": {
          "type": "add",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 5,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_quantity": false,
            "enable_dynamic_checkout": false,
            "content": ""
          }
        },
        "7047efab-7565-4d61-a7c4-2faa1de0fae1": {
          "type": "inventory",
          "settings": {
            "spacing_top": 5,
            "spacing_bottom": 20,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "threshold": 900
          }
        },
        "5c83445a-6b32-47e0-8d23-c7f6c875cca5": {
          "type": "description",
          "settings": {
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_open": true
          }
        }
      },
      "block_order": [
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-0",
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-1",
        "template--17169339908369__76fe60da-009f-44ae-8dc1-4912caebe748-16715704626f24cf9a-2",
        "7047efab-7565-4d61-a7c4-2faa1de0fae1",
        "5c83445a-6b32-47e0-8d23-c7f6c875cca5"
      ],
      "settings": {
        "product": "hexagon-marble",
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
        "layout_gallery_size": "w-full md:w-1\/2",
        "visibility": ""
      }
    },
    "9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8": {
      "type": "content-grid",
      "blocks": {
        "template--17169339908369__9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8-16715536444157b303-1": {
          "type": "content",
          "settings": {
            "heading": "Give your space a glow-up",
            "content": "<p>Revamp your living space with our stunning collection of new lighting fixtures, ranging from sleek and modern pendant lights to warm and inviting table lamps.<\/p>",
            "button_label": "Shop Lighting",
            "button_url": "shopify:\/\/collections\/lighting",
            "image_featured": "shopify:\/\/shop_images\/wu-yi-lOLfYckGMzI-unsplash_copy.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-overlay-2 color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__dark",
            "color_button": "btn btn--secondary",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-2",
            "enable_padding": true
          }
        },
        "template--17169339908369__9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8-16715536444157b303-0": {
          "type": "content",
          "settings": {
            "heading": "Are you a contractor?",
            "content": "<p>Sign up for our contractor pricing to receive the <strong>best deal on supplies<\/strong>.<\/p><p><br\/>✔️ 10% off store wide<\/p><p>✔️ industry news and guides<\/p><p>✔️ join our community of DIY-ers<\/p>",
            "button_label": "Sign up",
            "button_url": "shopify:\/\/pages\/contractor-pricing",
            "image_featured": "shopify:\/\/shop_images\/marissa-daeger-jCctpZe3sZo-unsplash_1.jpg",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 0,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-neutral color__text",
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
        }
      },
      "block_order": [
        "template--17169339908369__9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8-16715536444157b303-1",
        "template--17169339908369__9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8-16715536444157b303-0"
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
    "8c826e10-1fd2-449c-8568-b62ec5e511ee": {
      "type": "product-grid",
      "settings": {
        "collection": "lighting",
        "products_count": 8,
        "heading": "Brighten up",
        "content": "<p>Check out our newest arrivals, lighting!<\/p>",
        "button_label": "Shop all",
        "button_url": "shopify:\/\/collections\/lighting",
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "080a33e5-ce97-454e-a031-2e953de7c2a9": {
      "type": "content-grid",
      "blocks": {
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-0": {
          "type": "content",
          "settings": {
            "heading": "Tools",
            "content": "<p><a href=\"\/collections\/drill\" title=\"Drills\">Drills<\/a><\/p><p><a href=\"\/collections\/circular-saws\" title=\"Circular Saws\">Circular Saws<\/a><\/p><p><a href=\"\/collections\/jigsaws\" title=\"Jigsaws\">Jigsaws<\/a><\/p><p><a href=\"\/collections\/sanders\" title=\"Sanders\">Sanders<\/a><\/p><p><a href=\"\/collections\/tools\" title=\"Tools\"><strong>All tools<\/strong><\/a><\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-1": {
          "type": "content",
          "settings": {
            "heading": "Garden",
            "content": "<p><a href=\"\/collections\/gloves\" title=\"Gloves\">Gloves<\/a><\/p><p><a href=\"\/collections\/shovels\" title=\"Shovels\">Shovels<\/a><\/p><p><a href=\"\/collections\/wheelbarrows\" title=\"Wheelbarrows\">Wheelbarrows<\/a><\/p><p><a href=\"\/collections\/garden-tools\" title=\"Garden Tools\">Garden Tools<\/a><\/p><p><a href=\"\/collections\/garden\" title=\"Garden\"><strong>All garden<\/strong><\/a><\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-2": {
          "type": "content",
          "settings": {
            "heading": "Flooring & Tile",
            "content": "<p><a href=\"\/collections\/carpet\" title=\"Carpet\">Carpet<\/a><\/p><p><a href=\"\/collections\/hardwood\" title=\"Hardwood\">Hardwood<\/a><\/p><p><a href=\"\/collections\/tile\" title=\"Tile\">Tile<\/a><\/p><p><a href=\"\/collections\/flooring\" title=\"Flooring\"><strong>All flooring<\/strong><\/a><\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        },
        "2e1bdfb8-4d02-4587-9eba-3fbec968d1de": {
          "type": "content",
          "settings": {
            "heading": "Lighting",
            "content": "<p><a href=\"\/collections\/pendants\" title=\"Pendants\">Pendants<\/a><\/p><p><a href=\"\/collections\/sconces\" title=\"Sconces\">Sconces<\/a><\/p><p><a href=\"\/collections\/lamps\" title=\"Lamps\">Lamp<\/a><\/p><p><a href=\"\/collections\/chandeliers\" title=\"Chandeliers\">Chandelier<\/a> <\/p><p><a href=\"\/collections\/lighting\" title=\"Lighting\"><strong>All Lighting<\/strong><\/a><\/p>",
            "button_label": "",
            "button_url": "",
            "enable_autoplay": true,
            "enable_mute_toggle": true,
            "enable_loop": true,
            "spacing_top": 80,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "color_border": "color__border-divider-1",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1",
            "enable_padding": true
          }
        }
      },
      "block_order": [
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-0",
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-1",
        "template--17169339908369__080a33e5-ce97-454e-a031-2e953de7c2a9-1671851551ebb26559-2",
        "2e1bdfb8-4d02-4587-9eba-3fbec968d1de"
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
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "faa4a2e7-da36-4d7c-a137-62dffe0a444c": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 3,
        "heading": "Expand your skills",
        "content": "<p>Not only do we have the tools you need, learn how to use them here.<\/p>",
        "button_label": "See All",
        "button_url": "shopify:\/\/blogs\/news",
        "spacing_top": 80,
        "spacing_bottom": 80,
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": "",
        "enable_author": true,
        "enable_summary": true,
        "enable_date": true,
        "enable_tags": false
      }
    },
    "a3d6d847-821a-4004-9663-bdd0b1c01550": {
      "type": "icon-grid",
      "blocks": {
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-0": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/truck.png",
            "icon_height": "h-8",
            "heading": "Fast shipping",
            "content": "<p>Get your products next day with our overnight shipping service.<\/p>",
            "color_scheme": "color__bg-secondary color__secondary",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-col",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-1": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/chat.png",
            "icon_height": "h-8",
            "heading": "Friendly service",
            "content": "<p><a href=\"\/pages\/contact\" title=\"Contact\">Talk to our experts<\/a> to help you get your project done right.<\/p>",
            "color_scheme": "color__bg-secondary color__secondary",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-col",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1",
            "enable_padding": true
          }
        },
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-2": {
          "type": "icon",
          "settings": {
            "icon": "shopify:\/\/shop_images\/location.png",
            "icon_height": "h-8",
            "heading": "In-store pickup",
            "content": "<p>Need it now? Place and order and pick up at your <a href=\"\/pages\/locations\" title=\"Locations\">local store today<\/a><\/p>",
            "color_scheme": "color__bg-secondary color__secondary",
            "color_border": "!color__border-transparent",
            "layout_alignment": "flex-col",
            "layout_x_alignment": "text-left",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md:col-span-1",
            "enable_padding": true
          }
        }
      },
      "block_order": [
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-0",
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-1",
        "template--17430355149073__a3d6d847-821a-4004-9663-bdd0b1c01550-16728634047c8b2e44-2"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 20,
        "spacing_bottom": 20,
        "color_scheme": "color__bg-secondary color__secondary",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    }
  },
  "order": [
    "1658853151e8c4f7dd",
    "7c42deb3-6a19-4a7b-8346-5924594a4f25",
    "47a456e2-05f6-45f1-95a7-b479fe45aac5",
    "a5996071-c096-4edd-a711-173b623c54a5",
    "76fe60da-009f-44ae-8dc1-4912caebe748",
    "9f7b9bfc-fd99-49f0-9cc6-65b1b51880f8",
    "8c826e10-1fd2-449c-8568-b62ec5e511ee",
    "080a33e5-ce97-454e-a031-2e953de7c2a9",
    "faa4a2e7-da36-4d7c-a137-62dffe0a444c",
    "a3d6d847-821a-4004-9663-bdd0b1c01550"
  ]
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
        "color_scheme": "color__bg-overlay-1 color__text",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "style_border": "border--b-width",
        "layout_y_spacing": "min-h-[300px] md:min-h-[300px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start",
        "visibility": "",
        "enable_description": true,
        "enable_image": false
      }
    },
    "grid": {
      "type": "collection__main",
      "blocks": {
        "e3935f42-4b36-4289-b5d2-fc6f9b1aa4d4": {
          "type": "newsletter",
          "settings": {
            "heading": "SAVE 10%",
            "content": "<p>Sign up for our newsletter and save 10% on your first order<\/p>",
            "button_label": "Subscribe",
            "disclaimer": "",
            "success": "<p>Thanks for subscribing<\/p>",
            "index": 7,
            "background_color_scheme": "color__bg-neutral color__text",
            "column_size": "col-span-2"
          }
        }
      },
      "block_order": [
        "e3935f42-4b36-4289-b5d2-fc6f9b1aa4d4"
      ],
      "settings": {
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-5",
        "row_size_mobile": "grid grid-cols-2",
        "enable_sort": true,
        "enable_filter": true,
        "products_per_page": 23
      }
    },
    "recent": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--t-width",
        "visibility": ""
      }
    },
    "ef31c567-5a9b-4a67-99d6-be9d41e9e767": {
      "type": "content-grid",
      "blocks": {
        "template--16732987982097__ef31c567-5a9b-4a67-99d6-be9d41e9e767-166701556426d40da3-0": {
          "type": "content",
          "settings": {
            "heading": "",
            "content": "",
            "button_label": "",
            "button_url": "",
            "image_featured": "shopify:\/\/shop_images\/ra-dragon-1LWXx9kwlLw-unsplash.jpg",
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
            "layout_col_span": "col-span-1 md: md:col-span-2"
          }
        },
        "template--16732987982097__ef31c567-5a9b-4a67-99d6-be9d41e9e767-166701556426d40da3-1": {
          "type": "content",
          "settings": {
            "heading": "✓ Price match gurantee",
            "content": "<p>If you can find a better price we'll match it. It's that simple.<br\/><\/p>",
            "button_label": "Learn more",
            "button_url": "\/",
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
            "layout_col_span": "col-span-1 md: md:col-span-2"
          }
        }
      },
      "block_order": [
        "template--16732987982097__ef31c567-5a9b-4a67-99d6-be9d41e9e767-166701556426d40da3-0",
        "template--16732987982097__ef31c567-5a9b-4a67-99d6-be9d41e9e767-166701556426d40da3-1"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 60,
        "spacing_bottom": 60,
        "color_scheme": "color__bg-neutral color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--t-width",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-1",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    }
  },
  "order": [
    "banner",
    "grid",
    "recent",
    "ef31c567-5a9b-4a67-99d6-be9d41e9e767"
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
        "show_entire_image": false,
        "enable_lazy_loading": false,
        "show_video_background_mobile": true,
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "enable_gradient": false,
        "style_border": "",
        "layout_y_spacing": "min-h-[250px] md:min-h-[350px]",
        "layout_y_alignment": "items-end",
        "layout_x_alignment": "justify-start"
      }
    },
    "main": {
      "type": "list-collections__main",
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "row_size_desktop": "md:grid-cols-4",
        "row_size_mobile": "grid-cols-2",
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

<summary>templates/product.json</summary>

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
            "style_border": ""
          }
        },
        "6963d72e-056b-4a9f-879f-6bc3c1f25bb5": {
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
            "content": "<p>✓ Lifetime warranty<\/p><p>✓ Price match gurantee<\/p>",
            "spacing_top": 0,
            "spacing_bottom": 10,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_thumbnails_product_type": true,
            "enable_thumbnails_vendor": true,
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
        "6f7d1dc8-0cd8-44b4-b1ad-eb1d95259c8c": {
          "type": "options",
          "settings": {
            "spacing_top": 15,
            "spacing_bottom": 0,
            "color_scheme": "color__bg-body color__text",
            "style_border": ""
          }
        },
        "b78b560b-e1c2-428d-ad73-fb5f8aac6d53": {
          "type": "add",
          "settings": {
            "content": "<p>Free In-Store Pickup \/ Free Shipping Over $150<\/p>",
            "spacing_top": 15,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_quantity": true,
            "enable_dynamic_checkout": false,
            "enable_gift_card_recipient": false
          }
        },
        "9f1692ea-ccb9-4e4c-9c83-7a6ae53392aa": {
          "type": "inventory",
          "settings": {
            "spacing_top": 0,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width",
            "threshold": 100
          }
        },
        "c18a6be5-7074-4b70-a8e1-d4f845a9e665": {
          "type": "pickup",
          "settings": {
            "spacing_top": 15,
            "spacing_bottom": 15,
            "color_scheme": "color__bg-body color__text",
            "style_border": "border--b-width"
          }
        },
        "123fd04c-91f3-4248-a65a-614e2f64fdeb": {
          "type": "description",
          "settings": {
            "color_scheme": "color__bg-body color__text",
            "style_border": "",
            "enable_open": true
          }
        },
        "789d2687-28d2-4342-84dd-7045cbdff0ba": {
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
            "content": "<p>✓ Free In-Store Pickup <\/p><p>✓ Free Shipping Over $150<\/p>",
            "color_scheme": "color__bg-body color__text",
            "on_scroll": true
          }
        }
      },
      "block_order": [
        "bef9bd40-2a8e-45c2-ae54-59c9ef6f0e26",
        "6963d72e-056b-4a9f-879f-6bc3c1f25bb5",
        "853ae7f0-85c9-45dc-8326-6e4044bcf5e5",
        "62c29cd6-a0b5-4f8b-86c0-a48660869d22",
        "6f7d1dc8-0cd8-44b4-b1ad-eb1d95259c8c",
        "b78b560b-e1c2-428d-ad73-fb5f8aac6d53",
        "9f1692ea-ccb9-4e4c-9c83-7a6ae53392aa",
        "c18a6be5-7074-4b70-a8e1-d4f845a9e665",
        "123fd04c-91f3-4248-a65a-614e2f64fdeb",
        "789d2687-28d2-4342-84dd-7045cbdff0ba",
        "848f5aea-f7ad-4974-a5fb-020776e3e523"
      ],
      "settings": {
        "enable_default_variant": true,
        "spacing_top": 0,
        "spacing_bottom": 0,
        "media_gallery_style": "thumbnail-slider",
        "image_border": "!color__border-transparent",
        "enable_zoom": true,
        "enable_alt": false,
        "enable_variant_images": false,
        "media_color_scheme": "color__bg-body color__text",
        "media_ratio": "aspect-[1\/1] aspect-w-1 aspect-h-1",
        "media_object-sizing": "contain",
        "enable_ratio": true,
        "show_product_badges": true,
        "color_scheme": "color__bg-body",
        "color_border": "color__border-transparent",
        "layout_gallery_size": "w-full md:w-1\/2"
      }
    },
    "1c24b664-ff9e-4174-bc19-b1720ec32498": {
      "type": "content-grid",
      "blocks": {
        "template--16732988440849__1c24b664-ff9e-4174-bc19-b1720ec32498-166690057708a480b3-0": {
          "type": "content",
          "settings": {
            "heading": "✓ Lifetime warranty",
            "content": "<p>All our products are backed by our award winning lifetime warranty.<br\/><br\/><a href=\"\/\" title=\"\/\">Learn more<\/a><\/p>",
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
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "template--16732988440849__1c24b664-ff9e-4174-bc19-b1720ec32498-166690057708a480b3-1": {
          "type": "content",
          "settings": {
            "heading": "✓ Price match",
            "content": "<p>If you can find a better price we'll match it. It's that simple. <br\/><br\/><a href=\"\/\" title=\"\/\">Learn more<\/a><\/p>",
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
            "color_button": "btn btn--plain",
            "enable_gradient": false,
            "layout_y_alignment": "items-end",
            "layout_x_alignment": "",
            "layout_row_span": "row-span-1",
            "layout_col_span": "col-span-1 md: md:col-span-1"
          }
        },
        "afa46e39-e6b9-4df7-ac7d-28da7fface33": {
          "type": "content",
          "settings": {
            "heading": "✓ Friendly support",
            "content": "<p>24\/7 support available. Give us a call and we'll help out.<br\/><br\/><a href=\"\/\" title=\"\/\">Learn more<\/a><\/p>",
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
        "template--16732988440849__1c24b664-ff9e-4174-bc19-b1720ec32498-166690057708a480b3-0",
        "template--16732988440849__1c24b664-ff9e-4174-bc19-b1720ec32498-166690057708a480b3-1",
        "afa46e39-e6b9-4df7-ac7d-28da7fface33"
      ],
      "settings": {
        "heading": "",
        "content": "",
        "button_label": "",
        "button_url": "",
        "spacing_top": 100,
        "spacing_bottom": 80,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--t-width",
        "row_size_desktop": "md:grid-cols-3",
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
            "content": "<p>Free shipping will automatically be applied to all domestic orders over $150. Simply add over $150 to your cart and you will see the discount while checking out.<\/p>"
          }
        },
        "165592515344a810fb-1": {
          "type": "content",
          "settings": {
            "title": "Do you have curbside pickup?",
            "content": "<p>Yes, simply choose the location for pikcup on checkout. <\/p>"
          }
        },
        "165592515344a810fb-2": {
          "type": "content",
          "settings": {
            "title": "How do I contact you for help?",
            "content": "<p>For help, go to our <a href=\"\/pages\/contact\" title=\"Contact\">Contact<\/a> page to reach out to one of our associates.<\/p>"
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
        "button_url": "\/",
        "spacing_top": 0,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--plain",
        "style_border": "border--b-width",
        "layout_x_alignment": "justify-between",
        "visibility": ""
      }
    },
    "1669837915df3f5dd0": {
      "type": "apps",
      "blocks": {
        "9361c0e7-8e3b-47f1-b419-77b7c7f774d8": {
          "type": "shopify:\/\/apps\/product-reviews\/blocks\/reviews\/bae150af-8da8-48b2-9867-398188115e5f",
          "settings": {
          }
        }
      },
      "block_order": [
        "9361c0e7-8e3b-47f1-b419-77b7c7f774d8"
      ],
      "settings": {
        "spacing_top": 80,
        "spacing_bottom": 80,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width",
        "layout_padding": true
      }
    },
    "1649436645dda33170": {
      "type": "recent-slider",
      "settings": {
        "heading": "Recently viewed",
        "content": "",
        "spacing_top": 100,
        "spacing_bottom": 100,
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "",
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
        "spacing_top": 0,
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
    "1c24b664-ff9e-4174-bc19-b1720ec32498",
    "165592515341576314",
    "1669837915df3f5dd0",
    "1649436645dda33170",
    "1649436653425ff0fe"
  ]
}
```

</details>

<details>

<summary>templates/page.about.json</summary>

```json
{
  "sections": {
    "main": {
      "type": "page__main",
      "settings": {
        "color_scheme": "color__bg-body color__text"
      }
    },
    "74969cba-1d32-4237-bd1b-20391f5fe0dd": {
      "type": "content-grid",
      "blocks": {
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-0": {
          "type": "content",
          "settings": {
            "heading": "Block heading",
            "content": "<p>Describe a product, make announcements, or welcome customers to your store.<\/p>",
            "button_label": "Button",
            "button_url": "\/",
            "color_scheme": "color__bg-body color__text",
            "color_text": "color__text",
            "color_button": "btn",
            "enable_gradient": false
          }
        },
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-1": {
          "type": "content",
          "settings": {
            "heading": "Block heading",
            "content": "<p>Describe a product, make announcements, or welcome customers to your store.<\/p>",
            "button_label": "Button",
            "button_url": "\/",
            "color_scheme": "color__bg-body color__text",
            "color_text": "color__text",
            "color_button": "btn btn--secondary",
            "enable_gradient": false
          }
        },
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-2": {
          "type": "content",
          "settings": {
            "heading": "Block heading",
            "content": "<p>Describe a product, make announcements, or welcome customers to your store.<\/p>",
            "button_label": "Button",
            "button_url": "\/",
            "color_scheme": "color__bg-body color__text",
            "color_text": "color__text",
            "color_button": "btn btn--plain",
            "enable_gradient": true
          }
        }
      },
      "block_order": [
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-0",
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-1",
        "template--14375215431953__74969cba-1d32-4237-bd1b-20391f5fe0dd-16656865557c89a1ea-2"
      ],
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "style_border": "border--b-width"
      }
    },
    "23ffcfd4-b279-4466-90a2-26744a2fa8c1": {
      "type": "newsletter",
      "blocks": {
        "template--14375215431953__23ffcfd4-b279-4466-90a2-26744a2fa8c1-1665686556fbb80088-0": {
          "type": "newsletter",
          "settings": {
            "heading": "Email sign-up",
            "content": "<p>Tell customers why they should subscribe to your newsletter.<\/p>",
            "button_label": "Subscribe",
            "disclaimer": "<p><\/p>",
            "success": "<p>Thanks for subscribing<\/p>",
            "layout_desktop_width": 5,
            "layout_mobile_width": 12
          }
        },
        "template--14375215431953__23ffcfd4-b279-4466-90a2-26744a2fa8c1-1665686556fbb80088-1": {
          "type": "image",
          "settings": {
            "layout_desktop_width": 6,
            "layout_mobile_width": 12
          }
        }
      },
      "block_order": [
        "template--14375215431953__23ffcfd4-b279-4466-90a2-26744a2fa8c1-1665686556fbb80088-0",
        "template--14375215431953__23ffcfd4-b279-4466-90a2-26744a2fa8c1-1665686556fbb80088-1"
      ],
      "settings": {
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "layout_alignment": "items-start"
      }
    },
    "cdea5a9c-ef8b-42f6-abc4-af3b10bb772a": {
      "type": "article-grid",
      "settings": {
        "blog": "news",
        "items_count": 3,
        "heading": "Blog posts",
        "content": "<p>Explain what customers can expect from your content and the blog posts you've published.<\/p>",
        "button_label": "Button",
        "button_url": "\/",
        "color_scheme": "color__bg-body color__text",
        "color_border": "color__border-divider-1",
        "color_button": "btn btn--secondary",
        "style_border": "border--b-width",
        "row_size_desktop": "md:grid-cols-3",
        "row_size_mobile": "grid grid-cols-2",
        "enable_author": true,
        "enable_summary": true,
        "enable_date": true,
        "enable_tags": false
      }
    }
  },
  "order": [
    "main",
    "74969cba-1d32-4237-bd1b-20391f5fe0dd",
    "23ffcfd4-b279-4466-90a2-26744a2fa8c1",
    "cdea5a9c-ef8b-42f6-abc4-af3b10bb772a"
  ]
}
```

</details>

<details>

<summary>templates/blog.json</summary>

```json
{
  "sections": {
    "16558222329618bae3": {
      "type": "blog__banner",
      "settings": {
        "video_background": "",
        "content": "<p>Need inspiration? Check out some of our project ideas for your next home update. <\/p>",
        "button_label": "",
        "button_url": "\/collections\/all",
        "color_scheme": "color__bg-overlay-1",
        "color_text": "color__text",
        "color_border": "color__border-divider-1",
        "button_color": "btn",
        "enable_gradient": false,
        "style_border": "",
        "layout_y_spacing": "min-h-[250px] md:min-h-[350px]",
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
        "enable_author": false,
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

<summary>templates/article.json</summary>

```json
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
            "style_border": "border--b-width"
          }
        },
        "797ba560-2717-42ee-a1dc-547f7f40f214": {
          "type": "share",
          "settings": {
            "spacing_top": 20,
            "spacing_bottom": 20,
            "color_border": "color__border-divider-1",
            "style_border": "border--b-width"
          }
        },
        "f5ee0741-2dcf-40c5-8755-319620ca5fa2": {
          "type": "comment",
          "settings": {
            "spacing_top": 10,
            "spacing_bottom": 10,
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
