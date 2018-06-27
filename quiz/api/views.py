from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import Quiz
from ..serializers import QuizSerializers

class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializers
    queryset = Quiz.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user,updated_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)