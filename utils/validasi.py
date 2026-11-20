def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def input_angka(pesan, minimum=None, maksimum=None, desimal=False):
    while True:
        nilai = input(pesan).strip().replace(",", ".")
        try:
            angka = float(nilai) if desimal else int(nilai)
            if minimum is not None and angka < minimum:
                print(f"Nilai minimal adalah {minimum}.")
                continue
            if maksimum is not None and angka > maksimum:
                print(f"Nilai maksimal adalah {maksimum}.")
                continue
            return angka
        except ValueError:
            print("Masukkan angka yang valid.")


def input_nim(pesan="Masukkan NIM mahasiswa: "):
    return input_teks(pesan).upper()
