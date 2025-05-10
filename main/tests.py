from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Profile, Payments
from training.models import Task9, Task10, Task11, Task12
from datetime import datetime, timedelta
import json

class MainViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/accounts/login.html')

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/accounts/registration.html')

        response = self.client.post(reverse('registration'), {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com',
            'password': 'newpass123',
            'password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/accounts/profile.html')

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertFalse(self.profile.subscribe)
        self.assertIsNone(self.profile.period_subscribe)

    def test_profile_update(self):
        self.profile.telegram = '@testuser'
        self.profile.phone = '+79001234567'
        self.profile.subscribe = True
        self.profile.period_subscribe = datetime.now().date()
        self.profile.save()

        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.telegram, '@testuser')
        self.assertEqual(updated_profile.phone, '+79001234567')
        self.assertTrue(updated_profile.subscribe)
        self.assertIsNotNone(updated_profile.period_subscribe)

class PaymentsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_payment_creation(self):
        payment = Payments.objects.create(
            number=123456789,
            date=datetime.now().date(),
            amount=1000,
            status='Успешно',
            user=self.user
        )

        self.assertEqual(payment.number, 123456789)
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.status, 'Успешно')
        self.assertEqual(payment.user, self.user)

class APIViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)

        Task9.objects.create(
            Word="тест_9_1",
            Pass="т.ст_9_1",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task9.objects.create(
            Word="тест_9_2",
            Pass="т.ст_9_2",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task10.objects.create(
            Word="тест_10_1",
            Pass="т.ст_10_1",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task10.objects.create(
            Word="тест_10_2",
            Pass="т.ст_10_2",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task11.objects.create(
            Word="тест_11_1",
            Pass="т.ст_11_1",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task11.objects.create(
            Word="тест_11_2",
            Pass="т.ст_11_2",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task12.objects.create(
            Word="тест_12_1",
            Pass="т.ст_12_1",
            Context_Before="текст_до",
            Context_After="текст_после"
        )
        Task12.objects.create(
            Word="тест_12_2",
            Pass="т.ст_12_2",
            Context_Before="текст_до",
            Context_After="текст_после"
        )

    def test_get_user_sub(self):
        response = self.client.get(reverse('get_user_sub'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['sub'], False)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('get_user_sub'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['sub'], False)

        self.profile.subscribe = True
        self.profile.save()
        response = self.client.get(reverse('get_user_sub'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['sub'], True)

    def test_get_all_words(self):
        response = self.client.get(reverse('get_all_words', kwargs={'limit': 5}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('words', data)
        self.assertLessEqual(len(data['words']), 5)

    def test_get_random_words(self):
        response = self.client.get(reverse('get_random_words', kwargs={'task': 9, 'limit': 5}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('words', data)
        self.assertLessEqual(len(data['words']), 5)

    def test_get_random_word(self):
        response = self.client.get(reverse('get_random_word', kwargs={'task': 9}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, dict)
        self.assertIn('Word', data)
        self.assertIn('Pass', data)
        self.assertIn('Context_Before', data)
        self.assertIn('Context_After', data)

    def test_save_statistics(self):
        response = self.client.post(reverse('save_statistics'), json.dumps({
            'time': 100,
            'successes': 5,
            'mistakes': 2,
            'mistake_words': []
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['auntificated'])
        self.assertFalse(data['success'])

        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('save_statistics'), json.dumps({
            'time': 100,
            'successes': 5,
            'mistakes': 2,
            'mistake_words': []
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['auntificated'])
        self.assertTrue(data['success'])




