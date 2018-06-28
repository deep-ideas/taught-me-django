from django.db import models
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

from quiz.models import Quiz

# Create your models here.
class Answer(models.Model):
    class Meta:
        db_table='answer'

    name = models.CharField(max_length=100,blank=True, null=True)
    is_answer = models.BooleanField()


    created_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    #related for quiz id goes below

    question = models.ForeignKey(
        "question.Question",
        on_delete=models.CASCADE,
        blank=True, 
        null=True,
        related_name='from_question'
    ) 

    quiz = models.ForeignKey(
        "quiz.Quiz",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='from_quiz'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answer_by',
        blank=True, 
        null=True,
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answer_update_by',
        blank=True, 
        null=True,
    )



