from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def signup(request):
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def myorganizer(request):
    return render(request, "authentication/myorganizer.html")