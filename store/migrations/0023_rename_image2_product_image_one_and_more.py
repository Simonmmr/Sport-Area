# Generated by Django 5.1.3 on 2025-01-08 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_product_image2_product_image3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image2',
            new_name='image_one',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image3',
            new_name='image_two',
        ),
    ]
