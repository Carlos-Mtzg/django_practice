from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse

from .forms import categoriaForm


def lista_categorias(request):
    categorias = Categoria.objects.all()

    data = [{"nombre": p.nombre, "imagen": p.imagen} for p in categorias]

    return JsonResponse(data, safe=False)


def ver_categorias(request):
    return render(request, "ver_categorias.html")


def agregar_categoria(request):

    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("ver")
    else:
        form = categoriaForm()
    return render(request, "agregar_categoria.html", {"form": form})
