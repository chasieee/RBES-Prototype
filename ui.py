def ask_question(prompt, choices):
    print(f"\n{prompt}")
    for key, val in choices.items():
        print(f"{key}. {val['text']}")
    ans = input("Jawaban: ").strip().upper()
    note = input("Catatan (opsional): ").strip()
    return {"kode": choices[ans]['kode'], "note": note}

def collect_candidate_info():
    nama = input("Masukkan nama kandidat: ")
    posisi = input("Posisi yang dilamar (junior/middle): ").lower()
    return {"nama": nama, "posisi": posisi}
