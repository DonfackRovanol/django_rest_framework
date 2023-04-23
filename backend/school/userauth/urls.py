from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ListCreateList.as_view())
]
