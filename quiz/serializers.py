from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Quiz
from lecture.models import Lecture

class QuizSerializers(serializers.ModelSerializer):
    
    lecture = RecursiveField("lecture.serializers.LectureSerializersSimple",read_only=True)
    
    questions = RecursiveField('question.serializers.QuestionSerializersSimple',read_only=True,)

    from_answer = RecursiveField('answer.serializers.AnswerSerializerSimple',read_only=True,many=True)

    lecture_by = serializers.IntegerField(write_only=True)
    class Meta:
        model = Quiz
        fields = (
            'id',
            'name', 
            'answer',
            
            'from_answer',
            "questions",
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
        fields = ('id','name', 'answer',)                