from django.views.generic import TemplateView
from django.urls import path


app_name = "alpha"
urlpatterns = [
    path("", TemplateView.as_view(template_name="alpha/home.html"), name="home"),
    path("403", TemplateView.as_view(template_name="403.html"), name="403"),
    path("404", TemplateView.as_view(template_name="404.html"), name="404"),
    path("500", TemplateView.as_view(template_name="500.html"), name="500")
]
