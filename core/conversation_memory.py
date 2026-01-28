class ConversationMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []

    def add(self, user_text, bot_text):
        self.history.append((user_text, bot_text))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return " ".join([u for u, _ in self.history])