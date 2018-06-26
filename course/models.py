from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    class Meta:
        db_table = 'course'

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_enrolled = models.BooleanField(default=False)
    

    created_by = models.OneToOneField(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'course_created_by'
    )

    updated_by = models.OneToOneField(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'course_updated_by'
    )

    def __str__(self):
        return self.name
