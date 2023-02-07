from django.urls import path
from .views import *
from django.views.generic import TemplateView
from . import views

app_name = 'tayo'

urlpatterns = [
    path('main/', views.main, name='main'),

    path('reserve/', views.reserve, name='reserve'),
    path('reserve/add', views.reserve_add, name='reserve_add'),

    path('info/', views.info, name='info'),
    path('parking/', views.parking, name='parking'),
]

