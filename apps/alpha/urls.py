from django.views.generic import TemplateView
from django.urls import path


app_name = "alpha"
urlpatterns = [
    path("", TemplateView.as_view(template_name="alpha/home.html"), name="home"),
]
