# Embed YouTube videos

Use a **Custom Liquid** block to add a YouTube video anywhere in Keystone where blocks are supported.

## Add a YouTube embed

1. In Shopify admin, go to **Online Store > Themes**.
2. Click **Customize** on your active Keystone theme.
3. Navigate to the section where you want to show the video.
4. Add a **Custom Liquid** block.
5. In YouTube, open your video, click **Share > Embed**, and copy the embed code.
6. Paste the embed code into the Custom Liquid block, then save.

Example:

```html
<span>
  <iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/ALiyPTbL8Rg?si=rQKonpMMXeYSjJGC"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</span>
```

## Make the video full width (optional)

If you want the video to scale to the full width of its container, wrap each embed in a `.video-wrapper` element and add the CSS below.

```html
<div class="video-wrapper">
  <!-- Paste your YouTube embed code here -->
  <iframe
    src="https://www.youtube.com/embed/ALiyPTbL8Rg?si=rQKonpMMXeYSjJGC"
    title="YouTube video player"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</div>

<style>
  .video-wrapper {
    position: relative;
    padding-bottom: 56.25%; /* 16:9 ratio */
    height: 0;
    overflow: hidden;
    margin-bottom: 20px; /* spacing between videos */
  }

  .video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }
</style>
```

> Support note: If the responsive styling does not apply, place the `<style>` block before the first `<div class="video-wrapper">` block in your Custom Liquid content.

To add multiple videos, repeat the `<div class="video-wrapper">...</div>` block for each video.
