from django.urls import path,re_path
from .views import index,services,policy,sitemap,robots,contact,company,solutions,newsletter,twitter,facebook,linkedin,webdevelopment,custom_software,iot


urlpatterns=[
    path('',index,name='home'),
    path('services/',services,name='services'),
    path('privacy-policy/',policy,name='policy'),
    path('sitemap/',sitemap,name='sitemap'),
    re_path(r'^robots\.txt$', robots, name='robots'),
    path('contact/',contact,name='contact'),
    path('company/',company,name='about'),
    path('solutions/',solutions,name='solutions'),
    path('newsletter/',newsletter,name='news'),
    path('twitter/',twitter,name='twitter'),
    path('facebook/',facebook,name='facebook'),
    path('linkedIn/',linkedin,name='linkedin'),
    path('web-services/',webdevelopment,name='web'),
    path('custom-software/',custom_software,name='custom'),
    path('iot-solutions/',iot,name='iot')
]