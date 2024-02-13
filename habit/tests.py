from django.test import TestCase
from rest_framework import status

from habit.models import Habit, Reflex
from users.models import User
from rest_framework.authtoken.models import Token


class HabitTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='1@mail.ru', first_name='Rufat', last_name='Geydarov')
        self.client.login(username='1@mail.ru', password='12345')
        self.user.set_password('12345')

        self.user.save()
        self.client.force_authenticate(self.user)

    def test_habit_create(self):
        data = {
            'user': self.user.pk,
            'action': 'asdasd',
        }
        response = self.client.post('/habit/habit/create/', data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



 # periodicity = models.CharField(verbose_name='Переодичность', choices=periodicity, default='every_day', max_length=100)
 #    is_published = models.BooleanField(default=False, verbose_name='Публикация')
 #    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятности')
 #    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)
 #    fee = models.CharField(max_length=150, verbose_name='Вознагрождение', **NULLABLE)
 #    time_to_complete = models.PositiveIntegerField(verbose_name='Время выполнения', default=1)
 #    action = models.CharField(max_length=100, verbose_name='Активность')
 #    data = models.DateTimeField(verbose_name='Время действия')
 #    locale = models.CharField(max_length=150, verbose_name='Место действия')
 #    habit = models.ForeignKey(Habit, verbose_name='Привычка', on_delete=models.CASCADE, **NULLABLE)