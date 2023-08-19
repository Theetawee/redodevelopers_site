from django.shortcuts import render

# Create your views here.

def bloglist(request):
    return render(request,'blog/list.html')