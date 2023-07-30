from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from pathlib import Path
from django.core.mail import send_mail
from django.contrib import messages
from .models import Newsletter
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from datetime import datetime


def index(request):
    if request.POST:
        email = request.POST.get('email')
        try:
            new_user = Newsletter.objects.create(email=email)
            new_user.save()
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            return redirect('home')
        except IntegrityError:
            messages.error(request, 'This email is already subscribed to our newsletter.')
            return redirect('home')
        except ValidationError:
            messages.error(request, 'Invalid email format. Please enter a valid email address.')
            return redirect('home')
    return render(request, 'main/index.html')



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
        subject=request.POST['subject']
        user_message=request.POST['message']
        message=f'Email from: {email}\n Message: {user_message}'
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


def about(request):
    return render(request,'main/about.html' )


def community(request):
    date=datetime.now().date()
    return render(request,'main/community.html',{'date':date})