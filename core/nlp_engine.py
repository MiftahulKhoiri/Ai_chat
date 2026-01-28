from core.ainlp import AiNLP
from core.language_model import LanguageModel
from core.response_generator import ResponseGenerator
from core.conversation_memory import ConversationMemory
from core.reasoning_engine import ReasoningEngine

class ConversationalEngine:
    def __init__(self):
        self.ainlp = AiNLP()
        self.memory = ConversationMemory()
        self.lm = LanguageModel()
        self.generator = ResponseGenerator(self.lm)
        self.reasoner = ReasoningEngine(self.ainlp, self.memory)

    def chat(self, text):
        cleaned = self.ainlp.clean_text_full(text)
        tokens = self.ainlp.remove_stopwords(
            self.ainlp.tokenize_text(cleaned)
        )

        rule_response, score = self.reasoner.apply(cleaned, tokens)

        if rule_response:
            self.memory.add(text, rule_response, score)
            return rule_response

        response = self.generator.generate(cleaned) or "Bisa kamu jelaskan lebih lanjut?"
        self.memory.add(text, response, score)
        return response