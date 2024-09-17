from django.urls import path
from . import views
urlpatterns = [
    path('',views.ticketmanager,name='contact-us')
]
