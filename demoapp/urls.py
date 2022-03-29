from django.contrib import admin
from django.urls import path
from demoapp import views


urlpatterns = [
  path('', views.index, name='home'),
  path('submit_data/', views.submitData, name="submit_data"),
]
