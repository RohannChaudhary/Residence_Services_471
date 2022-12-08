import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, first_name, last_name,  **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password, first_name, last_name,  **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, first_name, last_name,  **extra_fields)

#     def create_superuser(self, email, first_name, last_name, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, first_name, last_name,  **extra_fields)

class Person(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField(('email address'), unique=True)
    phone_num = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

# Food_Plan model
class Food_Plan(models.Model):
    type = models.CharField(max_length=20,primary_key=True)
    days = models.IntegerField()

# Student model
class Student(models.Model):
    user = models.OneToOneField('Person', primary_key=True, on_delete=models.CASCADE)
    year = models.IntegerField()
    major = models.CharField(max_length=30)
    studentID = models.CharField(max_length=8)
    gender = models.CharField(max_length=30)
    type = models.ForeignKey(Food_Plan,on_delete = models.SET_NULL, null = True)
    
    def __str__(self):
        return str(self.user) + " (year:" + str(self.year) + ")"

# Staff model
class Staff(models.Model):
    user = models.OneToOneField('Person', primary_key=True, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.user

# Technician model
class Technician(Staff):
    technicianID = models.CharField(max_length=8)
    gender = models.CharField(max_length=30, null=True)
    specialization = models.CharField(max_length=100, null=True)
    # def __str__(self):
    #     return str(str(self.user) + '(' + self.specialization + ')')  

# Admin model
class Admin(Staff):
    adminID = models.CharField(max_length=8)
    gender = models.CharField(max_length=30,null=True)
    position = models.CharField(max_length=100, null=True)
    # def __str__(self):
    #     # list_display = [field.name for field in Admin._meta.get_fields()]
    #     # return list_display
    #     return str(self.user) + '(' + self.position + ')'  


# Building model
class Building(models.Model):
    buildingID = models.AutoField(primary_key=True)
    buildingName = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)

class Room(models.Model):
    roomNo = models.CharField(max_length=6)
    buildingID = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Constraint:
        constraints = [models.UniqueConstraint(fields=['roomNo','buildingID'], name = 'roomID')]
        
class Room_Booking(models.Model):
    roomNo = models.ForeignKey('Room',on_delete=models.CASCADE)
    studentID = models.OneToOneField('Student', on_delete=models.SET_NULL,null=True)

    class Constraint:
        constraints = [models.UniqueConstraint(fields=['roomNo','studentID'], name = 'roomBookingConstraint')]


class Maintenance(models.Model):
    STATUS = (
        ('RESOLVED','RESOLVED'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('NOT RESOLVED', 'NOT RESOLVED')
    )
    maintenanceID = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, blank=True)
    studentID = models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey('Room',on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=30,default='100')
    last_name = models.CharField(max_length=30,default='100')
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='NOT RESOLVED')

class Complain(models.Model):
    STATUS = (
        ('RESOLVED','RESOLVED'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('NOT RESOLVED', 'NOT RESOLVED')
    )
    complainID = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    student = models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    admin = models.ForeignKey('Admin',on_delete=models.SET_NULL ,null=True)
    details = models.CharField(max_length=1000)
    status = models.CharField(max_length=20, choices=STATUS, default='NOT RESOLVED')
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)

class Fulfills_Maintenance(models.Model):
    maintenanceID = models.ForeignKey('Maintenance',on_delete=models.SET_NULL,null=True)
    technicianID = models.ForeignKey('Technician',on_delete= models.SET_NULL,null=True)
    
class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    date = models.DateField()
    studentID = models.OneToOneField('Student',on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField()
    
    
class Mail(models.Model):
    mailID = models.AutoField(primary_key=True)
    date = models.DateField()
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
