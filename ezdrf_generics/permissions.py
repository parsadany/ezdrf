from rest_framework import permissions
from rest_framework.permissions import BasePermission
# from auth_app.models import *
from django.conf import settings
from ezdrf_generics.models import *

class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)

class RolePermission(BasePermission):
    """
    check Role and Permission
    # TODO Needs Test
    """
    def has_permission(self, request, view):
        print(view.__class__.__name__)
        try:
            view_obj = Permission.objects.get(view_name=view.__class__.__name__, method=str(request.method).upper())
            extended_user = ExtendedUser.objects.get(user = request.user)
            user_roles = extended_user.roles.all()
            print(view_obj, extended_user, user_roles)
            for role in user_roles:
                print("role", role)
                permissions = role.permissions.all()
                for permission in permissions:
                    print(permission, permission.view_name)
                    if permission == view_obj:
                        return True
            return False
        except:
            return False

