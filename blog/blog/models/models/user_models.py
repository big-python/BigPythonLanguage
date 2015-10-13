from django.db import models

# Create your models here.

class userInfo(models.Model):
    username = models.CharField(max_length=64);
    password = models.CharField(max_length=64);
    sex = models.IntegerField();
    telephone = models.CharField(max_length=32);
    email = models.CharField(max_length=255);
    add_time = models.IntegerField();