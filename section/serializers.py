from rest_framework import serializers
from .models import Section
from rest_framework_recursive.fields import RecursiveField

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple')
    curriculum_by = serializers.IntegerField(required=False,write_only=True)

    lectures = RecursiveField('lecture.serializers.LectureSerializersSimple',many=True,read_only=True)
    class Meta:
        model = Section
        fields=(
            'id',
            'name',


            'curriculum',
            'curriculum_by',

            'lectures',

            # 'created_by',
            # 'updated_by',
        )

    def create(self,validated_data):
        section = Section(**validated_data)
        section.save()
        return section

class SectionSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields=(
            'name',
        )
