from django.urls import path
from .views import article_list,createArticle,updateArticle, add_commentaire




urlpatterns = [
      path('homepage', article_list, name='homepage'),
      path('create', createArticle, name='create'),
      path('update/<int:article_id>', updateArticle, name='modifier'),
      path('article/<int:article_id>/commentaire/', add_commentaire, name='add_commentaire'),
]
