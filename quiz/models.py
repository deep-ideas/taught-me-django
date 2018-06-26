from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    class Meta:
        db_table='quiz'

    name = models.CharField(max_length=200,blank=True, null=True)
    answer = models.CharField(max_length=100)
    

    #realted goes here
