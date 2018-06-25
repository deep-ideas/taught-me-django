from django.db import models
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Answer(models.Model):
    class Meta:
        db_table='answer'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_answer = models.SmallIntegerField()

    #related for quiz id goes below