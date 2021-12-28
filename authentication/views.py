from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def signup(request):
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def myorganizer(request):
    return render(request, "authentication/myorganizer.html")

def activitydetails(request):
    return render(request, "authentication/activitydetails.html")

def resetpassword(request):
    return render(request, "authentication/reset.html")