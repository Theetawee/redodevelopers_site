from django.urls import path,re_path
from .views import index,services,policy,sitemap,robots,contact,company,solutions,newsletter,twitter,facebook,linkedin,iot,get_meeting,contact_sales


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
    path('support/sales/',contact_sales,name='sales')
]