from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework_recursive.fields import RecursiveField

from lecture.serializers import LectureSerializersSimple
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    # lecture = RecursiveField('lecture.seriaizers.LectureSerializersSimple', read_only = True, required = False)
    class Meta:
        model = Comment
        fields = (
            'text',

            'lecture',
            'updated_by',
            'created_by',
            )

class CommentSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'text',
        )
