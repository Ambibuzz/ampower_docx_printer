frappe.ui.form.on('Sales Order', {
    refresh(frm) {
        frappe.require("/assets/ampower_farmaans/js/get_print.js", ()=>{
            getPrint(frm)
        })    
    }
});