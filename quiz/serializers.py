from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Quiz
from lecture.models import Lecture

class QuizSerializers(serializers.ModelSerializer):
    
    lecture = RecursiveField("lecture.serializers.LectureSerializersSimple",read_only=True,required=False,)

    lecture_by = serializers.IntegerField(write_only=True)
    class Meta:
        model = Quiz
        fields = (
            'name', 
            'answer',

            'lecture',

            'lecture_by',    
        )

    def create(self, validated_data):
        lecture_by = validated_data.get("lecture_by")
        validated_data.pop("lecture_by", None)

        quiz = Quiz(**validated_data)

        #related 
        val = Lecture.objects.get(id=lecture_by)
        quiz.lecture = val
        quiz.save()
        
        return quiz

class QuizSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('name', 'answer',)                