from django.urls import path
from .views import article_list,createArticle,updateArticle, add_commentaire,like_article,register,CustomLoginView, deconnected
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
      path('', article_list, name='homepage'),
      path('articles/', article_list, name='article'),

      path('create', createArticle, name='create'),
      path('update/<int:article_id>', updateArticle, name='modifier'),
      path('like/<int:article_id>/', like_article, name='like_article'),
      path('commentaire/<int:article_id>/', add_commentaire, name='add_commentaire'),
      path('register/', register, name='register'),
      path('login/', CustomLoginView.as_view(), name='login'),

      ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)


