from mappings import MAPPING

def generate_report(candidat_info, answers, results, triggered_rules, hs_score=None, factor_scores=None, level_status=None):
    """Generate comprehensive report sesuai dengan Dual Process mechanism"""
    print("\n" + "="*80)
    print("LAPORAN HASIL SISTEM PAKAR SELEKSI KANDIDAT")
    print("="*80)

    # 1. INFORMASI KANDIDAT
    print(f"\nINFORMASI KANDIDAT:")
    print(f"   Nama      : {candidat_info['nama']}")
    print(f"   Posisi    : {candidat_info['posisi'].title()} Fullstack Developer")

    # 2. RINGKASAN INPUT PER DIMENSI
    print(f"\nRINGKASAN INPUT PER DIMENSI:")
    
    # Screening
    print(f"\n[LEVEL 1] SCREENING:")
    print(f"   Personality Test : {answers['Screening - Personality']['text']}")
    if answers['Screening - Personality']['note']:
        print(f"                      Note: {answers['Screening - Personality']['note']}")
    print(f"   Tes Tertulis     : {answers['Screening - Tes Tertulis']['text']}")
    if answers['Screening - Tes Tertulis']['note']:
        print(f"                      Note: {answers['Screening - Tes Tertulis']['note']}")

    # Hard Skills
    print(f"\n[LEVEL 2A] HARD SKILLS:")
    hs_questions = [
        ("Pemrograman", "Hard Skill - Pemrograman"),
        ("MySQL", "Hard Skill - Database MySQL"),
        ("Framework", "Hard Skill - Framework"),
        ("Unit Test", "Hard Skill - Unit Test"),
        ("SDLC", "Hard Skill - SDLC"),
        ("Design Pattern", "Hard Skill - Design Pattern"),
        ("Microservice", "Hard Skill - Microservice"),
        ("Docker", "Hard Skill - Docker"),
        ("CI/CD", "Hard Skill - CI/CD"),
        ("Cloud", "Hard Skill - Cloud"),
        ("Payment Gateway", "Hard Skill - Payment Gateway")
    ]
    
    for label, key in hs_questions:
        print(f"   {label:<15}: {answers[key]['text']}")
        if answers[key]['note']:
            print(f"   {'':<15}  Note: {answers[key]['note']}")
    
    if hs_score is not None:
        print(f"\n   TOTAL SKOR HARD SKILL: {hs_score}/33")

    # Soft Skills
    print(f"\n[LEVEL 2B] SOFT SKILLS:")
    ss_questions = [
        ("Problem Solving", "Soft Skill - Problem Solving"),
        ("Komunikasi", "Soft Skill - Komunikasi"),
        ("Adaptasi", "Soft Skill - Adaptasi")
    ]
    
    for label, key in ss_questions:
        print(f"   {label:<15}: {answers[key]['text']}")
        if answers[key]['note']:
            print(f"   {'':<15}  Note: {answers[key]['note']}")

    # Live Coding
    print(f"\n[LEVEL 3] LIVE CODING:")
    lc_questions = [
        ("Konsep Dasar", "Live Coding - Dasar Pemrograman"),
        ("Problem Solving", "Live Coding - Problem Solving"),
        ("Kualitas Kode", "Live Coding - Kualitas Kode")
    ]
    
    for label, key in lc_questions:
        print(f"   {label:<15}: {answers[key]['text']}")
        if answers[key]['note']:
            print(f"   {'':<15}  Note: {answers[key]['note']}")

    # Nilai Tambahan
    print(f"\n[LEVEL 4] NILAI TAMBAHAN:")
    ft_questions = [
        ("Dev Tools", "Faktor Tambahan - Development Tools"),
        ("Jam Aktif", "Faktor Tambahan - Jam Aktif"),
        ("Career Path", "Faktor Tambahan - Career Path"),
        ("Sertifikasi", "Faktor Tambahan - Sertifikasi")
    ]
    
    for label, key in ft_questions:
        print(f"   {label:<12}: {answers[key]['text']}")
        if answers[key]['note']:
            print(f"   {'':<12}  Note: {answers[key]['note']}")

    # 3. ALUR DUAL PROCESS
    print(f"\nALUR DUAL PROCESS:")
    if level_status:
        for level, status in level_status.items():
            status_symbol = "✓" if status == "PASS" else ("✗" if status == "STOP" else "→")
            print(f"   {level}: {status_symbol} {status}")

    # 4. RULES TRIGGERED
    print(f"\nRULES YANG TERPICU:")
    for i, rule in enumerate(triggered_rules, 1):
        print(f"   {i:2d}. {rule}")

    # 5. HASIL KEPUTUSAN
    print(f"\nHASIL KEPUTUSAN:")
    if results:
        final_result = results[-1]  # Ambil keputusan terakhir
        print(f"   REKOMENDASI: {final_result['Keputusan']}")
        print(f"   ALASAN     : {final_result['Alasan']}")
        if 'Level' in final_result:
            print(f"   LEVEL STOP : {final_result['Level']}")
        
        # Tampilkan semua keputusan jika ada lebih dari satu
        if len(results) > 1:
            print(f"\n   RIWAYAT KEPUTUSAN:")
            for i, result in enumerate(results, 1):
                level_info = f" (Level {result['Level']})" if 'Level' in result else ""
                print(f"     {i}. {result['Keputusan']}{level_info}")
    else:
        print("   REKOMENDASI: Kurang Layak (tidak ada rule global yang terpicu)")
        print("   ALASAN     : Sistem tidak dapat menentukan kualifikasi berdasarkan input yang diberikan")

    # 6. BREAKDOWN HARD SKILL (jika ada)
    if factor_scores:
        print(f"\nBREAKDOWN HARD SKILL:")
        mandatory_junior = ["HS1", "HS2", "HS5", "HS6"]
        mandatory_middle = ["HS1", "HS2", "HS3", "HS4", "HS5", "HS6", "HS8", "HS9"]
        
        for factor, data in factor_scores.items():
            mandatory_mark = ""
            if factor in mandatory_junior:
                mandatory_mark += " [M-Jr]"
            if factor in mandatory_middle:
                mandatory_mark += " [M-Mid]"
            
            print(f"   {factor}: {data['score']}/3{mandatory_mark}")
        
        print(f"\n   Keterangan: [M-Jr] = Mandatory untuk Junior, [M-Mid] = Mandatory untuk Middle")

    print("\n" + "="*80)
    print("END OF REPORT")
    print("="*80)