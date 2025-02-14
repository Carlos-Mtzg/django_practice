from django.urls import path
from .views import lista_categorias, ver_categorias, agregar_categoria

urlpatterns = [
    path("api/get/", lista_categorias, name="lista"),
    path("json/", ver_categorias, name="ver"),
    path("agregar/", agregar_categoria, name="agregar"),
]
