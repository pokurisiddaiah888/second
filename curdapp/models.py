from django.db import models

class empdata(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    htown=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    percentage=models.BigIntegerField()
    passoutyear=models.BigIntegerField()
