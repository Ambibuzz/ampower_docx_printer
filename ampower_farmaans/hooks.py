from . import __version__ as app_version

app_name = "ampower_farmaans"
app_title = "Ampower Farmaans"
app_publisher = "Ambibuzz Technologies LLP"
app_description = "by using custom .docx template create docx file or pdf for documents"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ithead@ambibuzz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ampower_farmaans/css/ampower_farmaans.css"
# app_include_js = "/assets/js/ampower_farmaans.js"

# include js, css files in header of web template
# web_include_css = "/assets/ampower_farmaans/css/ampower_farmaans.css"
# web_include_js = "/assets/ampower_farmaans/js/ampower_farmaans.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ampower_farmaans/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"product-traceability" : "public/js/farmaan_print.js"}

# include js in doctype views
doctype_js = {
    "Sales Order" : "public/js/custom_sales_order.js",
    "Delivery Note" : "public/js/custom_delivery_note.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

website_route_rules = [
    # Define custom routes here
    
]
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ampower_farmaans.install.before_install"
# after_install = "ampower_farmaans.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ampower_farmaans.uninstall.before_uninstall"
# after_uninstall = "ampower_farmaans.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ampower_farmaans.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ampower_farmaans.tasks.all"
#	],
#	"daily": [
#		"ampower_farmaans.tasks.daily"
#	],
#	"hourly": [
#		"ampower_farmaans.tasks.hourly"
#	],
#	"weekly": [
#		"ampower_farmaans.tasks.weekly"
#	]
#	"monthly": [
#		"ampower_farmaans.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "ampower_farmaans.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ampower_farmaans.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ampower_farmaans.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ampower_farmaans.auth.validate"
# ]

