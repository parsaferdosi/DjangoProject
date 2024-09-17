from django.urls import path,include
from . import views
app_name = 'homescreen'
urlpatterns = [
    path('',views.viewhome,name='welcom-page'),
    path('gamelist',views.gamelist,name='game-list'),
    path('<slug:m>',views.moresiscription),
    path('search/',views.search_future,name='search')
]
