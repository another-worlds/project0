from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=28)
    score = models.IntegerField(default=0)

class Cat(models.Model):
    name = models.CharField(max_length=48)
    score = models.IntegerField(default=0)
    owns = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField('cat_picture')
    
class Dog(models.Model):
    name = models.CharField(max_length=48)
    score = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField('dog picture')
