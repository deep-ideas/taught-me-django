from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.utils.functional import SimpleLazyObject
from user.models import User

from .models import Lecture
from section.models import Section
from quiz.models import Quiz

from section.serializers import SectionSerializer,SectionSerializersSimple
from quiz.serializers import QuizSerializersSimple

class LectureSerializers(serializers.ModelSerializer):
    section = RecursiveField("section.serializers.SectionSerializersSimple",read_only=True,required=False,)
    # section = SectionSerializersSimple()
    quizzes = RecursiveField("quiz.serializers.QuizSerializersSimple",read_only=True,required=False,many=True)
    comment = RecursiveField('comment.serializers.CommentSerializersSimple',read_only=True,many=True)
    section_id = serializers.IntegerField(allow_null=True,write_only=True,required=False,)
    class Meta:
        model=Lecture
        fields=(
            'id',
            "name",
            "description",
            "video_url",
            
            'is_allow_comment',
            'is_downloadable',
            'is_pubished',
            'is_free_preview',

            #related things
            "section",
            "quizzes",
            "comment",
            
            'section_id',
            # 'updated_by',
            # 'created_by',
    
        )
    
    # def get_custom_validated_data(self, validated_data):
    #     getSection = validated_data.get('getSection')
    #     validated_data.pop('getSection', None)
    #     if getSection:
    #         getSection = Section.objects.get(id=getSection)
    #         validated_data['section'] = getSection

    #     return validated_data

    def create(self, validated_data):
        section_id = validated_data.get("section_id")
        validated_data.pop("section_id", None)

        lecture = Lecture(**validated_data)

        #related with section
        section = Section.objects.get(id=section_id)
        lecture.section = section
        lecture.save()
        
        return lecture

    # def create(self, instance, validated_data):
    #     valdated_data = self.get_custom_validated_data()
        

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.video_url = validated_data.get('video_url', instance.video_url)
        instance.is_allow_comment = validated_data.get('is_allow_comment', instance.is_allow_comment)
        instance.is_downloadable = validated_data.get('is_downloadable', instance.is_downloadable)
        instance.is_downloadable = validated_data.get('is_downloadable', instance.is_downloadable)
        instance.is_pubished = validated_data.get('is_pubished', instance.is_pubished)
        instance.is_free_preview = validated_data.get('instrument', instance.is_free_preview)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        # if isinstance(instance.updated_by, LazyObject): 
        # # print type(instance.updated_by = validated_data.get('updated_by', instance.updated_by)) 
        #     print (type(instance.updated_by))
        
        instance.save()
        return instance
        

class LectureSerializersSimple(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields=(
            "name",
            "video_url",
        )