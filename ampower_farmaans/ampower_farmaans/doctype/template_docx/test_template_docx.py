# Copyright (c) 2023, Ambibuzz Technologies LLP and Contributors
# See license.txt

# import frappe
import unittest
import datetime
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

class TestTemplateDocx(unittest.TestCase):
    pass

# document ref
test_doc_name = ''
# test doctype
test_doctype = ''
# test template
test_template_ref = ''
@frappe.whitelist()
def test_attach_document():
    template_ref = test_template_ref
    doctype_ref = test_doctype
    document_ref = ''
    template_file = template_ref
    prepare_file = frappe.get_doc("File", {"file_url": template_file})
    filename = prepare_file.get_full_path()
    cur_doctype = doctype_ref
    cur_document =  document_ref
    # doctype_entry = frappe.get_doc(cur_doctype, cur_document)
    doctype_entry = frappe.get_value(cur_doctype, filters={"name":cur_document}, fieldname="*" )
    docm = DocxTemplate(filename)
    context = doctype_entry
    print(context)
    docm.render(dict(context))
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
def test_download_document(doctype_ref, document_ref, template_ref):
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
                        dt=None,
                        dn=None,
                        folder='Home')
    return {
        "prepare_file": prepare_file
       }

@frappe.whitelist()
def test_delete_document(document_name):
    frappe.delete_doc('File', document_name, force=True)
    return { "message": "file deleted" }