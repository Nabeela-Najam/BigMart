from django.db import models

# Create your models here.

class category_db(models.Model):
    cname=models.CharField(max_length=100, null=True, blank=True)
    cdescription=models.CharField(max_length=100, null=True, blank=True)
    cimage=models.ImageField(upload_to="Category Images", null=True, blank=True)

class product_db(models.Model):
    pcategory=models.CharField(max_length=100, null=True, blank=True)
    pname=models.CharField(max_length=100, null=True, blank=True)
    pprice=models.IntegerField(null=True, blank=True)
    pdescription=models.CharField(max_length=100, null=True, blank=True)
    pimage=models.ImageField(upload_to="Product Images", null=True, blank=True)