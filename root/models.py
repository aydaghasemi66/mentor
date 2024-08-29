from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

class NewsLetter (models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name
class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    context = models.TextField()
    image= models.ImageField(upload_to='events/',default='events/default-event.jpg')

    def __str__(self):
        return self.title

class Feature(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    duration_months = models.PositiveIntegerField()  
    features = models.ManyToManyField(Feature, blank=True)  

    def __str__(self):
        return self.title
