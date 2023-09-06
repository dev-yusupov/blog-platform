from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Manager for user."""
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Please provide a Username.")
        if not password:
            raise ValueError("Please provide password.")
        
        """Create a new user."""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user