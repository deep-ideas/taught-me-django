from rest_framework import serializers
from .models import Course
from rest_framework_recursive.fields import RecursiveField
# from curriculum.serializers import CurriculumSerializersSimple

class CourseSerializers(serializers.ModelSerializer):
    curriculum = RecursiveField("curriculum.serializers.CurriculumSerializersSimple",read_only=True)
    # to_course = CurriculumSerializersSimple()
    class Meta:
        model = Course
        fields = (
            'name',
            'description',
            'subtitle',

            'curriculum'
        ) 

class CourseSerializersSimple(serializers.ModelSerializer):
    # to_course = RecursiveField("curriculum.serializers.CurriculumSerializersSimple",read_only=True,many=True)
    # to_course = CurriculumSerializersSimple()
    class Meta:
        model = Course
        fields = (
            'name',
            # 'description',
            # 'subtitle',

            # 'to_course'
        ) 
