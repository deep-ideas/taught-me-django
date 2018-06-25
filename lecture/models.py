from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from section.models import Section
from curiculum.models import Curiculum
# Create your models here.

class Lecture(models.Model):
    class Meta:
        db_table = 'lecture'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200,blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    is_allow_comment = models.SmallIntegerField()
    is_downloadable = models.SmallIntegerField()
    is_pubished = models.SmallIntegerField()
    is_free_preview = models.SmallIntegerField()

    #Related Fields

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'lecture_created_by'
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'lecture_updated_by'
    )

    section = models.ForeignKey(
        Section,
        on_delete = models.CASCADE,
        related_name = 'lectures'
    )

    def __str__ (self):
        return self.name
