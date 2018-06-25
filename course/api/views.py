from rest_framework import viewsets
from ..serializers import CourseSerializers
from ..models import Course

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()