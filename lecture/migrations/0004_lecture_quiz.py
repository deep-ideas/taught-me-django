# Generated by Django 2.0.2 on 2018-06-27 11:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180627_1132'),
        ('lecture', '0003_auto_20180627_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]
