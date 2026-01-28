from core.ainlp import AiNLP
from core.reasoning_engine import ReasoningEngine
from core.language_model import LanguageModel
from core.response_generator import ResponseGenerator

class ConversationalEngine:
    def __init__(self):
        self.ainlp = AiNLP()
        self.reasoner = ReasoningEngine(self.ainlp)
        self.lm = LanguageModel()
        self.generator = ResponseGenerator(self.lm)

    def chat(self, text):
        cleaned = self.ainlp.clean_text_full(text)
        if not cleaned:
            return "Saya tidak memahami input tersebut."

        tokens = self.ainlp.tokenize_text(cleaned)
        tokens = self.ainlp.remove_stopwords(tokens)

        # 1️⃣ RULE BASED REASONING
        rule_response = self.reasoner.apply(cleaned, tokens)
        if rule_response:
            return rule_response

        # 2️⃣ LANGUAGE MODEL (fallback)
        response = self.generator.generate(cleaned)
        return response or "Bisa kamu jelaskan lebih lanjut?"