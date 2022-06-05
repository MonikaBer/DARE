from django.apps import AppConfig


class StatelessAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stateless_app'
