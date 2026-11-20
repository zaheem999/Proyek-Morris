    
from modules.mahasiswa import (
    tambah_mahasiswa,
    tampilkan_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa,
    cari_mahasiswa
)

from modules.kesehatan import (
    tampilkan_imt,
    perbarui_berat_tinggi
)

from modules.olahraga import (
    tambah_olahraga,
    tampilkan_olahraga
)

from modules.tidur import (
    tambah_tidur,
    tampilkan_tidur
)

from modules.statistik import tampilkan_statistik
from utils.penyimpanan import inisialisasi_data


# ==================================================
# FUNGSI GARIS
# ==================================================

def garis(panjang=50, karakter="═"):
    """Membuat garis pembatas pada terminal."""
    print(karakter * panjang)


# ==================================================
# TAMPILAN PEMBUKA
# ==================================================

def tampilan_pembuka():
    """Menampilkan tampilan pembuka aplikasi SIKMA."""

    print()
    garis(52, "═")

    print("     ███████╗██╗██╗  ██╗███╗   ███╗ █████╗")
    print("     ██╔════╝██║██║ ██╔╝████╗ ████║██╔══██╗")
    print("     ███████╗██║█████╔╝ ██╔████╔██║███████║")
    print("     ╚════██║██║██╔═██╗ ██║╚██╔╝██║██╔══██║")
    print("     ███████║██║██║  ██╗██║ ╚═╝ ██║██║  ██║")
    print("     ╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝")

    garis(52, "═")

    print("SIKMA - Sistem Informasi Kesehatan Mahasiswa".center(52))
    print("Tugas Akhir MORRIS Teknik Informatika 2026".center(52))

    print()
    print("Kelompok : [7] DT09")
    print("Tema     : Kesehatan Mahasiswa")

    print()
    print("Aplikasi ini membantu mencatat, mengelola,")
    print("dan memantau informasi kesehatan mahasiswa")
    print("secara praktis melalui terminal.")

    garis(52, "═")
    print()


# ==================================================
# MENU DATA MAHASISWA
# ==================================================

def menu_mahasiswa():

    while True:
        print("\n========== DATA MAHASISWA ==========")
        print("[1]. Tambah Data")
        print("[2]. Tampilkan Data")
        print("[3]. Ubah Data")
        print("[4]. Hapus Data")
        print("[5]. Cari Mahasiswa")
        print("[0]. Kembali")
        garis(36)

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tambah_mahasiswa()

        elif pilih == "2":
            tampilkan_mahasiswa()

        elif pilih == "3":
            ubah_mahasiswa()

        elif pilih == "4":
            hapus_mahasiswa()

        elif pilih == "5":
            cari_mahasiswa()

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# ==================================================
# MENU DATA KESEHATAN
# ==================================================

def menu_kesehatan():

    while True:
        print("\n========== DATA KESEHATAN ==========")
        print("[1]. Hitung IMT / BMI")
        print("[2]. Perbarui Berat dan Tinggi Badan")
        print("[0]. Kembali")
        garis(36)

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tampilkan_imt()

        elif pilih == "2":
            perbarui_berat_tinggi()

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# ==================================================
# MENU AKTIVITAS OLAHRAGA
# ==================================================

def menu_olahraga():

    while True:
        print("\n======= AKTIVITAS OLAHRAGA =======")
        print("[1]. Catat Aktivitas Olahraga")
        print("[2]. Lihat Riwayat Olahraga")
        print("[0]. Kembali")
        garis(34)

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tambah_olahraga()

        elif pilih == "2":
            tampilkan_olahraga()

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# ==================================================
# MENU POLA TIDUR
# ==================================================

def menu_tidur():

    while True:
        print("\n============ POLA TIDUR ============")
        print("[1]. Catat Pola Tidur")
        print("[2]. Lihat Riwayat Tidur")
        print("[0]. Kembali")
        garis(36)

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            tambah_tidur()

        elif pilih == "2":
            tampilkan_tidur()

        elif pilih == "0":
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# ==================================================
# MENU UTAMA
# ==================================================

def menu_utama():

    # Menampilkan pembuka hanya satu kali
    tampilan_pembuka()

    while True:

        print("\n")
        garis(52, "=")
        print("                    SIKMA")
        print("       SISTEM INFORMASI KESEHATAN MAHASISWA")
        garis(52, "=")

        print("[1]. Data Mahasiswa")
        print("[2]. Data Kesehatan")
        print("[3]. Aktivitas Olahraga")
        print("[4]. Pola Tidur")
        print("[5]. Statistik Kesehatan")
        print("[0]. Keluar")

        garis(52, "-")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            menu_mahasiswa()

        elif pilih == "2":
            menu_kesehatan()

        elif pilih == "3":
            menu_olahraga()

        elif pilih == "4":
            menu_tidur()

        elif pilih == "5":
            tampilkan_statistik()

        elif pilih == "0":
            print("\nTerima kasih telah menggunakan SIKMA!")
            print("Semoga kesehatanmu selalu terjaga.")
            garis(52, "═")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih kembali.")


# ==================================================
# PROGRAM UTAMA
# ==================================================

if __name__ == "__main__":

    # Memastikan file penyimpanan tersedia
    inisialisasi_data()

    # Menjalankan aplikasi
    menu_utama()
