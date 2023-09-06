from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.models.user_manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """User model."""

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()


    def __str__(self):
        return self.username