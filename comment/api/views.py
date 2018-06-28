from rest_framework import viewsets,status
from rest_framework.response import Response

from ..serializers import CommentSerializers
from ..models import Comment

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save(created_by=request.user,updated_by=request.user,name=request.user)
       return Response(serializer.data, status=status.HTTP_201_CREATED) 