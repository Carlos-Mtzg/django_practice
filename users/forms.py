from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re


INPUT_CLASSES = "form-control mt-2"


# Primer Formulario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "name",
            "surname",
            "control_number",
            "age",
            "tel",
            "password1",
            "password2",
        ]

        widgets = {
            "email": forms.EmailInput(
                attrs={"class": INPUT_CLASSES, "placeholder": "Write your email"}
            ),
            "name": forms.TextInput(
                attrs={"class": INPUT_CLASSES, "placeholder": "Write your name"}
            ),
            "surname": forms.TextInput(
                attrs={"class": INPUT_CLASSES, "placeholder": "Write your surname"}
            ),
            "control_number": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Write your control number",
                }
            ),
            "age": forms.NumberInput(
                attrs={"class": INPUT_CLASSES, "placeholder": "Write your age"}
            ),
            "tel": forms.TextInput(
                attrs={"class": INPUT_CLASSES, "placeholder": "Write your phone number"}
            ),
        }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_CLASSES,
                "required": True,
                "placeholder": "**************",
            }
        ),
    )

    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_CLASSES,
                "required": True,
                "placeholder": "**************",
            }
        ),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@utez.edu.mx"):
            raise forms.ValidationError(
                "El correo electrónico debe ser del dominio @utez.edu.mx"
            )
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if (
            len(password) < 8
            or not re.search(r"[!#$%&?]", password)
            or not re.search(r"\d", password)
        ):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, un símbolo (!, #, $, %, & o ?) y un número."
            )
        return password

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if len(control_number) != 10:
            raise forms.ValidationError("La matrícula debe tener 10 caracteres.")
        return control_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


# Segundo Formulario (Inicio de sesion)
class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Write your email",
                "required": True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Write your password",
                "required": True,
            }
        )
    )
