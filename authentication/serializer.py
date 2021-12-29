from django.db.models import fields
from rest_framework import serializers
from .models import EmpModel,EmployeeData

class EmployeeSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = EmpModel
         fields = ['id','empname','email','occupation','salary','gender']


         model = EmployeeData
         fields = ['emp_id','emp_fname','emp_lname','emp_email','emp_gender','emp_designation','emp_password','date']


     