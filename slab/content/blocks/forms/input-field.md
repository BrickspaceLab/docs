# Input field

<figure><img src="../../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

## Overview

A configurable form input block that renders different types of form inputs based on the selected input type, supporting text, textarea, email, checkbox, radio, select, date, file, and password input types.

## Common use cases

* Use appropriate input types for different data collection needs
* Provide clear labels and help text for better accessibility
* Consider required field settings based on form validation needs
* Create comprehensive forms by combining multiple input field blocks

## Block settings

### Content

| Setting               | Description                                                | Options                                                                                                       |
| --------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Input type            | Select the type of form input to display                   | <p>• Text<br>• Textarea<br>• Email<br>• Checkbox<br>• Radio<br>• Select<br>• Date<br>• File<br>• Password</p> |
| Label                 | Label text for the input field                             | Text input                                                                                                    |
| Placeholder           | Placeholder text shown in the input                        | <p>Text input<br><br>Visible when input type is not checkbox and input type is not radio</p>                  |
| Help text             | Additional help text displayed below the input             | <p>Rich text input<br><br>Visible when input type is not checkbox and input type is not radio</p>             |
| Options               | Comma-separated list of options for select or radio inputs | <p>Textarea input<br><br>Visible when input type is "select" or input type is "radio"</p>                     |
| Accepted file types   | File types accepted for file inputs                        | <p>Text input (default: .jpg, .jpeg, .png, .pdf, .svg, .gif)<br><br>Visible when input type is "file"</p>     |
| Enable multiple files | Allows multiple file selection for file inputs             | <p>Checkbox (default: false)<br><br>Visible when input type is "file"</p>                                     |
| Enable required field | Marks the input as required                                | Checkbox (default: false)                                                                                     |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
