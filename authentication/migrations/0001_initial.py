# Generated by Django 4.0 on 2021-12-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_fname', models.CharField(max_length=100)),
                ('emp_lname', models.CharField(max_length=100)),
                ('emp_email', models.CharField(max_length=100)),
                ('emp_gender', models.CharField(max_length=100)),
                ('emp_designation', models.CharField(max_length=100)),
                ('emp_password', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'empData',
            },
        ),
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
