# Generated by Django 2.0.2 on 2018-06-28 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pricing_plan', '0007_pricingplan_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pricing_plan.PricingPlan')),
            ],
            options={
                'db_table': 'one_time_payment',
            },
        ),
    ]
