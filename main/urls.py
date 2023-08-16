from django.urls import path,re_path
from .views import index,services,policy,sitemap,robots,contact,company,solutions


urlpatterns=[
    path('',index,name='home'),
    path('services/',services,name='services'),
    path('privacy-policy/',policy,name='policy'),
    path('sitemap/',sitemap,name='sitemap'),
    re_path(r'^robots\.txt$', robots, name='robots'),
    path('contact/',contact,name='contact'),
    path('company/',company,name='about'),
    path('solutions/',solutions,name='solutions')
]