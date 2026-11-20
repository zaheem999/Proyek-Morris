from utils.penyimpanan import baca_data, simpan_data
from utils.validasi import input_teks, input_angka, input_nim


def cari_index(data, nim):
    for index, mahasiswa in enumerate(data):
        if str(mahasiswa["nim"]).upper() == nim.upper():
            return index
    return -1


def cetak_tabel(header, baris, rata_kanan=()):
    """Mencetak tabel rapi dengan garis kotak.

    header     : list judul kolom
    baris      : list of list isi tiap baris
    rata_kanan : indeks kolom yang diratakan kanan (untuk angka)
    """
    baris = [[str(sel) for sel in b] for b in baris]
    lebar = [
        max(len(header[i]), *(len(b[i]) for b in baris))
        for i in range(len(header))
    ]

    def garis(kiri, tengah, kanan):
        return kiri + tengah.join("─" * (w + 2) for w in lebar) + kanan

    def cetak_baris(isi):
        sel = []
        for i, teks in enumerate(isi):
            if i in rata_kanan:
                sel.append(f" {teks:>{lebar[i]}} ")
            else:
                sel.append(f" {teks:<{lebar[i]}} ")
        print("│" + "│".join(sel) + "│")

    print(garis("┌", "┬", "┐"))
    cetak_baris([h.center(lebar[i]) for i, h in enumerate(header)])
    print(garis("├", "┼", "┤"))
    for b in baris:
        cetak_baris(b)
    print(garis("└", "┴", "┘"))


def tambah_mahasiswa():
    data = baca_data()
    print("\n--- TAMBAH DATA MAHASISWA ---")
    nim = input_nim()
    if cari_index(data, nim) != -1:
        print("NIM tersebut sudah digunakan.")
        return

    nama = input_teks("Nama lengkap: ")
    umur = input_angka("Umur (tahun): ", 1, 100)
    jenis_kelamin = input_teks("Jenis kelamin: ")
    tinggi = input_angka("Tinggi badan (cm): ", 50, 250, True)
    berat = input_angka("Berat badan (kg): ", 10, 300, True)

    mahasiswa = {
        "nim": nim,
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "tinggi_cm": tinggi,
        "berat_kg": berat,
        "olahraga": [],
        "tidur": []
    }
    data.append(mahasiswa)
    simpan_data(data)
    print("Data mahasiswa berhasil ditambahkan.")


def tampilkan_mahasiswa():
    data = baca_data()
    print("\n--- DAFTAR MAHASISWA ---")
    if not data:
        print("Belum ada data mahasiswa.")
        return

    header = ["No", "NIM", "Nama", "Umur", "Jenis Kelamin", "Tinggi (cm)", "Berat (kg)"]
    baris = [
        [no, m["nim"], m["nama"], m["umur"], m["jenis_kelamin"],
         f"{m['tinggi_cm']:.1f}", f"{m['berat_kg']:.1f}"]
        for no, m in enumerate(data, 1)
    ]
    cetak_tabel(header, baris, rata_kanan=(0, 3, 5, 6))
    print(f"Total: {len(data)} mahasiswa")


def ubah_mahasiswa():
    data = baca_data()
    print("\n--- UBAH DATA MAHASISWA ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return

    m = data[index]
    print("Kosongkan input jika tidak ingin mengubah nilai.")
    nama = input(f"Nama [{m['nama']}]: ").strip()
    umur = input(f"Umur [{m['umur']}]: ").strip()
    jk = input(f"Jenis kelamin [{m['jenis_kelamin']}]: ").strip()
    tinggi = input(f"Tinggi cm [{m['tinggi_cm']}]: ").strip().replace(",", ".")
    berat = input(f"Berat kg [{m['berat_kg']}]: ").strip().replace(",", ".")

    if nama:
        m["nama"] = nama
    if jk:
        m["jenis_kelamin"] = jk
    for key, nilai, minimum, maksimum in [
        ("umur", umur, 1, 100),
        ("tinggi_cm", tinggi, 50, 250),
        ("berat_kg", berat, 10, 300)
    ]:
        if nilai:
            try:
                angka = float(nilai) if key != "umur" else int(nilai)
                if not minimum <= angka <= maksimum:
                    raise ValueError
                m[key] = angka
            except ValueError:
                print(f"Nilai {key} tidak valid; nilai lama dipertahankan.")

    simpan_data(data)
    print("Data mahasiswa berhasil diperbarui.")


def hapus_mahasiswa():
    data = baca_data()
    print("\n--- HAPUS DATA MAHASISWA ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return

    konfirmasi = input(f"Yakin menghapus {data[index]['nama']}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        data.pop(index)
        simpan_data(data)
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def cari_mahasiswa():
    data = baca_data()
    print("\n--- PENCARIAN MAHASISWA ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    m = data[index]
    print(f"NIM            : {m['nim']}")
    print(f"Nama           : {m['nama']}")
    print(f"Umur           : {m['umur']} tahun")
    print(f"Jenis kelamin  : {m['jenis_kelamin']}")
    print(f"Tinggi badan   : {m['tinggi_cm']} cm")
    print(f"Berat badan    : {m['berat_kg']} kg")
