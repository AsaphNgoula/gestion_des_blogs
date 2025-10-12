from django.urls import path
from blog_.views import home


urlpatterns = [
        path('home',home,name='home'),

]

