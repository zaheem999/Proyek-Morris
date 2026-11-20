from datetime import date
from utils.penyimpanan import baca_data, simpan_data
from utils.validasi import input_nim, input_angka
from modules.mahasiswa import cari_index


def tambah_tidur():
    data = baca_data()
    print("\n--- CATAT POLA TIDUR ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    durasi = input_angka("Durasi tidur (jam): ", 0.5, 24, True)
    print("Kualitas tidur: 1. Buruk  2. Cukup  3. Baik")
    pilihan = input("Pilih kualitas: ").strip()
    kualitas_map = {"1": "Buruk", "2": "Cukup", "3": "Baik"}
    if pilihan not in kualitas_map:
        print("Pilihan kualitas tidak valid.")
        return
    tanggal = input(f"Tanggal [YYYY-MM-DD, default {date.today()}]: ").strip() or str(date.today())
    data[index]["tidur"].append({
        "durasi_jam": durasi,
        "kualitas": kualitas_map[pilihan],
        "tanggal": tanggal
    })
    simpan_data(data)
    print("Catatan tidur berhasil disimpan.")


def tampilkan_tidur():
    data = baca_data()
    print("\n--- RIWAYAT TIDUR ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    m = data[index]
    if not m["tidur"]:
        print("Belum ada catatan tidur.")
        return
    total = 0
    for nomor, item in enumerate(m["tidur"], 1):
        print(f"{nomor}. {item['tanggal']} | {item['durasi_jam']} jam | {item['kualitas']}")
        total += item["durasi_jam"]
    print(f"Rata-rata durasi tidur: {total / len(m['tidur']):.2f} jam")
