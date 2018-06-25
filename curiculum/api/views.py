from rest_framework import viewsets
from ..serializers import CuriculumSerializers
from ..models import Curiculum

class CuriculumViewSet(viewsets.ModelViewSet):
    serializer_class = CuriculumSerializers
    queryset = Curiculum.objects.all()