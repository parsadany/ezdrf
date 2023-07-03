from django.db import models

# Create your models here.

class TestParent(models.Model):
    char = models.CharField(max_length=10)

class TestModel(models.Model):
    fk = models.ForeignKey(TestParent, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='single')
    mtm = models.ManyToManyField(TestParent, blank=True, default=None, related_name='mtm')
    file = models.FileField(null=True, blank=True, default=None)
    text = models.TextField(null=True, blank=True, default=None)
    char = models.CharField(max_length=10, null=True, blank=True, default=None)
    integer = models.IntegerField(null=True, blank=True, default=None)
    biginteger = models.BigIntegerField(null=True, blank=True, default=None)
    bool = models.BooleanField(null=True, blank=True, default=None)
    datefield = models.DateField(null=True, blank=True, default=None)
    datetimefield = models.DateTimeField(null=True, blank=True, default=None)
    FloatField = models.FloatField(null=True, blank=True, default=None)
    url = models.URLField(null=True, blank=True, default=None)
    uuid = models.UUIDField(null=True, blank=True, default=None)
    email = models.EmailField(null=True, blank=True, default=None)
    Duration = models.DurationField(null=True, blank=True, default=None)
    binary = models.BinaryField(null=True, blank=True, default=None)