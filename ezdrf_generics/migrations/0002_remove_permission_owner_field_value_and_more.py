# Generated by Django 4.1.4 on 2023-06-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezdrf_generics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='owner_field_value',
        ),
        migrations.AlterField(
            model_name='permission',
            name='view_name',
            field=models.CharField(max_length=255, verbose_name='view name'),
        ),
    ]
