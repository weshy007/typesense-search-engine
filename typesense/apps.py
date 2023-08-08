from django.apps import AppConfig


class TypesenseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'typesense'

    def ready(self):
        from . import signals