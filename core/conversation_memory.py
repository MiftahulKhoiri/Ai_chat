class ConversationMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []  # (user, bot, sentiment_score)

    def add(self, user_text, bot_text, score):
        self.history.append((user_text, bot_text, score))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def avg_sentiment(self):
        if not self.history:
            return 0
        return sum(s for _, _, s in self.history) / len(self.history)