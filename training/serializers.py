from rest_framework import serializers

from training import models


class TaskSerializer(serializers.Serializer):
    Word = serializers.CharField()
    Context_Before = serializers.CharField()
    Pass = serializers.CharField()
    Context_After = serializers.CharField()
    class Meta:
        fields = [
            "Word",
            "Context_Before",
            "Pass",
            "Context_After"
        ]
        

class WordsSerializer(serializers.ListSerializer):
    child = TaskSerializer()

