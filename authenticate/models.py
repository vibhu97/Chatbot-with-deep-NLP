from django.db import models

# Create your models here.

class ShareAPI(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    share_date = models.DateTimeField(auto_now_add=True)
