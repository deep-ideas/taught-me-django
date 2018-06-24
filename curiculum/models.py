from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from courses.models import Course

# Create your models here.

class Curiculum(models.Model):
    class Meta:
        db_table = 'course'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=255, blank=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    #relational things

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="to_course"
    )

    created_by = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = 'created_by'
    )

    updated_by = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name = 'updated_by'
    )

    def __str__(self):
        return self.name
