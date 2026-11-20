from utils.penyimpanan import baca_data, simpan_data
from utils.validasi import input_nim, input_angka
from modules.mahasiswa import cari_index


def hitung_imt(berat_kg, tinggi_cm):
    tinggi_meter = tinggi_cm / 100
    return berat_kg / (tinggi_meter ** 2)


def kategori_imt(imt):
    if imt < 18.5:
        return "Berat badan kurang"
    if imt < 25:
        return "Normal"
    if imt < 30:
        return "Berat badan berlebih"
    return "Obesitas"


def tampilkan_imt():
    data = baca_data()
    print("\n--- HASIL INDEKS MASSA TUBUH ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    m = data[index]
    imt = hitung_imt(m["berat_kg"], m["tinggi_cm"])
    print(f"Nama       : {m['nama']}")
    print(f"Berat      : {m['berat_kg']} kg")
    print(f"Tinggi     : {m['tinggi_cm']} cm")
    print(f"Nilai IMT  : {imt:.2f}")
    print(f"Kategori   : {kategori_imt(imt)}")
    print("Catatan: IMT merupakan alat skrining sederhana, bukan diagnosis medis.")


def perbarui_berat_tinggi():
    data = baca_data()
    print("\n--- PERBARUI BERAT DAN TINGGI BADAN ---")
    nim = input_nim()
    index = cari_index(data, nim)
    if index == -1:
        print("Mahasiswa tidak ditemukan.")
        return
    m = data[index]
    print(f"Data saat ini: {m['berat_kg']} kg, {m['tinggi_cm']} cm")
    m["berat_kg"] = input_angka("Berat badan terbaru (kg): ", 10, 300, True)
    m["tinggi_cm"] = input_angka("Tinggi badan (cm): ", 50, 250, True)
    simpan_data(data)
    print("Data antropometri berhasil diperbarui.")
