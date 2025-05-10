"""training serializers"""
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    """Сериализатор слова

    :param Word: слово
    :param Context_Before: контекст перед словом
    :param Pass: слово с пропуском
    :param Context_After: контекст после слова
    """
    Word = serializers.CharField()
    Context_Before = serializers.CharField()
    Pass = serializers.CharField()
    Context_After = serializers.CharField()

    def create(self, validated_data): # pragma: no cover
        print("", end="")
        return super().create(validated_data)

    def update(self, instance, validated_data): # pragma: no cover
        print("", end="")
        return super().update(instance, validated_data)
    class Meta:
        """Мета класс для слова

        """
        fields = [
            "Word",
            "Context_Before",
            "Pass",
            "Context_After"
        ]


class WordsSerializer(serializers.ListSerializer):
    """Сериализатор слов

    :param child: TaskSerializer
    """
    child = TaskSerializer()

    def update(self, instance, validated_data): # pragma: no cover
        print("", end="")
        return super().update(instance, validated_data)
