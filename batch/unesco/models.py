from django.db import models

# Create your models here.
class Iso(models.Model):
    name = models.CharField(max_length=4)
    
class Region(models.Model):
    name = models.CharField(max_length=16)
    
class State(models.Model):
    name = models.CharField(max_length=16)
    
class Category(models.Model):
    name = models.CharField(max_length=16)
    
class Site(models.Model):
    name = models.TextField()
    description = models.TextField()
    justification = models.TextField()
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    