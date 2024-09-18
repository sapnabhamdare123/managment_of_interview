app_name = "managment_interview"
app_title = "Managment Interview"
app_publisher = "sapna"
app_description = "this is interview managment app"
app_email = "sapnabhamdare@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "managment_interview",
# 		"logo": "/assets/managment_interview/logo.png",
# 		"title": "Managment Interview",
# 		"route": "/managment_interview",
# 		"has_permission": "managment_interview.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/managment_interview/css/managment_interview.css"
# app_include_js = "/assets/managment_interview/js/managment_interview.js"

# include js, css files in header of web template
# web_include_css = "/assets/managment_interview/css/managment_interview.css"
# web_include_js = "/assets/managment_interview/js/managment_interview.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "managment_interview/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "managment_interview/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "managment_interview.utils.jinja_methods",
# 	"filters": "managment_interview.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "managment_interview.install.before_install"
# after_install = "managment_interview.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "managment_interview.uninstall.before_uninstall"
# after_uninstall = "managment_interview.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "managment_interview.utils.before_app_install"
# after_app_install = "managment_interview.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "managment_interview.utils.before_app_uninstall"
# after_app_uninstall = "managment_interview.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "managment_interview.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"managment_interview.tasks.all"
# 	],
# 	"daily": [
# 		"managment_interview.tasks.daily"
# 	],
# 	"hourly": [
# 		"managment_interview.tasks.hourly"
# 	],
# 	"weekly": [
# 		"managment_interview.tasks.weekly"
# 	],
# 	"monthly": [
# 		"managment_interview.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "managment_interview.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "managment_interview.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "managment_interview.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["managment_interview.utils.before_request"]
# after_request = ["managment_interview.utils.after_request"]

# Job Events
# ----------
# before_job = ["managment_interview.utils.before_job"]
# after_job = ["managment_interview.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"managment_interview.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

