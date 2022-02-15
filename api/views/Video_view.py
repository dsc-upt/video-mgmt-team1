from rest_framework import generics
from ..models.video import Video
from ..serializers.Video_serializer import VideoSerializer


class VideoList(generics.ListCreateAPIView):
	queryset = Video.objects.all()
	serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
