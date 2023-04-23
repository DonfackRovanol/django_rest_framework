from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
# create la table entreprise
class entreprise(models.Model):
    nom = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, unique=True, null= True)
    addresse = models.CharField(max_length=60, null=False)
    siteweb = models.CharField(max_length=100,null= True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    
    def __str__(self):
        return self.nom


#create la table service
class service(models.Model):
    nom = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.nom
