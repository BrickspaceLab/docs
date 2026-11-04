# Cart

Cart settings in **Theme settings > Cart** control what happens after cart updates on desktop and mobile, what happens when customers use the cart control, and an optional minimum order amount.



## How to change theme cart

{% stepper %}
{% step %}
### Set desktop and mobile behavior

* Open **Theme settings > Cart**.
* Set **Desktop cart behavior** for cart updates on large screens.
* Set **Mobile cart behavior** for cart updates on small screens.
{% endstep %}

{% step %}
### Set cart button behavior

* Set **Cart button behavior** for clicks on cart buttons or icons.
{% endstep %}

{% step %}
### Optional: minimum order

* Enter **Minimum order amount** if checkout should require a minimum. Use the format described in the table below.
{% endstep %}

{% step %}
### Test both viewports

* Add items and open the cart on desktop and mobile to confirm overlays or redirects match your flow.
{% endstep %}
{% endstepper %}



### Notes on cart behavior

* **Desktop cart behavior** and **Mobile cart behavior** apply after cart updates; **Cart button behavior** applies when opening the cart from navigation.
* If a cart overlay is already open, the theme does not open a second overlay on update.



## Cart settings

| Setting                 | What it controls                                                                 |
| ----------------------- | -------------------------------------------------------------------------------- |
| Desktop cart behavior   | After updates on desktop: primary overlay, alternative overlay, redirect to cart, or redirect to checkout. Default **Open primary cart overlay**. |
| Mobile cart behavior    | After updates on mobile: same options. Default **Open alternative cart overlay**. |
| Cart button behavior    | When using the cart control: primary overlay, alternative overlay, go to cart, or go to checkout. Default **Open primary cart overlay**. |
| Minimum order amount    | Minimum subtotal before checkout. Enter no currency symbol and no decimal point (for example, `10000` for $100.00 in a two-decimal currency). Blank means no minimum. |
