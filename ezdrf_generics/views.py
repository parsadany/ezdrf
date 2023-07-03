from rest_framework import exceptions, generics, serializers, status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination, CursorPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from ezdrf_generics.permissions import RolePermission
from ezdrf_generics.models import Permission, QuerySetFilter
from rest_framework.mixins import ListModelMixin
from django.apps import apps

##################################
### Our Base Objects:
##################################

class ViewClassDefine:
    is_view = True
    # Model Class Name and it's app name should be defined 
    model_class = None
    model_app_name = None
    # will be evaluated by __init__
    view_name = None
    auto_serializer = True
    fields = '__all__'
    join_fields=[]


    page_query_param = PageNumberPagination.page_query_param
    limit_query_param = LimitOffsetPagination.limit_query_param
    cursor_query_param = CursorPagination.cursor_query_param

    @classmethod
    def check_list_mro(cls):
        if ListModelMixin in cls.__mro__:
            return True
        return False

    # def __init__(self):
    #     print("__init__")
    #     self.view_name = self.__class__.__name__
    #     if self.check_list_mro():
    #         self.set_pagination_class()
    #     else:
    #         self.pagination_class = None
    #     if self.auto_serializer:
    #         self.auto_serialize()

    # @classmethod
    # def as_view(cls, **initkwargs):
    #     print("\n\n\nqazanfar\n\n\n")
    #     cls.__init__()
    #     return super().as_view(**initkwargs)

    def auto_serialize(self):
        #TODO dynamic joins must be provided.
        meta_attrs = {
                # "model": apps.get_model(self.model_app_name, self.model_class),
                "model": self.model_class,
                "fields":  self.fields
            }
        Meta = type("Meta", (), meta_attrs)
        serializer_class_name = self.model_app_name + self.model_class.__class__.__name__ + 'AutoSerializerFor' + self.__class__.__name__
        # locals() [serializer_class_name] = type(serializer_class_name, (serializers.ModelSerializer,), {"Meta": Meta})
        self.serializer_class =  type(serializer_class_name, (serializers.ModelSerializer,), {"Meta": Meta})
        return self.serializer_class

    def get_ez_queryset(self):
        # from django.contrib.contenttypes.models import ContentType 
        # z = self.model_class
        # apps.get_model(self.model_app_name, self.model_class)
        print("app_name" ,self.model_app_name, "view_name", self.__class__.__name__, "method", self.request.method)
        permission = Permission.objects.get(app_name=self.model_app_name, view_name=self.__class__.__name__, method=self.request.method)
        queryset_filters = permission.queryset_filters.all()
        filters = {}
        if permission.owner_only: #and permission.owner_field_name is not None and permission.owner_field_value is not None:
            filters[permission.owner_field_name] = self.request.user
        for f in queryset_filters:
            filters[f.field] = f.value
        return self.model_class.objects.filter(**filters)

    def set_pagination_class(self):
        """
        LimitOffsetPagination is prefered to other paginations and 
        PageNumberPagination is prefered to CursorPagination 
        if more than one reserved query param provided for pagination.
        """
        if self.request.query_params.get(self.limit_query_param, None) is None:
            self.pagination_class = LimitOffsetPagination
        elif self.request.query_params.get(self.page_query_param, None) is None:
            self.pagination_class = PageNumberPagination
        elif self.request.query_params.get(self.cursor_query_param, None) is None:
            self.pagination_class = CursorPagination
        else:
            self.pagination_class = None


##################################
### List Objects:
##################################

class ListCreate(generics.ListCreateAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]
    # pagination_class = LimitOffsetPagination

    # def paginate_queryset(self, queryset):
    #     print(self.paginator)
    #     if self.paginator and self.request.query_params.get(self.paginator.limit_query_param, None) is None:
    #         return None
    #     return super().paginate_queryset(queryset)

    methods = ['GET', 'POST',]

    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()

    filterset_fields = '__all__'
    ordering_fields = '__all__'
    
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]

class List(generics.ListAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]
    # pagination_class = LimitOffsetPagination

    methods = ['GET',]


    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        print(self.paginator)
        if self.paginator and self.request.query_params.get(self.paginator.limit_query_param, None) is None:
            return None
        return super().paginate_queryset(queryset)
    
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]

class Create(generics.CreateAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]

    methods = ['POST',]

    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()

##################################
### Retrive Destrot and Update:
##################################

class Retrieve(generics.RetrieveAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]

    methods = ['GET',]

    lookup_field = 'id'

    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


class Update(generics.UpdateAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]

    methods = ['PUT', 'PATCH',]

    lookup_field = 'id'

    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


class Destroy(generics.DestroyAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]

    methods = ['DELETE',]

    lookup_field = 'id'


    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


class RetrieveUpdate(generics.RetrieveUpdateAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]
    lookup_field = 'id'

    methods = ['GET', 'PUT', 'PATCH',]

    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


class RetrieveDestroy(generics.RetrieveDestroyAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]
    lookup_field = 'id'

    methods = ['GET', 'DELETE',]


    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]
    lookup_field = 'id'

    methods = ['GET', 'PUT', 'PATCH', 'DELETE',]


    def get_queryset(self):
        return self.get_ez_queryset()
    
    def get_serializer_class(self):
        if self.auto_serializer:
            return self.auto_serialize()
        return super().get_serializer_class()


##################################
### Retrive Destrot and Update:
##################################

class Generic(generics.GenericAPIView, ViewClassDefine):
    permission_classes = [
        RolePermission,
    ]




from rest_framework.response import Response


# class Test(generics.GenericAPIView):
#     serializer_class = None
#     queryset = Permission.objects.none()

#     def get(self, request, *args, **kwargs):
#         print(str(request.resolver_match.func))
#         return Response(request.resolver_match.app_name)

