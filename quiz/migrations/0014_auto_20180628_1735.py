# Generated by Django 2.0.2 on 2018-06-28 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20180628_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_answer', to='answer.Answer'),
        ),
    ]