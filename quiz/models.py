from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# from lecture.models import Lecture

# Create your models here.

class Quiz(models.Model):
    class Meta:
        db_table='quiz'

    name = models.CharField(max_length=200,blank=True, null=True)
    answer = models.CharField(max_length=100,blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    #realted goes here

    lecture = models.ForeignKey(
        "lecture.Lecture",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="quizzes",
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

    def __str__(self):
        return self.name