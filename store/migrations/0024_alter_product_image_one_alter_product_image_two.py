# Generated by Django 5.1.3 on 2025-01-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_rename_image2_product_image_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/one_file'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/two_file'),
        ),
    ]
