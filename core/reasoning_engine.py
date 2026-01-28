class ReasoningEngine:
    def __init__(self, ainlp):
        self.ainlp = ainlp

    def apply(self, tokens):
        sentiment = self.ainlp.sentiment_analysis(tokens)
        score = 0

        # hitung ulang score
        for w in tokens:
            score += self.ainlp.lexicon_positive_dict.get(w, 0)
            score += self.ainlp.lexicon_negative_dict.get(w, 0)

        # ===============================
        # RULE NEGATIF KUAT
        # ===============================
        if score <= -3:
            return (
                "Kami mohon maaf atas pengalaman yang kurang menyenangkan. "
                "Masukan Anda sangat berarti bagi kami."
            )

        # ===============================
        # RULE NEGATIF RINGAN
        # ===============================
        if -3 < score < 0:
            return (
                "Terima kasih atas masukannya. "
                "Kami akan berusaha memperbaiki ke depannya."
            )

        # ===============================
        # RULE POSITIF
        # ===============================
        if score >= 3:
            return (
                "Terima kasih atas apresiasinya 🙏 "
                "Kami senang layanan kami bermanfaat."
            )

        return None