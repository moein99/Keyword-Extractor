from keyword_extractor import settings
from perke.unsupervised.graph_based import SingleRank

from extractor.approaches.unsupervised.graph_based import KeyPhrase

valid_pos_tags = {'N', 'Ne', 'AJ', 'AJe'}


def get_single_rank_phrases(text, num_of_key_phrases):
    extractor = SingleRank(valid_pos_tags=valid_pos_tags)
    extractor.load_text(input=text, word_normalization_method=None)
    extractor.select_candidates()
    extractor.weight_candidates(settings.APPROACHES["PositionRank"]["WINDOW_SIZE"])
    key_phrases = extractor.get_n_best(n=num_of_key_phrases)

    return [
        KeyPhrase(weight=weight, key_phrase=key_phrase) for key_phrase, weight in key_phrases
    ]
