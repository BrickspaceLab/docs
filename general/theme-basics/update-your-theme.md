# Update your theme

Our themes are updated regularly with new features, general improvements, and bug fixes.&#x20;

Your theme will automatically update for minor fixes. Unfortunetly, Shopify does not automatically update themes for major updates or when you've made customizations to the theme code. If the code has been edited, you can install updates manually or [hire an expert](../support/hire-a-shopify-developer.md) for assistance.

Visit the Shopify help center to [learn more about updating themes](https://help.shopify.com/en/manual/online-store/themes/managing-themes/updating-themes).



### FAQs <a href="#h_ca638b6997" id="h_ca638b6997"></a>

<details>

<summary>How do I check what theme version I’m using?</summary>

The theme version is listed in a few places in your Shopify dashboard. To find this go to Shopify then navigate to **Online Store > Themes**. From here you view your installed themes and see which version each theme is using.

</details>

<details>

<summary>How do I check which theme version is the latest?</summary>

To confirm you are using the latest version, please refer to the Shopify theme store to reference the most recent released version. You can also find a notice in your Shopify dashboard that will highlight when a theme has a new version available. This can be seen when you navigate to **Online Store > Themes**.

</details>

<details>

<summary>How important is it to update to the latest version?</summary>

Update your theme is not a requirement. If you see we’ve released new features you’d like to take advantage of then updating would be the best option. It is generally a good idea to update to the latest version at least once a year - this way you get new features, improved performance and bug fixes.

</details>



### How to transfer settings after updating <a href="#h_a45de23e11" id="h_a45de23e11"></a>

{% hint style="info" %}
This process does not copy over code changes. If you’ve made code changes those will have to manually be copied over to your new theme.
{% endhint %}

{% stepper %}
{% step %}
#### Install the latest version

1. Sign in to your Shopify account
2. Click the dropdown in your Shopify theme to view the version number
3. Click “Add to theme library”
{% endstep %}

{% step %}
#### Back up your themes

1. Before continuing further it’s a good idea to create a backup copy of your themes
   * Learn more about [duplicating themes](https://help.shopify.com/en/manual/online-store/themes/managing-themes/duplicating-themes)
{% endstep %}

{% step %}
#### Transfer theme settings

1. In one tab open your original theme in the Code editor
   * Go to Online store > Themes > Actions > Edit code
2. In a second tab open the new theme in the Code editor
3. In your original theme, open the file settings\_data.json and copy the entire contents
4. In your new theme, open the file settings\_data.json then delete the entire file contents and paste the content you just copied
{% endstep %}

{% step %}
#### Transfer sections and block settings

1. In one tab open your original theme in the Code editor
   * Go to Online store > Themes > Actions > Edit code
2. In a second tab open the new theme in the Code editor
3. In your original theme, open the templates directory and take note of each file with a blue circle icon
   * For each file with a blue icon:
     1. In your original theme, open the file with a blue icon, copy the contents
     2. In your new theme, overwrite the file’s content by pasting the content you copied from the original theme


{% endstep %}
{% endstepper %}
