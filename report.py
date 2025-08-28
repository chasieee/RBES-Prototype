from mappings import MAPPING

def generate_report(candidat_info, answers, results, triggered_rules, hs_score=None, hs_cat=None):
    print("\n===== RINGKASAN HASIL =====\n")

    # INPUT
    print("\nINPUT:")
    print(f"- Nama Kandidat : {candidat_info['nama']}")
    print(f"- Posisi        : {candidat_info['posisi']}")
    print("\nJawaban & Catatan:")
    for q, ans in answers.items():
        print(f"- {q}: {MAPPING.get(ans['kode'], ans['kode'])} | Note: {ans['note']}")

    # PROSES
    print("\nPROSES:")
    for r in triggered_rules:
        print(f"{r}")


    # OUTPUT
    print("\nOUTPUT:")
    if results:
        final = results[-1]   # ambil keputusan terakhir
        print(f"REKOMENDASI: {final['Keputusan']}")
        print(f"ALASAN: {final['Alasan']}")
    else:
        # fallback kalau nggak ada rule global yang kepicu
        print("REKOMENDASI: Kurang Layak (default fallback)")
        print("ALASAN: Tidak memenuhi aturan global")


    # Breakdown tambahan
    if hs_score is not None and hs_cat is not None:
        print(f"\nBreakdown Hard Skill: total {hs_score} poin → {hs_cat}")