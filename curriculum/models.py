from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# from course.models import Course

# Create your models here.

class Curriculum(models.Model):
    class Meta:
        db_table = 'curriculum'

    name = models.CharField(max_length=255, blank=True , null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    #relational things

    course = models.ForeignKey(
        "course.Course",
        on_delete = models.CASCADE,
        related_name="curriculum",
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        blank=True, 
        null=True,
        related_name = 'curriculum_created_by',
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'curriculum_updated_by',
        blank=True, 
        null=True,
    )


    def __str__(self):
        return self.name
