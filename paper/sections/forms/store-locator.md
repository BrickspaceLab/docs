# Store locator

### Section overview

The store locator section allows merchants to display multiple store locations on an interactive map using Mapbox integration, with accordion-style location details.

#### Common use cases

* Displaying physical retail locations with address and operating hours
* Showcasing service areas or pickup points for e-commerce businesses
* Highlighting event locations or pop-up shops with relevant details
* Providing directional information for multiple business branches

#### Usage tips

* Ensure your Mapbox API key is properly configured in theme settings
* Use precise latitude and longitude coordinates for accurate location plotting
* Keep store details concise and formatted consistently across locations
* Consider mobile users by providing essential information first, as the map displays below the location list on smaller screens

### Section settings

| Setting            | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| Enable dynamic map | Toggle to display an interactive map or static image              |
| Image map          | Upload a static map image (displays when dynamic map is disabled) |
| Heading            | Add a title for the store locator section                         |
| Content            | Add descriptive text about your locations                         |
| Button label       | Add text for an optional call-to-action button                    |
| Button URL         | Set the destination URL for the button                            |
| Top spacing        | Adjust the padding above the section (0-300px)                    |
| Bottom spacing     | Adjust the padding below the section (0-300px)                    |
| Color scheme       | Select the background and text color combination                  |
| Border color       | Choose between subtle or strong border colors                     |
| Button color       | Select from various button style options                          |
| Border position    | Choose where borders appear (none, top, bottom, or both)          |
| Map style          | Select the Mapbox map visual style (standard, dark, or light)     |
| X alignment        | Control horizontal alignment of section content                   |
| Visibility         | Control section visibility across device types                    |

### Block settings

#### Store

This block adds a store location to the map with its details displayed in an accordion panel.

| Setting       | Description                                                                   |
| ------------- | ----------------------------------------------------------------------------- |
| Store name    | Name of the store location that appears in the accordion header               |
| Store details | Content describing the store, including address, hours, and other information |
| Latitude      | The latitude coordinate for the store marker position on the map              |
| Longitude     | The longitude coordinate for the store marker position on the map             |
