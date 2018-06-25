# Generated by Django 2.0.2 on 2018-06-24 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180624_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='user.Country'),
        ),
    ]