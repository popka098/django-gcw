from django.test import TestCase
from django.contrib.auth.models import User
from training.models import Task9, Stats, Atts, MistakesAnswers


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
