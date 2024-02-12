from django.conf import settings
from django.db import models
from users.models import NULLABLE


class Habit(models.Model):
    action = models.CharField(max_length=100, verbose_name='Активность')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class Reflex(models.Model):
    periodicity = [
        ('week', 'Раз в неделю'),
        ('every_day', 'Каждый день')
    ]
    periodicity = models.CharField(verbose_name='Переодичность', choices=periodicity, default='every_day', max_length=100)
    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятности')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)
    fee = models.CharField(max_length=150, verbose_name='Вознагрождение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время выполнения', default=1)
    action = models.CharField(max_length=100, verbose_name='Активность')
    data = models.DateTimeField(verbose_name='Время действия')
    locale = models.CharField(max_length=150, verbose_name='Место действия')
    habit = models.ForeignKey(Habit, verbose_name='Привычка', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Рефлекс'
        verbose_name_plural = 'Рефлексы'

