# Generated by Django 2.0.2 on 2018-07-03 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0009_auto_20180703_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='section_id',
            new_name='section',
        ),
    ]
