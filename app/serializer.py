from rest_framework import serializers
from . import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = '__all__'
        

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technician
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room_Booking
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maintenance
        fields = '__all__'

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complain
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class Fulfills_Maintenance(serializers.ModelSerializer):
    class Meta:
        model = models.Fulfills_Maintenance
        fields = '__all__'
        
class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mail
        fields = '__all__'
