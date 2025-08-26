# Mapping kode → deskripsi nilai sesuai tabel fakta

MAPPING = {
    # === Screening ===
    "FS1-1": "Personality Baik",
    "FS1-2": "Personality Kurang",
    "FS1-3": "Personality Buruk/Parah",

    "FS2-1": "Tes Tertulis Bagus (≥80%)",
    "FS2-2": "Tes Tertulis Baik (60–79%)",
    "FS2-3": "Tes Tertulis Kurang (<60%)",

    # === Hard Skills ===
    "HS1-1": "Pemrograman Mahir (PHP/JS/TS)",
    "HS1-2": "Pemrograman Cukup (salah satu/kurang pengalaman)",
    "HS1-3": "Pemrograman Kurang",

    "HS2-1": "MySQL Advanced (optimasi query, indexing)",
    "HS2-2": "MySQL Intermediate (join, indexing dasar)",
    "HS2-3": "MySQL Basic (CRUD)",

    "HS3-1": "Framework Multi (lebih dari satu)",
    "HS3-2": "Framework Satu",
    "HS3-3": "Tidak Menguasai Framework",

    "HS4-1": "Unit Test Mahir (berpengalaman implementasi)",
    "HS4-2": "Unit Test Cukup (pernah/paham konsep)",
    "HS4-3": "Tidak Pernah Unit Test",

    "HS5-1": "SDLC Bagus (Agile/Scrum & Waterfall)",
    "HS5-2": "SDLC Kurang (hanya Waterfall)",
    "HS5-3": "Tidak Paham SDLC",

    "HS6-1": "Design Pattern Mahir (MVC, DDD, dsb.)",
    "HS6-2": "Design Pattern Cukup (paham konsep)",
    "HS6-3": "Tidak Paham Design Pattern",

    "HS7-1": "Microservice Implementasi + Paham Konsep",
    "HS7-2": "Microservice Paham Konsep",
    "HS7-3": "Tidak Pernah Microservice (mau belajar)",

    "HS8-1": "Docker Mahir (deploy & CI/CD)",
    "HS8-2": "Docker Pernah (local dev/project)",
    "HS8-3": "Tidak Pernah Docker (mau belajar)",

    "HS9-1": "CI/CD Mahir (build pipeline)",
    "HS9-2": "CI/CD Pernah (pipeline sederhana)",
    "HS9-3": "Tidak Pernah CI/CD",

    "HS10-1": "Cloud Mahir (berbagai platform)",
    "HS10-2": "Cloud Pernah (pengalaman terbatas)",
    "HS10-3": "Tidak Pernah Cloud (mau belajar)",

    "HS11-1": "Payment Gateway Mahir (API integrasi)",
    "HS11-2": "Payment Gateway Terbatas",
    "HS11-3": "Tidak Pernah Payment Gateway",

    # === Soft Skills ===
    "SS1-1": "Problem Solving Sangat Baik",
    "SS1-2": "Problem Solving Baik",
    "SS1-3": "Problem Solving Lemah",

    "SS2-1": "Komunikasi Bagus",
    "SS2-2": "Komunikasi Cukup",
    "SS2-3": "Komunikasi Kurang",

    "SS3-1": "Adaptasi Bagus (langsung efektif)",
    "SS3-2": "Adaptasi Menyesuaikan (<1 minggu)",
    "SS3-3": "Adaptasi Lambat (>2 minggu)",

    # === Live Coding ===
    "LC1-1": "Menguasai Dasar Programming (PHP/JS/TS & MySQL)",
    "LC1-2": "Dasar Programming Kurang",

    "LC2-1": "Problem Solving & Critical Thinking Oke",
    "LC2-2": "Problem Solving Lemah",

    "LC3-1": "Kode Efisien & Rapi",
    "LC3-2": "Kode Cukup Rapi",
    "LC3-3": "Kode Tidak Efisien",

    # === Nilai Tambahan ===
    "FT1-1": "Development Tools Banyak",
    "FT1-2": "Development Tools Terbatas",

    "FT2-1": "Jam Aktif Pagi-Sore (sesuai tim)",
    "FT2-2": "Jam Aktif Malam (kurang fleksibel)",

    "FT3-1": "Career Path Konsisten di IT",
    "FT3-2": "Career Path Tidak Konsisten",

    "FT4-1": "Ada Sertifikasi Relevan",
    "FT4-2": "Tidak Ada Sertifikasi",
}

HS_SCORING = {
    "HS1-1": 5, "HS1-2": 3, "HS1-3": 0,
    "HS2-1": 5, "HS2-2": 3, "HS2-3": 1,
    "HS3-3": 5, "HS3-2": 3, "HS3-3": 1,
    "HS4-1": 5, "HS4-2": 1, "HS4-3": 0,
    "HS5-1": 5, "HS5-2": 1, "HS5-3": 0,
    "HS6-1": 5, "HS6-2": 3, "HS6-3": 0,
    "HS7-1": 5, "HS7-2": 3, "HS7-3": 1,
    "HS8-1": 5, "HS8-2": 3, "HS8-3": 0,
    "HS9-1": 5, "HS9-2": 3, "HS9-3": 0,
    "HS10-1": 5, "HS10-2": 3, "HS10-3": 0,
    "HS11-1": 5, "HS11-2": 1, "HS11-3": 0,
}