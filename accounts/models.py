from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Please provide an email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """ Custom user model class"""
    email = models.EmailField(unique=True, default='')
    user_name = models.CharField(unique=True, max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, default='')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # assigning 'email' as field to USERNAME_FIELD in the model for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    # assign new manager for objects creation
    objects = CustomUserManager()

    class Meta:
        """human-readable for model"""
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def __str__(self):
        """ string representation of the model objects"""
        return self.email
