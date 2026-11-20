# 🩺 SIKMA — Sistem Kesehatan Mahasiswa

> **Tugas Akhir MORRIS Teknik Informatika 2026**
> Tema: Kesehatan Mahasiswa

---

## 📌 Kelompok [7] DT09

| No | Nama Lengkap      | NPM | Peran |
|----|-------------------|-----|-------|
| 1 | Muhamad Ihsan Al Arabi | 714260016  | **Programmer** — Menulis kode `kesehatan.py` , `mahasiswa.py` & `olahraga.py` |
| 2 | Ridwan Sani Alamsyah | 613260004 | **Programmer** — Menulis kode `statistik.py` , `tidur.py` & `main.py` |
| 3 | Mohammad Septian Ramadhan | 613260008 | **Flowchart** — Membuat diagram alur logika program |
| 4 | Aiinah Syahqila Nur Jami | 714260019 | **Dokumentasi** — Menyusun README.md & Spesifikasi |
| 5 | ⁠Muhammad Raka Nizami Aliansyah | 714260032 | **Desainer Poster** — Merancang poster A3  |
| 6 | Jesar Dian Muhammad | 714260023 | **Penguji** — Menguji Program |
| 7 | Rasya Lingga Pratama | 613260019 | **Video/Integrasi** — Merekam & mengedit video |

---

## Deskripsi Aplikasi & Masalah yang Diselesaikan

### Latar Belakang

Kesehatan merupakan salah satu aspek penting yang perlu diperhatikan dalam menunjang aktivitas dan proses belajar mahasiswa. Kondisi kesehatan yang baik dapat membantu mahasiswa menjalankan kegiatan akademik maupun nonakademik secara optimal. Namun, dalam pelaksanaannya, informasi dan pemantauan kesehatan mahasiswa masih sering dilakukan secara manual dan belum terintegrasi dengan baik.

### Tujuan Aplikasi
**SIKMA (Sistem Kesehatan Mahasiswa)** merupakan sebuah aplikasi konsol yang dirancang untuk mempermudah pengelolaan informasi dan data kesehatan mahasiswa secara digital, terstruktur, dan terintegrasi.

Adapun tujuan dari pengembangan aplikasi SIKMA adalah:

1. Mempermudah mahasiswa dalam mengakses informasi terkait kesehatan.
2. Membantu proses pencatatan dan pengelolaan data kesehatan mahasiswa.
3. Memudahkan pemantauan kondisi kesehatan mahasiswa secara berkala.
4. Meningkatkan kesadaran mahasiswa terhadap pentingnya menjaga kesehatan.
5. Mendukung pelayanan kesehatan mahasiswa agar lebih efektif, efisien, dan mudah diakses.

---

## Daftar Fitur dan Cara Penggunaan

Setelah program dijalankan, tampil menu utama. Ketik nomor menu lalu tekan **Enter**. Ketik `0` untuk kembali atau keluar.

### Menu Utama

```
[1]. Data Mahasiswa
[2]. Data Kesehatan
[3]. Aktivitas Olahraga
[4]. Pola Tidur
[5]. Statistik Kesehatan
[0]. Keluar
```

###  Data Mahasiswa (Menu 1)

| Menu | Fitur | Cara Penggunaan |
| ---- | ----- | --------------- |
| 1 | **Tambah Data** | Masukkan NIM, nama, umur (1-100), jenis kelamin, tinggi (50-250 cm), dan berat (10-300 kg). NIM yang sudah terdaftar akan ditolak. |
| 2 | **Tampilkan Data** | Menampilkan seluruh mahasiswa dalam bentuk tabel beserta total data. |
| 3 | **Ubah Data** | Masukkan NIM, lalu isi data yang ingin diubah. **Kosongkan input (Enter)** untuk mempertahankan nilai lama. |
| 4 | **Hapus Data** | Masukkan NIM, lalu konfirmasi dengan `y` untuk menghapus atau `n` untuk membatalkan. |
| 5 | **Cari Mahasiswa** | Masukkan NIM untuk menampilkan detail satu mahasiswa. |

###  Data Kesehatan (Menu 2)

| Menu | Fitur | Cara Penggunaan |
| ---- | ----- | --------------- |
| 1 | **Hitung IMT / BMI** | Masukkan NIM. Program menampilkan berat, tinggi, nilai IMT, dan kategorinya. |
| 2 | **Perbarui Berat dan Tinggi Badan** | Masukkan NIM, lalu isi berat dan tinggi terbaru. |

Kategori IMT yang digunakan:

| Nilai IMT | Kategori |
| --------- | -------- |
| < 18,5 | Berat badan kurang |
| 18,5 - 24,9 | Normal |
| 25,0 - 29,9 | Berat badan berlebih |
| >= 30 | Obesitas |

> IMT hanya alat skrining , bukan diagnosis medis.

###  Aktivitas Olahraga (Menu 3)

| Menu | Fitur | Cara Penggunaan |
| ---- | ----- | --------------- |
| 1 | **Catat Aktivitas Olahraga** | Masukkan NIM, jenis olahraga (contoh: lari, futsal, gym), durasi (1-1440 menit), dan tanggal (format `YYYY-MM-DD`; kosongkan untuk memakai tanggal hari ini). |
| 2 | **Lihat Riwayat Olahraga** | Masukkan NIM. Program menampilkan daftar aktivitas dan total durasi olahraga. |

###  Pola Tidur (Menu 4)

| Menu | Fitur | Cara Penggunaan |
| ---- | ----- | --------------- |
| 1 | **Catat Pola Tidur** | Masukkan NIM, durasi tidur (0,5-24 jam), pilih kualitas (1 = Buruk, 2 = Cukup, 3 = Baik), dan tanggal (kosongkan untuk hari ini). |
| 2 | **Lihat Riwayat Tidur** | Masukkan NIM. Program menampilkan riwayat tidur dan rata-rata durasinya. |

###  Statistik Kesehatan (Menu 5)

Menampilkan ringkasan seluruh data:
- Jumlah mahasiswa
- Rata-rata IMT
- Total durasi olahraga (menit)
- Jumlah catatan tidur dan rata-rata durasi tidur (jam)
- Distribusi kategori IMT

### Fitur Pendukung

- **Validasi input:** teks tidak boleh kosong, angka harus valid dan sesuai batas minimum/maksimum. Koma desimal (`67,5`) otomatis dikonversi menjadi titik.
- **NIM tidak sensitif huruf besar/kecil:** NIM otomatis diubah menjadi huruf kapital.
- **Penyimpanan permanen:** semua perubahan langsung tersimpan ke `data/mahasiswa.json`.
- **Migrasi data lama:** kunci lama `"id"` otomatis diubah menjadi `"nim"`.

---

##  Alur Logika dan Penjelasan Setiap File

###  Struktur Folder

```
SIKMA/
├── main.py
├── README.md
├── data/
│   └── mahasiswa.json
├── modules/
│   ├── mahasiswa.py
│   ├── kesehatan.py
│   ├── olahraga.py
│   ├── tidur.py
│   └── statistik.py
└── utils/
    ├── penyimpanan.py
    └── validasi.py
```

###  Alur Umum Program

1. `main.py` dijalankan, lalu `inisialisasi_data()` memastikan folder `data/` dan file `mahasiswa.json` tersedia (dibuat kosong jika belum ada).
2. `menu_utama()` menampilkan tampilan pembuka sekali, lalu masuk ke perulangan menu utama.
3. Pengguna memilih menu, lalu program memanggil submenu atau fungsi yang sesuai di folder `modules/`.
4. Setiap fungsi modul membaca data dengan `baca_data()`, memproses sesuai kebutuhan, dan bila ada perubahan memanggil `simpan_data()`.
5. Input pengguna diperiksa oleh fungsi di `utils/validasi.py` sebelum diproses.
6. Program berakhir ketika pengguna memilih `0` di menu utama.

###  Penjelasan Per File

#### `main.py` (titik masuk program)
- `======()` mencetak garis pembatas.
- `tampilan_pembuka()` menampilkan logo ASCII SIKMA dan identitas kelompok.
- `menu_mahasiswa()`, `menu_kesehatan()`, `menu_olahraga()`, `menu_tidur()` adalah submenu, masing-masing berisi perulangan `while True` yang memanggil fungsi modul sesuai pilihan dan berhenti saat memilih `0`.
- `menu_utama()` menampilkan menu utama dan mengarahkan ke submenu atau `tampilkan_statistik()`.
- Blok `if __name__ == "__main__"` menjalankan `inisialisasi_data()` lalu `menu_utama()`.

#### `utils/penyimpanan.py` (lapisan penyimpanan data)
- Menentukan lokasi `data/mahasiswa.json` relatif terhadap folder proyek, sehingga program dapat dijalankan dari komputer mana pun.
- `inisialisasi_data()` membuat folder dan file data bila belum ada.
- `migrasi_nim(data)` mengubah kunci lama `id` menjadi `nim` dan menyimpan ulang jika ada perubahan.
- `baca_data()` membaca JSON, memastikan isinya berupa list, dan menjalankan migrasi. Jika file rusak, program menampilkan peringatan dan memakai data kosong agar tidak crash.
- `simpan_data(data)` menulis data ke JSON dengan indentasi rapi dan mendukung karakter non-ASCII.

#### `utils/validasi.py` (validasi input)
- `input_teks(pesan)` meminta teks dan mengulang sampai tidak kosong.
- `input_angka(pesan, minimum, maksimum, desimal)` meminta angka (bulat atau desimal), memeriksa rentang, dan mengulang jika tidak valid.
- `input_nim(pesan)` meminta NIM dan mengubahnya menjadi huruf kapital.

#### `modules/mahasiswa.py` (CRUD data mahasiswa)
- `cari_index(data, nim)` mencari posisi mahasiswa berdasarkan NIM, mengembalikan `-1` jika tidak ada. Fungsi ini dipakai oleh hampir semua modul lain.
- `cetak_tabel(header, baris, rata_kanan)` mencetak tabel berbingkai dengan lebar kolom otomatis.
- `tambah_mahasiswa()` memeriksa NIM unik, meminta data, lalu menambahkan record baru (dengan list `olahraga` dan `tidur` kosong).
- `tampilkan_mahasiswa()` menampilkan semua mahasiswa dalam tabel.
- `ubah_mahasiswa()` mengubah data per kolom; input kosong berarti nilai lama dipertahankan, dan nilai di luar rentang ditolak.
- `hapus_mahasiswa()` menghapus data setelah konfirmasi.
- `cari_mahasiswa()` menampilkan detail satu mahasiswa.

#### `modules/kesehatan.py` (IMT dan data antropometri)
- `hitung_imt(berat_kg, tinggi_cm)` menghitung IMT = berat / (tinggi dalam meter)^2.
- `kategori_imt(imt)` mengembalikan kategori berdasarkan nilai IMT.
- `tampilkan_imt()` mencari mahasiswa, menghitung IMT, dan menampilkan hasilnya.
- `perbarui_berat_tinggi()` memperbarui berat dan tinggi badan lalu menyimpannya.

#### `modules/olahraga.py` (aktivitas olahraga)
- `tambah_olahraga()` menambahkan catatan (`jenis`, `durasi_menit`, `tanggal`) ke list `olahraga` milik mahasiswa.
- `tampilkan_olahraga()` menampilkan riwayat bernomor beserta total durasi.

#### `modules/tidur.py` (pola tidur)
- `tambah_tidur()` menambahkan catatan (`durasi_jam`, `kualitas`, `tanggal`) ke list `tidur`.
- `tampilkan_tidur()` menampilkan riwayat dan rata-rata durasi tidur.

#### `modules/statistik.py` (statistik keseluruhan)
- `tampilkan_statistik()` menghitung dan menampilkan jumlah mahasiswa, rata-rata IMT, total olahraga, rata-rata tidur, dan distribusi kategori IMT dengan memanfaatkan `hitung_imt` dan `kategori_imt`.

#### `data/mahasiswa.json` (basis data)
File penyimpanan berupa list objek mahasiswa. Contoh struktur satu record:

```json
{
    "nim": "6123456789",
    "nama": "Lamine Yamal",
    "umur": 19,
    "jenis_kelamin": "Laki-Laki",
    "tinggi_cm": 180.0,
    "berat_kg": 67.0,
    "olahraga": [
        { "jenis": "Gym", "durasi_menit": 40, "tanggal": "2026-11-18" }
    ],
    "tidur": [
        { "durasi_jam": 7.0, "kualitas": "Baik", "tanggal": "2026-11-18" }
    ]
}
```

---

##  Cara Menjalankan Program di Komputer Lain

### Persyaratan
- **Python 3.8 atau lebih baru.** Cek dengan `python --version` (atau `python3 --version`).
- **Tidak perlu menginstal library tambahan.** Program hanya memakai pustaka bawaan Python (`json`, `pathlib`, `datetime`).
- Terminal yang mendukung **UTF-8** agar logo dan tabel tampil dengan benar (Windows Terminal, PowerShell, CMD modern, atau terminal Linux/macOS).

### Langkah-langkah

1. **Salin seluruh folder proyek** ke komputer tujuan (lewat flashdisk, ZIP, atau `git clone`). Pastikan struktur folder sama seperti pada bagian Struktur, yaitu `main.py` di folder utama serta folder `modules/`, `utils/`, dan `data/`.
2. **Buka terminal** lalu masuk ke folder proyek:
   ```bash
   cd path/ke/folder/SIKMA
   ```
3. **Jalankan program** dari folder utama (bukan dari dalam `modules/` atau `utils/`):
   ```bash
   python main.py
   ```
   Pada Linux/macOS, gunakan `python3 main.py` bila perintah `python` tidak tersedia.
4. Ikuti menu yang tampil di layar.


---

*SIKMA - Tugas Akhir MORRIS Teknik Informatika 2026 - Kelompok 7 DT09*
