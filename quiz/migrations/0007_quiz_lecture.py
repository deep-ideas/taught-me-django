# Generated by Django 2.0.2 on 2018-06-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0008_remove_lecture_quizzes'),
        ('quiz', '0006_remove_quiz_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizzes', to='lecture.Lecture'),
        ),
    ]