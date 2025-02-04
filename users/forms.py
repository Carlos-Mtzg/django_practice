from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


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
