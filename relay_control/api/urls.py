from django.urls import path
from .views import control_relay, get_relay_status, relay_control_page

urlpatterns = [
    path('control_relay/', control_relay, name='control_relay'),
    path('get_relay_status/', get_relay_status, name='get_relay_status'),
    path('', relay_control_page, name='relay_control_page'),
]