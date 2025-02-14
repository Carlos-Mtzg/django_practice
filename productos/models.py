from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


# Funcion que devuelva el objeto en forma de Dict
def to_ditc(self):
    return {
        # 'claveValor': 'valor'
        "nombre": self.nombre,
        "precio": self.precio,
        "imagen": self.imagen,
    }
