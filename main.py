from core.nlp_engine import NLPEngine
from core.bootstrap import bootstrap 

bootstrap()

engine = NLPEngine()

# TRAIN SEKALI
engine.train_language_model("data/training_data.xlsx")

# PREDIKSI
while True:
    text = input("Kamu: ")
    if text.lower() == "exit":
        break

    next_word = engine.predict_next_word(text)
    if next_word:
        print(f"Bot: mungkin kata berikutnya '{next_word}'")
    else:
        print("Bot: saya belum tahu kelanjutannya")