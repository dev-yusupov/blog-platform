from django.urls import path, include

from rest_framework.routers import DefaultRouter

from accounts.views import UserView

routers = DefaultRouter()

app_name = "accounts"

routers.register("", UserView)

urlpatterns = [
    path("", include(routers.urls))
]
