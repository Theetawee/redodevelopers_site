from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from pathlib import Path
from django.core.mail import send_mail
from django.contrib import messages
from .models import Newsletter


def index(request):
    title="Redo Developers Inc. | Innovating Solutions for a Connected World"
    description="Redo Developers Inc. is software and Technology Company commited to providing the best software services in Uganda, Africa and World at large."
    og_title="Innovative Software and Technology solutions for Individuals and Bussinesses"
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type,
    }
    return render(request, 'main/index.html',context)

def company(request):
    title="About Redo Developers Inc. | Leading Software Company in Uganda and Beyond"
    description="Discover Our Journey, Mission, and Commitment to Innovation"
    og_title="About Redo Developers Inc."
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="article"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/about.html',context)

def solutions(request):
    title = "Software Products | Redo Developers Inc."
    description = "Explore the best tailored Software products for Your Business Needs. These include Hospital Management System (HMS) and others"
    og_title = "Leading Software Products by Redo Developers Inc."
    image_url = "https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type = "website"
    context = {
        'title': title,
        'description': description,
        'og_title': og_title,
        'image': image_url,
        'og_type': og_type
    }
    
    return render(request, 'main/solutions.html', context)


def policy(request):
    title="Our Privacy Policy. | Redo Developers Inc."
    description="Curious on how Redo Developers Inc. handles your data? Explore how we handle and protect your data and information to make sure its safe 24/7."
    og_title="Privacy Policy."
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/privacy.html',context)


def robots(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path=os.path.join(BASE_DIR,'templates','main','robots.txt')
    response=HttpResponse(open(path).read(),content_type='application/text')
    return response

def sitemap(request):
    return render(request,'main/sitemap.xml')

def contact(request):
    title="Contact Redo Developers Inc. - Get in Touch with Us"
    description="Contact Redo Developers Inc. for any inquiries or assistance. We're here to help."
    og_title="Get in Touch with Redo Developers Inc."
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
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
        
    return render(request,'main/contact.html',context)


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
    title="Venture Into Internet of Things (IoT) | Redo Developers Inc. - Innovating the Future"
    description="Discover how Redo Developers Inc. pioneers the Internet of Things (IoT) revolution. Explore our innovative IoT solutions and how they are reshaping industries and businesses for a smarter and connected future."
    og_title="IoT | Redo Developers Inc."
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="article"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/iot.html',context )

def get_meeting(request):
    title="Request a Meeting"
    description="Request a meeting with us to discuss your needs with Redo Developers Inc."
    og_title="Request a Meeting"
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
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
        
    return render(request,'main/meeting.html',context )





def the_ceo(request):
    title="Khaotungkulmethee Pattawee - Co-Founder and Chairman | Redo Developers Inc."
    description="Learn about Khaotungkulmethee Pattawee, the Co-Founder and Chairman of Redo Developers Inc. Explore his background, vision, and contributions to the world of technology and software solutions."
    image_url="https://theetawee.github.io/company_staticfiles/images/thoe.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/ceo.html',context )



def contact_sales(request):
    title="Contact Sales | Redo Developers Inc."
    description="Call us, chat with us, or book a meeting with our sales team to learn how you can use Redo Developers Inc. to grow better."
    og_title="Contact Sales"
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/sales.html',context )


def carrer(request):
    title="Carrers | Redo Developers Inc."
    description="Exciting opportunities await you at Redo Developers Inc. Check back for our latest job postings and be a part of our innovative journey."
    og_title="Carrers"
    image_url="https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type="website"
    context={
        'title':title,
        'description':description,
        'og_title':og_title,
        'image':image_url,
        'og_type':og_type
    }
    
    return render(request,'main/carrer.html',context )
