from django.db import models

# Create your models here.
from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from quiz.models import Quiz

class Question(models.Model):
    class Meta:
        db_table="question"

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #relation

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        blank=True, 
        null=True,
        related_name="to_question"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, 
        null=True,
        related_name="question_by",
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, 
        null=True,
        related_name="question_updated_by",
    )
