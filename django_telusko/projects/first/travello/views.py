from django.shortcuts import render
from django.http import HttpResponse 
from .models import Destination
# Create your views here.


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests}) 

def about(request):
    return render(request, 'about.html')

def destination(request):
    return render(request, 'travel_destination.html')

def destination_details(request):
    return render(request, 'destination_details.html')

def elements(request):
    return render(request, 'elements.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def contact(request):
    return render(request, 'contact.html')

def add(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    res = num1 + num2
    return render(request, 'result.html', {'result': res}) 