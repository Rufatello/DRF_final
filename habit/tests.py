from rest_framework import status
from rest_framework.test import APITestCase
from habit.models import Habit, Reflex
from users.models import User


class HabitTest(APITestCase):
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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        Habit.objects.create(
            user=self.user, action='asd'
        )
        response = self.client.get('/habit/habit/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            [{'id': 2, 'action': 'asd', 'user': 2}])


class ReflexTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='1@mail.ru', first_name='Rufat', last_name='Geydarov')
        self.client.login(username='1@mail.ru', password='12345')
        self.user.set_password('12345')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_reflex_create(self):
        data = {
            "periodicity": 'week',
            'user': self.user.id,
            'fee': 'test',
            'time_to_complete': 12,
            'action': 'test',
            'data': '2021-01-01',
            'locale': 'test'
        }
        response = self.client.post('/habit/reflex/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_reflex(self):
        Reflex.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            action='test',
            data='2021-01-01',
            locale='test'

        )
        response = self.client.get('/habit/reflex/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            [{'id': 1, 'habit': None, 'periodicity': 'week', 'is_published': False, 'is_pleasant': False, 'fee': 'test','time_to_complete': 12, 'action': 'test', 'data': '2021-01-01T00:00:00Z', 'locale': 'test', 'user': 3}]
        )

    def test_reflex_delete(self):
        reflex = Reflex.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            action='test',
            data='2021-01-01',
            locale='test'
        )
        url = f'/habit/reflex/{reflex.id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_reflex_published(self):
        Reflex.objects.create(
            periodicity='week',
            is_published=True,
            user=self.user,
            fee='test',
            time_to_complete=12,
            action='test',
            data='2021-01-01',
            locale='test'

        )
        response = self.client.get('/habit/reflex/published/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 2, 'habit': None, 'periodicity': 'week', 'is_published': True, 'is_pleasant': False, 'fee': 'test', 'time_to_complete': 12, 'action': 'test', 'data': '2021-01-01T00:00:00Z', 'locale': 'test', 'user': 4}]})

    def test_reflex_update(self):

        reflex = Reflex.objects.create(
            periodicity='week',
            user=self.user,
            fee='test',
            time_to_complete=12,
            action='test',
            data='2021-01-01',
            locale='test'
        )
        updated_data = {
            'periodicity': 'week',
            'fee': 'updated_fee',
            'time_to_complete': 15,
            'action': 'updated_action',
            'data': '2022-02-13',
            'locale': 'updated_locale'
        }

        url = f'/habit/reflex/{reflex.id}/update/'
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


