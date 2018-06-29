from rest_framework import serializers
from .models import Course
from rest_framework_recursive.fields import RecursiveField
# from curriculum.serializers import CurriculumSerializersSimple

class CourseSerializers(serializers.ModelSerializer):
    # from_curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple', read_only = True)
    from_curriculum = RecursiveField('curriculum.serializers.CurriculumSerializersSimple',read_only=True,many=True)
    # to_course = CurriculumSerializersSimple()
    created_by = RecursiveField('user.serializers.UserSerializerSimple',read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple',read_only=True)
    class Meta:
        model = Course
        fields = (
            'name',
            'description',
            'subtitle',

            'is_enrolled',
            "from_curriculum",
            
            'updated_by',
            'created_by'
        ) 


class CourseSerializersSimple(serializers.ModelSerializer):
    # to_course = RecursiveField('curriculum.serializers.CurriculumSerializersSimple',read_only=True,many=True)
    # to_course = CurriculumSerializersSimple()
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            # 'description',
            # 'subtitle',

            # 'to_course'
        ) 
