# Generated by Django 3.2.12 on 2022-02-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220212_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]