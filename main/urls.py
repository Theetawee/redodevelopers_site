from django.urls import path
from .views import index,services,policy


urlpatterns=[
    path('',index,name='home'),
    path('services/',services,name='services'),
    path('privacy-policy/',policy,name='policy')
]