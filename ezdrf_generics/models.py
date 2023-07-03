from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = get_user_model()


# Create your models here.
class QuerySetFilter(models.Model):
    field = models.CharField(max_length=100)
    value = models.TextField(max_length=500)

class Permission(models.Model):
    METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        # ('OPTIONS', 'OPTIONS')
    )
    app_name = models.CharField(_('app name'), max_length=255)
    view_name = models.CharField(_('view name'), max_length=255)
    method = models.CharField(_('http method'), max_length=10, choices=METHOD_CHOICES)
    owner_only = models.BooleanField(default=False)
    owner_field_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    # owner_field_value = models.CharField(max_length=255, blank=True, null=True, default=None)
    queryset_filters = models.ManyToManyField(QuerySetFilter, help_text=_('filterings must be applied into the base queryset, for example owner=me'), blank=True)
    """
    view_name: The main idea is to use this in your local permissions:
    class Clazz():
        def get_name(self):
            return self.__class__.__name__
    """

    class Meta:
        unique_together = ('view_name', 'method',)

    def __str__(self):
        return str(self.id) + ": " + str(self.view_name) + " | " + str(self.method)


class Role(models.Model):
    name = models.CharField(_('role title'), max_length=90, unique=True)
    verbose_name = models.CharField(_('role verbose title'), max_length=30)
    description = models.TextField(_('role description'), max_length=500)
    permissions = models.ManyToManyField(Permission, help_text=_('any user with this role has permission to'), blank=True)
    datetime_created = models.DateTimeField(_('datetime created'), blank=True)
    datetime_last_change = models.DateTimeField(_('datetime last change'), blank=True)
    
    def save(self, *args, **kwargs):
        # On save, update timestamps. but not on edit.
        if not self.id:
            self.datetime_created = timezone.now()
        self.datetime_last_change = timezone.now()
        super(Role, self).save(*args, **kwargs)


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)