# Generated by Django 2.0.2 on 2018-06-25 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curiculum', '0005_auto_20180625_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curiculum',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curiculum', to='courses.Course'),
        ),
    ]
