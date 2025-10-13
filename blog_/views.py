from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .form import articleForm


# Create your views here.

def article_list(request, *args, **kwargs):
    article = Article.objects.all()
    context = {
      'articles': article
        }
    return render(request, 'articles/detail.html', context)


def createArticle(request):
    form =articleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = articleForm()
    return render(request, 'articles/create.html', {'form':form})