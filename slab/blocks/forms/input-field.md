# Input field


## Overview

A configurable form input block that renders different types of form inputs based on the selected input type, supporting text, textarea, email, checkbox, radio, select, date, file, and password input types.


## Common use cases

- Use appropriate input types for different data collection needs
- Provide clear labels and help text for better accessibility
- Consider required field settings based on form validation needs
- Create comprehensive forms by combining multiple input field blocks


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Input type | Select the type of form input to display | • Text<br>• Textarea<br>• Email<br>• Checkbox<br>• Radio<br>• Select<br>• Date<br>• File<br>• Password |
| Label | Label text for the input field | Text input |
| Placeholder | Placeholder text shown in the input | Text input<br><br>Visible when input type is not checkbox and input type is not radio |
| Help text | Additional help text displayed below the input | Rich text input<br><br>Visible when input type is not checkbox and input type is not radio |
| Options | Comma-separated list of options for select or radio inputs | Textarea input<br><br>Visible when input type is "select" or input type is "radio" |
| Accepted file types | File types accepted for file inputs | Text input (default: .jpg, .jpeg, .png, .pdf, .svg, .gif)<br><br>Visible when input type is "file" |
| Enable multiple files | Allows multiple file selection for file inputs | Checkbox (default: false)<br><br>Visible when input type is "file" |
| Enable required field | Marks the input as required | Checkbox (default: false) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
