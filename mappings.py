# Mapping sesuai dengan Tabel 4.8-4.12 dari Bab 4

MAPPING = {
    # === Screening (Tabel 4.8) ===
    "FS1-1": "Personality test - Excellent, leadership potential",
    "FS1-2": "Personality test - Baik, dapat bekerja dalam tim",
    "FS1-3": "Personality test - Kurang baik, butuh guidance",
    
    "FS2-1": "Tes Tertulis - Jawaban Benar ≥ 80%",
    "FS2-2": "Tes Tertulis - Jawaban Benar 60-79%", 
    "FS2-3": "Tes Tertulis - Jawaban Benar < 59%",

    # === Hard Skills (Tabel 4.9) === 
    "HS1-1": "Bahasa Pemrograman - Master PHP/JS/TS + experienced",
    "HS1-2": "Bahasa Pemrograman - Mahir 1-2 bahasa + cukup berpengalaman",
    "HS1-3": "Bahasa Pemrograman - Menguasai dan paham sintaks",
    
    "HS2-1": "MySQL - Advanced query + optimization + indexing strategy + able to use PLAIN SQL",
    "HS2-2": "MySQL - Intermediate + join kompleks + indexing dasar + able to use PLAIN/ORM SQL", 
    "HS2-3": "MySQL - Basic CRUD + simple join",
    
    "HS3-1": "Framework - Master 2+ framework + custom development",
    "HS3-2": "Framework - Mahir 1 framework",
    "HS3-3": "Framework - Tidak menguasai / paham konsep framework",
    
    "HS4-1": "Unit Testing - Experienced + integration testing",
    "HS4-2": "Unit Testing - Pernah unit testing + basic coverage",
    "HS4-3": "Unit Testing - Paham konsep testing / tidak berpengalaman",
    
    "HS5-1": "SDLC - Understanding Agile/Scrum + Waterfall + DevOps integration",
    "HS5-2": "SDLC - Agile / Scrum + basic project management",
    "HS5-3": "SDLC - Waterfall / basic methodology",
    
    "HS6-1": "Design Pattern - Ability to implement MVC + Repository + DDD + SOLID principles",
    "HS6-2": "Design Pattern - Repository + basic patterns implementation", 
    "HS6-3": "Design Pattern - Paham konsep design pattern",
    
    "HS7-1": "Microservice - Design + implement",
    "HS7-2": "Microservice - Basic implementation + API gateway",
    "HS7-3": "Microservice - Paham konsep / tidak berpengalaman",
    
    "HS8-1": "Docker - Multi-stage builds + integration + production deploy",
    "HS8-2": "Docker - Experienced in project / local dev",
    "HS8-3": "Docker - Paham konsep / tidak berpengalaman",
    
    "HS9-1": "CI/CD - Complex pipelines + automated testing + deployment strategies",
    "HS9-2": "CI/CD - Experienced in basic pipeline setup",
    "HS9-3": "CI/CD - Paham konsep / tidak berpengalaman",
    
    "HS10-1": "Cloud - Experienced in multi-platform",
    "HS10-2": "Cloud - 1 platform (limited experience) + basic services",
    "HS10-3": "Cloud - Paham konsep / tidak berpengalaman",
    
    "HS11-1": "Payment Gateway - Experienced in multiple gateways",
    "HS11-2": "Payment Gateway - Limited experience",
    "HS11-3": "Payment Gateway - Paham konsep / tidak berpengalaman",

    # === Soft Skills (Tabel 4.10) ===
    "SS1-1": "Problem Solving - Mandiri + creative solutions + team discussion",
    "SS1-2": "Problem Solving - Self-research + systematic approach", 
    "SS1-3": "Problem Solving - Need a time + Butuh guidance + basic troubleshooting",
    
    "SS2-1": "Komunikasi - Jelas + interaktif + responsive",
    "SS2-2": "Komunikasi - Jelas + passive",
    "SS2-3": "Komunikasi - Basic communication + too passive + perlu improvement",
    
    "SS3-1": "Adaptabilitas - Quick learner + embrace change",
    "SS3-2": "Adaptabilitas - Normal adaptation (< 1 week) + willing to learn",
    "SS3-3": "Adaptabilitas - Slow adaptation (> 2 week) + need support",

    # === Live Coding (Tabel 4.11) ===
    "LC1-1": "Pemahaman Konsep Dasar - Master fundamentals (PHP/JS/TS & SQL) + best practices",
    "LC1-2": "Pemahaman Konsep Dasar - Solid understanding + poor implementation",
    "LC1-3": "Pemahaman Konsep Dasar - Basic knowledge + needs improvement",
    
    "LC2-1": "Problem Solving & Critical Thinking - Analytical + innovative solutions",
    "LC2-2": "Problem Solving & Critical Thinking - Logical approach + research skills",
    "LC2-3": "Problem Solving & Critical Thinking - not so good problem solving",
    
    "LC3-1": "Efisiensi Kode - Clean code + optimized + scalable",
    "LC3-2": "Efisiensi Kode - Slightly messy + readable + functional",
    "LC3-3": "Efisiensi Kode - Functional + disorganized + needs refinement",

    # === Nilai Tambahan (Tabel 4.12) ===
    "FT1-1": "Development Tools - Mahir berbagai tools (Laragon, VSCode, debugging, dll)",
    "FT1-2": "Development Tools - Tools terbatas atau standard",
    
    "FT2-1": "Fleksibilitas Jam Kerja - Sesuai kebutuhan tim (pagi-sore)",
    "FT2-2": "Fleksibilitas Jam Kerja - Kurang fleksibel (hanya malam)",
    
    "FT3-1": "Konsistensi Career Path - Konsisten di bidang IT",
    "FT3-2": "Konsistensi Career Path - Tidak konsisten atau career change",
    
    "FT4-1": "Sertifikasi - Ada sertifikasi relevan + sesuai skill", 
    "FT4-2": "Sertifikasi - Tidak ada sertifikasi relevan",
}

# Hard Skill Scoring berdasarkan bobot pada Tabel 4.9
HS_SCORING = {
    # Bobot 3 = Expert
    "HS1-1": 3, "HS2-1": 3, "HS3-1": 3, "HS4-1": 3, "HS5-1": 3, 
    "HS6-1": 3, "HS7-1": 3, "HS8-1": 3, "HS9-1": 3, "HS10-1": 3, "HS11-1": 3,
    
    # Bobot 2 = Intermediate
    "HS1-2": 2, "HS2-2": 2, "HS3-2": 2, "HS4-2": 2, "HS5-2": 2,
    "HS6-2": 2, "HS7-2": 2, "HS8-2": 2, "HS9-2": 2, "HS10-2": 2, "HS11-2": 2,
    
    # Bobot 1 = Basic
    "HS1-3": 1, "HS2-3": 1, "HS3-3": 1, "HS4-3": 1, "HS5-3": 1,
    "HS6-3": 1, "HS7-3": 1, "HS8-3": 1, "HS9-3": 1, "HS10-3": 1, "HS11-3": 1,
}

# Mandatory factors untuk posisi (berdasarkan sub-bab 4.2.2 point 2)
MANDATORY_FACTORS = {
    "junior": ["HS1", "HS2", "HS5", "HS6"],  # Programming, MySQL, SDLC, Design Pattern
    "middle": ["HS1", "HS2", "HS3", "HS4", "HS5", "HS6", "HS8", "HS9"]  # Semua kecuali HS7, HS10, HS11
}

# Threshold untuk hard skill berdasarkan Tabel 4.15 
HARDSKILL_THRESHOLD = {
    "junior": {"min": 11, "max": 20},
    "middle": {"min": 21, "max": 33}
}

# HS_SCORING = {
#     "HS1-1": 5, "HS1-2": 3, "HS1-3": 0,
#     "HS2-1": 5, "HS2-2": 3, "HS2-3": 1,
#     "HS3-3": 5, "HS3-2": 3, "HS3-3": 1,
#     "HS4-1": 5, "HS4-2": 1, "HS4-3": 0,
#     "HS5-1": 5, "HS5-2": 1, "HS5-3": 0,
#     "HS6-1": 5, "HS6-2": 3, "HS6-3": 0,
#     "HS7-1": 5, "HS7-2": 3, "HS7-3": 1,
#     "HS8-1": 5, "HS8-2": 3, "HS8-3": 0,
#     "HS9-1": 5, "HS9-2": 3, "HS9-3": 0,
#     "HS10-1": 5, "HS10-2": 3, "HS10-3": 0,
#     "HS11-1": 5, "HS11-2": 1, "HS11-3": 0,
# }