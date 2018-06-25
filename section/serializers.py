from rest_framework import serializers
from .models import Section
from rest_framework_recursive.fields import RecursiveField

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    curiculum = RecursiveField('curiculum.serializers.CuriculumSerializersSimple')
    curiculum_by = serializers.IntegerField(required=False,write_only=True)

    lectures = RecursiveField('lecture.serializers.LectureSerializersSimple',many=True,read_only=True)
    class Meta:
        model = Section
        fields=(
            'id',
            'name',


            'curiculum',
            'curiculum_by',

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
