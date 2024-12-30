from django.urls import path, include 
from django.contrib import admin
from api import views

urlpatterns = [
    path('relays/control_relay/', views.control_relay, name='control_relay'),
    path('relays/', views.get_relay_status, name='get_relay_status'),
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]
