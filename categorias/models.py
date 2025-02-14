from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


# Funcion que devuelva el objeto en forma de Dict
def to_ditc(self):
    return {
        # 'claveValor': 'valor'
        "nombre": self.nombre,
        "imagen": self.imagen,
    }
