from django.apps import AppConfig


class GhbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GHB'

    def ready(self):
        import GHB.signals
