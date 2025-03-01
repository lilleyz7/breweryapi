from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Brewery
from .serializers import BrewerySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .openDB import OpenDB
# Create your views here.

class SaveBreweryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, brewery_id):
        user = request.user
        try:
            brewery = Brewery.objects.get(brew_id=brewery_id)
            if user in brewery.saved_by_users.all():
                brewery.saved_by_users.remove(user)
                return Response({'status': 'unsaved'}, status=status.HTTP_200_OK)
            else:
                brewery.saved_by_users.add(user)
                return Response({'status': 'saved'}, status=status.HTTP_200_OK)
        except Brewery.DoesNotExist:
            db = OpenDB()
            brewery_data = db.get_brewery_by_id(brewery_id)
            if len(brewery_data) == 0:
                return Response({'error': 'brewery not found'}, status=status.HTTP_404_NOT_FOUND)
            if (isinstance(brewery_data, str)):
                return Response({'error': 'We done diddly got an error'}, status=status.HTTP_404_NOT_FOUND)
            try:
                serializer = BrewerySerializer(data=brewery_data)
                if serializer.is_valid():
                    serializer.save()
                    brewery = Brewery.objects.get(brew_id=brewery_data['brew_id'])
                    brewery.saved_by_users.add(user)
                    return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class UserSavedBreweriesView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BrewerySerializer

    def get_queryset(self):
        return Brewery.objects.filter(saved_by_users=self.request.user)

class BreweryNameSearchView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, name):
        db = OpenDB()
        breweries = db.get_brewery_by_name(name)
        if not breweries:
            return Response({'error': 'No breweries found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'data': breweries}, status=status.HTTP_200_OK)
    
class BreweryCitySearchView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, city):
        db = OpenDB()
        breweries = db.get_breweries_by_city(city)
        if not breweries:
            return Response({'error': 'No breweries found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'data': breweries}, status=status.HTTP_200_OK)
    