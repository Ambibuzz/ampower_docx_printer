# Copyright (c) 2023, Ambibuzz Technologies LLP and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils.file_manager import save_file
import ampower_farmaans
import json
from docxtpl import DocxTemplate
import io
import re
import html
from bs4 import BeautifulSoup

class TemplateDocx(Document):
    pass

@frappe.whitelist()
def attach_document(template_ref, cur_document):
    context1 = extract_plain_text(cur_document)
    context2 = context1.replace("<", "(").replace(">",")")
    context = json.loads(context2)
    template_file = frappe.get_doc("File", {"file_url": template_ref})
    filename = template_file.get_full_path()
    # creates a object using DocxTemplate class
    docm = DocxTemplate(filename)
    # puting the data as a dictionary for jinja variables
    docm.render(context)
    print_file_name = re.sub(r'[^a-zA-Z0-9\-]', '-', context["name"])
    # to write and save .docx file in frappe the data should be byte
    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{print_file_name}.docx',
                        content=content,
                        dt=str(context["doctype"]),
                        dn=str(context["name"]))
    return {
        "prepare_file": prepare_file,
       }

@frappe.whitelist()
def download_document(template_ref, cur_document):
    context1 = extract_plain_text(cur_document)
    context2 = context1.replace("<", "(").replace(">",")")
    context = json.loads(context2)
    prepare_file = frappe.get_doc("File", {"file_url": template_ref})
    filename = prepare_file.get_full_path()
    # creates a object using DocxTemplate class
    docm = DocxTemplate(filename)
    # puting the data as a dictionary for jinja variables
    docm.render(context)
    print_file_name = re.sub(r'[^a-zA-Z0-9\-]', '-', context["name"])
    # to write and save .docx file in frappe the data should be byte
    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{print_file_name}.docx',
                        content=content,
                        dt=None,
                        dn=None,
                        folder='Home')
    return {
        "prepare_file": prepare_file,
       }

@frappe.whitelist()
def delete_document(document_name):
    frappe.delete_doc('File', document_name, force=True)
    return { "message": "file deleted" }


def extract_plain_text(data):
    if isinstance(data, str):
        # Parse the HTML and extract the text
        soup = BeautifulSoup(data, 'html.parser')
        return soup.get_text()
    else:
        frappe.throw(__("Unexpected Data-type"))
