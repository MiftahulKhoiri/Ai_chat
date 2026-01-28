import json

class ReasoningEngine:
    def __init__(self, ainlp, memory, rule_path="rules.json"):
        self.ainlp = ainlp
        self.memory = memory
        with open(rule_path, "r", encoding="utf-8") as f:
            self.rules = json.load(f)

    def sentiment_score(self, tokens):
        score = 0
        for w in tokens:
            score += self.ainlp.lexicon_positive_dict.get(w, 0)
            score += self.ainlp.lexicon_negative_dict.get(w, 0)
        return score

    def apply(self, cleaned_text, tokens):
        score = self.sentiment_score(tokens)
        avg_score = self.memory.avg_sentiment()

        # ========= PRIORITY 1: EMOSI =========
        emo = self.rules["emotion"]

        if score <= emo["negative_strong"]["threshold"] or avg_score <= -2:
            return emo["negative_strong"]["response"], score

        if score <= emo["negative_light"]["threshold"]:
            return emo["negative_light"]["response"], score

        if score >= emo["positive"]["threshold"]:
            return emo["positive"]["response"], score

        # ========= PRIORITY 2: INFO =========
        if any(media in cleaned_text for media in self.ainlp.news_media):
            return self.rules["info"]["media_response"], score

        # ========= PRIORITY 3: CHIT-CHAT =========
        return None, score