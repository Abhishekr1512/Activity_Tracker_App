from django.db import models

# Create your models here.

class EmpModel(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1)


    class Meta:
        db_table = "employee"

class EmployeeData(models.Model):
    emp_id = models.IntegerField()
    emp_fname = models.CharField(max_length=100)
    emp_lname = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    emp_gender = models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=100)
    emp_password = models.CharField(max_length=100)
    date = models.DateField()




    class Meta:
        db_table = "empData"




