from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    class Meta:
        db_table='transaction'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_price = models.SmallIntegerField()
    
