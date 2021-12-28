from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.resetpassword, name="reset"),
    path('activitydetails', views.activitydetails, name="activitydetails"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('myorganizer', views.myorganizer, name="myorganizer")
]
