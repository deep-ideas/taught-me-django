from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
import uuid

from .models import Curriculum
from course.models import Course
from course.serializers import CourseSerializersSimple
from section.serializers import SectionSerializersSimple


class CurriculumSerializers(serializers.ModelSerializer):
    course = RecursiveField('course.serializers.CourseSerializersSimple',allow_null=True,required=False)
    # course = [RecursiveField('course.serializers.CourseSerializersSimple',many=True,blank=True, null=True)]
    # course = [CourseSerializersSimple(read_only=True,many=True ,required=False)]
    curriculum = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    


    # section_id = [RecursiveField('section.serializers.SectionSerializersSimple',read_only=True)]
    sections = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = Curriculum
        fields = (
            'url',
            'name',
            'course',
            'curriculum',
            'sections',

        )

    def create(self, validated_data):

        curriculumRef = Curriculum(**validated_data)

        #course
        # getCourse = Course.objects.filter(id=curriculum)
        # curriculumRef.course = getCourse
        curriculumRef.save()

        return curriculumRef

    # def update(self, instance, validated_data):
    #     validated_data = self.get_custom_validated_data(validated_data)
    #     branch = Curriculum.objects.filter(id=instance.id)
    #     branch.update(**validated_data)
    #     return branch.get()

class CurriculumSerializersSimple(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = (
            'url',
            'name',
        )
