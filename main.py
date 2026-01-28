from core.nlp_engine import ConversationalEngine

bot = ConversationalEngine()

# TRAIN SEKALI
# bot.train("data/training_data.xlsx")

print("Bot siap berbicara (ketik exit untuk keluar)")

while True:
    user = input("Kamu: ")
    if user.lower() == "exit":
        break

    reply = bot.chat(user)
    print("Bot:", reply)