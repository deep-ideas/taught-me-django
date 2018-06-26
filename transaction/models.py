from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from course.models import Course
# Create your models here.

class Transaction(models.Model):
    class Meta:
        db_table='transaction'

    is_price = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True,)


    #realtion to user
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        blank=True, 
        null=True,
    )
    #relation to course
    course = models.OneToOneField(
        Course,        
        on_delete = models.CASCADE,
        blank=True, 
        null=True,
    )
    
