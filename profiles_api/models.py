from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
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

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        # name of the remote model == class UserProfile or default django model
        # adding this to reference AUTH_USER_MODEL and create user without having to redo the create user
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE  # If user is deleted, do what to Profile? remove : null
    )
    status_text = models.CharField(max_length=255)  # text of the feed update
    created_on = models.DateTimeField(auto_now_add=True)

    # string representation of the model
    def __str__(self):
        """Return the model as a string"""
        return self.status_text
