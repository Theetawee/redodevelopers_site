from django.urls import path,re_path
from .views import index,services,policy,sitemap,robots,contact,company,solutions,newsletter,twitter,facebook,linkedin,iot,get_meeting,hepb,reg_done,download_apk,space_app,space_website


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
    path('iot-solutions/',iot,name='iot'),
    path('request/meeting/',get_meeting,name='meeting'),
    path('iihas-HepB-Campaign/',hepb,name='hep'),
    path('done/',reg_done,name='done'),
    path('apps/space/',space_app,name='space'),
    path('space-website/',space_website,name='space-website'),
    path('downloads/space/',download_apk,name='space-apk')
]