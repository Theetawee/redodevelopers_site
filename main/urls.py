from django.urls import path
from .views import index,services


urlpatterns=[
    path('',index,name='home'),
    path('services/',services,name='services')
]