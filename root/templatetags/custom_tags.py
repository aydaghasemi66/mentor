from django import template
from course.models import Course, Trainer, Category
from root.models import Service
from accounts.models import CustomeUser


register = template.Library()

@register.filter
def truncate(content: str, number: int):
    if not isinstance(content, str):
        return content  
    if not isinstance(number, int):
        return content  
    return content[:number]

@register.filter
def truncate2(content: str, number: int):
    if not isinstance(content, str):
        return content  
    if not isinstance(number, int):
        return content  
    lst = content.split()[:number]
    return " ".join(lst)
@register.simple_tag
def last_three_course(number:int):
    last_three = Course.objects.filter(status=True)[:number]
    return last_three


@register.simple_tag
def last_three_trainer():
    last_triner = Trainer.objects.filter(status=True)[:3]
    return last_triner


@register.simple_tag
def category():
    category = Category.objects.all()
    return category

@register.simple_tag
def service():
    service = Service.objects.filter(status=True)
    return service
