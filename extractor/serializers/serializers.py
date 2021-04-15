from rest_framework import serializers


class Method:
    multipartite = "multipartite"
    text = "text"
    single = "single"
    topic = "topic"
    position = "position"


class ExtractorSerializer(serializers.Serializer):
    METHODS = [
        (Method.multipartite, "Multipartite Rank"),
        (Method.text, "Text Rank"),
        (Method.single, "Single Rank"),
        (Method.topic, "Topic Rank"),
        (Method.position, "Position Rank"),
    ]
    text = serializers.CharField()
    method = serializers.ChoiceField(choices=METHODS)
    num_of_keywords = serializers.IntegerField()
