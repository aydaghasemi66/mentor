from django.urls import path
from .views import home, about,contact, pricing, events
app_name = 'root'


urlpatterns = [
    path("",home,name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("pricing/", pricing, name="pricing"),
    path("events/", events, name="events"),

]