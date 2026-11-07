from django.shortcuts import render, redirect
from .models import Actualite, Photo, Activite, MessageContact

def accueil(request):
    return render(request, 'village/accueil.html')

def presentation(request):
    return render(request, 'village/presentation.html')

def histoire(request):
    return render(request, 'village/histoire.html')

def localisation(request):
    return render(request, 'village/localisation.html')

def culture(request):
    return render(request, 'village/culture.html')

def activites(request):
    activites = Activite.objects.all()
    return render(request, 'village/activites.html', {'activites': activites})

def galerie(request):
    photos = Photo.objects.all()
    return render(request, 'village/galerie.html', {'photos': photos})

def actualites(request):
    actus = Actualite.objects.all().order_by('-date')
    return render(request, 'village/actualites.html', {'actus': actus})

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        MessageContact.objects.create(nom=nom, email=email, message=message)
        return render(request, 'village/contact.html', {'success': True})
    return render(request, 'village/contact.html')

def galerie(request):
    return render(request, 'village/galerie.html')

def histoire(request):
    return render(request, 'village/histoire.html')

def localisation(request):
    return render(request, 'village/localisation.html')

def culture(request):
    return render(request, 'village/culture.html')

def activites(request):
    return render(request, 'village/activites.html')

def actualites(request):
    return render(request, 'village/actualites.html')

def contact(request):
    if request.method == "POST":
        # Ici tu pourras envoyer l'email plus tard
        nom = request.POST.get('nom')
        message = request.POST.get('message')
        print(f"Message de {nom}: {message}")
    return render(request, 'village/contact.html')