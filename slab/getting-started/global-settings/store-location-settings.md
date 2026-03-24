# Store location

Store location settings in **Theme settings > Store location** control optional local business information and the Mapbox key used for dynamic maps.



## How to change theme store location

{% stepper %}
{% step %}
### Enable local business

* Open **Theme settings > Store location**.
* Turn **Enable local business** on if you want the theme to output local business details for search and rich results (useful for a single physical location).
{% endstep %}

{% step %}
### Add Mapbox when needed

* If your theme uses a Mapbox map, enter **Mapbox API key**.
* See [Creating a Mapbox API key](https://help.brickspacelab.com/en/articles/9939363-creating-a-mapbox-api-key) if you need to create one.
{% endstep %}

{% step %}
### Confirm store address

* Set your address in Shopify admin **Settings > General** so it matches your real location.
{% endstep %}
{% endstepper %}



### Notes on store location

* Turn **Enable local business** off if you do not want that metadata or you have no public address.
* The Mapbox key is only required where a dynamic map uses Mapbox.



## Store location settings

| Setting               | What it controls                                                                 |
| --------------------- | -------------------------------------------------------------------------------- |
| Enable local business | Shares local business details with search and rich results where supported. Default off. |
| Mapbox API key        | Key for Mapbox-powered maps. Required only where those maps are used.              |
