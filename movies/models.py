from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre= models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    image=models.CharField()
    director=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
