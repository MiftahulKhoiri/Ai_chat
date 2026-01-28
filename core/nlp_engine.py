from core.ainlp import AiNLP
from core.conversation_memory import ConversationMemory
from core.reasoning_engine import ReasoningEngine
from core.language_model import LanguageModel
from core.response_generator import ResponseGenerator

class ConversationalEngine:
    def __init__(self):
        self.ainlp = AiNLP()
        self.memory = ConversationMemory()
        self.reasoner = ReasoningEngine(self.ainlp, self.memory)
        self.lm = LanguageModel()
        self.generator = ResponseGenerator(self.lm)

    def chat(self, text):
        cleaned = self.ainlp.clean_text_full(text)
        if not cleaned:
            return "Saya tidak memahami input tersebut."

        tokens = self.ainlp.remove_stopwords(
            self.ainlp.tokenize_text(cleaned)
        )

        # 🔥 SENTIMENT LANGSUNG DARI AiNLP
        sentiment_result = self.ainlp.sentiment_analysis(tokens)

        rule_response, score = self.reasoner.apply(
            cleaned,
            tokens,
            sentiment_result
        )

        if rule_response:
            self.memory.add(text, rule_response, score)
            return rule_response

        response = self.generator.generate(cleaned) or "Bisa kamu jelaskan lebih lanjut?"
        self.memory.add(text, response, score)
        return response