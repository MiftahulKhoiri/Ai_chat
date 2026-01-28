import random

class ResponseGenerator:
    def __init__(self, language_model):
        self.lm = language_model

    def generate(self, cleaned_text):
        words = cleaned_text.split()
        if not words:
            return None

        last_word = words[-1]
        next_word = self.lm.predict_next(last_word)

        if not next_word:
            return None

        return f"{cleaned_text} {next_word}"