from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Lecture

from section.serializers import SectionSerializersSimple

class LectureSerializers(serializers.ModelSerializer):
    section = [RecursiveField("section.serializers.SectionSerializersSimple",read_only=True,many=True,required=False)]
    # section = SectionSerializersSimple()
    class Meta:
        model=Lecture
        fields=(
            "name",
            "description",
            "video_url",

            #related things
            'section'
        )
    
    def create(self,validated_data):
        lecture = Lecture(**validated_data)
        lecture.save()
        return lecture

class LectureSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields=(
            "name",
            "video_url",
        )