from django.db import models

class tenis (models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True, default='cars/default.jpg')

    def __str__(self):
        return f"{self.name}"
    
