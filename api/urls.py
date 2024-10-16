from django.urls import path
from .views import UserSavedBreweriesView, SaveBreweryView, BreweryCitySearchView, BreweryNameSearchView

urlpatterns = [
    path('save_brewery/<str:brewery_id>', SaveBreweryView.as_view(), name='save_brewery'),
    path('view_saves', UserSavedBreweriesView.as_view(), name='view_saves'),
    path('search_city/<str:city>', BreweryCitySearchView.as_view(), name='city_search'),
    path('search_name/<str:name>', BreweryNameSearchView.as_view(), name='name_search'),
]
