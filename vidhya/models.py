from django.db import models

# Create your models here.
class Vidhya(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.CharField(max_length=50)
    blog= models.SlugField(max_length=50)
