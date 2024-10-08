from django.db import models
from accounts.models import CustomeUser
import datetime
# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length= 255)
    
    def __str__(self):
        return self.name
    

class Trainer(models.Model):
    info=models.ForeignKey(CustomeUser, on_delete= models.CASCADE)
    skills = models.ManyToManyField(Skill)
    description = models.TextField(blank=True)
    instagrm = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher',default='teacher/default-teacher.jpg')
    status = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info.username

class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    image = models.ImageField(upload_to='course/',default='course/default-course.jpg')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    teacher = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    available_seat = models.IntegerField(default=0)
    schedule = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_date']

    def __str__(self) :
        return self.title
    
    def snip(self):
        return self.content[:20] + '...'
    
    def capt(self):
        return self.title.capitalize()
    

class Comment(models.Model):
    which_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user.username
    

class Reply(models.Model):
    which_comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user