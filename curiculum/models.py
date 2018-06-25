from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from courses.models import Course

# Create your models here.

class Curiculum(models.Model):
    class Meta:
        db_table = 'curiculum'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=255, blank=True , null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    #relational things

    course = models.OneToOneField(
        Course,
        on_delete = models.CASCADE,
        related_name="curiculum"
    )

    created_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'curiculum_created_by'
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'curiculum_updated_by'
    )

    def save(self, pk=None):
        course = Curiculum.objects.get(pk=pk)
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save()
    #    return Response(serializer.data, status=status.HTTP_201_CREATED) 
    

    def __str__(self):
        return self.name
