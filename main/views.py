from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import View
from .models import Newsletter
from django.template import loader

def index(request):
    title="Redo Developers: Innovative Tech & Software Solutions"
    description="Redo Developers Inc. - A leading technology and software company specializing in innovative solutions for businesses."
    context={
        'title':title,
        'description':description,
    }
    return render(request, 'main/index.html',context)



def company(request):
    title="About Redo Developers Inc: Innovating Software & Technology Solutions"
    description="Discover the story behind Redo Developers Inc, a leading software and technology company. Learn about our mission, values, and team."
    context={
        'title':title,
        'description':description
    }
    
    return render(request,'main/about.html',context)


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


class RobotsTxtView(View):
    def get(self, request):
        # Assuming you have placed the robots.txt file in your templates/base/ directory
        template = loader.get_template("main/robots.txt")
        content = template.render()
        return HttpResponse(content, content_type="text/plain; charset=utf-8")


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




def get_meeting(request):
    title="Redo Developers Inc: Request Meeting "
    description="Discover Redo Developers Inc. for software and technology solutions. Schedule a meeting today!"
    context={
        'title':title,
        'description':description,
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
    title="Meet Khaotungkulmethee Pattawee, Current chairman of Redo Developers Inc."
    description="Meet Khaotungkulmethee Pattawee, the Chairman of Redo Developers Inc., a leading software and technology company. Discover his background, vision and prospects."
    context={
        'title':title,
        'description':description,
    }
    
    return render(request,'main/ceo.html',context )



def contact_sales(request):
    title="Revamp Your Tech with Redo Developers Inc: Sales Page"
    description="Discover the cutting-edge solutions offered by Redo Developers Inc, a leading software and technology company. Boost your business with our innovative products."
    context={
        'title':title,
        'description':description,
    }
    
    return render(request,'main/sales.html',context )


def carrer(request):
    title="Redo Developers Inc: Careers in Software & Technology"
    description="Discover exciting career opportunities at Redo Developers Inc, a leading software and technology company. Join us today!"
    context={
        'title':title,
        'description':description,
        }
    
    return render(request,'main/carrer.html',context )


def investors(request):
    return render(request,'main/investors.html' )