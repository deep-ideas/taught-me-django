# Generated by Django 2.0.2 on 2018-06-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180627_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='lecture.Lecture'),
        ),
    ]
