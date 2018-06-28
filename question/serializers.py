from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

# from quiz.serializers import QuizSerializersSimple,QuizSerializers
from .models import Question
from quiz.models import Quiz

class QuestionSerializers(serializers.ModelSerializer):
    quiz = RecursiveField('quiz.serializers.QuizSerializersSimple',read_only=True)

    quiz_by = serializers.IntegerField(write_only=True,required=False,)

    class Meta:
        model = Question
        fields=(
            "id",
            "name",

            "quiz",

            "quiz_by",
        )

    def create(self, validated_data):
        quiz_by = validated_data.get("quiz_by")
        validated_data.pop("quiz_by", None)

        question = Question(**validated_data)

        #related with section
        var = Quiz.objects.get(id=quiz_by)
        question.quiz = var
        question.save()
        
        return question


class QuestionSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=(
            "name",
        )