from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=50)
    decription =models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    date_modification =models.DateTimeField(auto_now=True)
    auteur =models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    nombre_vues = models.PositiveIntegerField(default=0)
    nombre_likes = models.PositiveIntegerField(default=0)

    verbose_Name='Article'
    verbose_Name_plural='Articles'


    def __str__(self):
        return self.titre

