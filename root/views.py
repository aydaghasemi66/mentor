from django.shortcuts import render
from .models import Service, Events
from course.models import Category, Course, Trainer
from accounts.models import CustomeUser


def home(request):
    ev_count = Events.objects.count()
    service_count = Service.objects.filter(status=True).count()
    course_count = Course.objects.filter(status=True).count()
    teacher_count = Trainer.objects.filter(status=True).count()
    student_count = CustomeUser.objects.filter(is_active=True).count()

    services = Service.objects.all()
    category = Category.objects.all()

    context = {
        'category': category,
        'services': services,
        'service_count': service_count,
        'ev_count': ev_count,
        'teacher_count': teacher_count,
        'student_count': student_count,
        'course_count': course_count,
    }

    return render(request, 'root/index.html', context=context)


def about(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'root/about.html',context=context) 

def contact(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'root/contact.html',context=context)

def pricing(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'root/pricing.html',context=context)

def events(request):
    category = Category.objects.all()
    events=Events.objects.all()
    context = {
        'category': category,
        'events': events,
    }
    return render(request, 'root/events.html',context=context)

