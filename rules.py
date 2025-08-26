from experta import KnowledgeEngine, Rule, Fact, MATCH, TEST
from facts import Candidate, Screening, HardSkill, SoftSkill, LiveCoding, Tambahan, Result


class RecruitmentEngine(KnowledgeEngine):
    """
    Rule-Based Expert System untuk Seleksi Kandidat Fullstack Developer
    Berdasarkan competency assessment (R1–R31) + explainable logs
    """

    def __init__(self):
        super().__init__()
        self.results = []
        self.triggered_rules = []

    def add_result(self, keputusan, alasan):
        """Simpan hasil keputusan + alasan untuk report"""
        self.results.append({"Keputusan": keputusan, "Alasan": alasan})

    # ===============================
    # R1–R4 : Screening
    # ===============================
    # R1
    @Rule(Fact(FS1='FS1-1'), Fact(FS2=MATCH.fs2), TEST(lambda fs2: fs2 in ['FS2-1','FS2-2']))
    def r1(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="baik"))
        msg = f"[R1] triggered → Screening=baik (FS1=FS1-1, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)

    # R2
    @Rule(Fact(FS1='FS1-2'), Fact(FS2=MATCH.fs2), TEST(lambda fs2: fs2 in ['FS2-1','FS2-2']))
    def r2(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="cukup_baik"))
        msg = f"[R2] triggered → Screening=cukup_baik (FS1=FS1-2, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)

    # R3
    @Rule(Fact(FS1='FS1-3'), Fact(FS2=MATCH.fs2), TEST(lambda fs2: fs2 in ['FS2-1','FS2-2']))
    def r3(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="kurang_baik"))
        msg = f"[R3] triggered → Screening=kurang_baik (FS1=FS1-3, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)

    # R4
    @Rule(Fact(FS2='FS2-3'))
    def r4(self):
        self.declare(Fact(Kualifikasi_Screening="tidak_lolos"))
        msg = "[R4] triggered → Screening=tidak_lolos (Tes tertulis <60%)"
        print(msg)
        self.triggered_rules.append(msg)

    # ========== R5 – R12 : Hard Skill ==========
    # Junior
    @Rule(Fact(posisi='junior'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt > 15))
    def r7(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="bagus"))
        msg = f"[R7] triggered → Hardskill=bagus (Junior, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(posisi='junior'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: 11 <= bt <= 15))
    def r8(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="cukup"))
        msg = f"[R8] triggered → Hardskill=cukup (Junior, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(posisi='junior'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt < 11))
    def r9(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="kurang"))
        msg = f"[R9] triggered → Hardskill=kurang (Junior, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    # Middle
    @Rule(Fact(posisi='middle'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt > 27))
    def r10(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="bagus"))
        msg = f"[R10] triggered → Hardskill=bagus (Middle, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(posisi='middle'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: 22 <= bt <= 27))
    def r11(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="cukup"))
        msg = f"[R11] triggered → Hardskill=cukup (Middle, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(posisi='middle'), Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt < 22))
    def r12(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="kurang"))
        msg = f"[R12] triggered → Hardskill=kurang (Middle, bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    # ===============================
    # R13–R15 : SoftSkill
    # ===============================

    # R13: semua sangat baik
    @Rule(Fact(SS1='SS1-1'), Fact(SS2='SS2-1'), Fact(SS3='SS3-1'))
    def r13(self):
        self.declare(Fact(Kualifikasi_Softskill="sangat_baik"))
        msg = "[R13] triggered → Softskill=sangat_baik"
        print(msg)
        self.triggered_rules.append(msg)

    # R14: semua buruk
    @Rule(Fact(SS1='SS1-3'), Fact(SS2='SS2-3'), Fact(SS3='SS3-3'))
    def r14(self):
        self.declare(Fact(Kualifikasi_Softskill="kurang_baik"))
        msg = "[R14] triggered → Softskill=kurang_baik"
        print(msg)
        self.triggered_rules.append(msg)

    # R15: kombinasi lain → cukup_baik (asal FA10 & FA11 tidak terpenuhi)
    @Rule(Fact(SS1=MATCH.ss1), Fact(SS2=MATCH.ss2), Fact(SS3=MATCH.ss3),
          Fact(FA10=False), Fact(FA11=False),
          TEST(lambda ss1, ss2, ss3: not (ss1 == 'SS1-1' and ss2 == 'SS2-1' and ss3 == 'SS3-1')),
          TEST(lambda ss1, ss2, ss3: not (ss1 == 'SS1-3' and ss2 == 'SS2-3' and ss3 == 'SS3-3')))
    def r15(self, ss1, ss2, ss3):
        self.declare(Fact(Kualifikasi_Softskill="cukup_baik"))
        msg = f"[R15] triggered → Softskill=cukup_baik (SS1={ss1}, SS2={ss2}, SS3={ss3})"
        print(msg)
        self.triggered_rules.append(msg)

    # ===============================
    # R16–R18 : LiveCoding
    # ===============================

    # R16: semua sangat baik → sangat_baik
    @Rule(Fact(LC1='LC1-1'), Fact(LC2='LC2-1'), Fact(LC3='LC3-1'))
    def r16(self):
        self.declare(Fact(Kualifikasi_Livecoding="sangat_baik"))
        self.declare(Fact(FA13=True))
        msg = "[R16] triggered → LiveCoding=sangat_baik (LC1=LC1-1, LC2=LC2-1, LC3=LC3-1)"
        print(msg)
        self.triggered_rules.append(msg)

    # R17: kombinasi → cukup_baik
    # Kombinasi 1
    @Rule(Fact(LC1='LC1-1'), Fact(LC2='LC2-1'), Fact(LC3='LC3-2'))
    def r17a(self):
        self.declare(Fact(Kualifikasi_Livecoding="cukup_baik"))
        self.declare(Fact(FA14=True))
        msg = "[R17a] triggered → LiveCoding=cukup_baik (LC1=LC1-1, LC2=LC2-1, LC3=LC3-2)"
        print(msg)
        self.triggered_rules.append(msg)

    # Kombinasi 2
    @Rule(Fact(LC1='LC1-1'), Fact(LC2='LC2-2'), Fact(LC3='LC3-1'))
    def r17b(self):
        self.declare(Fact(Kualifikasi_Livecoding="cukup_baik"))
        self.declare(Fact(FA14=True))
        msg = "[R17b] triggered → LiveCoding=cukup_baik (LC1=LC1-1, LC2=LC2-2, LC3=LC3-1)"
        print(msg)
        self.triggered_rules.append(msg)

    # Kombinasi 3
    @Rule(Fact(LC1='LC1-1'), Fact(LC2='LC2-2'), Fact(LC3='LC3-2'))
    def r17c(self):
        self.declare(Fact(Kualifikasi_Livecoding="cukup_baik"))
        self.declare(Fact(FA14=True))
        msg = "[R17c] triggered → LiveCoding=cukup_baik (LC1=LC1-1, LC2=LC2-2, LC3=LC3-2)"
        print(msg)
        self.triggered_rules.append(msg)

    # R18: fallback → tidak_layak
    @Rule(Fact(LC1=MATCH.lc1), Fact(LC2=MATCH.lc2), Fact(LC3=MATCH.lc3),
          Fact(FA13=False), Fact(FA14=False))
    def r18(self, lc1, lc2, lc3):
        self.declare(Fact(Kualifikasi_Livecoding="tidak_layak"))
        self.declare(Fact(FA15=True))
        msg = f"[R18] triggered → LiveCoding=tidak_layak (LC1={lc1}, LC2={lc2}, LC3={lc3})"
        print(msg)
        self.triggered_rules.append(msg)

    # ===============================
    # R19–R21 : Tambahan
    # ===============================

    # R19 → poinplus_tinggi
    @Rule(Fact(FT1='FT1-1'),
          Fact(FT2=MATCH.ft2), TEST(lambda ft2: ft2 in ['FT2-1', 'FT2-2']),
          Fact(FT3='FT3-1'),
          Fact(FT4=MATCH.ft4), TEST(lambda ft4: ft4 in ['FT4-1', 'FT4-2']))
    def r19(self, ft2, ft4):
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_tinggi"))
        self.declare(Fact(FA16=True))
        msg = f"[R19] triggered → Tambahan=poinplus_tinggi (FT1=FT1-1, FT2={ft2}, FT3=FT3-1, FT4={ft4})"
        print(msg)
        self.triggered_rules.append(msg)

    # R20 → poinplus_cukup
    @Rule(
        Fact(FT1='FT1-1'),
        Fact(FT2=MATCH.ft2), TEST(lambda ft2: ft2 in ['FT2-1', 'FT2-2']),
        Fact(FT3='FT3-2'),
        Fact(FT4=MATCH.ft4), TEST(lambda ft4: ft4 in ['FT4-1', 'FT4-2'])
    )
    def r20a(self, ft2, ft4):
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_cukup"))
        self.declare(Fact(FA17=True))
        msg = f"[R20a] triggered → Tambahan=poinplus_cukup (FT1=FT1-1, FT2={ft2}, FT3=FT3-2, FT4={ft4})"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(
        Fact(FT1='FT1-2'),
        Fact(FT2=MATCH.ft2), TEST(lambda ft2: ft2 in ['FT2-1', 'FT2-2']),
        Fact(FT3='FT3-1'),
        Fact(FT4=MATCH.ft4), TEST(lambda ft4: ft4 in ['FT4-1', 'FT4-2'])
    )
    def r20b(self, ft2, ft4):
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_cukup"))
        self.declare(Fact(FA17=True))
        msg = f"[R20b] triggered → Tambahan=poinplus_cukup (FT1=FT1-2, FT2={ft2}, FT3=FT3-1, FT4={ft4})"
        print(msg)
        self.triggered_rules.append(msg)

    # R21 → fallback → poinplus_kosong
    @Rule(Fact(FA16=False), Fact(FA17=False))
    def r21(self):
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_kosong"))
        self.declare(Fact(FA18=True))
        msg = "[R21] triggered → Tambahan=poinplus_kosong (fallback, FA16=False, FA17=False)"
        print(msg)
        self.triggered_rules.append(msg)

    # ===============================
    # R22–R31 : Kualifikasi Global
    # ===============================

    # R22
    @Rule(Fact(Kualifikasi_Screening="baik"),
          Fact(Kualifikasi_Hardskill="bagus"),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]))
    def r22(self, ss):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        msg = f"[R22] triggered → Global=Layak"
        alasan = "Kandidat lolos screening dengan baik, memiliki hardskill yang sangat kuat, performa live coding sangat baik, dan softskill memadai."
        self.add_result("Layak", alasan)
        print(msg)
        self.triggered_rules.append(msg)

    # R23
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: hs in ["bagus", "cukup"]),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan="poinplus_tinggi"))
    def r23(self, sc, hs, ss):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        alasan = "Meskipun screening dan hardskill bervariasi, kandidat menonjol dengan live coding sangat baik, softskill positif, dan memiliki poin tambahan tinggi."
        self.add_result("Layak", alasan)
        msg = f"[R23] triggered → Global=Layak"
        print(msg)
        self.triggered_rules.append(msg)

    # R24
    @Rule(Fact(Kualifikasi_Screening="baik"),
          Fact(Kualifikasi_Hardskill="bagus"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill="sangat_baik"),
          Fact(Kualifikasi_Tambahan=MATCH.tb), TEST(lambda tb: tb in ["poinplus_tinggi", "poinplus_cukup"]))
    def r24(self, tb):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        alasan = "Kandidat memiliki dasar kuat di screening, hardskill bagus, live coding cukup baik, softskill sangat baik, serta dukungan poin tambahan."
        self.add_result("Layak", alasan)
        msg = f"[R24] triggered → Global=Layak"
        print(msg)
        self.triggered_rules.append(msg)

    # R25
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill="cukup"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan=MATCH.tb), TEST(lambda tb: tb in ["poinplus_tinggi", "poinplus_cukup"]))
    def r25(self, sc, ss, tb):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Kandidat menunjukkan hardskill cukup, live coding cukup baik, softskill positif, dan mendapat nilai tambah. Perlu dipertimbangkan lebih lanjut."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = f"[R25] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R26
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill="bagus"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]))
    def r26(self, sc, ss):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Hardskill bagus dan live coding cukup baik didukung softskill positif, namun belum memenuhi kriteria Layak penuh."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = f"[R26] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R27
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: hs in ["bagus", "cukup"]),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]))
    def r27(self, sc, hs, ss):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Live coding sangat baik menjadi keunggulan, meskipun screening/hardskill bervariasi. Softskill positif mendukung kandidat."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = f"[R27] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R28
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik"]),
          Fact(Kualifikasi_Hardskill="cukup"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill="cukup_baik"))
    def r28(self, sc):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Kandidat cukup baik dalam semua aspek (screening, hardskill, live coding, softskill). Direkomendasikan untuk dipertimbangkan."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = f"[R28] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R29 - dipecah menjadi beberapa rule yang lebih spesifik
    @Rule(Fact(Kualifikasi_Screening="baik"),
          Fact(Kualifikasi_Hardskill="cukup"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan=MATCH.ft), TEST(lambda ft: ft in ["poinplus_tinggi", "poinplus_cukup"]))
    def r29a(self, ss, ft):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Screening baik, hardskill cukup, live coding cukup baik, softskill memadai, serta mendapat poin tambahan."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = "[R29a] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(Kualifikasi_Screening="cukup_baik"),
          Fact(Kualifikasi_Hardskill="cukup"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan=MATCH.ft), TEST(lambda ft: ft in ["poinplus_tinggi", "poinplus_cukup"]))
    def r29b(self, ss, ft):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Screening cukup baik, hardskill cukup, live coding cukup baik, softskill memadai, serta mendapat poin tambahan."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = "[R29b] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(Fact(Kualifikasi_Screening="kurang_baik"),
          Fact(Kualifikasi_Hardskill="cukup"),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan=MATCH.ft), TEST(lambda ft: ft in ["poinplus_tinggi", "poinplus_cukup"]))
    def r29c(self, ss, ft):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Screening kurang baik, tetapi hardskill cukup, live coding cukup baik, softskill memadai, serta didukung poin tambahan."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = "[R29c] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R30
    @Rule(Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: hs in ["bagus", "cukup"]),
          Fact(Kualifikasi_Livecoding=MATCH.lc), TEST(lambda lc: lc in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Tambahan="poinplus_tinggi"))
    def r30(self, sc, hs, lc, ss):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        alasan = "Screening/hardskill/live coding bervariasi, tetapi poin tambahan tinggi mendukung kandidat untuk dipertimbangkan."
        self.add_result("Layak Dipertimbangkan", alasan)
        msg = f"[R30] triggered → Global=Layak Dipertimbangkan"
        print(msg)
        self.triggered_rules.append(msg)

    # R31 Fallback: jika belum ada keputusan global lain
    @Rule(
        Fact(Kualifikasi_Screening=MATCH.sc),
        Fact(Kualifikasi_Hardskill=MATCH.hs), 
        Fact(Kualifikasi_Livecoding=MATCH.lc),
        Fact(Kualifikasi_Softskill=MATCH.ss),
        ~Fact(Kualifikasi_Global=MATCH.kg),
        salience=-10
    )
    def r31(self, sc, hs, lc, ss):
        self.declare(Fact(Kualifikasi_Global="Kurang Layak"))
        alasan = "Kandidat tidak memenuhi kriteria untuk kategori Layak maupun Layak Dipertimbangkan."
        self.add_result("Kurang Layak", alasan)
        msg = "[R31] triggered → Global=Kurang Layak (fallback)"
        print(msg)
        self.triggered_rules.append(msg)