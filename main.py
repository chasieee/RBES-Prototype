from experta import *
from facts import *
from rules import RecruitmentEngine
from ui import ask_question, collect_candidate_info
from report import generate_report
from mappings import MAPPING, HS_SCORING, MANDATORY_FACTORS
from debug_facts import debug_facts, debug_results

def calculate_hardskill_score(answers):
    """Hitung skor hard skill berdasarkan jawaban"""
    hs_questions = [
        "Hard Skill - Pemrograman", "Hard Skill - Database MySQL", 
        "Hard Skill - Framework", "Hard Skill - Unit Test",
        "Hard Skill - SDLC", "Hard Skill - Design Pattern", 
        "Hard Skill - Microservice", "Hard Skill - Docker", 
        "Hard Skill - CI/CD", "Hard Skill - Cloud", 
        "Hard Skill - Payment Gateway"
    ]
    
    total_score = 0
    factor_scores = {}
    
    for i, q in enumerate(hs_questions, 1):
        if q in answers:
            kode = answers[q]["kode"]
            score = HS_SCORING.get(kode, 0)
            total_score += score
            factor_scores[f"HS{i}"] = {"kode": kode, "score": score}
    
    return total_score, factor_scores

def check_mandatory_factors(factor_scores, posisi):
    """Cek apakah mandatory factors terpenuhi"""
    mandatory = MANDATORY_FACTORS.get(posisi, [])
    mandatory_junior = True
    mandatory_middle = True
    
    # Check junior mandatory factors
    for factor in MANDATORY_FACTORS["junior"]:
        if factor in factor_scores:
            if factor_scores[factor]["score"] < 1:  # Bobot harus >= 1
                mandatory_junior = False
                break
    
    # Check middle mandatory factors  
    for factor in MANDATORY_FACTORS["middle"]:
        if factor in factor_scores:
            if factor_scores[factor]["score"] < 1:  # Bobot harus >= 1
                mandatory_middle = False
                break
    
    return mandatory_junior, mandatory_middle

def main():
    print("=== RULE-BASED EXPERT SYSTEM ===")
    print("=== SELEKSI KANDIDAT FULLSTACK DEVELOPER ===\n")
    
    # 1. Input kandidat
    info = collect_candidate_info()

    # 2. Pertanyaan sesuai dengan tabel fakta dari Bab 4
    questions = {
        # === Screening (Tabel 4.8) ===
        "Screening - Personality": {
            "A": {"text": MAPPING["FS1-1"], "kode": "FS1-1"},
            "B": {"text": MAPPING["FS1-2"], "kode": "FS1-2"},
            "C": {"text": MAPPING["FS1-3"], "kode": "FS1-3"},
        },
        "Screening - Tes Tertulis": {
            "A": {"text": MAPPING["FS2-1"], "kode": "FS2-1"},
            "B": {"text": MAPPING["FS2-2"], "kode": "FS2-2"},
            "C": {"text": MAPPING["FS2-3"], "kode": "FS2-3"},
        },

        # === Hard Skills (Tabel 4.9) ===
        "Hard Skill - Pemrograman": {
            "A": {"text": MAPPING["HS1-1"], "kode": "HS1-1"},
            "B": {"text": MAPPING["HS1-2"], "kode": "HS1-2"},
            "C": {"text": MAPPING["HS1-3"], "kode": "HS1-3"},
        },
        "Hard Skill - Database MySQL": {
            "A": {"text": MAPPING["HS2-1"], "kode": "HS2-1"},
            "B": {"text": MAPPING["HS2-2"], "kode": "HS2-2"},
            "C": {"text": MAPPING["HS2-3"], "kode": "HS2-3"},
        },
        "Hard Skill - Framework": {
            "A": {"text": MAPPING["HS3-1"], "kode": "HS3-1"},
            "B": {"text": MAPPING["HS3-2"], "kode": "HS3-2"},
            "C": {"text": MAPPING["HS3-3"], "kode": "HS3-3"},
        },
        "Hard Skill - Unit Test": {
            "A": {"text": MAPPING["HS4-1"], "kode": "HS4-1"},
            "B": {"text": MAPPING["HS4-2"], "kode": "HS4-2"},
            "C": {"text": MAPPING["HS4-3"], "kode": "HS4-3"},
        },
        "Hard Skill - SDLC": {
            "A": {"text": MAPPING["HS5-1"], "kode": "HS5-1"},
            "B": {"text": MAPPING["HS5-2"], "kode": "HS5-2"},
            "C": {"text": MAPPING["HS5-3"], "kode": "HS5-3"},
        },
        "Hard Skill - Design Pattern": {
            "A": {"text": MAPPING["HS6-1"], "kode": "HS6-1"},
            "B": {"text": MAPPING["HS6-2"], "kode": "HS6-2"},
            "C": {"text": MAPPING["HS6-3"], "kode": "HS6-3"},
        },
        "Hard Skill - Microservice": {
            "A": {"text": MAPPING["HS7-1"], "kode": "HS7-1"},
            "B": {"text": MAPPING["HS7-2"], "kode": "HS7-2"},
            "C": {"text": MAPPING["HS7-3"], "kode": "HS7-3"},
        },
        "Hard Skill - Docker": {
            "A": {"text": MAPPING["HS8-1"], "kode": "HS8-1"},
            "B": {"text": MAPPING["HS8-2"], "kode": "HS8-2"},
            "C": {"text": MAPPING["HS8-3"], "kode": "HS8-3"},
        },
        "Hard Skill - CI/CD": {
            "A": {"text": MAPPING["HS9-1"], "kode": "HS9-1"},
            "B": {"text": MAPPING["HS9-2"], "kode": "HS9-2"},
            "C": {"text": MAPPING["HS9-3"], "kode": "HS9-3"},
        },
        "Hard Skill - Cloud": {
            "A": {"text": MAPPING["HS10-1"], "kode": "HS10-1"},
            "B": {"text": MAPPING["HS10-2"], "kode": "HS10-2"},
            "C": {"text": MAPPING["HS10-3"], "kode": "HS10-3"},
        },
        "Hard Skill - Payment Gateway": {
            "A": {"text": MAPPING["HS11-1"], "kode": "HS11-1"},
            "B": {"text": MAPPING["HS11-2"], "kode": "HS11-2"},
            "C": {"text": MAPPING["HS11-3"], "kode": "HS11-3"},
        },

        # === Soft Skills (Tabel 4.10) ===
        "Soft Skill - Problem Solving": {
            "A": {"text": MAPPING["SS1-1"], "kode": "SS1-1"},
            "B": {"text": MAPPING["SS1-2"], "kode": "SS1-2"},
            "C": {"text": MAPPING["SS1-3"], "kode": "SS1-3"},
        },
        "Soft Skill - Komunikasi": {
            "A": {"text": MAPPING["SS2-1"], "kode": "SS2-1"},
            "B": {"text": MAPPING["SS2-2"], "kode": "SS2-2"},
            "C": {"text": MAPPING["SS2-3"], "kode": "SS2-3"},
        },
        "Soft Skill - Adaptasi": {
            "A": {"text": MAPPING["SS3-1"], "kode": "SS3-1"},
            "B": {"text": MAPPING["SS3-2"], "kode": "SS3-2"},
            "C": {"text": MAPPING["SS3-3"], "kode": "SS3-3"},
        },

        # === Live Coding (Tabel 4.11) ===
        "Live Coding - Dasar Pemrograman": {
            "A": {"text": MAPPING["LC1-1"], "kode": "LC1-1"},
            "B": {"text": MAPPING["LC1-2"], "kode": "LC1-2"},
            "C": {"text": MAPPING["LC1-3"], "kode": "LC1-3"},
        },
        "Live Coding - Problem Solving": {
            "A": {"text": MAPPING["LC2-1"], "kode": "LC2-1"},
            "B": {"text": MAPPING["LC2-2"], "kode": "LC2-2"},
            "C": {"text": MAPPING["LC2-3"], "kode": "LC2-3"},
        },
        "Live Coding - Kualitas Kode": {
            "A": {"text": MAPPING["LC3-1"], "kode": "LC3-1"},
            "B": {"text": MAPPING["LC3-2"], "kode": "LC3-2"},
            "C": {"text": MAPPING["LC3-3"], "kode": "LC3-3"},
        },

        # === Faktor Tambahan (Tabel 4.12) ===
        "Faktor Tambahan - Development Tools": {
            "A": {"text": MAPPING["FT1-1"], "kode": "FT1-1"},
            "B": {"text": MAPPING["FT1-2"], "kode": "FT1-2"},
        },
        "Faktor Tambahan - Jam Aktif": {
            "A": {"text": MAPPING["FT2-1"], "kode": "FT2-1"},
            "B": {"text": MAPPING["FT2-2"], "kode": "FT2-2"},
        },
        "Faktor Tambahan - Career Path": {
            "A": {"text": MAPPING["FT3-1"], "kode": "FT3-1"},
            "B": {"text": MAPPING["FT3-2"], "kode": "FT3-2"},
        },
        "Faktor Tambahan - Sertifikasi": {
            "A": {"text": MAPPING["FT4-1"], "kode": "FT4-1"},
            "B": {"text": MAPPING["FT4-2"], "kode": "FT4-2"},
        },
    }

    # 3. Collect answers
    answers = {}
    print("\n=== MULAI ASSESSMENT ===\n")
    
    try:
        for q, choices in questions.items():
            answers[q] = ask_question(q, choices)
    except Exception as e:
        print(f"ERROR saat mengumpulkan jawaban: {e}")
        return

    # 4. Hitung skor dan mandatory factors
    hs_score, factor_scores = calculate_hardskill_score(answers)
    mandatory_junior, mandatory_middle = check_mandatory_factors(factor_scores, info["posisi"])
    
    print(f"\n=== HASIL PENILAIAN ===")
    print(f"Total Hard Skill Score: {hs_score}")
    print(f"Mandatory Junior: {'✓' if mandatory_junior else '✗'}")
    print(f"Mandatory Middle: {'✓' if mandatory_middle else '✗'}")

    # 5. Jalankan RBES dengan Dual Process
    engine = RecruitmentEngine()
    engine.reset()
    
    # Declare kandidat
    engine.declare(Candidate(nama=info["nama"], posisi=info["posisi"]))

    # Declare facts untuk Level 1: Screening
    engine.declare(Fact(FS1=answers["Screening - Personality"]["kode"]))
    engine.declare(Fact(FS2=answers["Screening - Tes Tertulis"]["kode"]))

    # Declare facts untuk Level 2: Hard Skills + Soft Skills
    engine.declare(Fact(posisi=info["posisi"]))
    engine.declare(Fact(bobot_total=hs_score))
    engine.declare(Fact(mandatory_junior=mandatory_junior))
    engine.declare(Fact(mandatory_middle=mandatory_middle))
    
    engine.declare(Fact(SS1=answers["Soft Skill - Problem Solving"]["kode"]))
    engine.declare(Fact(SS2=answers["Soft Skill - Komunikasi"]["kode"]))
    engine.declare(Fact(SS3=answers["Soft Skill - Adaptasi"]["kode"]))

    # Declare facts untuk Level 3: Live Coding
    engine.declare(Fact(LC1=answers["Live Coding - Dasar Pemrograman"]["kode"]))
    engine.declare(Fact(LC2=answers["Live Coding - Problem Solving"]["kode"]))
    engine.declare(Fact(LC3=answers["Live Coding - Kualitas Kode"]["kode"]))

    # Declare facts untuk Level 4: Nilai Tambahan
    engine.declare(Fact(FT1=answers["Faktor Tambahan - Development Tools"]["kode"]))
    engine.declare(Fact(FT2=answers["Faktor Tambahan - Jam Aktif"]["kode"]))
    engine.declare(Fact(FT3=answers["Faktor Tambahan - Career Path"]["kode"]))
    engine.declare(Fact(FT4=answers["Faktor Tambahan - Sertifikasi"]["kode"]))

    print("\n=== MENJALANKAN DUAL PROCESS INFERENCE ===\n")
    
    # DEBUG: Print facts sebelum run
    debug_facts(engine)
    
    try:
        engine.run()
        
        print(f"\n=== RANGKUMAN PROSES ===")
        print(f"Total rules triggered: {len(engine.triggered_rules)}")
        print(f"Level status: {engine.level_status}")
        
        # Debug results
        debug_results(engine)
        
    except Exception as e:
        print(f"ERROR saat menjalankan inference engine: {e}")
        print("Menggunakan hasil fallback...")
        
        # Fallback result jika ada error
        if not engine.results:
            engine.add_result("Kurang Layak", f"Sistem mengalami error: {str(e)}", "Error")

    # 6. Generate report
    generate_report(info, answers, engine.results, engine.triggered_rules, 
                   hs_score, factor_scores, engine.level_status)

if __name__ == "__main__":
    main()