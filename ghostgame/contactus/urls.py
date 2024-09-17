from django.urls import path
from . import views
urlpatterns = [
    path('',views.viewContactUs,name='contact-us')
]
