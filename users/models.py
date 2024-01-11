from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.CharField(max_length=10, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users', verbose_name='фото', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []