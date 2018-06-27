from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


from section.models import Section
# Create your models here.

class Lecture(models.Model):
    class Meta:
        db_table = 'lecture'

    name = models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200,blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    is_allow_comment = models.BooleanField()
    is_downloadable = models.BooleanField()
    is_pubished = models.BooleanField()
    is_free_preview = models.BooleanField()

    #Related Fields

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'lecture_created_by',
        blank=True, 
        null=True,
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'lecture_updated_by',
        blank=True, 
        null=True,
    )

    section = models.ForeignKey(
        Section,
        on_delete = models.CASCADE,
        related_name = 'lectures',
    )

    def __str__ (self):
        return self.name
