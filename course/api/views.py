from rest_framework import viewsets
from ..serializers import CourseSerializers
from ..models import Course

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()

    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save(created_by=request.user,updated_by=request.user)
       return Response(serializer.data, status=status.HTTP_201_CREATED)