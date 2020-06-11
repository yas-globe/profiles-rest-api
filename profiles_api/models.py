from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager():
    """Manager for user profiles"""

    def create_user(self, email, name, password=None): # allow none password
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  # under AbstractBaseUser, to hash password
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save new user with given info"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # allows you to activate or deactivate an account
    is_staff = models.BooleanField(default=False)  # have access to Django admin or not

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # override username field with email, no need to provide
    REQUIRED_FIELDS = ['name']  # now required fields are email and name

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def get_full_email(self):
        return self.email

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email
