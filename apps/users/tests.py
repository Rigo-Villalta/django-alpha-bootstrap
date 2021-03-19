from django.test import Client, TestCase, client
from django.urls import reverse
from django.utils import translation


class AuthUrlsTests(TestCase):
    """
    Pruebas para verificar que todos las url
    de autenticación(de la app Users) funcionen
    y sea revertidas(usando reverse)
    """

    def test_login_url(self):
        """
        Prueba unitaria de la url para ingresar al sistema
        """
        with translation.override("en"):
            self.assertEqual(reverse("users:login"), "/users/login/")
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_logout_url(self):
        """
        Prueba unitaria de la url para salir del sistema
        """
        with translation.override("en"):
            self.assertEqual(reverse("users:logout"), "/users/logout/")
        response = self.client.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_change_password_url_not_authenticated(self):
        """
        Prueba unitaria de la url para cambiar la contraseña de 
        un usuario no autenticado(falla)
        """
        with translation.override("en"):
            self.assertEqual(
                reverse("users:change_password"), "/users/change_password/"
            )
            response = self.client.get(reverse("users:change_password"))
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, "/users/login/?next=/users/change_password/")
    
    def test_reset_password_url(self):
        """
        Prueba unitaria de la url para recuperar la contraseña de 
        un usuario no autenticado(¿olvido su contraseña?)
        """
        with translation.override("en"):
            self.assertEqual(
                reverse("users:form_reset_password"), "/users/form_reset_password/"
            )
            response = self.client.get(reverse("users:form_reset_password"))
            self.assertEqual(response.status_code, 200)
    
    def test_add_user(self):
        """
        Prueba unitaria de la url para crear un nuevo usuario con
        un usuario no autenticado
        """
        with translation.override("en"):
            self.assertEqual(
                reverse("users:add"), "/users/add/"
            )
            response = self.client.get(reverse("users:add"))
            self.assertEqual(response.status_code, 200)