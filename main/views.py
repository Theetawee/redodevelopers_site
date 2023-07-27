from django.http import HttpResponse
from django.shortcuts import render
import os
from pathlib import Path


# Create your views here.
def index(request):
    return render(request,'main/index.html' )


def services(request):
    return render(request,'main/services.html')

def policy(request):
    return render(request,'main/privacy.html')


def robots(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path=os.path.join(BASE_DIR,'templates','main','robots.txt')
    response=HttpResponse(open(path).read(),content_type='application/text')
    return response

def sitemap(request):
    return render(request,'main/sitemap.xml')

def contact(request):
    return render(request,'main/contact.html')
