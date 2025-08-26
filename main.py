from experta import *
from facts import *
from rules import RecruitmentEngine
from ui import ask_question, collect_candidate_info
from report import generate_report
from mappings import MAPPING, HS_SCORING

def main():
    # 1. Input kandidat
    info = collect_candidate_info()

    # 2. Pertanyaan contoh (nanti diisi semua sesuai tabel)
    questions = {
        # === Screening ===
        "Personality": {
            "A": {"text": MAPPING["FS1-1"], "kode": "FS1-1"},
            "B": {"text": MAPPING["FS1-2"], "kode": "FS1-2"},
            "C": {"text": MAPPING["FS1-3"], "kode": "FS1-3"},
        },
        "Tes Tertulis": {
            "A": {"text": MAPPING["FS2-1"], "kode": "FS2-1"},
            "B": {"text": MAPPING["FS2-2"], "kode": "FS2-2"},
            "C": {"text": MAPPING["FS2-3"], "kode": "FS2-3"},
        },

        # === Hard Skills ===
        "Pemrograman": {
            "A": {"text": MAPPING["HS1-1"], "kode": "HS1-1"},
            "B": {"text": MAPPING["HS1-2"], "kode": "HS1-2"},
            "C": {"text": MAPPING["HS1-3"], "kode": "HS1-3"},
        },
        "Database MySQL": {
            "A": {"text": MAPPING["HS2-1"], "kode": "HS2-1"},
            "B": {"text": MAPPING["HS2-2"], "kode": "HS2-2"},
            "C": {"text": MAPPING["HS2-3"], "kode": "HS2-3"},
        },
        "Framework": {
            "A": {"text": MAPPING["HS3-1"], "kode": "HS3-1"},
            "B": {"text": MAPPING["HS3-2"], "kode": "HS3-2"},
            "C": {"text": MAPPING["HS3-3"], "kode": "HS3-3"},
        },
        "Unit Test": {
            "A": {"text": MAPPING["HS4-1"], "kode": "HS4-1"},
            "B": {"text": MAPPING["HS4-2"], "kode": "HS4-2"},
            "C": {"text": MAPPING["HS4-3"], "kode": "HS4-3"},
        },
        "SDLC": {
            "A": {"text": MAPPING["HS5-1"], "kode": "HS5-1"},
            "B": {"text": MAPPING["HS5-2"], "kode": "HS5-2"},
            "C": {"text": MAPPING["HS5-3"], "kode": "HS5-3"},
        },
        "Design Pattern": {
            "A": {"text": MAPPING["HS6-1"], "kode": "HS6-1"},
            "B": {"text": MAPPING["HS6-2"], "kode": "HS6-2"},
            "C": {"text": MAPPING["HS6-3"], "kode": "HS6-3"},
        },
        "Microservice": {
            "A": {"text": MAPPING["HS7-1"], "kode": "HS7-1"},
            "B": {"text": MAPPING["HS7-2"], "kode": "HS7-2"},
            "C": {"text": MAPPING["HS7-3"], "kode": "HS7-3"},
        },
        "Docker": {
            "A": {"text": MAPPING["HS8-1"], "kode": "HS8-1"},
            "B": {"text": MAPPING["HS8-2"], "kode": "HS8-2"},
            "C": {"text": MAPPING["HS8-3"], "kode": "HS8-3"},
        },
        "CI/CD": {
            "A": {"text": MAPPING["HS9-1"], "kode": "HS9-1"},
            "B": {"text": MAPPING["HS9-2"], "kode": "HS9-2"},
            "C": {"text": MAPPING["HS9-3"], "kode": "HS9-3"},
        },
        "Cloud": {
            "A": {"text": MAPPING["HS10-1"], "kode": "HS10-1"},
            "B": {"text": MAPPING["HS10-2"], "kode": "HS10-2"},
            "C": {"text": MAPPING["HS10-3"], "kode": "HS10-3"},
        },
        "Payment Gateway": {
            "A": {"text": MAPPING["HS11-1"], "kode": "HS11-1"},
            "B": {"text": MAPPING["HS11-2"], "kode": "HS11-2"},
            "C": {"text": MAPPING["HS11-3"], "kode": "HS11-3"},
        },

        # === Soft Skills ===
        "Problem Solving": {
            "A": {"text": MAPPING["SS1-1"], "kode": "SS1-1"},
            "B": {"text": MAPPING["SS1-2"], "kode": "SS1-2"},
            "C": {"text": MAPPING["SS1-3"], "kode": "SS1-3"},
        },
        "Komunikasi": {
            "A": {"text": MAPPING["SS2-1"], "kode": "SS2-1"},
            "B": {"text": MAPPING["SS2-2"], "kode": "SS2-2"},
            "C": {"text": MAPPING["SS2-3"], "kode": "SS2-3"},
        },
        "Adaptasi": {
            "A": {"text": MAPPING["SS3-1"], "kode": "SS3-1"},
            "B": {"text": MAPPING["SS3-2"], "kode": "SS3-2"},
            "C": {"text": MAPPING["SS3-3"], "kode": "SS3-3"},
        },

        # === Live Coding ===
        "Live Coding - Dasar Pemrograman": {
            "A": {"text": MAPPING["LC1-1"], "kode": "LC1-1"},
            "B": {"text": MAPPING["LC1-2"], "kode": "LC1-2"},
        },
        "Live Coding - Problem Solving": {
            "A": {"text": MAPPING["LC2-1"], "kode": "LC2-1"},
            "B": {"text": MAPPING["LC2-2"], "kode": "LC2-2"},
        },
        "Live Coding - Kualitas Kode": {
            "A": {"text": MAPPING["LC3-1"], "kode": "LC3-1"},
            "B": {"text": MAPPING["LC3-2"], "kode": "LC3-2"},
            "C": {"text": MAPPING["LC3-3"], "kode": "LC3-3"},
        },

        # === Faktor Tambahan ===
        "Development Tools": {
            "A": {"text": MAPPING["FT1-1"], "kode": "FT1-1"},
            "B": {"text": MAPPING["FT1-2"], "kode": "FT1-2"},
        },
        "Jam Aktif": {
            "A": {"text": MAPPING["FT2-1"], "kode": "FT2-1"},
            "B": {"text": MAPPING["FT2-2"], "kode": "FT2-2"},
        },
        "Career Path": {
            "A": {"text": MAPPING["FT3-1"], "kode": "FT3-1"},
            "B": {"text": MAPPING["FT3-2"], "kode": "FT3-2"},
        },
        "Sertifikasi": {
            "A": {"text": MAPPING["FT4-1"], "kode": "FT4-1"},
            "B": {"text": MAPPING["FT4-2"], "kode": "FT4-2"},
        },
    }

    answers = {}
    for q, ch in questions.items():
        answers[q] = ask_question(q, ch)

    # 3. Jalankan RBES
    engine = RecruitmentEngine()
    engine.reset()
    engine.results = []   # tempat nyimpen hasil keputusan
    
    # inisialisasi flag livecoding
    engine.declare(Fact(FA13=False), Fact(FA14=False), Fact(FA15=False))
    # inisialisasi flag softskill
    engine.declare(Fact(FA10=False), Fact(FA11=False))
    # inisialisasi flag tambahan
    engine.declare(Fact(FA16=False), Fact(FA17=False), Fact(FA18=False))

    # declare kandidat
    engine.declare(Candidate(nama=info["nama"], posisi=info["posisi"]))

    # declare screening - PERBAIKAN: gunakan Fact() langsung
    engine.declare(Fact(FS1=answers["Personality"]["kode"]))
    engine.declare(Fact(FS2=answers["Tes Tertulis"]["kode"]))

    # Hitung skor hard skill
    hs_score = sum(
        HS_SCORING[answers[q]["kode"]] 
        for q in ["Pemrograman", "Database MySQL", "Framework", "Unit Test",
        "SDLC", "Design Pattern", "Microservice", "Docker", "CI/CD",
        "Cloud", "Payment Gateway"] 
        if answers[q]["kode"] in HS_SCORING
    )

    # Declare posisi dan bobot untuk hard skill rules
    engine.declare(Fact(posisi=info["posisi"]))
    engine.declare(Fact(bobot_total=hs_score))

    # declare soft skill - PERBAIKAN: gunakan Fact() langsung
    engine.declare(Fact(SS1=answers["Problem Solving"]["kode"]))
    engine.declare(Fact(SS2=answers["Komunikasi"]["kode"]))
    engine.declare(Fact(SS3=answers["Adaptasi"]["kode"]))

    # declare live coding - PERBAIKAN: gunakan Fact() langsung
    engine.declare(Fact(LC1=answers["Live Coding - Dasar Pemrograman"]["kode"]))
    engine.declare(Fact(LC2=answers["Live Coding - Problem Solving"]["kode"]))
    engine.declare(Fact(LC3=answers["Live Coding - Kualitas Kode"]["kode"]))

    # declare faktor tambahan - PERBAIKAN: gunakan Fact() langsung
    engine.declare(Fact(FT1=answers["Development Tools"]["kode"]))
    engine.declare(Fact(FT2=answers["Jam Aktif"]["kode"]))
    engine.declare(Fact(FT3=answers["Career Path"]["kode"]))
    engine.declare(Fact(FT4=answers["Sertifikasi"]["kode"]))

    print("\n=== MENJALANKAN EXPERT SYSTEM ===")
    
    # DEBUG: Print facts sebelum run
    from debug_facts import debug_facts
    debug_facts(engine)
    
    engine.run()
    
    print(f"\nTotal rules triggered: {len(engine.triggered_rules)}")
    print(f"Total results: {len(engine.results)}")

    # 4. Simpan hasil
    results = engine.results if hasattr(engine, "results") else []
    
    generate_report(info, answers, engine.results, engine.triggered_rules, hs_score)

if __name__ == "__main__":
    main()