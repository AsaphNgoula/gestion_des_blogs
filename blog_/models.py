from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    nombre_vues = models.PositiveIntegerField(default=0)
    nombre_likes = models.PositiveIntegerField(default=0)
    commentaire = models.TextField(max_length=1000, blank=True,default=True)

    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'


    def __str__(self):
        return self.titre

