from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('presentation/', views.presentation, name='presentation'),
    path('histoire/', views.histoire, name='histoire'),
    path('localisation/', views.localisation, name='localisation'),
    path('culture/', views.culture, name='culture'),
    path('activites/', views.activites, name='activites'),
    path('galerie/', views.galerie, name='galerie'),
    path('actualites/', views.actualites, name='actualites'),
    path('contact/', views.contact, name='contact'),
    path('galerie/', views.galerie, name='galerie'),
    path('histoire/', views.histoire, name='histoire'),
    path('localisation/', views.localisation, name='localisation'),
    path('culture/', views.culture, name='culture'),
    path('activites/', views.activites, name='activites'),
    path('actualites/', views.actualites, name='actualites'),
    path('contact/', views.contact, name='contact'),
]

