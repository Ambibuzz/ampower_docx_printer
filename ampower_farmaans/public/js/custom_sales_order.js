frappe.ui.form.on('Sales Order', {
    refresh(frm) {
        console.log("testing")
        frm.add_custom_button(__('Get Print'), function () {
            var dialog = new frappe.ui.Dialog({
                title: __('Select Template'),
                fields: [
                    {
                        fieldname: 'template',
                        label: __('Template'),
                        fieldtype: 'Link',
                        options: 'Template Docx',
                        get_query: function () {
                            return {
                                filters: {
                                    doctype_for: frm.doctype
                                }
                            };
                        },
                        reqd: 1
                    }
                ],
                primary_action_label: __('Attach Docx'),
                primary_action: function () {
                    // Get the selected template from the dialog
                    var template = dialog.get_value('template');
                    // Fetch the 'docx_file' field value from the selected template
                    frappe.call({
                        method: 'frappe.client.get_value',
                        args: {
                            doctype: 'Template Docx',
                            filters: {
                                name: template
                            },
                            fieldname: 'template_file'
                        },
                        callback: function (r) {
                            if (!r.exc) {
                                var docxFile = r.message.template_file;
                                frappe.call({
                                    method: 'ampower_farmaans.ampower_farmaans.doctype.template_docx.template_docx.attach_document',
                                    args: {
                                       
                                            template_ref: docxFile,
                                            doctype_ref: frm.doctype,
                                            document_ref: frm.doc.name,
                                        
                                    },
                                    callback: function (r) {
                                        if (!r.exc) {
                                            var result = JSON.parse(JSON.stringify(r.message));
                                            console.log("result from backend", result);
                                            frm.reload_doc();
                                            frappe.show_alert('Print document attached', 5);                                            
                                        }
                                    }
                                });
                            }
                        }
                    });
                    dialog.hide();
                },
                secondary_action_label: __('Download Docx'),
                secondary_action: function () {
                    // Get the selected template from the dialog
                    var template = dialog.get_value('template');
                    // Fetch the 'docx_file' field value from the selected template
                    
                    if (!template) {
                        frappe.msgprint(__('Please select a template.'));
                        return;
                    }
                    frappe.call({
                        method: 'frappe.client.get_value',
                        args: {
                            doctype: 'Template Docx',
                            filters: {
                                name: template
                            },
                            fieldname: 'template_file'
                        },
                        callback: function (r) {
                            if (!r.exc) {
                                var docxFile = r.message.template_file;
                                frappe.call({
                                    method: 'ampower_farmaans.ampower_farmaans.doctype.template_docx.template_docx.download_document',
                                    args: {
                                        template_ref: docxFile,
                                        doctype_ref: frm.doctype,
                                        document_ref: frm.doc.name,
                                    },
                                    callback: function (r) {
                                        if (!r.exc) {
                                            var result = JSON.parse(JSON.stringify(r.message));
                                            console.log("result from backend", result);
                                            frm.reload_doc();
                                            window.open(result.prepare_file.file_url)
                                            frappe.show_alert('Print document downloaded', 5);
                                            frappe.call({
                                                method: 'ampower_farmaans.ampower_farmaans.doctype.template_docx.template_docx.delete_document',
                                                args: {
                                                    document_name: result.prepare_file.name
                                                },
                                                callback: function (r) {
                                                    if (!r.exc) {
                                                        var result = JSON.parse(JSON.stringify(r.message));
                                                        console.log("result from backend", result);
                                                    }
                                                }

                                            })
                                            
                                        }
                                    }
                                });
                            }
                        }
                    });
                    dialog.hide();
                }, 
            })
            dialog.show();
        });
    }
});
