from django.db import models

# Create your models here.
class MyModel(models.Model):
    text = models.TextField()
    score = models.IntegerField(default=0)
    
class MySubmodel(models.Model):
    text = models.TextField()
    score = models.IntegerField(default=0)
    model = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    