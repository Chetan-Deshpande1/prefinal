from django.db import models
from django.contrib.auth.models import User

class Extract(models.Model):
    serial_no = models.SlugField(max_length=30)
    image     = models.CharField(max_length= 40)
    name1     = models.CharField(max_length=60)
    email     = models.EmailField(max_length=80)
    address =   models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



  
