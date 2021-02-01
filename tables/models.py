from django.db import models

# Create your models here.


class userTbl(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    pwd = models.CharField(max_length=15)
    uId = models.AutoField(primary_key=True)


class itemTbl(models.Model):
    itemId = models.AutoField(primary_key=True)
    uId = models.ForeignKey(userTbl, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    qty = models.CharField(max_length=10)
    status = models.IntegerField()
    date = models.DateField()