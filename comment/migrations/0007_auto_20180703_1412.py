# Generated by Django 2.0.2 on 2018-07-03 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_auto_20180703_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='lecture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='lecture.Lecture'),
        ),
    ]
