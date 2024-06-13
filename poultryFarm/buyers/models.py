from django.db import models

# Create your models here.
class buyerdb(models.Model):
    buyerUsername= models.CharField(max_length=100)
    buyerPhonenum= models.CharField(max_length=15)
    buyerPassword= models.CharField(max_length=255)
    buyerAddress=models.CharField(max_length=100)
    
    class meta:
        db_table ="buyerdb"

