from django.db import models

# Create your models here.
class Email(models.Model):
    sign_in=models.CharField()
    username= models.CharField()
    #OTP=models.IntegerField
    #email=models.CharField()
    #img=models.IntegerField()


