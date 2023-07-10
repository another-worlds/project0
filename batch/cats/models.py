from django.db import models

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=128)

class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    breed= models.ForeignKey(Breed, on_delete=models.CASCADE,null=False)
    weight = models.FloatField()
    
    def __str__(self):
        return f"""
Cat named: {self.nickname}
With Breed: {self.breed.name}
Weighting: {self.weight}
------------------------------"""
    