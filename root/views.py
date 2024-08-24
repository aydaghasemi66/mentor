from django.shortcuts import render
from .models import Service
# Create your views here.
def home(request):
    services = Service.objects.all
    context = {
        'services': services
    }
    return render(request, 'root/index.html', context=context)

def about(request):
    return render(request, 'root/about.html') 

def contact(request):
    return render(request, 'root/contact.html')

def pricing(request):
    return render(request, 'root/pricing.html')

def events(request):
    return render(request, 'root/events.html')

