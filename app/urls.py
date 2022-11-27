from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login', views.studentLogin ,name='login'),
    path('index',views.index,name='index'),
    path('maintenanceRequest', views.maintenanceRequest ,name='maintenanceRequest')
    # path('student/<str:username>', views.post, name = 'post')
]
