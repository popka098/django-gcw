from django.test import TestCase
from training.serializers import TaskSerializer, WordsSerializer

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

