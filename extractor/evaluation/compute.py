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
    # "single": get_single_rank_phrases,
    # "topic": get_topic_rank_phrases,
    # "text": get_text_rank_phrases,
}
METRICS = {approach_name: Metric(0, 0, 0) for approach_name in APPROACHES}


def read_data(data_set_address):
    with open(data_set_address, 'r') as file:
        return json.load(file)


def store_results():
    result = {}
    for name in METRICS:
        precision = METRICS[name].true_p / METRICS[name].prec_denom
        recall = METRICS[name].true_p / METRICS[name].rec_denom
        result[name] = {
            "precision": precision,
            "recall": recall,
            "f1": f1(precision, recall),
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
            partial_tp = len(set(extracted_keywords).intersection(set(document_keywords)))
            partial_precision_denom = len(extracted_keywords)
            partial_recall_denom = len(document_keywords)
            METRICS[approach_name].true_p += partial_tp
            METRICS[approach_name].prec_denom += partial_precision_denom
            METRICS[approach_name].rec_denom += partial_recall_denom
        print(counter)
        counter += 1


data = read_data("data.test")
compute_metrics(data)
store_results()
