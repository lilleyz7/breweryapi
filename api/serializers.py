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
        fields = ['name', 'brew_id','city', 'street', 'state', 'phone', 'brewery_type', 'website_url', 'saved_by_users']