from django.apps import AppConfig


class BuildApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'build_api'

    # def ready(self):
    #     import signals