from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserAddForm(UserCreationForm):
    """
    Formulario personalizado para la creación de un Usuario
    sin los campos first_name y last_name
    """

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class ChangeUserForm(UserChangeForm):
    """
    Formulario para el cambio de datos de un User
    sin incluir su password
    """

    password = None

    class Meta:
        model = User
        fields = ["username", "email"]
