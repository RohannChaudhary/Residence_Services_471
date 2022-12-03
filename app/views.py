from datetime import date
import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
from . import serializer
from .serializer import StudentSerializer,PersonSerializer, AdminSerializer, StaffSerializer, TechnicianSerializer, PaymentSerializer, ComplainSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
def index(request):
    return render(request,'index.html')

def studentLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passowrd = request.POST['password']

        person = models.Person.objects.all()
        
        personSerializer = PersonSerializer(person,many=True)
        personContent = JSONRenderer().render(personSerializer.data)

        xs = json.loads(personContent)
        
        for x in xs:
            if x['username'] == username and x['password'] == passowrd:
                a = x
                break

        if(a['is_student']):
            
            student = models.Student.objects.all()
            serializer = StudentSerializer(student,many=True)
            content = JSONRenderer().render(serializer.data)
            
                
            payment = models.Payment.objects.all()
            paymentSerializer = PaymentSerializer(payment,many=True)
            paymentContent = JSONRenderer().render(paymentSerializer.data)
                
            ys = json.loads(content)
            zs = json.loads(paymentContent)

            for y in ys:
                if y['user'] == username:
                    b = y 
                    break       

            for z in zs:
                if z['studentID'] == username:
                    c = z
                    break        
                
        
            a = dict(a)
            b = dict(b)
            # c = dict(c)


            # #Payment Due
            # if c['date'][0:4:1] == str(date.today().year):
            #     amountDue = 10000 - c['amount']
            # else :
            #     amountDue = 10000


            return render(request,'student.html',{'a':a, 'b':b})              
        
        elif(a['is_admin']):
            
            staff = models.Staff.objects.all()
            staffSerializer = StaffSerializer(staff,many=True)
            staffContent = JSONRenderer().render(staffSerializer.data)
            
                
            admin = models.Admin.objects.all()
            adminSerializer = AdminSerializer(admin,many=True)
            adminContent = JSONRenderer().render(adminSerializer.data)
            
            xs = json.loads(staffContent)
            ys = json.loads(adminContent)
            
            for y in ys:
                if y['user'] == username:
                    b = y 
                    break 
                 
   
            complain = models.Complain.objects.all()
            complainSerializer = ComplainSerializer(complain,many=True)
            complainContent = JSONRenderer().render(complainSerializer.data)
            
            zs = json.loads(complainContent)
            
            zs_dict = [z for z in zs if z['admin'] == username]
                           
            return render(request,'adminDashboard.html',{'zs':zs_dict})
    
        elif(a['is_technician']):
            
            staff = models.Staff.objects.all()
            staffSerializer = StaffSerializer(staff,many=True)
            staffContent = JSONRenderer().render(staffSerializer.data)
            
            technician = models.Technician.objects.all()
            technicianSerializer = TechnicianSerializer(admin,many=True)
            technicianContent = JSONRenderer().render(technicianSerializer.data)
            
            xs = json.loads(staffContent)
            ys = json.loads(technicianContent)
            
            for y in ys:
                if y['user'] == username:
                    b = y 
                    break 
                
            maintance = models.Maintenance.objects.all()
            maintanceSerializer = MaintanceSerializer(maintance,many=True)
            maintanceContent = JSONRenderer().render(maintanceSerializer.data)
            
            zs = json.loads(maintanceContent) 
            
            zs_dict = [z for z in zs if z['technician'] == username]
            
            return render(request,'technicianDashboard.html',{'zs':zs_dict})
        else:
            messages.info(request,'Credentials Invalid')
            return JsonResponse(serializer.data,safe=False)
            return redirect ('login')

  

        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('/')
        # else:
        #     messages.info(request,'Credentials Invalid')
        #     return redirect ('login')
    else:
       return render(request,'login.html') 

def maintenanceRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        details = request.POST['details']
        building = request.POST['building']
        
        # room1 = models.Room.objects.filter(roomNo = room , buildingID = building)
        # room = models.Room(room1)
        room_list = list(models.Room.objects.all())
        student_list = list(models.Student.objects.all())
        
        student = models.Student()
        room= models.Room()
        for student1 in student_list:
            if(student1.user == username):
                student = student1
                break

        for room1 in room_list:
            if room1.roomNo == room and room1.buildingID == building:
                room = room1
                break

        if(student is not None and room is not None):
            detailsAdd = username + " RoomNo: " + room + "Building ID:" + building
            m = models.Maintenance(studentID = student, date = date.today(), room = room, details = details + "\n" + detailsAdd, status = 'NOT RESOLVED')
            m.save_base()
            messages.info(request,'Maintenance Request Submitted')
            return redirect('maintenanceRequest')
        else:
            messages.info(request,'Invalid Username')
            return redirect('maintenanceRequest')
    else:
        return render(request,'maintenanceRequest.html')
def complainRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        admin = request.POST['admin']
        details = request.POST['details']
        building = request.POST['building']
        
        admin_list = list(models.Admin.objects.all())
        student_list = list(models.Student.objects.all())
        
        student = models.Student()
        admin = models.Admin()
        for student1 in student_list:
            if(student1.user == username):
                student = student1
                break

        for admin1 in admin_list:
            if admin1.position == admin:
                admin  = admin1
                break

        if(student is not None and admin is not None):
            detailsAdd = username
            m = models.Complain(student = student, date = date.today(), admin = admin, details = details + "\n" + detailsAdd, status = 'NOT RESOLVED')
            m.save_base()
            messages.info(request,'Complain Submitted')
            return redirect('complainRequest')
        else:
            messages.info(request,'Invalid Username')
            return redirect('complainRequest')
    else:
        return render(request,'complainRequest.html')
    
def admin(request,zs):
    return render(request,'adminDashboard.html',{'zs':zs})