from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from pathlib import Path
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime


def index(request):
    
    return render(request, 'main/index.html')

def proposal(request):
    return redirect('https://docs.google.com/document/d/e/2PACX-1vSX_hPfOJ1zkVIqCf9PyuxpfChEPok4kjI21GgrDMF0ITs1NeEOLY4KujpAcDyCwat-a_Y0TR1-3nqA/pub#h.3at9u9s4e0vp')


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
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        subject=request.POST['subject']
        user_message=request.POST['message']
        message=f'Email from: {email}\nName:{name}\n Message: {user_message}'
        try:
            send_mail(
                subject,
                message,
                'redodevs@gmail.com',
                ['redodevs@gmail.com'],
                fail_silently=True
            )
            messages.success(request,'Your message was successfully received.')
            return redirect('home')
        except:
            messages.error(request,'We ran into an issue please try again')
            return redirect('contact')   
        
    return render(request,'main/contact.html')


def custom_404_view(request,exception):
    return render(request, 'main/error.html', status=404)

def custom_500_view(request):
    return render(request, 'main/505.html', status=500)
