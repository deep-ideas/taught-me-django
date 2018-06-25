from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Country(models.Model):
    class Meta:
        db_table="country"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=45,)
    flag = models.URLField(max_length=200, blank=True,)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return '%s' % (self.name)

class Profile(models.Model):
    class Meta:
        db_table="profile"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13,)
    gender = models.SmallIntegerField()
    address_line = models.CharField(max_length=200,)
    city = models.CharField(max_length=45,)
    region = models.CharField(max_length=45,)
    postal_code = models.CharField(max_length=6,)
    
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now_add=True,)

    #relation ke user id
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user',
    )
    #related ke country id
    country = models.OneToOneField(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='country'
    )
    