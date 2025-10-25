from django.apps import AppConfig


class BasePyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base_Py'
