from django import forms
from .models import Categoria

INPUT_CLASSES = "form-control mt-2"


class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Ingrese aqui su nombre de categoria",
                }
            ),
            "imagen": forms.URLInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "https://tu-url-de-imagen-aqui"
                }),
        }

        labels = {
            "nombre": "Nombre de categoria:",
            "imagen": "URL de la imagen:",
        }
