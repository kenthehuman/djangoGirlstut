from django.urls import path
from . import models

urlpatterns =[
    path('', include('blog.urls')),
]