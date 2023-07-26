from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html' )


def services(request):
    return render(request,'main/services.html')

def policy(request):
    return render(request,'main/privacy.html')