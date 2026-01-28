class ReasoningEngine:
    def __init__(self, ainlp):
        self.ainlp = ainlp

    def apply(self, cleaned_text, tokens):
        """
        cleaned_text : hasil clean_text_full
        tokens       : hasil tokenize + stopword removal
        """

        words = set(tokens)

        # ===============================
        # RULE 1 — EMOSI NEGATIF (LEXICON)
        # ===============================
        neg_hits = [w for w in words if w in self.ainlp.lexicon_negative_dict]
        if neg_hits:
            return (
                "Saya menangkap adanya perasaan kurang nyaman. "
                "Terima kasih sudah menyampaikannya, kami akan menindaklanjuti."
            )

        # ===============================
        # RULE 2 — EMOSI POSITIF
        # ===============================
        pos_hits = [w for w in words if w in self.ainlp.lexicon_positive_dict]
        if pos_hits:
            return (
                "Terima kasih atas respon positifnya 🙏 "
                "Kami senang bisa membantu."
            )

        # ===============================
        # RULE 3 — LAPAR + PUASA (LOGIKA)
        # ===============================
        if "lapar" in words and "puasa" in words:
            return (
                "Jika sedang puasa, rasa lapar memang wajar. "
                "Tetap semangat menjalankan puasanya."
            )

        # ===============================
        # RULE 4 — MEDIA VS INDIVIDU
        # ===============================
        if any(media in cleaned_text for media in self.ainlp.news_media):
            return (
                "Informasi ini berasal dari media. "
                "Perlu verifikasi lebih lanjut untuk memastikan kebenarannya."
            )

        # ===============================
        # TIDAK ADA RULE COCOK
        # ===============================
        return None