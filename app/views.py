from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
from django.http import JsonResponse
from .models import Usuarios, ErrorLog


# Create your views here.
def index(request):
    return render(request, "index.html", status=200)


def error_404_view(request, exception):
    return render(request, "404.html", status=404)


def error_500_view(request, exception):
    return render(request, "500.html", status=500)


def generar_error(request):
    return 7 / 0


def one_page(request):
    return render(request, "onepage.html", status=200)


def prueba_front(request):
    text = request.GET.get("texto", "")

    # Vamos a generar informacion en python
    objecto1 = {
        "id": "001",
        "titulo": text,
        "descripcion": "texto generico 1",
    }

    objeto2 = {
        "id": "002",
        "titulo": "segundo titulo",
        "descripcion": "texto generico 2",
    }

    objeto3 = {
        "id": "003",
        "titulo": "tercer titulo",
        "descripcion": "texto generico 3",
    }

    conjunto = [objecto1, objeto2, objeto3]

    # Como mandar un objeto (variable) de python a la vista:

    # Obtener los datos de la base de datos
    personas = Usuarios.objects.values("id", "nombres", "apellidos", "edad")
    lista_personas = list(personas)

    return render(
        request,
        "prueba.html",
        {"objeto": objecto1, "arreglo": conjunto, "lista": lista_personas},
    )


def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})


def error_logs(request):
    return render(request, "error_logs.html")


def get_error_logs(request):
    errors = ErrorLog.objects.values("id", "codigo", "mensaje", "fecha")
    return JsonResponse({"data": list(errors)})
