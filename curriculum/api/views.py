from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from ..serializers import CurriculumSerializers
from ..models import Curriculum

class CurriculumViewSet(viewsets.ModelViewSet):
    serializer_class = CurriculumSerializers
    queryset = Curriculum.objects.all()

    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save(created_by=request.user,updated_by=request.user)
       return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None, format='json'):
        instance = self.queryset.get(pk=pk)
        serializer = CurriculumSerializers(instance, data=request.data, partial=True)
        # print('INSTANCE', instance)
        # print('SERIALIZER :', serializer)
        if serializer.is_valid():
            curriculum = serializer.save(updated_by=request.user)
            if curriculum :
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'error' : serializer.error}, status=status.HTTP_403_FORBIDDEN)

