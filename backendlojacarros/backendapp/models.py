from django.db import models


class Carros(models.Model):
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    urlimagem = models.CharField(max_length=255)
    def __str__(self):
        return self.modelo
    
