from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    actype = models.CharField(max_length=100)
    Reason = models.CharField(max_length=200)
    utype = models.CharField(max_length=100)
    fureason = models.CharField(max_length=100)



class usertweets_Model(models.Model):
    userId = models.ForeignKey(ClientRegister_Model, on_delete=CASCADE)
    uname = models.CharField(max_length=300)
    tcity = models.CharField(max_length=300)
    uses = models.CharField(max_length=100)
    tdesc = models.CharField(max_length=500)
    topics = models.CharField(max_length=300)
    sanalysis = models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    senderstatus = models.CharField(default="process", max_length=300 )
    ratings = models.IntegerField(default=0)
    usefulcounts = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)



class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)


