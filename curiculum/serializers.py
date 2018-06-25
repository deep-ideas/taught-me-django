from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
import uuid

from .models import Curiculum
from courses.models import Course
from courses.serializers import CourseSerializersSimple
from section.serializers import SectionSerializersSimple


class CuriculumSerializers(serializers.ModelSerializer):
    # course = [RecursiveField('courses.serializers.CourseSerializersSimple',many=True,read_only=True)]
    course = [CourseSerializersSimple(read_only=True,many=True ,required=False)]
    course_by = serializers.UUIDField(write_only=True, required=False, allow_null=True)


    # section_id = [RecursiveField('section.serializers.SectionSerializersSimple',read_only=True)]
    sections = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = Curiculum
        fields = (
            'url',
            'name',
            'course',
            'course_by',
            'sections',

        )
    
    def create(self, validated_data):

        data = Curiculum(**validated_data)
        
        #related name
        value = Course.objects.filter(id=course_by)
        data.course = value
        data.save()

        return data

class CuriculumSerializersSimple(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curiculum
        fields = (
            'url',
            'name',
        )
