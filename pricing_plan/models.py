import datetime

#built-in django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#module
from course.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here

class PricingPlan(models.Model):
    class Meta:
        db_table = 'pricing_plan'
    
    name = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2), MinValueValidator(0)])
    purchase_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_recuring = models.BooleanField(default=False)


    #relation many to one with coursea
    course = models.ForeignKey(
        Course,
        on_delete = models.CASCADE,
        related_name='pricing_plan',
        blank = True,
        null = True
    )

    #relation to user django
    created_by = models.ForeignKey(
        User,
        on_delete = models.SET_DEFAULT,
        related_name = 'pricing_plan_created_by',
        null = True,
        default = 1,
        blank = True,
    )

    updated_by = models.ForeignKey(
        User,
        on_delete = models.SET_DEFAULT,
        related_name = 'pricing_plan_updated_by',
        null = True,
        default = 1,
        blank = True
    )
    
    def __str__(self):
        return self.name