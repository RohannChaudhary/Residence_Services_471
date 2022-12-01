from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.Staff)
admin.site.register(models.Building)
admin.site.register(models.Food_Plan)
admin.site.register(models.Room)
admin.site.register(models.Admin)
admin.site.register(models.Technician)
admin.site.register(models.Student)
admin.site.register(models.Room_Booking)
admin.site.register(models.Payment)
admin.site.register(models.Maintenance)
admin.site.register(models.Fulfills_Maintenance)
admin.site.register(models.Complain)