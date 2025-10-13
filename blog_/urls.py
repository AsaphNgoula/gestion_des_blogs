from django.urls import path
from .views import article_list,createArticle




urlpatterns = [
      path('detail', article_list,name='detail'),
      path('create', createArticle, name='create'),
]

