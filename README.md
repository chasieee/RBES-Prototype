# Rule-Based Expert System (RBES) Prototype - Full-stack Developer Recruitment

Sistem Pakar berbasis aturan untuk seleksi kandidat Fullstack Developer menggunakan **Dual Process Mechanism** dengan 5 level evaluasi bertingkat.

## 🚀 Features

- **Dual Process Evaluation**: Sistem evaluasi berlapis dengan 5 level (Screening → Hard Skills + Soft Skills → Live Coding → Nilai Tambahan → Keputusan Akhir)
- **Position-Based Assessment**: Mendukung posisi Junior dan Middle Fullstack Developer dengan kriteria berbeda
- **Mandatory Factor Checking**: Validasi faktor wajib sesuai level posisi
- **Interactive CLI Interface**: Interface command-line yang user-friendly
- **Comprehensive Reporting**: Laporan lengkap dengan breakdown per dimensi dan alur keputusan
- **31 Expert Rules**: Implementasi 31 aturan pakar yang komprehensif

## 📋 System Requirements

- Python 3.8+
- experta library

## 🛠️ Installation

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/yourusername/rbes-recruitment.git
   cd rbes-recruitment
   ```

2. **Install dependencies:**
   ```bash
   pip install experta
   ```

3. **Jalankan sistem:**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
rbes-recruitment/
│
├── main.py              # Entry point aplikasi
├── rules.py             # 31 Expert rules dengan Dual Process
├── facts.py             # Definisi fakta dan struktur data
├── mappings.py          # Mapping kriteria dan scoring
├── ui.py                # User interface dan input handling
├── report.py            # Generator laporan komprehensif
├── debug_facts.py       # Utility debugging
└── README.md           # Dokumentasi ini
```

## 🎯 How to Use

### 1. Jalankan Aplikasi
```bash
python main.py
```

### 2. Input Informasi Kandidat
- Masukkan nama kandidat
- Pilih posisi yang dilamar (Junior/Middle Fullstack Developer)

### 3. Assessment Process
Sistem akan memandu Anda melalui 5 level evaluasi:

#### **Level 1: Screening**
- Personality Test
- Tes Tertulis (minimal 60% untuk lanjut)

#### **Level 2: Technical & Interpersonal Skills**
**Hard Skills (11 aspek):**
- Bahasa Pemrograman (PHP/JS/TS)
- Database MySQL
- Framework Development
- Unit Testing
- SDLC (Software Development Life Cycle)
- Design Pattern
- Microservice Architecture
- Docker Containerization
- CI/CD Pipeline
- Cloud Platform
- Payment Gateway Integration

**Soft Skills (3 aspek):**
- Problem Solving
- Komunikasi
- Adaptabilitas

#### **Level 3: Live Coding Session**
- Pemahaman Konsep Dasar
- Problem Solving & Critical Thinking
- Efisiensi & Kualitas Kode

#### **Level 4: Nilai Tambahan**
- Development Tools Mastery
- Fleksibilitas Jam Kerja
- Konsistensi Career Path
- Sertifikasi Relevan

#### **Level 5: Keputusan Akhir**
Sistem menghasilkan rekomendasi:
- **Layak**: Kandidat memenuhi semua kriteria dengan baik
- **Layak Dipertimbangkan**: Kandidat cukup baik dengan beberapa keunggulan
- **Kurang Layak**: Kandidat tidak memenuhi kriteria minimum

### 4. Hasil & Laporan
Sistem akan menghasilkan laporan komprehensif berisi:
- Ringkasan input per dimensi
- Alur Dual Process evaluation
- Rules yang terpicu
- Rekomendasi final dengan alasan
- Breakdown scoring hard skills

## 🔧 System Logic

### Dual Process Mechanism
Sistem menggunakan pendekatan **binary gate** di setiap level:
- ✅ **PASS**: Lanjut ke level berikutnya
- ❌ **STOP**: Sistem berhenti, kandidat dinyatakan "Kurang Layak"

### Mandatory Factors
**Junior Developer:**
- HS1 (Programming), HS2 (MySQL), HS5 (SDLC), HS6 (Design Pattern)

**Middle Developer:**
- Semua Hard Skills kecuali HS7 (Microservice), HS10 (Cloud), HS11 (Payment Gateway)

### Scoring System
**Hard Skills Scoring:**
- Level 3 (Expert): Bobot 3
- Level 2 (Intermediate): Bobot 2  
- Level 1 (Basic): Bobot 1

**Threshold:**
- Junior: 11-20 poin
- Middle: 21+ poin

## 📊 Example Output

```
=== LAPORAN HASIL SISTEM PAKAR SELEKSI KANDIDAT ===

INFORMASI KANDIDAT:
   Nama      : John Doe
   Posisi    : Middle Fullstack Developer

ALUR DUAL PROCESS:
   Level1: ✓ PASS
   Level2: ✓ PASS
   Level3: ✓ PASS
   Level4: ✓ PASS
   Level5: → COMPLETE

HASIL KEPUTUSAN:
   REKOMENDASI: Layak
   ALASAN     : Kandidat lolos screening dengan sangat baik, memiliki hardskill yang memenuhi, performa live coding sangat baik, dan softskill memadai.
```

## 🧪 Testing

Untuk testing sistem, Anda bisa menggunakan kombinasi input berikut:

### Test Case 1: Layak (Junior)
- Screening: A, A
- Hard Skills: Pilih level 2-3 untuk mandatory factors
- Soft Skills: A/B untuk semua
- Live Coding: A/B untuk semua
- Nilai Tambahan: Bebas

### Test Case 2: Kurang Layak (Screening Gagal)
- Screening: -, C
- Sistem akan berhenti di Level 1

### Test Case 3: Layak Dipertimbangkan
- Screening: B, B
- Hard Skills: Level 2 untuk sebagian besar
- Soft Skills: B untuk semua
- Live Coding: B untuk semua
- Nilai Tambahan: A untuk beberapa

## 👎😔 Weaknesses of this Prototype

1. Rules and Facts are still static
2. Rules and Facts are derived from heuristic analysis based on expert subjectivity
3. Positions used are still limited to one technical position, which is a full-stack developer
4. The system is not integrated with existing recruitment systems  

## 🤝 Contributing

1. Fork repository ini
2. Buat branch feature (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request

---

⭐ **Star this repo if you find it helpful!** ⭐
