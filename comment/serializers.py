from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field=("text")