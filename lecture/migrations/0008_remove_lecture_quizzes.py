# Generated by Django 2.0.2 on 2018-06-27 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0007_auto_20180627_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='quizzes',
        ),
    ]
