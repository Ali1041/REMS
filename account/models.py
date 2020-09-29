from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from django.urls import reverse_lazy
from django.utils.text import slugify


# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Enter a valid Email')
        if not username:
            raise ValueError('Enter a valid username')

        myuser = self.model(
            email=self.normalize_email(email),
            username=username,
            # purpose=purpose
        )
        myuser.set_password(password)
        myuser.save(using=self._db)
        return myuser

    def create_superuser(self, email, username, password):
        myuser = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        myuser.is_superuser = True
        myuser.is_staff = True
        myuser.is_admin = True
        myuser.save(using=self._db)
        return myuser


class User(AbstractBaseUser):
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=100, unique=True)
    purpose = models.CharField(max_length=10)
    slug = models.SlugField(allow_unicode=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.purpose)
        super(User, self).save(*args, **kwargs)


