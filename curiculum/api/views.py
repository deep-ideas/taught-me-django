from rest_framework import viewsets
from ..serializers import CuriculumSerializers
from ..models import Curiculum

class CuriculumViewSet(viewsets.ModelViewSet):
    serializer_class = CuriculumSerializers
    queryset = Curiculum.objects.all()

    def create(self, request, *args, **kwargs,):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED) 