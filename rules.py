from experta import KnowledgeEngine, Rule, Fact, MATCH, TEST
from facts import Candidate, Screening, HardSkill, SoftSkill, LiveCoding, Tambahan, Result, BinaryFlag
from mappings import MANDATORY_FACTORS, HARDSKILL_THRESHOLD
from experta import AND, OR


class RecruitmentEngine(KnowledgeEngine):
    """
    Rule-Based Expert System untuk Seleksi Kandidat Fullstack Developer
    Implementasi Dual Process dengan 5 Level Evaluasi sesuai Bab 4
    """

    def __init__(self):
        super().__init__()
        self.results = []
        self.triggered_rules = []
        self.level_status = {}

    def add_result(self, keputusan, alasan, level=None):
        """Simpan hasil keputusan + alasan untuk report"""
        result = {"Keputusan": keputusan, "Alasan": alasan}
        if level:
            result["Level"] = level
        self.results.append(result)

    def check_mandatory_factors(self, answers, posisi):
        """Check mandatory factors untuk hard skill"""
        mandatory = MANDATORY_FACTORS.get(posisi, [])
        for factor in mandatory:
            # Cek apakah factor ini memiliki bobot >= 1
            factor_answer = None
            for q, ans in answers.items():
                if factor.lower().replace("hs", "") in q.lower():
                    factor_answer = ans["kode"]
                    break
            
            if not factor_answer or factor_answer.endswith("-3"):
                return False  # Mandatory factor tidak terpenuhi
        return True

    # ===============================
    # LEVEL 1: SCREENING (R1-R4)
    # ===============================
    
    @Rule(Fact(FS1='FS1-1'), 
          Fact(FS2=MATCH.fs2), 
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r1_screening_sangat_baik(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="sangat_baik"))
        self.declare(BinaryFlag(level1_pass=True))
        msg = f"[R1] Level 1 → Screening=sangat_baik (FS1=FS1-1, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level1"] = "PASS"

    @Rule(Fact(FS1='FS1-2'), 
          Fact(FS2=MATCH.fs2), 
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r2_screening_cukup_baik(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="cukup_baik"))
        self.declare(BinaryFlag(level1_pass=True))
        msg = f"[R2] Level 1 → Screening=cukup_baik (FS1=FS1-2, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level1"] = "PASS"

    @Rule(Fact(FS1='FS1-3'), 
          Fact(FS2=MATCH.fs2), 
          TEST(lambda fs2: fs2 in ['FS2-1', 'FS2-2']))
    def r3_screening_kurang_baik(self, fs2):
        self.declare(Fact(Kualifikasi_Screening="kurang_baik"))
        self.declare(BinaryFlag(level1_pass=True))
        msg = f"[R3] Level 1 → Screening=kurang_baik (FS1=FS1-3, FS2={fs2})"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level1"] = "PASS"

    @Rule(Fact(FS2='FS2-3'))
    def r4_screening_gagal(self):
        self.declare(Fact(Kualifikasi_Screening="gagal"))
        self.declare(BinaryFlag(level1_pass=False))
        self.declare(Fact(Kualifikasi_Global="Kurang Layak"))
        msg = "[R4] Level 1 → Screening=gagal → STOP (Tes tertulis <60%)"
        alasan = "Kandidat tidak memenuhi batas minimum tes tertulis (skor < 60%). Sistem berhenti pada Level 1."
        self.add_result("Kurang Layak", alasan, "Level 1")
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level1"] = "STOP"

    # ===============================
    # LEVEL 2: HARD SKILL + SOFT SKILL (R5-R15)
    # ===============================
    
    # Hard Skill Rules untuk Junior
    @Rule(BinaryFlag(level1_pass=True),
          Fact(posisi='junior'), 
          Fact(bobot_total=MATCH.bt), 
          TEST(lambda bt: 11 <= bt <= 20),
          Fact(mandatory_junior=True))
    def r10_hardskill_junior_memenuhi(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="Memenuhi_Junior"))
        self.declare(BinaryFlag(hardskill_pass=True))
        msg = f"[R10] Level 2 → Hardskill=Memenuhi_Junior (bobot={bt}, mandatory=OK)"
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(BinaryFlag(level1_pass=True),
          Fact(posisi='junior'), 
          Fact(bobot_total=MATCH.bt), 
          TEST(lambda bt: bt >= 21),
          Fact(mandatory_junior=True),
          Fact(mandatory_middle=True))
    def r10_hardskill_junior_upgrade(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="Memenuhi_Junior"))  # Tapi bisa upgrade
        self.declare(BinaryFlag(hardskill_pass=True))
        msg = f"[R10-upgrade] Level 2 → Junior qualified but Middle capable (bobot={bt})"
        print(msg)
        self.triggered_rules.append(msg)

    # Hard Skill Rules untuk Middle
    @Rule(BinaryFlag(level1_pass=True),
          Fact(posisi='middle'), 
          Fact(bobot_total=MATCH.bt), 
          TEST(lambda bt: bt >= 21),
          Fact(mandatory_middle=True))
    def r11_hardskill_middle_memenuhi(self, bt):
        self.declare(Fact(Kualifikasi_Hardskill="Memenuhi_Middle"))
        self.declare(BinaryFlag(hardskill_pass=True))
        msg = f"[R11] Level 2 → Hardskill=Memenuhi_Middle (bobot={bt}, mandatory=OK)"
        print(msg)
        self.triggered_rules.append(msg)

    # Hard Skill Tidak Memenuhi
    @Rule(BinaryFlag(level1_pass=True),
          OR(
              # Junior tidak memenuhi
              AND(Fact(posisi='junior'),
                  OR(Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt < 11),
                     Fact(mandatory_junior=False))),
              # Middle tidak memenuhi  
              AND(Fact(posisi='middle'),
                  OR(Fact(bobot_total=MATCH.bt), TEST(lambda bt: bt < 21),
                     Fact(mandatory_middle=False)))
          ))
    def r12_hardskill_tidak_memenuhi(self):
        self.declare(Fact(Kualifikasi_Hardskill="Tidak_Memenuhi"))
        self.declare(BinaryFlag(hardskill_pass=False))
        self.declare(Fact(Kualifikasi_Global="Kurang Layak"))
        msg = "[R12] Level 2 → Hardskill=Tidak_Memenuhi → STOP"
        alasan = "Kandidat tidak memenuhi threshold minimum hard skill atau mandatory factors untuk posisi yang dilamar. Sistem berhenti pada Level 2."
        self.add_result("Kurang Layak", alasan, "Level 2")
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level2"] = "STOP"

    # Soft Skill Rules
    @Rule(BinaryFlag(hardskill_pass=True),
          Fact(SS1='SS1-1'), 
          Fact(SS2='SS2-1'), 
          Fact(SS3='SS3-1'))
    def r13_softskill_sangat_baik(self):
        self.declare(Fact(Kualifikasi_Softskill="sangat_baik"))
        self.declare(BinaryFlag(level2_pass=True))
        msg = "[R13] Level 2 → Softskill=sangat_baik"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level2"] = "PASS"

    @Rule(BinaryFlag(hardskill_pass=True),
          Fact(SS1='SS1-3'), 
          Fact(SS2='SS2-3'), 
          Fact(SS3='SS3-3'))
    def r14_softskill_kurang_baik(self):
        self.declare(Fact(Kualifikasi_Softskill="kurang_baik"))
        self.declare(BinaryFlag(level2_pass=True))  # Masih bisa lanjut karena domain expert bilang softskill bisa dikembangkan
        msg = "[R14] Level 2 → Softskill=kurang_baik (tapi masih lanjut)"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level2"] = "PASS"

    @Rule(BinaryFlag(hardskill_pass=True),
          Fact(SS1=MATCH.ss1), 
          Fact(SS2=MATCH.ss2), 
          Fact(SS3=MATCH.ss3),
          ~Fact(Kualifikasi_Softskill="sangat_baik"),
          ~Fact(Kualifikasi_Softskill="kurang_baik"))
    def r15_softskill_cukup_baik(self, ss1, ss2, ss3):
        self.declare(Fact(Kualifikasi_Softskill="cukup_baik"))
        self.declare(BinaryFlag(level2_pass=True))
        msg = f"[R15] Level 2 → Softskill=cukup_baik (kombinasi {ss1},{ss2},{ss3})"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level2"] = "PASS"

    # ===============================
    # LEVEL 3: LIVE CODING (R16-R18)
    # ===============================
    
    @Rule(BinaryFlag(level2_pass=True),
          Fact(LC1='LC1-1'), 
          Fact(LC2='LC2-1'), 
          Fact(LC3='LC3-1'),
          salience=10)
    def r16_livecoding_sangat_baik(self):
        self.declare(Fact(Kualifikasi_Livecoding="sangat_baik"))
        self.declare(BinaryFlag(level3_pass=True))
        msg = "[R16] Level 3 → LiveCoding=sangat_baik"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level3"] = "PASS"

    # Kombinasi kurang_baik berdasarkan Tabel 4.20 (yang FALSE)
    @Rule(BinaryFlag(level2_pass=True),
          OR(
              # Efisiensi kode kurang_baik → otomatis kurang_baik
              Fact(LC3='LC3-3'),
              # Atau kombinasi pemahaman + problem solving kurang tapi efisiensi baik/cukup
              AND(Fact(LC1='LC1-3'), Fact(LC2='LC2-3'), 
                  Fact(LC3=MATCH.lc3), TEST(lambda lc3: lc3 in ['LC3-1', 'LC3-2']))
          ),
          salience=9)
        #   ~Fact(Kualifikasi_Livecoding="sangat_baik"),
        #   ~Fact(Kualifikasi_Livecoding="cukup_baik"))
    def r18_livecoding_kurang_baik(self):
        self.declare(Fact(Kualifikasi_Livecoding="kurang_baik"))
        self.declare(BinaryFlag(level3_pass=False))
        self.declare(Fact(Kualifikasi_Global="Kurang Layak"))
        msg = "[R18] Level 3 → LiveCoding=kurang_baik → STOP"
        alasan = "Kandidat tidak menunjukkan kemampuan coding yang memadai dalam sesi live coding. Sistem berhenti pada Level 3."
        self.add_result("Kurang Layak", alasan, "Level 3")
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level3"] = "STOP"

    # Kombinasi untuk cukup_baik berdasarkan Tabel 4.20
    @Rule(BinaryFlag(level2_pass=True),
          ~Fact(Kualifikasi_Livecoding="sangat_baik"),
          ~Fact(Kualifikasi_Livecoding="kurang_baik"))
    def r17_livecoding_cukup_baik(self):
        self.declare(Fact(Kualifikasi_Livecoding="cukup_baik"))
        self.declare(BinaryFlag(level3_pass=True))
        msg = "[R17] Level 3 → LiveCoding=cukup_baik"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level3"] = "PASS"


    # ===============================
    # LEVEL 4: NILAI TAMBAHAN (R19-R21)
    # ===============================
    
    @Rule(BinaryFlag(level3_pass=True),
          Fact(FT1='FT1-1'),
          Fact(FT2='FT2-1'), 
          Fact(FT3='FT3-1'),
          Fact(FT4='FT4-1'))
    def r19_tambahan_bonus_tinggi(self):
        self.declare(Fact(Kualifikasi_Tambahan="bonus_tinggi"))
        self.declare(BinaryFlag(level4_pass=True))
        msg = "[R19] Level 4 → Tambahan=bonus_tinggi"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level4"] = "PASS"

    @Rule(BinaryFlag(level3_pass=True),
          ~Fact(Kualifikasi_Tambahan="bonus_tinggi"),
          ~Fact(Kualifikasi_Tambahan="bonus_kosong"))
    def r20_tambahan_bonus_sedang(self):
        self.declare(Fact(Kualifikasi_Tambahan="bonus_sedang"))
        self.declare(BinaryFlag(level4_pass=True))
        msg = "[R20] Level 4 → Tambahan=bonus_sedang"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level4"] = "PASS"

    @Rule(BinaryFlag(level3_pass=True),
          Fact(FT1='FT1-2'),
          Fact(FT2='FT2-2'),
          Fact(FT3='FT3-2'),
          Fact(FT4='FT4-2'))
    def r21_tambahan_bonus_kosong(self):
        self.declare(Fact(Kualifikasi_Tambahan="bonus_kosong"))
        self.declare(BinaryFlag(level4_pass=True))
        msg = "[R21] Level 4 → Tambahan=bonus_kosong"
        print(msg)
        self.triggered_rules.append(msg)
        self.level_status["Level4"] = "PASS"

    # ===============================
    # LEVEL 5: KEPUTUSAN AKHIR (R22-R31)
    # ===============================
    
    # R22 - Layak (screening baik + hardskill bagus + livecoding sangat baik + softskill bagus/cukup)
    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening="sangat_baik"),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]))
    def r22_global_layak(self, hs, ss):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        msg = f"[R22] Level 5 → Global=Layak"
        alasan = "Kandidat lolos screening dengan sangat baik, memiliki hardskill yang memenuhi, performa live coding sangat baik, dan softskill memadai."
        self.add_result("Layak", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    # R23 - Layak dengan bonus tinggi kompensasi
    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan="bonus_tinggi"))
    def r23_global_layak_bonus_tinggi(self, sc, hs, ss):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        msg = f"[R23] Level 5 → Global=Layak (bonus tinggi kompensasi)"
        alasan = "Meskipun screening bervariasi, kandidat menonjol dengan live coding sangat baik, softskill positif, dan memiliki poin tambahan tinggi."
        self.add_result("Layak", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    # R24 - Layak dengan softskill sangat baik kompensasi
    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening="sangat_baik"),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill="sangat_baik"),
          Fact(Kualifikasi_Tambahan=MATCH.tb), TEST(lambda tb: tb in ["bonus_tinggi", "bonus_sedang"]))
    def r24_global_layak_softskill_kompensasi(self, hs, tb):
        self.declare(Fact(Kualifikasi_Global="Layak"))
        msg = f"[R24] Level 5 → Global=Layak (softskill sangat baik + bonus)"
        alasan = "Kandidat memiliki dasar kuat di screening, hardskill memenuhi, live coding cukup baik, softskill sangat baik, serta dukungan poin tambahan."
        self.add_result("Layak", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    # R25-R30 - Layak Dipertimbangkan (berbagai kombinasi)
    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Tambahan=MATCH.tb), TEST(lambda tb: tb in ["bonus_tinggi", "bonus_sedang"]),
          ~Fact(Kualifikasi_Global="Layak"))
    def r25_global_layak_dipertimbangkan_1(self, sc, hs, ss, tb):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        msg = f"[R25] Level 5 → Global=Layak Dipertimbangkan (cukup baik + bonus)"
        alasan = "Kandidat menunjukkan hardskill memenuhi, live coding cukup baik, softskill positif, dan mendapat nilai tambah. Perlu dipertimbangkan lebih lanjut."
        self.add_result("Layak Dipertimbangkan", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="sangat_baik"),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik"]),
          ~Fact(Kualifikasi_Global="Layak"))
    def r26_global_layak_dipertimbangkan_2(self, sc, hs, ss):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        msg = f"[R26] Level 5 → Global=Layak Dipertimbangkan (live coding excellent)"
        alasan = "Live coding sangat baik menjadi keunggulan, hardskill memenuhi, dan softskill positif mendukung kandidat."
        self.add_result("Layak Dipertimbangkan", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding="cukup_baik"),
          Fact(Kualifikasi_Softskill="cukup_baik"),
          ~Fact(Kualifikasi_Global="Layak"))
    def r27_global_layak_dipertimbangkan_3(self, sc, hs):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        msg = f"[R27] Level 5 → Global=Layak Dipertimbangkan (semua cukup baik)"
        alasan = "Kandidat cukup baik dalam semua aspek (screening, hardskill, live coding, softskill). Direkomendasikan untuk dipertimbangkan."
        self.add_result("Layak Dipertimbangkan", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc), TEST(lambda sc: sc in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Hardskill=MATCH.hs), TEST(lambda hs: "Memenuhi" in hs),
          Fact(Kualifikasi_Livecoding=MATCH.lc), TEST(lambda lc: lc in ["sangat_baik", "cukup_baik"]),
          Fact(Kualifikasi_Softskill=MATCH.ss), TEST(lambda ss: ss in ["sangat_baik", "cukup_baik", "kurang_baik"]),
          Fact(Kualifikasi_Tambahan="bonus_tinggi"),
          ~Fact(Kualifikasi_Global="Layak"))
    def r28_global_layak_dipertimbangkan_4(self, sc, hs, lc, ss):
        self.declare(Fact(Kualifikasi_Global="Layak Dipertimbangkan"))
        msg = f"[R28] Level 5 → Global=Layak Dipertimbangkan (bonus tinggi kompensasi)"
        alasan = "Screening/hardskill/live coding bervariasi, tetapi poin tambahan tinggi mendukung kandidat untuk dipertimbangkan."
        self.add_result("Layak Dipertimbangkan", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)

    # R31 - Fallback Kurang Layak
    @Rule(BinaryFlag(level4_pass=True),
          Fact(Kualifikasi_Screening=MATCH.sc),
          Fact(Kualifikasi_Hardskill=MATCH.hs), 
          Fact(Kualifikasi_Livecoding=MATCH.lc),
          Fact(Kualifikasi_Softskill=MATCH.ss),
          ~Fact(Kualifikasi_Global=MATCH.kg),
          salience=-10)
    def r31_global_fallback_kurang_layak(self, sc, hs, lc, ss):
        self.declare(Fact(Kualifikasi_Global="Kurang Layak"))
        msg = "[R31] Level 5 → Global=Kurang Layak (fallback)"
        alasan = "Kandidat tidak memenuhi kriteria untuk kategori Layak maupun Layak Dipertimbangkan berdasarkan kombinasi hasil evaluasi."
        self.add_result("Kurang Layak", alasan, "Level 5")
        print(msg)
        self.triggered_rules.append(msg)