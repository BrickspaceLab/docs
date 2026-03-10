# Subscription options

Shopify subscriptions can be a bit tricky to setup. This guide will walk you through different options for displaying subscription options on your product page.

#### Using the built-in subscription options

Our Shopify themes come with built‑in subscription options. We recommend using this approach as you'll have more control over the experience and can customize this with the help of a developer.

However, this may cause complications with your product templates if you've already installed a third-party subscription widget.

* Ensure the third‑party subscription widget is disabled
* Ensure the product block Options is included on your product template

#### Using third-party subscription options

Disabling the default subscription options is possible if you'd like to stick to using a third‑party widget. There are a few more steps here.

{% stepper %}
{% step %}
Go to **Online** **Store** > **Themes** > **Customize**
{% endstep %}

{% step %}
Click the top dropdown > **Products** > **Create template**
{% endstep %}

{% step %}
Label this template "subscription"
{% endstep %}

{% step %}
On the left-hand side, click into the **Product** section
{% endstep %}

{% step %}
Check **Enable default selling plan widget**
{% endstep %}

{% step %}
On the left-hand side, click into the **Options** block and click **Remove block**
{% endstep %}

{% step %}
Go into your subscription app and follow instructions to install the subscription widget
{% endstep %}

{% step %}
Assign the "subscription" product template to all products that have a subscription plan
{% endstep %}

{% step %}
Hit **Save**
{% endstep %}
{% endstepper %}
