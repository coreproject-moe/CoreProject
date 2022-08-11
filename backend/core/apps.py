from django.contrib.admin.apps import AdminConfig


class CoreProjectAdminConfig(AdminConfig):
    default_site = "core.admin.CoreProjectAdmin"
