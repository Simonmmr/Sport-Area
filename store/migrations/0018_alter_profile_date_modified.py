# Generated by Django 5.1.3 on 2024-12-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_customer_is_subscribed_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
