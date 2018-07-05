from django.db import models
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

from lecture.models import Lecture
# Create your models here.

class Comment(models.Model):
    class Meta:
        db_table='comment'

    text = models.CharField(max_length=200,blank=True,null=True)
    
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)

    #Related goes below

    name = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'from_name',
        null=True,
    )

    lecture = models.ForeignKey(
        "lecture.Lecture",
        on_delete = models.SET_NULL,
        related_name = "comment",
        null = True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'comment_created_by'
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'comment_updated_by'
    )

def __str__(self):
    return self.name

