frappe.ui.form.on('Delivery Note', {
    refresh(frm) {
        frappe.require("/assets/ampower_farmaans/js/get_print.js", ()=>{
            getPrint(frm)
        })    
    }
});