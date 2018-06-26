from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.t

class SubscriptionPayment(models.Model):
    class Meta:
        db_table='subscription_payment'

    price = models.DecimalField(max_digits=12,decimal_places=12)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
