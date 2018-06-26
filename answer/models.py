from django.db import models
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Answer(models.Model):
    class Meta:
        db_table='answer'
    name = models.CharField(max_length=100,blank=True, null=True)
    is_answer = models.BooleanField()

    #related for quiz id goes below