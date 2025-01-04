from django.urls import path
from .views import RelayStatusView, login_view

urlpatterns = [
    path('api/relay/', RelayStatusView.as_view(), name='relay_status'),
    path('api/login/', login_view, name='login'),
]