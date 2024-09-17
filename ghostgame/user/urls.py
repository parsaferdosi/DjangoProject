from django.urls import path
from . import views
urlpatterns=[
    path('',views.profileView,name='profile'),
    path('login',views.ViewLogin,name="login"),
    path('register',views.registerView,name="register")
]