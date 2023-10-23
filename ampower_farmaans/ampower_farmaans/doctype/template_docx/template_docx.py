# Copyright (c) 2023, Ambibuzz Technologies LLP and contributors
# For license information, please see license.txt
import frappe
import json
import ampower_farmaans
from frappe.model.document import Document
from frappe.utils.file_manager import save_file, get_file_path, download_file
from docxtpl import DocxTemplate
import io
import subprocess
import tempfile
import os

class TemplateDocx(Document):
    pass

@frappe.whitelist()
def attach_document(template_ref, cur_document):
    context = json.loads(cur_document)
    template_file = frappe.get_doc("File", {"file_url": template_ref})
    filename = template_file.get_full_path()
    # creates a object using DocxTemplate class
    docm = DocxTemplate(filename)
    # puting the data as a dictionary for jinja variables
    docm.render(context)
    # to write and save .docx file in frappe the data should be byte
    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{context["name"]}.docx', 
                        content=content,
                        dt=str(context["doctype"]),
                        dn=str(context["name"]))
    return {
        "prepare_file": prepare_file,
       }

@frappe.whitelist()
def download_document(template_ref, cur_document):
    context = json.loads(cur_document)
    prepare_file = frappe.get_doc("File", {"file_url": template_ref})
    filename = prepare_file.get_full_path()
    # creates a object using DocxTemplate class
    docm = DocxTemplate(filename)
    # puting the data as a dictionary for jinja variables
    docm.render(context)
    # to write and save .docx file in frappe the data should be byte
    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{context["name"]}.docx',
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