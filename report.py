from mappings import MAPPING

def generate_report(candidat_info, answers, results, triggered_rules, hs_score=None, hs_cat=None):
    print("\n===== RINGKASAN HASIL =====\n")
    
    # print(f"Nama Kandidat : {candidat_info['nama']}")
    # print(f"Posisi        : {candidat_info['posisi']}")
    # print("\nJawaban & Catatan:")

    # for q, ans in answers.items():
    #     kode = ans['kode']
    #     deskripsi = MAPPING.get(kode, kode)  # tampilkan deskripsi kalau ada
    #     note = ans['note']
    #     print(f"- {q}: {deskripsi} | Note: {note}")

    # print("\nHasil Keputusan:")
    # for res in results:
    #     print(f"- {res['Keputusan']} (Alasan: {res['Alasan']})")

    # INPUT
    print("\nINPUT:")
    print(f"- Nama Kandidat : {candidat_info['nama']}")
    print(f"- Posisi        : {candidat_info['posisi']}")
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