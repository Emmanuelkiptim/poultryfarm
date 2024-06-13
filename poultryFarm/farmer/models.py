from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class farmer_detail(models.Model):
    dbfarmerUsername= models.CharField(max_length=100)
    dbfarmerPhonenum= models.CharField(max_length=15)
    dbfarmerPassword= models.CharField(max_length=255)
    dbfarmerEmail=models.CharField(max_length=100)
    dbfarmerAddress=models.CharField(max_length=100)

    class meta:
        db_table ="farmer"
        
