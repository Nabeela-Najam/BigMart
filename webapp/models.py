from django.db import models

# Create your models here.

class contact_db(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class register_db(models.Model):
    rname=models.CharField(max_length=100,null=True,blank=True)
    remail=models.EmailField(max_length=100,null=True,blank=True)
    rpassword=models.CharField(max_length=100,null=True,blank=True)
    cpassword=models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Username=models.CharField(max_length=100, null=True, blank=True)
    Productname=models.CharField(max_length=100, null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    Totalprice=models.IntegerField(null=True, blank=True)