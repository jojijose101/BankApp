from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Districts(models.Model):
    dists = models.CharField(max_length=250)

    def __str__(self):
        return self.dists

class Branches(models.Model):
    dist = models.ForeignKey(Districts,on_delete=models.CASCADE)
    branch = models.CharField(max_length=250)
    link = models.URLField()
    def __str__(self):
        return self.branch


class BankAccount(models.Model):


    name = models.CharField(max_length=100)
    DOB = models.DateField('Date of Birth')
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=500)

    def __str__(self):
        return self.name

