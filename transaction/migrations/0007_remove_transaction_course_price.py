# Generated by Django 2.0.2 on 2018-06-28 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_transaction_pricing_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='course_price',
        ),
    ]
