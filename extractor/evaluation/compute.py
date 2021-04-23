import json

from extractor.approaches.unsupervised.graph_based.multipartite_rank import get_multipartite_rank_phrases
from extractor.approaches.unsupervised.graph_based.position_rank import get_position_rank_phrases
from extractor.approaches.unsupervised.graph_based.single_rank import get_single_rank_phrases
from extractor.approaches.unsupervised.graph_based.text_rank import get_text_rank_phrases
from extractor.approaches.unsupervised.graph_based.topic_rank import get_topic_rank_phrases
from extractor.evaluation.metrics import *

KEYWORDS_LIMIT = 5

APPROACHES = {
    "position": get_position_rank_phrases,
    "multipartite": get_multipartite_rank_phrases,
    "single": get_single_rank_phrases,
    "topic": get_topic_rank_phrases,
    "text": get_text_rank_phrases,
}
METRICS = {approach_name: [] for approach_name in APPROACHES}


def read_data(data_set_address):
    with open(data_set_address, 'r') as file:
        return json.load(file)


def store_results():
    result = {}
    for name in METRICS:
        result[name] = {
            "precision": sum(metric.p for metric in METRICS[name]) / len(METRICS[name]),
            "recall": sum(metric.r for metric in METRICS[name]) / len(METRICS[name]),
            "f1": sum(metric.f1 for metric in METRICS[name]) / len(METRICS[name]),
        }
    with open("result.txt", 'w') as file:
        json.dump(result, file)


def compute_metrics(data):
    counter = 1
    for document in data:
        for approach_name, approach_function in APPROACHES.items():
            extracted_keywords = [
                item.key_phrase for item in
                approach_function(
                    text=document["body"],
                    num_of_key_phrases=KEYWORDS_LIMIT,
                )
            ]
            document_keywords = document["keyphrases"][:KEYWORDS_LIMIT]
            p, r = precision(extracted_keywords, document_keywords), recall(extracted_keywords, document_keywords)
            f_one = f1(p, r)
            METRICS[approach_name].append(Metric(p, r, f_one))
        print(counter)
        counter += 1


data = read_data("data.test")
compute_metrics(data[:100])
store_results()
