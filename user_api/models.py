from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Manager for user profile
class UserProfileManager(BaseUserManager):
    """The manager for the User Profile model"""

    def create_user(self, email, name, password=None):
        """Create a new user in database"""
        if not email:
            raise ValueError("The user must have an email.")

        email = self.normalize_email(email=email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User Profile database model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self) -> str:
        """Returns the name of the user"""
        return self.name

    def __str__(self) -> str:
        """Returns the str form of the profile"""
        return "Name:\t{0}\nUsername:\t{1}\nIs admin:\t{2}\n".format(self.name, self.email, self.is_admin)