from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User

from .models import Comment
from lecture.models import Lecture

class CommentSerializers(serializers.ModelSerializer):
    lecture = RecursiveField('lecture.serializers.LectureSerializersSimple', read_only = True)
    name = RecursiveField("user.serializers.UserSerializerName",read_only=True)

    lecture_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = (
            'name',

            'text',

            'lecture',

            "lecture_id",
        )
    def create(self, validated_data):
        lecture_id = validated_data.get("lecture_id")
        validated_data.pop("lecture_id")
        comment = Comment(**validated_data)
        
        ref = Lecture.objects.get(id=lecture_id)
        comment.lecture = ref
        comment.save()
        return comment



class CommentSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'name',
            'text',
        )
