from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from training.models import Stats, Atts, MistakesAnswers
from main.models import Profile

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Создаем или получаем профиль с активной подпиской для пользователя
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={'subscribe': True}
        )
        if not created:
            self.profile.subscribe = True
            self.profile.save()

        self.client.login(username='testuser', password='testpass123')

        # Создаем тестовые данные
        self.stats = Stats.objects.create(
            time=100,
            successes=5,
            mistakes=2,
            user=self.user
        )
        self.att = Atts.objects.create(
            time=50,
            successes=3,
            mistakes=1,
            user=self.user
        )
        self.mistake = MistakesAnswers.objects.create(
            input_answer="неправильный",
            correct_answer="правильный",
            att=self.att
        )

    def test_training_view(self):
        # Тест для задания 9
        response = self.client.get(reverse('task9'))
        self.assertEqual(response.status_code, 200)

        # Тест для несуществующего задания
        response = self.client.get('/training/task999/')
        self.assertEqual(response.status_code, 404)

        # Тест для задания 15 (которого нет в TASK_MODELS)
        response = self.client.get('/training/task15/')
        self.assertEqual(response.status_code, 404)

    def test_statistics_page_view(self):
        # Удаляем все существующие статистики для пользователя
        Stats.objects.filter(user=self.user).delete()
        # Создаем новую статистику
        self.stats = Stats.objects.create(
            time=100,
            successes=5,
            mistakes=2,
            user=self.user
        )

        response = self.client.get(reverse('statistics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/statistics/general_statistics.html')

        # Проверяем контекст
        self.assertEqual(response.context['time_all'], 100)
        self.assertEqual(response.context['success_all'], 5)
        self.assertEqual(response.context['mistakes_all'], 2)

    def test_mistakes_page_view(self):
        response = self.client.get(reverse('mistakes', args=[self.att.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/statistics/mistakes.html')

        # Проверяем контекст
        self.assertEqual(response.context['att_id'], self.att.id)
        self.assertEqual(len(response.context['mistakes']), 1)

        # Тест доступа к чужой попытке
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        other_att = Atts.objects.create(
            time=30,
            successes=2,
            mistakes=1,
            user=other_user
        )
        response = self.client.get(reverse('mistakes', args=[other_att.id]))
        self.assertEqual(response.status_code, 404)

