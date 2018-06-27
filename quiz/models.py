from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from lecture.models import Lecture
# Create your models here.

class Quiz(models.Model):
    class Meta:
        db_table='quiz'

    name = models.CharField(max_length=200,blank=True, null=True)
    answer = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    #realted goes here

    lecture = models.ForeignKey(
        "lecture.Lecture",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        blank=True, 
        null=True,
        related_name = 'quiz_created_by',
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'quiz_update_by',
        blank=True, 
        null=True,
    )