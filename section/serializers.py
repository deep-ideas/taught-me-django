from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Section
from curriculum.models import Curriculum


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple',required=False,read_only=True)
    lectures = RecursiveField('lecture.serializers.LectureSerializersSimple',many=True,read_only=True)
    curriculum_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    created_by = RecursiveField('user.serializers.UserSerializerName', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerName', read_only=True)
    class Meta:
        model = Section
        fields=(
            'id',
            'name',

            #related fields
            'curriculum',
            'lectures',
            #custom input data for post
            'curriculum_id',
            'updated_by',
            'created_by'
        )


    def get_custom_validated_data(self, validated_data):
        curriculum_id = validated_data.get('curriculum_id')
        validated_data.pop('curriculum_id', None)
        if curriculum_id:
            curriculum_id = Curriculum.objects.get(id=curriculum_id)
            validated_data['curriculum'] = curriculum_id
        return validated_data

    def create(self, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        section = Section.objects.create(**validated_data)
        return section

    def update(self, instance, validated_data):
        validated_data.pop('curriculum_id', None)
        section = Section.objects.filter(id=instance.id)
        section.update(**validated_data)
        return section.get()

class SectionSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields=(
            'name',
        )
