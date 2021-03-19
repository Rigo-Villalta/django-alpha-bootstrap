from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView
from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    ChangePassword,
    ResetPassword,
    LinkResetPassword,
    AddUserView,
)

app_name = "users"
urlpatterns = [
    path(_("login/"), LoginView.as_view(), name="login"),
    path(_("logout/"), LogoutView.as_view(), name="logout"),
    # cambiar la contraseña de un usuario autenticado
    path(_("change_password/"), ChangePassword.as_view(), name="change_password"),
    # Formulario para ingresar correo solicitando recuperación de password
    path(
        _("form_reset_password/"),
        ResetPassword.as_view(),
        name="form_reset_password",
    ),
    # muestra de que la solicitud de restablecer contraseña ha sido hecha
    path(
        _("password_reset_aplication_done/"), 
        PasswordResetDoneView.as_view(), name="password_reset_aplication_done"),
    # Formulario para ingresar la nueva contraseña
    path(
        "<uidb64>/<token>/",
        LinkResetPassword.as_view(),
        name="link_reset_password",
    ),
    path(_("add/"), AddUserView.as_view(), name="add"),
]