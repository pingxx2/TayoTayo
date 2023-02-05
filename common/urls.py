from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    path('mypage/', views.mypage, name='mypage'),
    path('mypage/<int:parking_number>/', views.mypage_detail, name="mypage_detail"),
    path('mypage/<int:parking_number>/modify/', views.parking_modify, name='parking_modify'),
    
    path('add/', views.add, name='add'),
    path('add/parking', views.parking_add, name='parking_add'),

    path('myreserve/', views.myreserve , name="myreserve"),
    path('myreserve/delete/<int:res_id>', views.myreserve_delete, name='myreserve_delete'),
]

