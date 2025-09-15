def ask_question(prompt, choices):
    """UI untuk mengajukan pertanyaan dengan pilihan ganda"""
    print(f"\n{prompt}")
    print("-" * 60)
    
    for key, val in choices.items():
        print(f"{key}. {val['text']}")
    
    while True:
        ans = input(f"\nPilihan Anda ({'/'.join(choices.keys())}): ").strip().upper()
        if ans in choices:
            break
        print(f"Pilihan tidak valid! Harap pilih dari: {', '.join(choices.keys())}")
    
    note = input("Catatan tambahan (opsional): ").strip()
    
    print(f"✓ Dipilih: {choices[ans]['text']}")
    if note:
        print(f"  Catatan: {note}")
    
    return {"kode": choices[ans]['kode'], "note": note, "text": choices[ans]['text']}

def collect_candidate_info():
    """Collect basic candidate information"""
    print("=== INFORMASI KANDIDAT ===")
    
    nama = input("Masukkan nama kandidat: ").strip()
    while not nama:
        print("Nama tidak boleh kosong!")
        nama = input("Masukkan nama kandidat: ").strip()
    
    print("\nPilih posisi yang dilamar:")
    print("1. Junior Fullstack Developer")
    print("2. Middle Fullstack Developer")
    
    while True:
        posisi_input = input("Pilihan (1/2): ").strip()
        if posisi_input == "1":
            posisi = "junior"
            break
        elif posisi_input == "2":
            posisi = "middle"
            break
        else:
            print("Pilihan tidak valid! Harap pilih 1 atau 2.")
    
    print(f"\n✓ Kandidat: {nama}")
    print(f"✓ Posisi: {posisi.title()} Fullstack Developer")
    
    return {"nama": nama, "posisi": posisi}