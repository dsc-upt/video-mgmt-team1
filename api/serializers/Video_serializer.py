from ..models.video import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		exclude = ['id',]
