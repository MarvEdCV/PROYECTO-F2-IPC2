from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('adminlogin/',views.login),
    path('adminoperaciones/',views.adminoperaciones),
]