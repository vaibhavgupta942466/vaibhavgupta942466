from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.TextField(max_length=20)
    Last_Name = models.TextField(max_length=20)
    Email = models.EmailField(max_length=264, unique=True)


    
