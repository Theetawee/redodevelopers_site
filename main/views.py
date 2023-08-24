from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from pathlib import Path
from django.core.mail import send_mail
from django.contrib import messages
from .models import Newsletter

def index(request):
    
    return render(request, 'main/index.html')

def company(request):
    return render(request,'main/about.html')

def solutions(request):
    return render(request,'main/solutions.html')

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
            return redirect('contact')
        except:
            messages.error(request,'We ran into an issue please try again')
            return redirect('contact')   
        
    return render(request,'main/contact.html')


def custom_404_view(request,exception):
    return render(request, 'main/error.html', status=404)

def custom_500_view(request):
    return render(request, 'main/505.html', status=500)

def newsletter(request):
    referring_url = request.META.get('HTTP_REFERER')
    if request.POST:
        email=request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request,f'{email} is already subscribed to our newsletter!')
            return redirect(referring_url)
        new=Newsletter.objects.create(email=email)
        new.save()
        send_mail(
                'Newsletter',
                f'New newsletter subscription from {email}',
                'redodevs@gmail.com',
                ['redodevs@gmail.com'],
                fail_silently=True
            )
        messages.success(request, f'Added {email}')
        return redirect(referring_url)
    return redirect('home')


def facebook(request):
    return redirect('https://www.facebook.com/profile.php?id=61550525012526')

def twitter(request):
    return redirect('https://twitter.com/redodevs')

def linkedin(request):
    return redirect('https://www.linkedin.com/company/redo-io')



def iot(request):
    return render(request,'main/iot.html' )