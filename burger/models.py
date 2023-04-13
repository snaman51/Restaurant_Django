from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    Offer_per = models.IntegerField()
    offer_price = models.DecimalField(default=0.0,max_digits=4,decimal_places=2)
