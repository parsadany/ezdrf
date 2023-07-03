from django.shortcuts import render

# Create your views here.
from ezdrf_generics.views import *


from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
class Test(Generic):
    model_class = QuerySetFilter
    model_app_name = 'ezdrf_generics'
    permission_classes = [
        AllowAny,
    ]
    
    def get(self, request):
        print(self.allowed_methods)