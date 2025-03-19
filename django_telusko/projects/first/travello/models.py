from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics/')
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)
    
 