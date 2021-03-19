from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


from alpha.views import SuperCreateView
from .forms import ChangeUserForm, UserAddForm
from .models import User


class ChangePassword(SuccessMessageMixin, PasswordChangeView):
    """
    Vista para cambiar la contraseña de un usuario autenticado
    """

    success_message = _(
        "Password successfully updated. Login into the system using your new password."
    )
    success_url = reverse_lazy("users:login")


class ResetPassword(PasswordResetView):
    """
    Vista para que un usuario pueda recuperar su contraseña
    con el correo electrónico registrado
    """

    success_url = reverse_lazy("users:password_reset_aplication_done")


class LinkResetPassword(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Vista para el enlace creado por el sistema para recuperar
    la contraseña. El mensaje se envía por correo electrónico
    """

    success_message = _(
        "Your password has been reseted."
        " You can login into the system typing your new password."
    )
    success_url = reverse_lazy("users:login")


class AddUserView(SuperCreateView):
    """
    Vista para crear un nuevo usuario
    """

    model = User
    form_class = UserAddForm
    template_name = "users/new_user.html"
    success_message = _("User %(username)s successfully created")
    success_url = reverse_lazy("alpha:home")
