from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse,Http404
from .models import Article,Commentaire
from .form import articleForm
from django.contrib.auth.decorators import login_required

 


# Create your views here.

def article_list(request, *args, **kwargs):
    article = Article.objects.all()
    context = {
      'articles': article
        }
    return render(request, 'articles/detail.html', context)

# @login_required
def createArticle(request):
    form =articleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = articleForm()
    return render(request, 'articles/create.html', {'form':form})

# @login_required
def updateArticle(request, my_id):
    messages = ""
    obj = get_object_or_404(Article, id=my_id)
    
    form = articleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages = 'Your modification was successfully done'
    
    return render(request, 'articles/update.html', {'form': form, 'message': messages})

# @login_required
def add_commentaire(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == "POST":
        contenu = request.POST.get('contenu')
        if contenu:
            Commentaire.objects.create(
                article=article,
                auteur=request.user,
                contenu=contenu
            )
        return redirect('detail_article', article_id=article.id)
    
    return render(request, 'ajouter_commentaire.html', {'article': article})

# @login_required
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.user in article.likes.all():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True

    return JsonResponse({'liked': liked, 'total_likes': article.likes.count()})

