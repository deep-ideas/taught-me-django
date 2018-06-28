from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# from course.models import Course
# Create your models here.

class Transaction(models.Model):
    class Meta:
        db_table='transaction'

    course_price = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    is_price = models.BooleanField()

    #realtion to user
    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank=True, 
        null=True,
    )
    #relation to course
    course = models.ForeignKey(
        'course.Course',        
        on_delete = models.CASCADE,
        blank=True, 
        null=True,
    )
    

    #relation to pricing plan
    pricing_plan = models.ForeignKey(
        'pricing_plan.PricingPlan',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )


    def __str__(self):
        return '%s : %s' % (self.course, self.course_price)