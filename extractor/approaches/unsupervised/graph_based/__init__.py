class KeyPhrase:
    def __init__(self, key_phrase, weight):
        self.key_phrase = key_phrase
        self.weight = weight

    def to_json(self):
        return {"key": self.key_phrase, "weight": self.weight}
