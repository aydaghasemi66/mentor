from django.contrib import admin
from .models import Service, NewsLetter, ContactUs, Events

# Register your models here.


class AdminServices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_filter = ['status']
    search_fields = ['title']


admin.site.register(Service,AdminServices)
admin.site.register(NewsLetter)
admin.site.register(ContactUs)
admin.site.register(Events)