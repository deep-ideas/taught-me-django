# Generated by Django 2.0.2 on 2018-07-03 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_auto_20180626_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculum', to='course.Course'),
        ),
    ]
