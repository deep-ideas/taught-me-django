# Generated by Django 2.0.2 on 2018-06-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180624_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
