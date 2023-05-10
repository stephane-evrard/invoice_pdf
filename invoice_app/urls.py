
from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', home,  name="home"),
    path('pdf/', pdf,  name="pdf"),
]