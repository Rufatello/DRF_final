from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=150, verbose_name='Почта')
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    surname = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    chat_id = models.CharField(max_length=20, verbose_name='Номер чата', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    code = models.CharField(max_length=10, verbose_name='Код подтверждения', **NULLABLE)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'



