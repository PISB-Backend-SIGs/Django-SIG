from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('Task1',views.Task1 ,name='Task1' ),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]
