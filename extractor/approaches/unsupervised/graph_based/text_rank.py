from django.conf import settings
from perke.unsupervised.graph_based import TextRank

from extractor.approaches.unsupervised.graph_based import KeyPhrase

valid_pos_tags = {'N', 'Ne', 'AJ', 'AJe'}


def get_text_rank_phrases(text, num_of_key_phrases):
    extractor = TextRank(valid_pos_tags=valid_pos_tags)
    extractor.load_text(input=text, word_normalization_method=None)
    extractor.weight_candidates(
        window_size=settings.APPROACHES["TextRank"]["WINDOW_SIZE"],
        top_t_percent=settings.APPROACHES["TextRank"]["TOP_T_PERCENT"]
    )
    key_phrases = extractor.get_n_best(n=num_of_key_phrases)
    return [
        KeyPhrase(weight=weight, key_phrase=key_phrase) for key_phrase, weight in key_phrases
    ]
