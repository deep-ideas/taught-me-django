from django.contrib.auth.models import User
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import detail_route, list_route
from django_filters.rest_framework import DjangoFilterBackend
import requests
from rest_framework_jwt.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action



from ..serializers import CourseSerializers
from ..models import Course

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = CourseSerializers
    queryset = Course.objects.all()

    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save(created_by=request.user,updated_by=request.user)
       return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None, format='json'):
        instance = self.queryset.get(pk=pk)
        serializer = CourseSerializers(instance, data=request.data, partial=True)
        if serializer.is_valid():
            course = serializer.save(updated_by=request.user)
            if course:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)

    @action(methods=['get'], permission_classes=[IsAuthenticated], detail=False)
    def get_schema(self, request):
        fields = Course._meta.get_fields()
        field_names = [f.name for f in fields
            if not (f.is_relation)]

        return Response(
            field_names,
            status=status.HTTP_200_OK
        )
    @action(methods=['get'], permission_classes=[IsAuthenticated], detail=True)    
    def curriculum(self, request, pk=None):
        name = Course.objects.get(id=pk)

        serializer = CourseSerializers(name,)
        return Response(serializer.data['from_curriculum'])

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]