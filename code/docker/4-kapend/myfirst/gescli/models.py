from django.db import models

class Clients(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    sexe = models.CharField(max_length=2)
