# Generated by Django 2.0.2 on 2018-06-27 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0008_remove_lecture_quizzes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0009_auto_20180627_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quiz',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizzes', to='lecture.Lecture'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_update_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
