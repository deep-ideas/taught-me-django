from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Section
from curriculum.models import Curriculum


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple',required=False,read_only=True)
    sections = serializers.IntegerField(required=False,write_only=True)

    lectures = RecursiveField('lecture.serializers.LectureSerializersSimple',many=True,read_only=True)
    class Meta:
        model = Section
        fields=(
            'id',
            'name',


            'curriculum',
            'sections',

            'lectures',
        )

    # def create(self, validated_data):
    #     # validated_data.pop('name_by_id',None)
    #     sections = validated_data.get('sections')
    #     validated_data.pop('sections',None)

    #     var = Section(**validated_data)
        
    #     #related name
    #     getCurri = Curriculum.objects.filter(id=sections).first()
    #     var.curriculum = getCurri
    #     var.save()

    #     return var

    def get_custom_validated_data(self, validated_data):
        sections = validated_data.get('sections')
        validated_data.pop('sections', None)
        if sections:
            sections = Curriculum.objects.get(id=sections)
            validated_data['curriculum'] = sections

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Section.objects.create(**validated_data)
        return branch

    def update(self, instance, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        branch = Section.objects.filter(id=instance.id)
        branch.update(**validated_data)
        return branch.get()

class SectionSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields=(
            'name',
        )
