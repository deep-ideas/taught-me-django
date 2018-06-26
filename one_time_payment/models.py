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

    
    transaction = models.ForeignKey(
        Transaction,
        on_delete = models.CASCADE
    )


