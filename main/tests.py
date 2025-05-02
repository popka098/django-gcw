from django.test import TestCase, Client
from django.urls import reverse

from main.forms import UserRegistrationForm

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.response_url = reverse('registration')
        self.response = {
            'get': self.client.get(self.response_url),
            'post': self.client.post(self.response_url)
        }

    def test_registration_page_get(self):
        response = self.response['get']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/accounts/registration.html')

    def test_registration_form_get(self):
        response = self.response['get']
        user = response.context['user_form']
        self.assertIsInstance(user, UserRegistrationForm)

    def test_registration_form_post(self):
        response = self.response['post']
        user = response.context['user_form']
        self.assertIsInstance(user, UserRegistrationForm)




    