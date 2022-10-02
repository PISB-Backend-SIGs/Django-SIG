from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home, name='new_home'),
    path('register/', views.register, name='new_register')
]
