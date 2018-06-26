from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields = ("name", "is_answer")                

class AnswerSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ("name", "is_answer")
                                                