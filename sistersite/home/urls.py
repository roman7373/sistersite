from django.urls import path

from . import views


app_name = 'about'

urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('', views.AboutAuthorView.as_view(), name='author'),
    path('profess/', views.AboutProfessView.as_view(), name='profess'),
    path('team/', views.AboutTeamView.as_view(), name='team'),
    path('teaching/', views.AboutTeachingView.as_view(), name='teaching'),
]
