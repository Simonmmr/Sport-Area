# Generated by Django 5.1.3 on 2024-12-26 02:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='old_cart',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=4000, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
