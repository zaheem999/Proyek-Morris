from utils.penyimpanan import baca_data
from modules.kesehatan import hitung_imt, kategori_imt


def tampilkan_statistik():
    data = baca_data()
    print("\n--- STATISTIK KESEHATAN SIKMA ---")
    if not data:
        print("Belum ada data untuk dihitung.")
        return

    jumlah = len(data)
    daftar_imt = [hitung_imt(m["berat_kg"], m["tinggi_cm"]) for m in data]
    total_olahraga = sum(
        item["durasi_menit"] for m in data for item in m["olahraga"]
    )
    semua_tidur = [item["durasi_jam"] for m in data for item in m["tidur"]]

    print(f"Jumlah mahasiswa       : {jumlah}")
    print(f"Rata-rata IMT          : {sum(daftar_imt) / jumlah:.2f}")
    print(f"Total olahraga         : {total_olahraga} menit")
    print(f"Jumlah catatan tidur   : {len(semua_tidur)}")
    if semua_tidur:
        print(f"Rata-rata durasi tidur : {sum(semua_tidur) / len(semua_tidur):.2f} jam")
    else:
        print("Rata-rata durasi tidur : Belum tersedia")

    print("\nDistribusi kategori IMT:")
    kategori = {}
    for nilai in daftar_imt:
        nama = kategori_imt(nilai)
        kategori[nama] = kategori.get(nama, 0) + 1
    for nama, jumlah_kategori in kategori.items():
        print(f"- {nama}: {jumlah_kategori} mahasiswa")
