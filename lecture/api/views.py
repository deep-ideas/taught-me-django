from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from ..serializers import LectureSerializers
from ..models import Lecture


class LectureViewSet(viewsets.ModelViewSet):
    serializer_class = LectureSerializers
    queryset = Lecture.objects.all()
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user,updated_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, instance, validated_Data, ):
    #     # user= request.user._wrapped if hasattr(request.user,'_wrapped') else request.user
    #     # var = self.get_var(data=request.data)
    #     # var.is_valid(raise_exception=True)
    #     # var.save(updated_by=request.user)
    #     # return Response(var.data, status=status.HTTP_200_OK)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(updated_by=request.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def update(self, request,  validated_data, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.update(**validated_data)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

        

