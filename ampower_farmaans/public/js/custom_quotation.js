frappe.ui.form.on('Quotation', {
    refresh(frm) {
        frappe.require("/assets/ampower_farmaans/js/get_print.js", ()=>{
            getPrint(frm)
        })    
    }
});
