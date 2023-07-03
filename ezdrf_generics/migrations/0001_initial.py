# Generated by Django 4.1.4 on 2023-05-22 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=255, verbose_name='app name')),
                ('view_name', models.CharField(max_length=255, unique=True, verbose_name='view name')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], max_length=10, verbose_name='http method')),
                ('owner_only', models.BooleanField(default=False)),
                ('owner_field_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('owner_field_value', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuerySetFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
                ('value', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, unique=True, verbose_name='role title')),
                ('verbose_name', models.CharField(max_length=30, verbose_name='role verbose title')),
                ('description', models.TextField(max_length=500, verbose_name='role description')),
                ('datetime_created', models.DateTimeField(blank=True, verbose_name='datetime created')),
                ('datetime_last_change', models.DateTimeField(blank=True, verbose_name='datetime last change')),
                ('permissions', models.ManyToManyField(blank=True, help_text='any user with this role has permission to', to='ezdrf_generics.permission')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='queryset_filters',
            field=models.ManyToManyField(blank=True, help_text='filterings must be applied into the base queryset, for example owner=me', to='ezdrf_generics.querysetfilter'),
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.ManyToManyField(to='ezdrf_generics.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together={('view_name', 'method')},
        ),
    ]