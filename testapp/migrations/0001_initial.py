# Generated by Django 4.1.4 on 2023-06-06 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('char', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('integer', models.IntegerField(blank=True, default=None, null=True)),
                ('biginteger', models.BigIntegerField(blank=True, default=None, null=True)),
                ('bool', models.BooleanField(blank=True, default=None, null=True)),
                ('datefield', models.DateField(blank=True, default=None, null=True)),
                ('datetimefield', models.DateTimeField(blank=True, default=None, null=True)),
                ('FloatField', models.FloatField(blank=True, default=None, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('Duration', models.DurationField(blank=True, default=None, null=True)),
                ('binary', models.BinaryField(blank=True, default=None, null=True)),
                ('fk', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='single', to='testapp.testparent')),
                ('mtm', models.ManyToManyField(blank=True, default=None, related_name='mtm', to='testapp.testparent')),
            ],
        ),
    ]
