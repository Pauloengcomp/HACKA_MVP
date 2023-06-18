from django.shortcuts import render, redirect
from .models import Doador

def home(request):
    doador = Doador.objects.all()
    return render(request, "index.html", {"doador": doador} )

def cad_doador(request):
    vnome = request.POST.get("nome")
    Doador.objects.create(nome=vnome)
    doador = Doador.objects.all()
    return render(request, "index.html", {"doador": doador} )

def editar(request, id):
    doador = Doador.objects.get(id=id)
    return render(request, "update.html", {"doador": doador} )

def update(request, id):
    vnome = request.POST.get("nome")
    doador = Doador.objects.get(id=id)
    doador.nome = vnome
    doador.save()
    return redirect(home)

def delete(request, id):
    doador = Doador.objects.get(id=id)
    doador.delete()
    return redirect(home)
