from django.db import models

# Create your models here.
class Email(models.Model):
    username= models.CharField()
    password=models.CharField()
