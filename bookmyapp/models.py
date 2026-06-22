from django.db import models
class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    
class Movie(models.Model):
    user = models.ForeignKey(
        UserRegister,
        on_delete=models.CASCADE,
        related_name='movie'
    )    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/')    
    genre = models.CharField(max_length=50,null=True, blank=True)

    duration = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    video = models.FileField(
        upload_to='movie_videos/',
        null=True,
        blank=True
    )

   
# Create your models here.
