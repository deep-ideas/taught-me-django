from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from course.serializers import CourseSerializers

from .models import PricingPlan
class PricingPlanSerializer(serializers.ModelSerializer):
    course = RecursiveField('course.serializers.CourseSerializersSimple',)
    class Meta : 
        model = PricingPlan
        fields = (
            'name',
            'payment_type',
            'purchase_url',
            'is_recuring',
            

            #relation fields
            'course',
        )