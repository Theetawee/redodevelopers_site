from django.http import HttpResponse,FileResponse
from django.shortcuts import redirect, render
import os
from pathlib import Path
from django.core.mail import send_mail
from django.contrib import messages
from .models import Newsletter
from .forms import HepBForm
from django.conf import settings


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

def get_meeting(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        role=request.POST['role']
        phone=request.POST['phone']
        company=request.POST['company']
        needs=request.POST['needs']
        if Newsletter.objects.filter(email=email).exists():
            pass
        else:
            new=Newsletter.objects.create(email=email)
            new.save()
        send_mail(
                'Meeting Request',
                f'New meeting request:\nName: {name}\nEmail: {email}\nRole: {role}\nPhone: {phone}\nCompany: {company}\nNeeds: {needs}',
                'redodevs@gmail.com',
                ['redodevs@gmail.com'],
                fail_silently=True
            )
        messages.success(request, f'Thank you for contacting us. We have sent you an email containing more information about your demo')
        return redirect('meeting')
        
    return render(request,'main/meeting.html' )





def hepb(request):
    if request.method == 'POST':
        form = HepBForm(request.POST)
        if form.is_valid():
            reg=form.save()
            subject = 'Registration Confirmation'
            message = f'Name: {reg.name} \nPhone: {reg.phone}\nGender: {reg.gender}\nSchool: {reg.school}\nState: {reg.state}'
            from_email = 'redodevs@gmail.com'
            recipient_list = ['redodevs@gmail.com']
            send_mail(subject, message, from_email, recipient_list,fail_silently=True)            
            return redirect('done')
    else:
        form = HepBForm()

    context = {
        'form': form
    }

    return render(request, 'main/hep.html', context)

def reg_done(request):
    return render(request,'main/done.html' )




from django.http import StreamingHttpResponse

def download_apk(request):
    # Define the path to your APK file
    BASE_DIR = Path(__file__).resolve().parent.parent
    apk_file_path = os.path.join(BASE_DIR, 'templates', 'main', 'Space.apk')

    # Check if the file exists
    if os.path.exists(apk_file_path):
        # Function to stream the file in chunks
        def file_iterator(file_path, chunk_size=8192):
            with open(file_path, 'rb') as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk

        # Set the content type as 'application/vnd.android.package-archive'
        response = StreamingHttpResponse(
            file_iterator(apk_file_path),
            content_type='application/vnd.android.package-archive'
        )
        # Set the content disposition to force download
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(apk_file_path)}"'
        return response
    else:
        # Handle the case where the file doesn't exist
        return HttpResponse('APK file not found', status=404)
