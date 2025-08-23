from experta import KnowledgeEngine, Rule, Fact, MATCH, TEST
from facts import Candidate, Screening, HardSkill, SoftSkill, LiveCoding, Tambahan, Result


class RecruitmentEngine(KnowledgeEngine):
    """
    Rule-Based Expert System untuk Seleksi Kandidat Fullstack Developer
    Berdasarkan competency assessment (R1–R36) + explainable logs
    """

    # ========== R1 – R4 : Screening ==========
    @Rule(Screening(FS1='FS1-1', FS2=MATCH.fs2),
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r1(self, fs2):
        print("[R1] Screening = baik")
        self.declare(Fact(Kualifikasi_Screening="baik"))

    @Rule(Screening(FS1='FS1-2', FS2=MATCH.fs2),
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r2(self, fs2):
        print("[R2] Screening = cukup_baik")
        self.declare(Fact(Kualifikasi_Screening="cukup_baik"))

    @Rule(Screening(FS1='FS1-3', FS2=MATCH.fs2),
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r3(self, fs2):
        print("[R3] Screening = kurang_baik")
        self.declare(Fact(Kualifikasi_Screening="kurang_baik"))

    @Rule(Screening(FS2='FS2-3'))
    def r4(self):
        print("[R4] Screening = tidak_lolos")
        self.declare(Fact(Kualifikasi_Screening="tidak_lolos"))

    # ========== R5 – R6 : Skor Minimum ==========
    @Rule(Candidate(posisi='junior'))
    def r5(self):
        print("[R5] Skor_min = 11 (junior)")
        self.declare(Fact(Skor_min=11))

    @Rule(Candidate(posisi='middle'))
    def r6(self):
        print("[R6] Skor_min = 27 (middle)")
        self.declare(Fact(Skor_min=27))

    # ========== R7 – R12 : Hard Skill ==========
    @Rule(Candidate(posisi='junior'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: bt > 15))
    def r7(self, bt):
        print(f"[R7] Junior Hard Skill = bagus (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="bagus"))

    @Rule(Candidate(posisi='junior'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: 11 <= bt <= 15))
    def r8(self, bt):
        print(f"[R8] Junior Hard Skill = cukup (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="cukup"))

    @Rule(Candidate(posisi='junior'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: bt < 11))
    def r9(self, bt):
        print(f"[R9] Junior Hard Skill = kurang (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="kurang"))

    @Rule(Candidate(posisi='middle'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: bt >= 27))
    def r10(self, bt):
        print(f"[R10] Middle Hard Skill = bagus (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="bagus"))

    @Rule(Candidate(posisi='middle'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: 20 <= bt < 27))
    def r11(self, bt):
        print(f"[R11] Middle Hard Skill = cukup (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="cukup"))

    @Rule(Candidate(posisi='middle'), Fact(bobot_total=MATCH.bt),
          TEST(lambda bt: bt < 20))
    def r12(self, bt):
        print(f"[R12] Middle Hard Skill = kurang (bobot={bt})")
        self.declare(Fact(Kualifikasi_Hard_Skill="kurang"))

    # ========== R13 – R18 : Soft Skill ==========
    @Rule(SoftSkill(SS1='SS1-3', SS2='SS2-1', SS3='SS3-1'))
    def r13(self):
        print("[R13] SoftSkill = sangat_baik")
        self.declare(Fact(Kualifikasi_SoftSkill="sangat_baik"))

    @Rule(SoftSkill(SS1='SS1-3', SS2='SS2-2', SS3='SS3-1'))
    def r14(self):
        print("[R14] SoftSkill = cukup_baik")
        self.declare(Fact(Kualifikasi_SoftSkill="cukup_baik"))

    @Rule(SoftSkill(SS1='SS1-3', SS2='SS2-1', SS3=MATCH.ss3),
          TEST(lambda ss3: ss3 in ['SS3-2', 'SS3-3']))
    def r15(self, ss3):
        print(f"[R15] SoftSkill = cukup_baik (SS3={ss3})")
        self.declare(Fact(Kualifikasi_SoftSkill="cukup_baik"))

    @Rule(SoftSkill(SS1='SS1-1'))
    def r16(self):
        print("[R16] SoftSkill = sangat_baik")
        self.declare(Fact(Kualifikasi_SoftSkill="sangat_baik"))

    @Rule(SoftSkill(SS1='SS1-2'))
    def r17(self):
        print("[R17] SoftSkill = cukup_baik")
        self.declare(Fact(Kualifikasi_SoftSkill="cukup_baik"))

    @Rule(SoftSkill(SS1=MATCH.ss1),
          TEST(lambda ss1: ss1 not in ['SS1-1','SS1-2','SS1-3']))
    def r18(self, ss1):
        print(f"[R18] SoftSkill = kurang_baik (SS1={ss1})")
        self.declare(Fact(Kualifikasi_SoftSkill="kurang_baik"))

    # ========== R19 – R25 : Live Coding ==========
    @Rule(LiveCoding(LC1='LC1-1', LC2='LC2-1', LC3='LC3-1'))
    def r19(self):
        print("[R19] LiveCoding = sangat_baik")
        self.declare(Fact(Kualifikasi_LiveCoding="sangat_baik"))

    @Rule(LiveCoding(LC1='LC1-1', LC2='LC2-1', LC3='LC3-2'))
    def r20(self):
        print("[R20] LiveCoding = cukup_baik")
        self.declare(Fact(Kualifikasi_LiveCoding="cukup_baik"))

    @Rule(LiveCoding(LC1='LC1-2', LC2='LC2-1', LC3='LC3-1'))
    def r21(self):
        print("[R21] LiveCoding = kurang_baik")
        self.declare(Fact(Kualifikasi_LiveCoding="kurang_baik"))

    @Rule(LiveCoding(LC1='LC1-1', LC2='LC2-2', LC3=MATCH.lc3),
          TEST(lambda lc3: lc3 in ['LC3-1','LC3-2']))
    def r22(self, lc3):
        print(f"[R22] LiveCoding = kurang_baik (LC3={lc3})")
        self.declare(Fact(Kualifikasi_LiveCoding="kurang_baik"))

    @Rule(LiveCoding(LC1=MATCH.lc1, LC2=MATCH.lc2, LC3='LC3-3'),
          TEST(lambda lc1, lc2: lc1 in ['LC1-1','LC1-2'] and lc2 in ['LC2-1','LC2-2']))
    def r23(self, lc1, lc2):
        print(f"[R23] LiveCoding = tidak_layak (LC1={lc1},LC2={lc2},LC3=LC3-3)")
        self.declare(Fact(Kualifikasi_LiveCoding="tidak_layak"))

    @Rule(LiveCoding(LC1='LC1-2', LC2='LC2-2'))
    def r24(self):
        print("[R24] LiveCoding = tidak_layak")
        self.declare(Fact(Kualifikasi_LiveCoding="tidak_layak"))

    @Rule(LiveCoding(LC1=MATCH.l1, LC2=MATCH.l2, LC3=MATCH.l3))
    def r25(self, l1, l2, l3):
        print(f"[R25] LiveCoding default = tidak_layak ({l1},{l2},{l3})")
        self.declare(Fact(Kualifikasi_LiveCoding="tidak_layak"))

    # ========== R26 – R28 : Tambahan ==========
    @Rule(Tambahan(FT1='FT1-1', FT2=MATCH.ft2, FT3='FT3-1', FT4=MATCH.ft4),
          TEST(lambda ft2: ft2 in ['FT2-1','FT2-2']),
          TEST(lambda ft4: ft4 in ['FT4-1','FT4-2']))
    def r26(self, ft2, ft4):
        print("[R26] Tambahan = poinplus_tinggi")
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_tinggi"))

    @Rule(Tambahan(FT1=MATCH.ft1, FT2=MATCH.ft2, FT3=MATCH.ft3, FT4=MATCH.ft4),
          TEST(lambda ft1: ft1 in ['FT1-1','FT1-2']),
          TEST(lambda ft2: ft2 in ['FT2-1','FT2-2']),
          TEST(lambda ft3: ft3 in ['FT3-1','FT3-2']),
          TEST(lambda ft4: ft4 in ['FT4-1','FT4-2']))
    def r27(self, ft1, ft2, ft3, ft4):
        print("[R27] Tambahan = poinplus_cukup")
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_cukup"))

    @Rule(Tambahan(FT1='FT1-2', FT2=MATCH.ft2, FT3='FT3-2', FT4=MATCH.ft4),
          TEST(lambda ft2: ft2 in ['FT2-1','FT2-2']),
          TEST(lambda ft4: ft4 in ['FT4-1','FT4-2']))
    def r28(self, ft2, ft4):
        print("[R28] Tambahan = poinplus_kosong")
        self.declare(Fact(Kualifikasi_Tambahan="poinplus_kosong"))

   # ========== R29 – R36 : Global ==========
    @Rule(Fact(Kualifikasi_Screening=MATCH.ks),
          TEST(lambda ks: ks in ['tidak_lolos','kurang_baik']))
    def r29(self, ks):
        print(f"[R29] Global = Kurang_Layak (screening {ks})")
        result = {"Keputusan": "Kurang_Layak", "Alasan": "Screening gagal"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Hard_Skill='kurang') |
          Fact(Kualifikasi_LiveCoding='kurang_baik') |
          Fact(Kualifikasi_LiveCoding='tidak_layak'))
    def r30(self):
        print("[R30] Global = Kurang_Layak (teknikal lemah)")
        result = {"Keputusan": "Kurang_Layak", "Alasan": "Hard skill/Live coding buruk"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_SoftSkill='kurang_baik'))
    def r31(self):
        print("[R31] Global = Kurang_Layak (softskill buruk)")
        result = {"Keputusan": "Kurang_Layak", "Alasan": "Soft skill buruk"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Hard_Skill='bagus'),
          Fact(Kualifikasi_LiveCoding='sangat_baik'),
          Fact(Kualifikasi_SoftSkill='sangat_baik'),
          Fact(Kualifikasi_Screening='baik'),
          Fact(Kualifikasi_Tambahan='poinplus_tinggi'))
    def r32(self):
        print("[R32] Global = Layak (kombinasi ideal)")
        result = {"Keputusan": "Layak", "Alasan": "Kombinasi ideal"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Hard_Skill='bagus'),
          Fact(Kualifikasi_LiveCoding='sangat_baik'))
    def r33(self):
        print("[R33] Global = Layak (unggul di teknikal utama)")
        result = {"Keputusan": "Layak", "Alasan": "Unggul teknikal"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Screening=MATCH.ks),
          Fact(Kualifikasi_Hard_Skill='bagus'),
          Fact(Kualifikasi_SoftSkill=MATCH.ss),
          Fact(Kualifikasi_LiveCoding=MATCH.lc),
          Fact(Kualifikasi_Tambahan=MATCH.ft),
          TEST(lambda ks: ks in ['baik','cukup_baik']),
          TEST(lambda ss: ss in ['sangat_baik','cukup_baik']),
          TEST(lambda lc: lc in ['sangat_baik','cukup_baik']),
          TEST(lambda ft: ft in ['poinplus_tinggi','poinplus_cukup']))
    def r34(self, ks, ss, lc, ft):
        print("[R34] Global = Layak (memadai semua aspek)")
        result = {"Keputusan": "Layak", "Alasan": "Memadai semua aspek"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Screening=MATCH.ks),
          Fact(Kualifikasi_Hard_Skill='cukup'),
          Fact(Kualifikasi_SoftSkill=MATCH.ss),
          Fact(Kualifikasi_LiveCoding=MATCH.lc),
          Fact(Kualifikasi_Tambahan=MATCH.ft),
          TEST(lambda ks: ks in ['baik','cukup_baik']),
          TEST(lambda ss: ss in ['sangat_baik','cukup_baik']),
          TEST(lambda lc: lc in ['sangat_baik','cukup_baik']),
          TEST(lambda ft: ft in ['poinplus_tinggi','poinplus_cukup']))
    def r35(self, ks, ss, lc, ft):
        print("[R35] Global = Layak Dipertimbangkan (hard skill cukup, aspek lain kuat)")
        result = {"Keputusan": "Layak Dipertimbangkan", "Alasan": "Hard skill cukup, aspek lain menutup"}
        self.declare(Result(**result))
        self.results.append(result)

    @Rule(Fact(Kualifikasi_Screening=MATCH.ks),
          Fact(Kualifikasi_Hard_Skill=MATCH.hs),
          Fact(Kualifikasi_SoftSkill=MATCH.ss),
          Fact(Kualifikasi_LiveCoding=MATCH.lc),
          Fact(Kualifikasi_Tambahan=MATCH.ft))
    def r36(self, ks, hs, ss, lc, ft):
        print("[R36] Global = Kurang_Layak (default fallback)")
        result = {"Keputusan": "Kurang_Layak", "Alasan": "Tidak memenuhi kombinasi aturan"}
        self.declare(Result(**result))
        self.results.append(result)

