from django.db import models

# Create your models here.

class emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    adress=models.CharField(max_length=200, default='')
    working = models.BooleanField(default=True)
    depertment=models.CharField(max_length=10 , default='CSE')
    

