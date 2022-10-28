from django.urls import path 
from . import views

urlpatterns = [
    path('', views.nums, name='nums'),
]
