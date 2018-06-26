from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from curriculum.models import Curriculum
# Create your models here.

class Section(models.Model):
    class Meta:
        db_table="section"

    name = models.CharField(max_length=100,blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    #relation

    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name='sections'
    )

    created_by = models.ForeignKey(
        User,
        null = True,
        on_delete=models.SET_NULL,
        related_name='section_created_by',
    )

    updated_by = models.ForeignKey(
        User,
        null = True,
        on_delete=models.SET_NULL,
        related_name='section_updated_by',
    )

    def __str__ (self):
        return self.name
