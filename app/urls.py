from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login', views.studentLogin ,name='login'),
    path('index',views.index,name='index'),
    path('maintenanceRequest', views.maintenanceRequest ,name='maintenanceRequest'),
    path('adminDashboard',views.admin,name='admin'),
    path('complainRequest', views.complainRequest,name='complainRequest'),
    path('register', views.register, name='register'),
    # path('student/<str:username>', views.post, name = 'post')
]
