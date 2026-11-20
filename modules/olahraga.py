from datetime import date
from utils.penyimpanan import baca_data, simpan_data
from utils.validasi import input_nim, input_teks, input_angka
from modules.mahasiswa import cari_index


def tambah_olahraga():
    data = baca_data()
    print("\n--- CATAT AKTIVITAS OLAHRAGA ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    jenis = input_teks("Jenis olahraga (contoh: lari, futsal, gym): ")
    durasi = input_angka("Durasi (menit): ", 1, 1440)
    tanggal = input(f"Tanggal [YYYY-MM-DD, default {date.today()}]: ").strip() or str(date.today())
    data[index]["olahraga"].append({
        "jenis": jenis,
        "durasi_menit": durasi,
        "tanggal": tanggal
    })
    simpan_data(data)
    print("Aktivitas olahraga berhasil dicatat.")


def tampilkan_olahraga():
    data = baca_data()
    print("\n--- RIWAYAT OLAHRAGA ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    m = data[index]
    if not m["olahraga"]:
        print("Belum ada catatan olahraga.")
        return
    print(f"Riwayat olahraga {m['nama']}:")
    total = 0
    for nomor, item in enumerate(m["olahraga"], 1):
        print(f"{nomor}. {item['tanggal']} | {item['jenis']} | {item['durasi_menit']} menit")
        total += item["durasi_menit"]
    print(f"Total durasi: {total} menit")
