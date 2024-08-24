from django.contrib import admin
from .models import *


admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Trainer)
admin.site.register(Comment)
admin.site.register(Reply)