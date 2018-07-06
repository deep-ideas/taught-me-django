from rest_framework import serializers
from .models import Course
from rest_framework_recursive.fields import RecursiveField
# from curriculum.serializers import CurriculumSerializersSimple

class CourseSerializers(serializers.ModelSerializer):
    # from_curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple', read_only = True)
    curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple',read_only=True,many=True)
    created_by = RecursiveField('user.serializers.UserSerializerName',read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerName',read_only=True)
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description',
            'subtitle',
            "curriculum",
            
            #related to user
            'updated_by',
            'created_by'
        ) 


class CourseSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
        ) 
