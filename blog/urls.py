from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog-home'),
    path('nos', views.nos, name ='nos')
]