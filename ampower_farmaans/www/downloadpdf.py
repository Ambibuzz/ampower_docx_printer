import frappe
from frappe import _


@frappe.whitelist()
def get_context(context):
    context.name = frappe.form_dict.name
    name = str(context.name)
    file = frappe.get_doc("File", name)
    frappe.response.filename = file.file_name
    frappe.response.filecontent = file.get_content()
    frappe.response.type = "download"
    frappe.response.display_content_as = "attachment"
    
