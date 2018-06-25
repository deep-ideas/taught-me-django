from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    class Meta:
        db_table = 'course'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    

    created_by = models.OneToOneField(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'created_by'
    )

    updated_by = models.OneToOneField(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'updated_by'
    )

    def __str__(self):
        return self.name
