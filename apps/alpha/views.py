from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView


class SuperCreateView(SuccessMessageMixin, CreateView):
    """
    Una CBV genérica que permite crear instancias de un modelo
    Incluye un mensaje de confirmación si se crea la instancia
    """

    pass


class SuperUpdateView(SuccessMessageMixin, UpdateView):
    """
    Una CBV genérica que permite actualizar intancias de un modelo
    Incluye un mensaje de confirmación si se crea la instancia
    """

    pass
