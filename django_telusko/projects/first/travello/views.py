from django.shortcuts import render
from django.http import HttpResponse 
from .models import Destination
# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.description = "The city that never sleeps"
    dest1.image = "mumbai.png"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Margao"
    dest2.description = "The city that's always half-asleep."
    dest2.image = "margao.png"
    dest2.price = 500

    dest3 = Destination()
    dest3.name = "Panaji"
    dest3.description = "capital of Goa."
    dest3.image = "panaji.png"
    dest3.price = 600

    dests = [dest1, dest2, dest3]
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