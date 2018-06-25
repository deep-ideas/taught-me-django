from rest_framework import viewsets
from ..serializers import SectionSerializer
from ..models import Section

class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()