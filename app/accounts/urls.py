from django.urls import path, include

from rest_framework.routers import DefaultRouter

from accounts.views import CreateUserView, CreateTokenView, UserProfileView

routers = DefaultRouter()

app_name = "accounts"

# routers.register("", CreateUserView)

urlpatterns = [
    path("registration/", CreateUserView.as_view(), name="registeration"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    # path("", include(routers.urls))
]
