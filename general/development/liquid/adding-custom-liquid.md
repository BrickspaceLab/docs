# Adding custom liquid

The Custom liquid section can be used to add any code snippet to a template. This is a great way to add app install scripts if an app requires manual installation. This is a great approach to take - your theme code remains un-edited and you still have access to easily update the theme.

{% stepper %}
{% step %}
**Add Custom liquid section**

* Click **Add section**.
* Click **Custom liquid** to add the section.

{% hint style="info" %}
If you want to install a code snippet across your entire site then you can move your section to the Footer group.
{% endhint %}
{% endstep %}

{% step %}
**Add your code**

* Paste in your code.
* Remove the section padding and borders.
* This section renders liquid so if you plan to add JavaScript or CSS you'll need to include that within a `<script>` or a `style` tag.
{% endstep %}

{% step %}
#### Save your changes

Click **Save**
{% endstep %}
{% endstepper %}
