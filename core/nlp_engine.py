from core.ainlp import AiNLP
from core.language_model import LanguageModel
import os

class NLPEngine:
    def __init__(self):
        self.ainlp = AiNLP()
        self.lm = LanguageModel()

        model_path = "model/language_model.pkl"
        if os.path.exists(model_path):
            self.lm.load(model_path)

    def train_language_model(self, excel_path):
        df = self.ainlp.preprocess_and_analyze(excel_path)

        # PAKAI TEKS ASLI / CLEANED, BUKAN STEMMED
        text_col = 'full_text' if 'full_text' in df.columns else 'comment'
        sentences = df[text_col].str.lower().tolist()

        self.lm.train(sentences)
        self.lm.save("model/language_model.pkl")

    def predict_next_word(self, text):
        last_word = text.lower().split()[-1]
        return self.lm.predict_next(last_word)