# Generated by Django 3.2.12 on 2022-02-25 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20220225_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='secondaryImage1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='secondaryImage2',
        ),
    ]
