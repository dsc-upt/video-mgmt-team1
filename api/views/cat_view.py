from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.Category_serializer import CategorySerializer

from ..models.category import Category


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def get_by_id(request, id):
	try:
		if request.method == 'GET':
			catg = Category.objects.get(id=id)
			serializer = CategorySerializer(catg)
			return Response(serializer.data)
		if request.method == 'POST':
			serializer = CategorySerializer(request.data)
			if serializer.is_valid():
				if Category.objects.filter(title=request.data['name']).exists():
					serializer.save()
					return Response(serializer.data,
									status=status.HTTP_202_ACCEPTED)
		if request.method == 'PUT':
			serializer = CategorySerializer(request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,
								status=status.HTTP_202_ACCEPTED)
		if request.method == 'DELETE':
			Category.objects.get(id=id).delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
	except Category.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_cat_list(request):
	catgs = Category.objects.all()
	serializer = CategorySerializer(catgs, many=True)
	return Response(serializer.data)
