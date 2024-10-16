from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brewery

class BrewerySerializer(serializers.ModelSerializer):
    saved_by_users = serializers.SlugRelatedField(
        slug_field='username',  
        queryset=User.objects.all(),
        many=True,
        required=False
    )
    class Meta:
        model = Brewery
        fields = ['name', 'brew_id','city', 'address', 'state', 'phone', 'type', 'url', 'saved_by_users']