from django.urls import path,re_path
from .views import index,policy,RobotsTxtView,contact,company,newsletter,twitter,facebook,linkedin,iot,get_meeting,contact_sales,the_ceo,carrer


urlpatterns=[
    path('',index,name='home'),
    path('legal/privacy-policy/',policy,name='policy'),
    re_path(r'^robots\.txt$', RobotsTxtView.as_view(), name='robots'),
    path('contact/',contact,name='contact'),
    path('company/',company,name='about'),
    path('newsletter/',newsletter,name='news'),
    path('twitter/',twitter,name='twitter'),
    path('facebook/',facebook,name='facebook'),
    path('linkedIn/',linkedin,name='linkedin'),
    path('iot-solutions/',iot,name='iot'),
    path('request/meeting/',get_meeting,name='meeting'),
    path('support/sales/',contact_sales,name='sales'),
    path('board/chairman/',the_ceo,name='ceo'),
    path('carrers/',carrer,name='carrer')
]