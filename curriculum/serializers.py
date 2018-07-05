from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
import uuid

from .models import Curriculum
from course.models import Course
from course.serializers import CourseSerializersSimple
from section.serializers import SectionSerializersSimple


class CurriculumSerializers(serializers.ModelSerializer):
    course = RecursiveField('course.serializers.CourseSerializersSimple',allow_null=True,required=False,read_only=True)
    # curriculum = RecursiveField('curriculum.serializers.CurricilumSerializersSimple',read_only=True)
    # course = [RecursiveField('course.serializers.CourseSerializersSimple',many=True,blank=True, null=True)]
    # course = [CourseSerializersSimple(read_only=True,many=True ,required=False)]
    course_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

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
            'sections',

            'course_id',

        )

    # def create(self, validated_data):
    #     # validated_data.pop('name_by_id',None)
        
    #     course_id = validated_data.get('course_id')
    #     validated_data.pop('course_id',None)
    #     var = Curriculum(**validated_data)
        
    #     #related name
    #     getCourse = Course.objects.filter(id=course_id).first()
    #     var.course = getCourse
    #     var.save()

    #     return var

    def get_custom_validated_data(self, validated_data):
        course_id = validated_data.get('course_id')
        validated_data.pop('course_id', None)
        if course_id:
            course_id = Course.objects.get(id=course_id)
            validated_data['course'] = course_id

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Curriculum.objects.create(**validated_data)
        return branch

    def update(self, instance, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Curriculum.objects.filter(id=instance.id)
        branch.update(**validated_data)
        return branch.get()

class CurriculumSerializersSimple(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerName',read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerName',read_only=True)
    class Meta:
        model = Curriculum
        fields = (
            'name',
            'course',
            'created_at',
            'updated_at',

            'created_by',
            'updated_by',
        )
