from django.db import models
class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/')    

    def __str__(self):
        return self.name
# Create your models here.
