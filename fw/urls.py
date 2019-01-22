from django.urls import path
from . import views


urlpatterns = [
    path('', views.fw_list, name='fw_list'),
]