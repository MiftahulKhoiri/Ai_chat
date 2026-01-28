from collections import deque

class SentimentMonitor:
    def __init__(self, window=10):
        self.scores = deque(maxlen=window)

    def add(self, score):
        self.scores.append(score)

    def status(self):
        avg = sum(self.scores) / len(self.scores) if self.scores else 0
        if avg <= -2:
            return "🔴 Emosi Negatif Dominan"
        if avg >= 2:
            return "🟢 Emosi Positif Dominan"
        return "🟡 Emosi Netral"