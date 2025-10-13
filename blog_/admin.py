from django.contrib import admin
from .models import Article,Commentaire


# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('titre','description', 'auteur','date_publication','date_modification', 'nombre_vues', 'nombre_likes')


class AdminComentaire(admin.ModelAdmin):
    list_display = ('article', 'auteur', 'date_creation', 'contenu', 'date_creation')
   
admin.site.register(Article, AdminArticle)
