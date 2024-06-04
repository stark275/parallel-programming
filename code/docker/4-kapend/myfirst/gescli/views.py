from django.shortcuts import render, redirect
from .models import Clients
from django.http import HttpRequest
def index(request):
    #return HttpRequest("hello kerto")
    #objet client
    client = Clients.objects.all()
    return render(request,'index.html',{'client':client})

def ajout(request):
    return render(request,'ajout.html')

def ajoutvalider(request):
    nom = request.POST['nom']
    pre = request.POST['pre']
    age = request.POST['age']
    sexe = request.POST['sexe']

    client = Clients(nom=nom,prenom=pre,age=age,sexe=sexe)
    client.save()
    return redirect("/")

def supprimer(request, id):
    client = Clients.objects.get(id=id)
    client.delete()
    return redirect("/")

def modifier(request,id):
    client = Clients.objects.get(id=id)
    return render(request,'modifier.html',{'client':client})

def modifiervalider(request,id):
    nom = request.POST['nom']
    pre = request.POST['pre']
    age = request.POST['age']
    sexe = request.POST['sexe']
    client = Clients.objects.get(id=id)
    client.nom = nom
    client.prenom=pre
    client.age=age
    client.sexe=sexe
    client.save()
    return redirect("/")
    