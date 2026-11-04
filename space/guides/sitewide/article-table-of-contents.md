# Article table of contents

***

## Create metafield definition

1. Navigate to Settings > Custom data > Blog posts
2. Click Add definition
3. In the name field type "Table of contents"
4. Ensure the namespace and key field is `custom.table_of_contents`
5. Click Select type and select "Single line text"
6. Select List of values
7. Click save

[![](https://downloads.intercomcdn.com/i/o/1200374601/91a97cfc6fb36e9c972ea93d/CleanShot+2024-10-01+at+13_32_14%402x.png?expires=1744835400\&signature=aca077e5e45c0cd734f8306e5782aee452f18428ad17286dfa2211fecf73ab4c\&req=dSInFsp5mYdfWPMW1HO4zRjQF3hZJEh8kAEtwK17CEVjfQB1m5%2FPv%2BI%2FNVb1%0AedGmyqvm8a05zRuMFBg%3D%0A)](https://downloads.intercomcdn.com/i/o/1200374601/91a97cfc6fb36e9c972ea93d/CleanShot+2024-10-01+at+13_32_14%402x.png?expires=1744835400\&signature=aca077e5e45c0cd734f8306e5782aee452f18428ad17286dfa2211fecf73ab4c\&req=dSInFsp5mYdfWPMW1HO4zRjQF3hZJEh8kAEtwK17CEVjfQB1m5%2FPv%2BI%2FNVb1%0AedGmyqvm8a05zRuMFBg%3D%0A)

## Update metafield values

1. Navigate to the blog post you'd like to update
2.  Scroll to the bottom and click Show all next to metafields

    [![](https://downloads.intercomcdn.com/i/o/1200379290/e6d714566cbadcb3b9877bcb/CleanShot+2024-10-01+at+13_33_55%402x.png?expires=1744835400\&signature=1f06cc21110d1b74f1086d94f99e54e5c1c88e28ad7d61399cd06360ca43a298\&req=dSInFsp5lINWWfMW1HO4zdNnDOd8349bd8WmKbRlzGSdeNVxOGSeJu96i%2Bxm%0AfzNn%0A)](https://downloads.intercomcdn.com/i/o/1200379290/e6d714566cbadcb3b9877bcb/CleanShot+2024-10-01+at+13_33_55%402x.png?expires=1744835400\&signature=1f06cc21110d1b74f1086d94f99e54e5c1c88e28ad7d61399cd06360ca43a298\&req=dSInFsp5lINWWfMW1HO4zdNnDOd8349bd8WmKbRlzGSdeNVxOGSeJu96i%2Bxm%0AfzNn%0A)
3.  Enter in values for each heading you want to appear in your table of contents

    [![](https://downloads.intercomcdn.com/i/o/1200398712/c8b2bc38f7da460a834df5be/CleanShot%2B2024-10-01%2Bat%2B13_35_31-402x.png?expires=1744835400\&signature=c121cdec98b7c1c117ff5c98676901ae06ce2296b46325dda5d01a544570b090\&req=dSInFsp3lYZeW%2FMW1HO4zZaQvQHxn2CIB0rSvJKWpydv6FYZMStM95qk3XPT%0A4stm%0A)](https://downloads.intercomcdn.com/i/o/1200398712/c8b2bc38f7da460a834df5be/CleanShot%2B2024-10-01%2Bat%2B13_35_31-402x.png?expires=1744835400\&signature=c121cdec98b7c1c117ff5c98676901ae06ce2296b46325dda5d01a544570b090\&req=dSInFsp3lYZeW%2FMW1HO4zZaQvQHxn2CIB0rSvJKWpydv6FYZMStM95qk3XPT%0A4stm%0A)

## Add block

1. In the Shopify theme editor navigate to the blog post template
2. Click Add block under Article main
3. Search and select "Table of contents"

[![](https://downloads.intercomcdn.com/i/o/1200387726/ce09a886b1628f0ccfceeb9b/CleanShot+2024-10-01+at+13_42_34%402x.png?expires=1744835400\&signature=0d4f5fcb624ce21b26bb1c516d56ecd0186ca9758b8516da1d38fdbfac4a23a6\&req=dSInFsp2moZdX%2FMW1HO4zUZwRjp8RRdqws%2BBjExlBupczgJUnj8ViKaHNyBP%0AcEbV50jYJDi1dYhZMno%3D%0A)](https://downloads.intercomcdn.com/i/o/1200387726/ce09a886b1628f0ccfceeb9b/CleanShot+2024-10-01+at+13_42_34%402x.png?expires=1744835400\&signature=0d4f5fcb624ce21b26bb1c516d56ecd0186ca9758b8516da1d38fdbfac4a23a6\&req=dSInFsp2moZdX%2FMW1HO4zUZwRjp8RRdqws%2BBjExlBupczgJUnj8ViKaHNyBP%0AcEbV50jYJDi1dYhZMno%3D%0A)

## Update headings

1. In Shopify navigate to the blog post you'd like to update
2. Click the "Show HTML" icon on your blog content
3. Add id="HEADING-NAME" to your heading tags
   1. The id attribute should match the table of contents
   2. For example, you click a table of contents link you'll notice the URL bar is updated - this will give you the value that is needed for your id attribute
   3.  The heading tags should now look like this

       ```
       <h1 id="your-heading-text">Your Heading Text</h1>
       ```

       [![](https://downloads.intercomcdn.com/i/o/1200396515/e07b0686cf8333df4de12f10/CleanShot+2024-10-01+at+13_48_22%402x.png?expires=1744835400\&signature=35b6618068257e70deb8579b3750374d90cd370cfc977ce99c67e91ab3844527\&req=dSInFsp3m4ReXPMW1HO4zfEMOZL2qXiWwB8wgKQjqmGKy5OWIgY6CWFXtsr4%0AVpO4%0A)](https://downloads.intercomcdn.com/i/o/1200396515/e07b0686cf8333df4de12f10/CleanShot+2024-10-01+at+13_48_22%402x.png?expires=1744835400\&signature=35b6618068257e70deb8579b3750374d90cd370cfc977ce99c67e91ab3844527\&req=dSInFsp3m4ReXPMW1HO4zfEMOZL2qXiWwB8wgKQjqmGKy5OWIgY6CWFXtsr4%0AVpO4%0A)
