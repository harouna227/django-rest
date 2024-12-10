from django.db import models

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=225)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
