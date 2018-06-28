from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Answer
from quiz.models import Quiz
from question.models import Question

class AnswerSerializer(serializers.ModelSerializer):
    quiz = RecursiveField("quiz.serializers.QuizSerializersSimple",read_only=True)
    question = RecursiveField("question.serializers.QuestionSerializersSimple",read_only=True)

    quiz_by = serializers.IntegerField(write_only=True,required=True)
    question_by = serializers.IntegerField(write_only=True,required=True)
    class Meta:
        model=Answer
        fields = (
            "name", 
            "is_answer",

            "quiz",
            "question",

            "quiz_by",
            "question_by",
        )                
    
    
    def get_custom_validated_data(self, validated_data):
        quiz_by = validated_data.get('quiz_by')
        validated_data.pop('quiz_by', None)
        if quiz_by:
            quiz_by = Quiz.objects.get(id=quiz_by)
            validated_data['quiz'] = quiz_by
            
        question_by = validated_data.get('question_by')
        validated_data.pop('question_by', None)
        if question_by:
            question_by = Question.objects.get(id=question_by)
            validated_data['question'] = question_by

        return validated_data

    def create(self, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        addData = Answer.objects.create(**validated_data)
        return addData

    def update(self, instance, validated_data):
        validated_data = self.get_custom_validated_data(validated_data)
        getUpdate = Answer.objects.filter(id=instance.id)
        getUpdate.update(**validated_data)
        return getUpdate.get()



class AnswerSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ("name", "is_answer")
                                                