# Generated by Django 3.2.12 on 2022-02-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20220225_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='primaryImage',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
