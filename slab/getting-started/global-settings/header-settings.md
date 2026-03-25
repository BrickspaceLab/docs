# Header

Header settings in **Theme settings > Header** control how the header behaves while customers scroll and whether top sections can render under the header when overlap is enabled at the theme and section level.



## How to change theme header

{% stepper %}
{% step %}
### Choose header position

* Open **Theme settings > Header**.
* Under **Position**, choose **Sticky**, **Standard**, or **Dynamic**.
* Preview desktop and mobile before changing overlap.
{% endstep %}

{% step %}
### Configure overlap

* Turn on **Enable header overlap** only when top sections are designed for content under the header.
* Set **Desktop overlap** and **Mobile overlap** when overlap is enabled.
{% endstep %}

{% step %}
### Enable overlap on sections

* Open each section that should sit under the header.
* Turn on that section’s **Enable header overlap** setting.
* If either the theme-level or section-level overlap setting is off, the section stays in normal flow.
{% endstep %}
{% endstepper %}



### Notes on header behavior

* **Sticky** keeps the header visible while scrolling; **Standard** scrolls with the page; **Dynamic** can hide the header while scrolling down and show it when scrolling up—preview your main templates.
* Overlap values use 5 px steps from 5 to 200 px; tune them to your logo and bar height.



## Header settings

| Setting                 | What it controls                                                                 |
| ----------------------- | -------------------------------------------------------------------------------- |
| Position                | **Sticky**, **Standard**, or **Dynamic**. Default **Standard**.                  |
| Enable color difference | When enabled, header content can invert over overlapping page content for contrast. Default off. Best with light-on-dark or high-contrast artwork. |
| Enable header overlap   | Allows supported sections to render under the header when their overlap is on. Default off. |
| Desktop overlap         | Overlap offset on desktop when overlap is enabled (5–200 px, step 5, default 90 px). |
| Mobile overlap          | Overlap offset on mobile when overlap is enabled (5–200 px, step 5, default 80 px). |
