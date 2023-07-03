from django.apps import AppConfig

from ezdrf_generics.initial import init_permissions

class EzdrfGenericsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ezdrf_generics'

    def ready(self) -> None:
        init_permissions()
        return super().ready()