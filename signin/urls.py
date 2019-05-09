from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.hacking, name='hacking'),
    path('', views.games, name='games'),
    path('', views.about, name='about')
]
