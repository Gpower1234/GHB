from django.db import models

# Create your models here.
        
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return(self.name) 

class HairType(models.Model):
    category = models.ManyToManyField(Category)
    subCategory = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.subCategory}: ${self.price}'