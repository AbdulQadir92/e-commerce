# Generated by Django 3.2.12 on 2022-02-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20220225_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='secondary_image3',
            field=models.ImageField(blank=True, null=True, upload_to='secondaryImages'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_image1',
            field=models.ImageField(blank=True, null=True, upload_to='secondaryImages'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_image2',
            field=models.ImageField(blank=True, null=True, upload_to='secondaryImages'),
        ),
    ]
