import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
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
    
    def __str__(self):
        return str(self.type) + " (days:" + str(self.days) + ")"

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
    def __str__(self):
        return self.user

# Technician model
class Technician(Staff):
    technicianID = models.CharField(max_length=8)
    gender = models.CharField(max_length=30, null=True)
    specialization = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(str(self.user) + '(' + self.specialization + ')')  

# Admin model
class Admin(Staff):
    adminID = models.CharField(max_length=8)
    gender = models.CharField(max_length=30,null=True)
    position = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.user) + '(' + self.position + ')'  


# Building model
class Building(models.Model):
    buildingID = models.AutoField(primary_key=True)
    buildingName = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.buildingID) + " (name:" + str(self.buildingName) + ")"

class Room(models.Model):
    roomNo = models.CharField(max_length=6)
    buildingID = models.ForeignKey(Building, on_delete=models.CASCADE)

    class Constraint:
        constraints = [models.UniqueConstraint(fields=['roomNo','buildingID'], name = 'roomID')]
        
    def __str__(self):
        return str(self.roomNo) + " (buildingID:" + str(self.buildingID) + ")"
        
class Room_Booking(models.Model):
    roomNo = models.ForeignKey('Room',on_delete=models.CASCADE)
    studentID = models.OneToOneField('Student', on_delete=models.SET_NULL,null=True)

    class Constraint:
        constraints = [models.UniqueConstraint(fields=['roomNo','studentID'], name = 'roomBookingConstraint')]
    
    def __str__(self):
        return str(self.roomNo) + " (studentID:" + str(self.studentID) + ")"


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
    
    def __str__(self):
        return str(self.maintenanceID) + " (studentID:" + str(self.studentID) + ")"

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

    def __str__(self):
        return str(self.complainID) + " (studentID:" + str(self.student) + ")"
    
class Fulfills_Maintenance(models.Model):
    maintenanceID = models.ForeignKey('Maintenance',on_delete=models.SET_NULL,null=True)
    technicianID = models.ForeignKey('Technician',on_delete= models.SET_NULL,null=True)
    
    def __str__(self):
        return str(self.maintenanceID) + " (technicianID:" + str(self.technicianID) + ")"
    
class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    date = models.DateField()
    studentID = models.OneToOneField('Student',on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField()
    
    def __str__(self):
        return str(self.paymentID) + " (studentID: " + str(self.studentID) + " amount: " + str(self.amount) + ")"
    
    
class Mail(models.Model):
    mailID = models.AutoField(primary_key=True)
    date = models.DateField()
    studentID = models.ForeignKey(Student,on_delete=models.CASCADE)
    pickedUp = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.mailID) + " (studentID:" + str(self.studentID) + " pcikedUp: " + str(self.pickedUp) + ")"
