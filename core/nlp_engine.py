from core.ainlp import AiNLP
from core.language_model import LanguageModel
from core.conversation_memory import ConversationMemory
from core.response_generator import ResponseGenerator
import os

class ConversationalEngine:
    def __init__(self):
        self.ainlp = AiNLP()
        self.memory = ConversationMemory()
        self.lm = LanguageModel()
        self.generator = ResponseGenerator(self.lm)

        model_path = "model/language_model.pkl"
        if os.path.exists(model_path):
            self.lm.load(model_path)

    def train(self, excel_path):
        df = self.ainlp.preprocess_and_analyze(excel_path)
        text_col = 'full_text' if 'full_text' in df.columns else 'comment'
        sentences = df[text_col].str.lower().tolist()
        self.lm.train(sentences)
        self.lm.save("model/language_model.pkl")

    def chat(self, text):
        cleaned = self.ainlp.clean_text_full(text)
        if not cleaned:
            return "Saya tidak memahami input tersebut."

        response = self.generator.generate(cleaned)

        if not response:
            response = "Bisa jelaskan lebih lanjut?"

        self.memory.add(text, response)
        return response