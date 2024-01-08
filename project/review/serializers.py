from rest_framework import serializers 
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='id_user.first_name')
    last_name = serializers.CharField(source='id_user.last_name')
    class Meta:
        model = Review
        fields = '__all__'


