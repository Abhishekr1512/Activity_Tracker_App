from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.fields import empty
from authentication.serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import  EmployeeData
import random

# Create your views here.

@api_view(['GET','POST'])
def signup(request):
    if request.method == 'POST':

        num =random.randint(1000000,9999999)

        fname = request.POST.get('emp_fname') 
        lname = request.POST.get('emp_lname')
        email = request.POST.get('emp_email')
        gender = 'M'
        designation = request.POST.get('emp_designation')
        password = request.POST.get('emp_password')
        date1 = datetime.now().strftime ("%Y-%m-%d")

        data = {}
        data['emp_id'] = num
        data['emp_fname'] = fname
        data['emp_lname'] = lname
        data['emp_email'] = email
        data['emp_gender'] = gender
        data['emp_designation'] = designation
        data['emp_password'] = password
        data['date'] = date1

        # print(data)     

        serializer = EmployeeSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return render(request, "authentication/signinup.html")
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    return render(request, "authentication/signinup.html")

@api_view(['GET','POST'])
def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
     
    user = EmployeeData.objects.filter(emp_email = username,emp_password =password)
    serializer = EmployeeSerializer(data =user,many=True)
    
    if serializer.is_valid():
           print(serializer.data)
           return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
    else:
        #  print(serializer.data)
        # return Response(serializer.data, status = status.HTTP_200_OK)
         return HttpResponseRedirect( "/myorganizer")

def myorganizer(request):
    return render(request, "authentication/myorganizer.html")

def activitydetails(request):
    return render(request, "authentication/activitydetails.html")

def resetpassword(request):
    return render(request, "authentication/reset.html")