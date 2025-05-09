from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from training.models import Task9, Stats, Atts, MistakesAnswers
from training.views import training, statistics_page, mistakes_page
from training.serializers import TaskSerializer, WordsSerializer
from main.models import Profile

# Create your tests here.

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task9.objects.create(
            Word="тест",
            Context_Before="перед",
            Pass="те.т",
            Context_After="после"
        )

    def test_task_creation(self):
        self.assertEqual(self.task.Word, "тест")
        self.assertEqual(self.task.Context_Before, "перед")
        self.assertEqual(self.task.Pass, "те.т")
        self.assertEqual(self.task.Context_After, "после")

class StatsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.stats = Stats.objects.create(
            time=100,
            successes=5,
            mistakes=2,
            user=self.user
        )

    def test_stats_creation(self):
        self.assertEqual(self.stats.time, 100)
        self.assertEqual(self.stats.successes, 5)
        self.assertEqual(self.stats.mistakes, 2)
        self.assertEqual(self.stats.user, self.user)

class AttsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.att = Atts.objects.create(
            time=50,
            successes=3,
            mistakes=1,
            user=self.user
        )

    def test_att_creation(self):
        self.assertEqual(self.att.time, 50)
        self.assertEqual(self.att.successes, 3)
        self.assertEqual(self.att.mistakes, 1)
        self.assertEqual(self.att.user, self.user)

class MistakesAnswersModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
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

    def test_mistake_creation(self):
        self.assertEqual(self.mistake.input_answer, "неправильный")
        self.assertEqual(self.mistake.correct_answer, "правильный")
        self.assertEqual(self.mistake.att, self.att)

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


class SerializersTest(TestCase):
    def setUp(self):
        self.task_data = {
            'Word': 'тест',
            'Context_Before': 'перед',
            'Pass': 'те.т',
            'Context_After': 'после'
        }
        self.tasks_data = [
            {
                'Word': 'тест',
                'Context_Before': 'перед',
                'Pass': 'те.т',
                'Context_After': 'после'
            },
            {
                'Word': 'пример',
                'Context_Before': 'до',
                'Pass': 'пр.мер',
                'Context_After': 'после'
            }
        ]

    def test_task_serializer(self):
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid(), f"Validation errors: {serializer.errors}")
        self.assertEqual(serializer.validated_data['Word'], 'тест')
        self.assertEqual(serializer.validated_data['Context_Before'], 'перед')
        self.assertEqual(serializer.validated_data['Pass'], 'те.т')
        self.assertEqual(serializer.validated_data['Context_After'], 'после')

    def test_words_serializer(self):
        serializer = WordsSerializer(data=self.tasks_data)
        self.assertTrue(serializer.is_valid(), f"Validation errors: {serializer.errors}")
        self.assertEqual(len(serializer.validated_data), 2)
        self.assertEqual(serializer.validated_data[0]['Word'], 'тест')
        self.assertEqual(serializer.validated_data[1]['Word'], 'пример')
