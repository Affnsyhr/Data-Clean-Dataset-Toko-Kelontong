# 🏪 Sistem Pembersihan Data Penjualan Toko Cahaya LKZ

Aplikasi berbasis Streamlit untuk melakukan pembersihan (cleaning), transformasi, dan kategorisasi data penjualan secara otomatis sebelum digunakan pada proses analisis dan visualisasi menggunakan Looker Studio.

---

## 📌 Deskripsi

Aplikasi ini dikembangkan untuk membantu proses pengolahan data penjualan Toko Cahaya LKZ periode 2022–2025. Sistem dapat membaca file Excel mentah hasil ekspor dari sistem kasir toko, kemudian melakukan cleaning dan kategorisasi produk secara otomatis.

Hasil akhir berupa dataset bersih yang siap digunakan untuk analisis data dan pembuatan dashboard di Looker Studio.

---

## 🚀 Fitur Utama

* Upload file Excel penjualan mentah
* Cleaning data otomatis
* Standarisasi nama kolom
* Konversi tipe data
* Pembentukan atribut waktu (tahun, bulan, minggu, hari)
* Kategorisasi produk otomatis
* Statistik dataset
* Visualisasi distribusi kategori
* Deteksi produk yang belum terkategorikan
* Export hasil ke format CSV
* Export hasil ke format Excel
* Dataset siap digunakan pada Looker Studio

---

## 📂 Struktur Proyek

```text
toko-cleaning-app/
│
├── app.py
│
├── assets/
│   └── bundalogo.jpeg
│
├── modules/
│   ├── cleaning.py
│   └── categorization.py
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Kategori Produk

Produk akan dikategorikan ke dalam kelompok berikut:

1. Rokok
2. Minuman
3. Makanan
4. Kebutuhan Rumah Tangga
5. Kebutuhan Pribadi
6. Sembako

---

## 🔄 Alur Pengolahan Data

```text
Data Penjualan Mentah
        ↓
Upload ke Aplikasi
        ↓
Cleaning Data
        ↓
Kategorisasi Produk
        ↓
Validasi Produk Lainnya
        ↓
Download Data Bersih
        ↓
Looker Studio
```

---

## ⚠️ Batasan Sistem

Aplikasi ini TIDAK dirancang sebagai alat cleaning data universal.

Sistem hanya dapat digunakan pada dataset penjualan yang memiliki struktur dan format serupa dengan data penjualan Toko Cahaya LKZ.

Beberapa asumsi yang digunakan dalam proses cleaning:

* File sumber berupa format Excel (.xlsx)
* Header data dimulai pada baris ke-4 (header=3)
* Memiliki kolom:

  * No. Faktur
  * Tanggal
  * Kode
  * Item
  * Harga
  * Banyak
  * Total
* Struktur data mengikuti format laporan penjualan yang digunakan dalam penelitian ini

Jika format kolom berbeda, proses cleaning dan kategorisasi dapat menghasilkan error atau data yang tidak sesuai.

---

## 📈 Penggunaan

1. Jalankan aplikasi Streamlit

```bash
streamlit run app.py
```

2. Upload file Excel penjualan mentah

3. Klik tombol "Proses Pembersihan"

4. Tinjau hasil cleaning dan kategorisasi

5. Download hasil dalam format CSV atau Excel

6. Import hasil ke Looker Studio

---

## 🛠️ Library

* Streamlit
* Pandas
* OpenPyXL
* XlsxWriter

---

## 🎓 Tujuan Pengembangan

Aplikasi ini dikembangkan sebagai bagian dari penelitian analisis data penjualan Toko Cahaya LKZ menggunakan pendekatan Business Intelligence dan visualisasi dashboard pada Looker Studio.

Output aplikasi digunakan sebagai proses ETL (Extract, Transform, Load) sederhana untuk menghasilkan dataset yang konsisten, bersih, dan siap dianalisis.
