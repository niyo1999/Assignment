from django.urls import path
from .views import participant_registration, success, vehicle_list

urlpatterns = [
    path('', participant_registration, name='registration'),
    path('success/', success, name='success'),
    path('vehicles_form/', vehicle_list, name='vehicles_form'),

    
]
