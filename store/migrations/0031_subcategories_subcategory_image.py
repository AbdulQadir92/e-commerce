# Generated by Django 3.2.12 on 2022-02-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_categories_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='subcategory_image',
            field=models.ImageField(null=True, upload_to='subcategoryImages'),
        ),
    ]
