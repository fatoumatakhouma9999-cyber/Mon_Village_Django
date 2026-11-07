from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.titre

class Photo(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.titre

class Activite(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self): return self.nom

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.nom} - {self.email}"
