from datetime import date
import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import models
from . import serializer
from .serializer import StudentSerializer,PersonSerializer, AdminSerializer, StaffSerializer, TechnicianSerializer, PaymentSerializer, ComplainSerializer, MaintenanceSerializer, Fulfills_Maintenance, RoomBookingSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def complainRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        details = request.POST['details']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
 
    
        person = models.Person.objects.all()
        serializer = PersonSerializer(person,many=True)
        content = JSONRenderer().render(serializer.data)
        
        xs = json.loads(content)
        
        array = []
        for x in xs:
            array.append(x['username'])
            if x['username'] == username and x['password'] == password:
                a = x
                break
            elif(x['username'] == username and x['password']!=password):
                messages.info(request,'Incorrect Password')
                return redirect('complainRequest')
            
        if not (username in array):
            messages.info(request,"Invalid Username")
            return redirect('complainRequest')
        
        student_list = list(models.Student.objects.all())
        
        student = models.Student()
        for student1 in student_list:
            if(str(student1.user) == username):
                student = student1
                break
    

        if(student is not None and admin is not None):
            detailsAdd = username
            m = models.Complain(first_name = first_name , last_name = last_name, student = student, date = date.today(), details = details + "\n" + detailsAdd, status = 'NOT RESOLVED')
            m.save_base()
            messages.info(request,'Complain Submitted')
            return redirect('complainRequest')
        else:
            messages.info(request,'Invalid Username')
            return redirect('complainRequest')
    else:
        return render(request,'complainRequest.html')

def studentLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passowrd = request.POST['password']

        person = models.Person.objects.all()
        
        personSerializer = PersonSerializer(person,many=True)
        personContent = JSONRenderer().render(personSerializer.data)

        xs = json.loads(personContent)
        
        array = []
        for x in xs:
            array.append(x['username'])
            if x['username'] == username and x['password'] == passowrd:
                a = x
                break
            elif(x['username'] == username and x['password']!=passowrd):
                messages.info(request,'Incorrect Password')
                return redirect('login')
            
        if not (username in array):
            messages.info(request,"Invalid Username")
            return redirect('login')
            
            
               
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
                
            complain = models.Complain.objects.all()
            complainSerializer = ComplainSerializer(complain,many=True)
            complainContent = JSONRenderer().render(complainSerializer.data)
            
            zs = json.loads(complainContent)
            
            zs_dict = [z for z in zs if z['student'] == username]
            
            
            maintenance1 = models.Maintenance.objects.all()
            maintanceSerializer1 = MaintenanceSerializer(maintenance1,many=True)
            maintanceContent1 = JSONRenderer().render(maintanceSerializer1.data)
            
            roomBooking = models.Room_Booking.objects.all()
            roomBookingSerializer = RoomBookingSerializer(roomBooking,many=True)
            roomBookingContent = JSONRenderer().render(roomBookingSerializer.data)
            
            
            bs = json.loads(maintanceContent1)
            cs = json.loads(roomBookingContent)
            

            ys_dict = [z for z in bs if z['studentID']==username]
            
            
            for z in cs:
                if z['studentID'] == username:
                    c = z
                    break 
        
            a = dict(a)
            b = dict(b)
            c = dict(c)


            # #Payment Due
            # if c['date'][0:4:1] == str(date.today().year):
            #     amountDue = 10000 - c['amount']
            # else :
            #     amountDue = 10000


            return render(request,'student.html',{'a':a, 'b':b, 'c':c,'zs':zs_dict, 'ys':ys_dict})              
        
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
            
            zs_dict = [z for z in zs if z['admin'] == username and z['status'] != 'RESOLVED']
            ys_dict = [y for y in zs if y['admin'] == username and y['status'] == 'RESOLVED']               
            
            return render(request,'adminDashboard.html',{'a':a, 'b':b,'zs':zs_dict, 'ys':ys_dict})
    
        elif(a['is_technician']):
            
            staff = models.Staff.objects.all()
            staffSerializer = StaffSerializer(staff,many=True)
            staffContent = JSONRenderer().render(staffSerializer.data)
            
            technician = models.Technician.objects.all()
            technicianSerializer = TechnicianSerializer(technician,many=True)
            technicianContent = JSONRenderer().render(technicianSerializer.data)
            
            xs = json.loads(staffContent)
            ys = json.loads(technicianContent)
            
            for y in ys:
                if y['user'] == username:
                    b = y 
                    break 
                
            maintance = models.Fulfills_Maintenance.objects.all()
            maintanceSerializer = Fulfills_Maintenance(maintance,many=True)
            maintanceContent = JSONRenderer().render(maintanceSerializer.data)
            
            maintenance1 = models.Maintenance.objects.all()
            maintanceSerializer1 = MaintenanceSerializer(maintenance1,many=True)
            maintanceContent1 = JSONRenderer().render(maintanceSerializer1.data)
            
            zs = json.loads(maintanceContent) 
            bs = json.loads(maintanceContent1)
            
            zs_dict = [z for z in zs if z['technicianID'] == username]
            
           
            for z in zs_dict :
                array.append(z['maintenanceID'])
                
            ys = [z for z in bs if z['maintenanceID'] in array and z['status'] == 'RESOLVED']
            zs = [z for z in bs if z['maintenanceID'] in array and z['status'] != 'RESOLVED']

            return render(request,'technicianDashboard.html',{'a':a, 'b': b ,'zs':zs, 'ys':ys})
        else:
            messages.info(request,'Credentials Invalid')
            return redirect ('login')
    else:
       return render(request,'login.html') 

def maintenanceRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        roomnumber = request.POST['room']
        details = request.POST['details']
        building = request.POST['building']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        
        # room1 = models.Room.objects.filter(roomNo = room , buildingID = building)
        # room = models.Room(room1)
        room_list = list(models.Room.objects.all())
        student_list = list(models.Student.objects.all())
        
        person = models.Person.objects.all()
        serializer = PersonSerializer(person,many=True)
        content = JSONRenderer().render(serializer.data)
        
        xs = json.loads(content)
        
        array = []
        for x in xs:
            array.append(x['username'])
            if x['username'] == username and x['password'] == password:
                a = x
                break
            elif(x['username'] == username and x['password']!=password):
                messages.info(request,'Incorrect Password')
                return redirect('maintenanceRequest')
            
        if not (username in array):
            messages.info(request,"Invalid Username")
            return redirect('maintenanceRequest')
        
        student = models.Student()
        room= models.Room()
        for student1 in student_list:
            if(str(student1.user) == username):
                student = student1
                break

        for room1 in room_list:
            if str(room1.roomNo) == roomnumber and str(room1.buildingID) == building:
                room = room1
                break

        if(student is not None and room is not None):
            detailsAdd = "   Username :" + username + " RoomNo : " + str(roomnumber) + " Building ID:" + building
            m = models.Maintenance(studentID = student, first_name = first_name, last_name = last_name, date = date.today(), room = room, details = details + "\n" + detailsAdd, status = 'NOT RESOLVED')
            m.save_base()
            messages.info(request,'Maintenance Request Submitted')
            return redirect('maintenanceRequest')
        else:
            messages.info(request,'Invalid Username')
            return redirect('maintenanceRequest')
    else:
        return render(request,'maintenanceRequest.html')

    
def admin(request,zs):
    return render(request,'adminDashboard.html',{'zs':zs})

    