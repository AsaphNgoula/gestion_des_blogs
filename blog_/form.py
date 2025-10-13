from django import forms
from blog_.views import Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'description', 'auteur', 'image', 'likes')
        exclude = ['date_publication', 'date_modification']  # Exclure explicitement