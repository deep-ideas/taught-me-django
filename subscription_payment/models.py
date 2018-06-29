from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.t

class SubscriptionPayment(models.Model):
    class Meta:
        db_table='subscription_payment'


    price = models.FloatField(default=0, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    is_recuring = models.BooleanField(default=True)

    pricing_plan = models.ForeignKey(
        'pricing_plan.PricingPlan',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
