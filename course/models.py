# from django.db import models

# # Create your models here.
# class Skill(models.Model):
#     name = models.CharField(max_length= 255)
    
#     def __str__(self) -> str:
#         return self.name
    

# class Trainer(models.Model):
#     info=models.ForeignKey(User)
#     skills = models.ForeignKey(Skill)
#     instagrm = models.CharField(max_length=255)
#     linkedin = models.CharField(max_length=255)
#     facebook = models.CharField(max_length=255)
#     twitter = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='teacher_images/')
#     status = models.BooleanField(default=True)

