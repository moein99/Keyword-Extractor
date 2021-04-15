from django.http import JsonResponse
from rest_framework import generics
from rest_framework.status import HTTP_400_BAD_REQUEST

from extractor.approaches.unsupervised.graph_based.multipartite_rank import get_multipartite_rank_phrases
from extractor.approaches.unsupervised.graph_based.position_rank import get_position_rank_phrases
from extractor.approaches.unsupervised.graph_based.single_rank import get_single_rank_phrases
from extractor.approaches.unsupervised.graph_based.text_rank import get_text_rank_phrases
from extractor.approaches.unsupervised.graph_based.topic_rank import get_topic_rank_phrases
from extractor.serializers.serializers import ExtractorSerializer, Method

extractor_functions = {
    Method.position: get_position_rank_phrases,
    Method.multipartite: get_multipartite_rank_phrases,
    Method.single: get_single_rank_phrases,
    Method.topic: get_topic_rank_phrases,
    Method.text: get_text_rank_phrases,
}


class Extractor(generics.GenericAPIView):
    serializer_class = ExtractorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        result = {
            "result": [
                item.to_json() for item in extractor_functions.get(data["method"])(
                    text=data["text"],
                    num_of_key_phrases=data["num_of_keywords"]
                )
            ]
        }
        return JsonResponse(result)
