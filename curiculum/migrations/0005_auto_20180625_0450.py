# Generated by Django 2.0.2 on 2018-06-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiculum', '0004_auto_20180625_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curiculum',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
