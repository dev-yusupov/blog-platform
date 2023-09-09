from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/api/v1/", include("accounts.urls"))
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
        path("api/redoc/", SpectacularRedocView.as_view(url_name="schema")),
    ]