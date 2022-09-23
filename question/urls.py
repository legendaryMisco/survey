from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/second-survey', views.secondQuestion, name='second'),
    path('/third-survey', views.thirdQuestion, name='third'),
    path('/fourth-survey', views.fourthQuestion, name='fourth'),
    path('/fifth-survey', views.fifthQuestion, name='fifth'),
    path('/sixth-survey', views.sixthuestion, name='sixth'),
    path('review/', views.Votes, name='review'),
]