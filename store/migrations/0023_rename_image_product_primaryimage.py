# Generated by Django 3.2.12 on 2022-02-25 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20220225_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='primaryImage',
        ),
    ]
