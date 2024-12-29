from django.urls import path
from api.views import *


urlpatterns = [
    path('api/data1/', get_data),
    path('api/data2/', get_data),
    path('api/data/', get_data_html),
]
