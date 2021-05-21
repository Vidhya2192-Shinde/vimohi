from django.db import models

# Create your models here.
class Mohini(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.CharField(max_length=50)
    #active=models.CharField(default='Y')