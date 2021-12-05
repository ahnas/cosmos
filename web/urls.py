from django.urls import path
from . import views

app_name = 'web' 

urlpatterns = [
    path('', views.index,name="index"),
    path('service', views.service,name="service"),
    path('cycleservice', views.cycleservice,name="cycleservice"),
    path('shuttleservice', views.shuttleservice,name="shuttleservice"),
    path('fitnessServiceOnsite', views.fitnessServiceOnsite,name="fitnessServiceOnsite"),
    path('fitnessServiceBranch', views.fitnessServiceBranch,name="fitnessServiceBranch"),
    
]