from .views import *
from django.urls import include, path

urlpatterns = [
    path('',home,name='home'),
]