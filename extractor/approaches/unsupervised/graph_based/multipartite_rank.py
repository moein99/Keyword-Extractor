from keyword_extractor import settings
from perke.base.types import HierarchicalClusteringMetric, HierarchicalClusteringLinkageMethod, WordNormalizationMethod
from perke.unsupervised.graph_based import MultipartiteRank

from extractor.approaches.unsupervised.graph_based import KeyPhrase

valid_pos_tags = {'N', 'Ne', 'AJ', 'AJe'}


def get_multipartite_rank_phrases(text, num_of_key_phrases):
    extractor = MultipartiteRank(valid_pos_tags=valid_pos_tags)
    extractor.load_text(input=text, word_normalization_method=WordNormalizationMethod.stemming)
    extractor.select_candidates()
    extractor.weight_candidates(
        threshold=settings.APPROACHES["MultipartiteRank"]["THRESHOLD"],
        metric=HierarchicalClusteringMetric.jaccard,
        linkage_method=HierarchicalClusteringLinkageMethod.average,
        alpha=settings.APPROACHES["MultipartiteRank"]["ALPHA"])
    key_phrases = extractor.get_n_best(n=num_of_key_phrases)

    return [
        KeyPhrase(weight=weight, key_phrase=key_phrase) for key_phrase, weight in key_phrases
    ]
