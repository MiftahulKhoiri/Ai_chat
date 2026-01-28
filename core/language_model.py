import pickle
from collections import defaultdict

class LanguageModel:
    def __init__(self):
        self.model = defaultdict(lambda: defaultdict(int))

    def train(self, sentences):
        for sentence in sentences:
            words = sentence.split()
            for i in range(len(words) - 1):
                self.model[words[i]][words[i + 1]] += 1

    def predict_next(self, word):
        if word not in self.model:
            return None
        return max(self.model[word], key=self.model[word].get)

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(dict(self.model), f)

    def load(self, path):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self.model = defaultdict(lambda: defaultdict(int), data)