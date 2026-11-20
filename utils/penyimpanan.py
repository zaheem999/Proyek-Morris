import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
FILE_MAHASISWA = DATA_DIR / "mahasiswa.json"


def inisialisasi_data():
    DATA_DIR.mkdir(exist_ok=True)
    if not FILE_MAHASISWA.exists():
        simpan_data([])


def migrasi_nim(data):
    """Mengubah kunci lama "id" menjadi "nim" agar data lama tetap terbaca."""
    berubah = False
    hasil = []
    for m in data:
        if "id" in m and "nim" not in m:
            m = {("nim" if k == "id" else k): v for k, v in m.items()}
            berubah = True
        hasil.append(m)
    if berubah:
        simpan_data(hasil)
    return hasil


def baca_data():
    inisialisasi_data()
    try:
        with FILE_MAHASISWA.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            return []
        return migrasi_nim(data)
    except (json.JSONDecodeError, OSError):
        print("Peringatan: file data tidak dapat dibaca. Data kosong digunakan.")
        return []


def simpan_data(data):
    DATA_DIR.mkdir(exist_ok=True)
    with FILE_MAHASISWA.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
