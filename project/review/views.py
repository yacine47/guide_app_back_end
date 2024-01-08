from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializer(reviews,many=True)
    return Response(
        serializers.data,
    )


@api_view(['DELETE'])
def delete_review(request,id):
    try:
        review = Review.objects.get(id=id)
        review.delete()
        return Response({
            'details': 'Review removed successfully',
        }, status=status.HTTP_200_OK)
    except Review.DoesNotExist:
        return Response({
            'details': 'Review does not exist for this user and place',
        }, status=status.HTTP_404_NOT_FOUND)


