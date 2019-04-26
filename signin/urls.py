from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.news, name='news'),
    path('', views.about, name='about')
]
