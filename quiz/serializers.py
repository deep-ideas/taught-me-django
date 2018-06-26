from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Quiz

class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("name", "answer")

class QuizSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("name", "answer")                