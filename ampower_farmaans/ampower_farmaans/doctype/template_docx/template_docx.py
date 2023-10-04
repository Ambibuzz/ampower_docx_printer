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
def attach_document(doctype_ref, document_ref, template_ref):
    template_file = template_ref
    prepare_file = frappe.get_doc("File", {"file_url": template_file})
    filename = prepare_file.get_full_path()
    cur_doctype = doctype_ref
    cur_document =  document_ref
    doctype_entry = frappe.get_doc(cur_doctype, cur_document)

    docm = DocxTemplate(filename)

    context = doctype_entry

    docm.render(context.as_dict())

    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{cur_document}.docx', 
                        content=content, 
                        dt=str(cur_doctype), 
                        dn=str(cur_document))
    return {
        "prepare_file": prepare_file
       }


@frappe.whitelist()
def download_document(doctype_ref, document_ref, template_ref):
    template_file = template_ref
    prepare_file = frappe.get_doc("File", {"file_url": template_file})
    filename = prepare_file.get_full_path()
    cur_doctype = doctype_ref
    cur_document =  document_ref
    doctype_entry = frappe.get_doc(cur_doctype, cur_document)

    docm = DocxTemplate(filename)

    context = doctype_entry

    docm.render(context.as_dict())

    with io.BytesIO() as output_buffer:
        docm.save(output_buffer)
        content = output_buffer.getvalue()
        prepare_file = save_file(
                        f'{cur_document}.docx', 
                        content=content)
    return {
        "prepare_file": prepare_file
       }

