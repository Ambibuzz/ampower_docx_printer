frappe.ui.form.on('Purchase Order', {
    refresh(frm) {
        frappe.require("/assets/ampower_farmaans/js/get_print.js", ()=>{
            getPrint(frm)
        })    
    }
});