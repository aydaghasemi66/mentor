from django.shortcuts import render
from .models import Service, Events
from course.models import Category
# Create your views here.
def home(request):
    service_count=Service.objects.filter(status=True).count()
    services = Service.objects.all
    category = Category.objects.all
    
    context = {
        'category': category,
        'services': services,
        'service_count': service_count,

    }
    return render(request, 'root/index.html', context=context)

def about(request):
    category = Category.objects.all
    context = {
        'category': category,
    }
    return render(request, 'root/about.html',context=context) 

def contact(request):
    category = Category.objects.all
    context = {
        'category': category,
    }
    return render(request, 'root/contact.html',context=context)

def pricing(request):
    category = Category.objects.all
    context = {
        'category': category,
    }
    return render(request, 'root/pricing.html',context=context)

def events(request):
    category = Category.objects.all
    events=Events.objects.all
    context = {
        'category': category,
        'events': events,
    }
    return render(request, 'root/events.html',context=context)

