## Ampower Farmaans

Ampower Farmaans is a custom Frappe app designed to allow users to customize the print format for documents of a specific DocType using `.docx` files.

## Features

- Customize the print format for various documents.
- Utilizes `.docx` files for defining print formats.
- Support for both static and dynamic data in print formats.
- Easily map dynamic data from the document to the `.docx` template using Jinja templating.
- Field names for dynamic data are available in the DocType customization section.

## How to Use

### Creating a Custom Print Format

To create a custom print format, follow these steps:

1. **Create a `.docx` Template:** Start by creating a `.docx` file that contains your custom print format. This file should have both static and dynamic sections. Refer to ![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/0680bc76-39b2-4c02-8229-ec8eb2a7f4ca)
 for an example of highlighting field names and labels in the DocType.

2. **Jinja Templating:** For dynamic data, use Jinja templating by placing field names in double curly braces, e.g., `{{ fieldname }}`. For populate tables need to add for loop Refer to ![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/e3654c94-8898-4c5b-ad7a-1d5698c802ca)
 for an example of Jinja tags in a `.docx` file.

3. **Select DocType:** In the "Template Docx" DocType, select the relevant DocType from the "DocType For" dropdown list. This associates your custom print format with a specific DocType.

4. **Upload Template:** Use the "Template File" field to upload your `.docx` template.![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/83008482-28bb-41c1-abb1-8ab2ba7aca29)
Template file list ![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/c5741c05-50c2-4a52-9c3e-ee5dcbbc774c)

### Using Custom Print Formats

On the document page of a specific DocType, you'll find a "Get Print" button. Follow these steps to use your custom print format:

1. **Click "Get Print":** Click the "Get Print" button to open a dialog.

2. **Template Selection:** Choose your custom template from the dropdown list. Refer to ![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/aa79b175-4257-4842-83b1-cae835678c61)

3. **Attach Docx:** Click "Attach Docx" to attach the `.docx` print format to the current document. This will populate the document with data from the template.

4. **Download Docx:** Alternatively, you can click "Download Docx" to download the print format in `.docx` format.![image](https://github.com/Ambibuzz/ampower_docx_printer/assets/97584010/c8cfafdf-54c7-4e47-b858-0be5df814260)

## Technical Details

### Extending to Other DocTypes

To extend this feature to other DocTypes, follow these steps:

1. **Create Custom Script:** Create a custom script similar to the ones provided for "Sales Order," "Sales Invoice," and "Delivery Note." Adjust the DocType name in the script to match the desired DocType.

2. **Modify hooks.py:** Add the path to your custom script in the `hooks.py` file under the `doctype_js` dictionary. This associates your custom script with the specific DocType.

## License

MIT License

## Contributors

- Ambibuzz Technologies LLP and contributors

---

**Note:** Ensure that you have correctly set up your naming series, field values, and templates to use this app effectively.


#### License

MIT