# Generated by Django 2.0.2 on 2018-06-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiculum', '0003_auto_20180625_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curiculum',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
