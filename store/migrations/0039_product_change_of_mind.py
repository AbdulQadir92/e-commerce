# Generated by Django 3.2.12 on 2022-03-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_auto_20220307_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='change_of_mind',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
