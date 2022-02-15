from rest_framework import generics
from ..models.Video import Video
from ..serializers import Video_serializer

class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = Video_serializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = Video_serializer