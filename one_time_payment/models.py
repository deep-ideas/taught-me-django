from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from transaction.models import Transaction
# Create your models here.


class OneTimePayment(models.Model):
    class Meta:
        db_table='one_time_payment'

    
    # transaction = models.ForeignKey(
    #     Transaction,
    #     on_delete = models.CASCADE,
    #     null =True,
    #     blank = True
    # )
    is_recuring = models.BooleanField(default=False)
    price = models.FloatField(default=0, null=True, blank=True)
    pricing_plan = models.ForeignKey(
    'pricing_plan.PricingPlan',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

