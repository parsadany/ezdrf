from rest_framework import serializers
from django.apps import apps

def auto_serialize(view_name, app_name, model_class_name, fields = '__all__', join_fields=[]):
    #TODO dynamic joins must be provided.
    meta_attrs = {
            "model": apps.get_model(app_name, model_class_name),
            "fields":  fields
        }
    Meta = type("Meta", (), meta_attrs)
    serializer_class_name = app_name + model_class_name + 'AutoSerializerFor' + view_name
    # locals() [serializer_class_name] = type(serializer_class_name, (serializers.ModelSerializer,), {"Meta": Meta})
    return type(serializer_class_name, (serializers.ModelSerializer,), {"Meta": Meta})
    #TODO make a class with this name!


    