from datetime import date
import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
from . import serializer
from .serializer import StudentSerializer,PersonSerializer, AdminSerializer, StaffSerializer, TechnicianSerializer, PaymentSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
def index(request):
    return render(request,'index.html')

def studentLogin(request):
    # student = models.Student.objects.all()
    # serializer = StudentSerializer(student,many=True)
    # content = JSONRenderer().render(serializer.data)
    # person = models.Person.objects.all()
    # personSerializer = PersonSerializer(person,many=True)
    # personContent = JSONRenderer().render(personSerializer.data)

    # ys = json.loads(content)
    # xs = json.loads(personContent)

    # if request.method == 'POST':
    #     user = request.POST['username']
    #     password = request.POST['password']

    #     for x in xs:
    #         if x['username'] == user and x['password'] == password:
    #             a = x
    #             return JsonResponse(personSerializer.data,safe=False)
    #             break
        
    #     if a is None:
    #         messages.info(request,'Credentials Invalid')
    #         return redirect ('/')

    #     for y in ys:
    #         if y['user'] == user:
    #            b = y 
    #            break       
                
    #     a = dict(a)
    #     b = dict(b)
    #     return render(request,'student.html',{'a':a, 'b':b})
    # return JsonResponse(personSerializer.data,safe=False)
    if request.method == 'POST':
        username = request.POST['username']
        passowrd = request.POST['password']

        student = models.Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        content = JSONRenderer().render(serializer.data)

        person = models.Person.objects.all()
        personSerializer = PersonSerializer(person,many=True)
        personContent = JSONRenderer().render(personSerializer.data)

        payment = models.Payment.objects.all()
        paymentSerializer = PaymentSerializer(payment,many=True)
        paymentContent = JSONRenderer().render(paymentSerializer.data)

        ys = json.loads(content)
        xs = json.loads(personContent)
        zs = json.loads(paymentContent)
        
        for x in xs:
            if x['username'] == username and x['password'] == passowrd:
                a = x
                break
        
        if a is None:
            messages.info(request,'Credentials Invalid')
            return redirect ('login')

        for y in ys:
            if y['user'] == username:
               b = y 
               break       

        for z in zs:
            if z['studentID'] == username:
               c = z
               break    
                
        
        if(a is not None and b is not None):
            a = dict(a)
            b = dict(b)
        if(c is not None):
            c = dict(c)


        #Payment Due
        if c['date'][0:4:1] == str(date.today().year):
            amountDue = 10000 - c['amount']
        else :
            amountDue = 10000


        return render(request,'student.html',{'a':a, 'b':b, 'amountDue': amountDue})        

        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('/')
        # else:
        #     messages.info(request,'Credentials Invalid')
        #     return redirect ('login')
    else:
       return render(request,'login.html') 
def post(request):
    return render(request,'student.html')

def maintenanceRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        details = request.POST['details']
        building = request.POST['building']
        
        # room1 = models.Room.objects.filter(roomNo = room , buildingID = building)
        # room = models.Room(room1)
        room_list = list(models.Room.objects.all())
        person_list = list(models.Person.objects.all())
        
        student = models.Person()
        room= models.Room()
        for person1 in person_list:
            if(person1.username == username):
                student = person1
                break
        for room1 in room_list:
            if room1.roomNo == room and room1.buildingID == building:
                room = room1
                break
        # student1 = models.Student.objects.filter(user=username)
        # student = models.Student(student1)
        if(student and room):
            studentobject = models.Student(user=student)
            m = models.Maintenance(studentID = studentobject, date = date.today(), room = room, details = details, status = 'NOT RESOLVED')
            m.save_base()
            messages.info(request,'Maintenance Request Submitted')
            return redirect('maintenanceRequest')
        else:
            messages.info(request,'Invalid Username')
            return redirect('maintenanceRequest')
    else:
        # student = models.Student.objects.all()
        # serializer = StudentSerializer(student,many=True)
        # content = JSONRenderer().render(serializer.data)
        # return JsonResponse(serializer.data,safe=False)
        return render(request,'maintenanceRequest.html')