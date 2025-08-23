from mappings import MAPPING

def generate_report(candidat_info, answers, results):
    print("\n===== RINGKASAN HASIL =====")
    print(f"Nama Kandidat : {candidat_info['nama']}")
    print(f"Posisi        : {candidat_info['posisi']}")
    print("\nJawaban & Catatan:")

    for q, ans in answers.items():
        kode = ans['kode']
        deskripsi = MAPPING.get(kode, kode)  # tampilkan deskripsi kalau ada
        note = ans['note']
        print(f"- {q}: {deskripsi} | Note: {note}")

    print("\nHasil Keputusan:")
    for res in results:
        print(f"- {res['Keputusan']} (Alasan: {res['Alasan']})")
