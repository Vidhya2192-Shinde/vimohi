from django.db import models

# Create your models here.
class Email(models.Model):

    username= models.CharField()
    OTP=models.IntegerField
    email=models.CharField()
    img=models.IntegerField()


