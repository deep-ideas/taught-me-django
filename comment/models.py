from django.db import models
import datetime
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    class Meta:
        db_table='comment'
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    text = models.CharField(max_length=200,blank=True,null=True)
    
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now)

    #Related goes below

