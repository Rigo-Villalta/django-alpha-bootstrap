import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path("", include("alpha.urls", namespace="alpha")),
    path(_("users/"), include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
