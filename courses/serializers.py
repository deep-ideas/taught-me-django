from rest_framework import serializers
from .models import Course
from rest_framework_recursive.fields import RecursiveField
# from curiculum.serializers import CuriculumSerializersSimple

class CourseSerializers(serializers.ModelSerializer):
    curiculum = RecursiveField("curiculum.serializers.CuriculumSerializersSimple",read_only=True)
    # to_course = CuriculumSerializersSimple()
    class Meta:
        model = Course
        fields = (
            'name',
            'description',
            'subtitle',

            'curiculum'
        ) 

class CourseSerializersSimple(serializers.ModelSerializer):
    # to_course = RecursiveField("curiculum.serializers.CuriculumSerializersSimple",read_only=True,many=True)
    # to_course = CuriculumSerializersSimple()
    class Meta:
        model = Course
        fields = (
            'name',
            # 'description',
            # 'subtitle',

            # 'to_course'
        ) 
