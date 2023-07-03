from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
#from reversion.admin import VersionAdmin
# Register your models here.
"""
class MyModelAdmin(admin.ModelAdmin):
    list_filter = ['*',]
    search_fields = ['*',]
"""
models = apps.get_models()

app_models = apps.get_app_config('testapp').get_models()
for model in app_models:
    try:
        #admin.site.register(model, MyModelAdmin)
        admin.site.register(model)
    except: AlreadyRegistered