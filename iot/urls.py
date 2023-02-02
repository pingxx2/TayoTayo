from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'iot'

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('sec_file/', SecFileListView.as_view(), name='list'),
    path('sec_file/<int:pk>', SecFileDetailView.as_view(), name='detail'),
]

