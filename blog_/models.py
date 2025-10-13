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
    likes = models.ManyToManyField(User, related_name='articles_likes', blank=True)
    nombre_vues = models.PositiveIntegerField(default=0)
    nombre_likes = models.PositiveIntegerField(default=0)


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=1000)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur.username} sur {self.article.titre}"

    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'
        verbose_name='Commentaire'
        verbose_name_plural='Commentaires'


    def __str__(self):
        return self.titre

