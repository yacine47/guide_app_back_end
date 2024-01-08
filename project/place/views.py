from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from .serializers import PlaceSerializer,CategorySerializer
from .models import Place,Category
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from favorite.models import Favorite

# Create your views here.

# get all Places
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_places(request):
    places = Place.objects.all()
    serializers = PlaceSerializer(places,many=True)
    return Response({
        'places':serializers.data,
    })

# get all categories
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.all()
    serializers = CategorySerializer(categories,many=True)
    return Response(serializers.data,)


# get all Places
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_places_favorite(request):
    user_profile = request.user 
    favorites = Favorite.objects.filter(id_user =user_profile)
    places_ids = favorites.values_list('id_place',flat=True)
    places = Place.objects.filter(id__in = places_ids)
    serializers = PlaceSerializer(places,many=True)
    return Response(serializers.data)

