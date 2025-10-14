from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse,Http404
from .models import Article,Commentaire
from .form import articleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Create your views here.

def article_list(request, *args, **kwargs):
    article = Article.objects.all()
    context = {
      'articles': article
        }
    return render(request, 'articles/homepage.html', context)


# @login_required
def createArticle(request):
    if request.method == 'POST':
        form = articleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user  # Associer l'auteur
            article.save()
            return redirect('homepage')
    else:
        form = articleForm()
    return render(request, 'articles/create.html', {'form': form})

# @login_required
def updateArticle(request, article_id):
    messages = ""
    obj = get_object_or_404(Article, id=article_id)
    
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
        return redirect('homepage')
    
    return render(request, 'ajouter_commentaire.html', {'article': article})

# @login_required
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    # redirige simplement vers la page d’où vient la requête
    return redirect(request.META.get('HTTP_REFERER', 'homepage'))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'articles/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'      # nom du template que tu veux utiliser
    redirect_authenticated_user = True  # si un utilisateur déjà connecté visite /login/, on le redirige

@login_required
def deconnected(request):
    logout(request)
    return redirect('login')
    



