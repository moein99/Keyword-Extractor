from django.conf import settings
from perke.unsupervised.graph_based.position_rank import PositionRank
from extractor.approaches.unsupervised.graph_based import KeyPhrase

valid_pos_tags = {'N', 'Ne', 'AJ', 'AJe'}
grammar = r"""
    NP:
        <P>{<N>}<V>
    NP:
        {<DETe?|Ne?|NUMe?|AJe|PRO|CL|RESe?><DETe?|Ne?|NUMe?|AJe?|PRO|CL|RESe?>*}
        <N>}{<.*e?>
"""


def get_position_rank_phrases(text, num_of_key_phrases):
    extractor = PositionRank(valid_pos_tags=valid_pos_tags)
    extractor.load_text(input=text, word_normalization_method=None)
    extractor.select_candidates(
        grammar=grammar,
        maximum_word_number=settings.APPROACHES["PositionRank"]["MAX_KEY_PHRASE_WORD_COUNT"]
    )
    extractor.weight_candidates(settings.APPROACHES["PositionRank"]["WINDOW_SIZE"])
    key_phrases = extractor.get_n_best(n=num_of_key_phrases)

    return [
        KeyPhrase(weight=weight, key_phrase=key_phrase) for key_phrase, weight in key_phrases
    ]
