# Praktikum 3 · Clustering

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/__REPO_SLUG__/blob/main/notebooks/praktikum03_clustering.ipynb)
[![Repo](https://img.shields.io/badge/GitHub-__REPO_SLUG_BADGE__-181717?logo=github)](https://github.com/__REPO_SLUG__)
[![Pemeriksaan](https://github.com/__REPO_SLUG__/actions/workflows/check-submission.yml/badge.svg)](https://github.com/__REPO_SLUG__/actions/workflows/check-submission.yml)

**EF235161 Topik Dalam Data Mining (P) · S-2 Teknik Informatika · ITS**
Clustering & Unsupervised Data Mining · pengerjaan asinkron, ±3 jam

---

## Identitas

Isi tabel ini lebih dulu, lalu commit. Ini bagian pertama yang diperiksa.

| | |
|---|---|
| **Nama** | _(isi)_ |
| **NRP** | _(isi)_ |
| **Username GitHub** | _(isi)_ |

---

## Pesan utama

> **Plot yang rapi bukan bukti. Cluster baru layak diklaim bila mengalahkan lantai tanpa struktur, stabil, dan dipilih tanpa mengintip label.**

Sesi pekan 6 membahas mengapa evaluasi unsupervised lebih sulit daripada supervised. Praktikum ini adalah sisi eksperimennya: Anda membandingkan K-Means dan DBSCAN secara adil pada enam dataset berkarakter berbeda, menambah satu algoritma pilihan Anda sendiri, lalu memeriksa apakah struktur yang ditemukan bisa dipertanggungjawabkan.

| | Tahap | Inti |
|---|---|---|
| 1 | **Enam dataset** (Blok 1) | Globular, bulan sabit, noise, kepadatan dan skala berbeda, data nyata 13 dimensi, dan kontrol tanpa struktur. |
| 2 | **Protokol dan lantai** (Blok 2 sampai 3) | Label dikunci. Berapa skor yang didapat ketika tidak ada cluster sama sekali? |
| 3 | **Pencarian setara, dipilih tanpa label** (Blok 4 sampai 5) | Anggaran sama, preprocessing sama. **Tugas kode Anda ada di sini.** |
| 4 | **Sensitivitas, stabilitas, jebakan visual** (Blok 6 sampai 7) | Stabil belum tentu bermakna; t-SNE membuat data acak tampak berkelompok. |
| 5 | **Buka label sekali** (Blok 8 sampai 11) | ARI dan NMI, harga tidak punya label, profil cluster data nyata. |

---

## Mulai: pilih satu jalur

### Jalur A · Google Colab (dianjurkan, tanpa instalasi)

1. Klik badge **Open In Colab** di atas.
2. Klik **Copy to Drive** di bar atas notebook.
3. Kerjakan. Untuk menyimpan, ikuti penyambungan di bawah, sekali saja.

### Menyambungkan Colab ke repositori Anda, sekali di awal

1. **Klik `Copy to Drive`** di bar atas notebook. Tanpa ini, menu `File` tidak menampilkan pilihan simpan ke GitHub (yang ada hanya *Save a copy as a GitHub Gist*, bukan itu yang kita pakai).
2. **Hubungkan akun GitHub:** `File → Open notebook → tab GitHub`, centang **Include private repositories**, lalu *Authorize*. Repositori Anda privat, jadi tanpa centang ini ia tidak muncul.
3. Sesudahnya `File → Save a copy in GitHub` tersedia. Pilih repositori praktikum Anda, branch `main`, dan **perbaiki path menjadi** `notebooks/praktikum03_clustering.ipynb` (Colab sering mengisinya `Copy of ...`).

**Jalan terakhir bila gagal:** `File → Download → Download .ipynb`, lalu di repositori klik `Add file → Upload files`, letakkan di `notebooks/` dengan nama yang sama.

Tidak ada berkas data yang harus diunggah: semua dataset dibangkitkan atau dimuat langsung dari scikit-learn.

### Jalur B · Lokal (Jupyter)

```bash
git clone https://github.com/__REPO_SLUG__.git
cd __REPO_NAME__
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/praktikum03_clustering.ipynb
```

### Jalur C · GitHub Codespaces

**Code → Codespaces → Create codespace on main**, lalu `pip install -r requirements.txt`.

---

## Isi repositori

```
.
├── notebooks/praktikum03_clustering.ipynb <- kerjakan di sini
├── laporan/LAPORAN.md                     <- dan di sini
├── data/DATA_CARD.md                      <- asal-usul keenam dataset
├── docs/
│   ├── ALUR_PRAKTIKUM.md                  <- peta blok beserta maksudnya
│   ├── RUBRIK.md                          <- dasar penilaian, termasuk nilai tambah
│   └── BACAAN_LANJUTAN.md                 <- bacaan setelah praktikum
├── tools/check_submission.py              <- pemeriksa yang dijalankan CI
├── outputs/                               <- gambar hasil notebook
└── requirements.txt
```

---

## Deliverable

1. **`notebooks/praktikum03_clustering.ipynb`**: dijalankan penuh dari atas ke bawah, output tersimpan, setiap blok diberi interpretasi, dan `ALGORITMA_SAYA` terisi dengan satu algoritma dari keluarga berbeda.
2. **`laporan/LAPORAN.md`**: empat temuan (Temuan → Bukti → Implikasi), **Kartu Validitas Struktur** untuk penelitian Anda sendiri beserta **Research Gap Final** (versi kelas dari FigJam, versi revisi, dan paragraf perubahan yang menyebut uji U1 sampai U4), satu paragraf audit klaim visual, refleksi, dan penggunaan bantuan AI.
3. **Opsional, nilai tambah hingga +10:** jalankan protokol pada data penelitian Anda sendiri (sel terakhir notebook) dan laporkan di Bagian 6.
4. Commit dan push sebelum tenggat. Yang dinilai adalah commit terakhir sebelum tenggat.

---

## Pemeriksaan otomatis

Setiap push, GitHub Actions menjalankan `tools/check_submission.py`. Hasilnya berupa centang hijau atau silang merah, dan rincian di tab **Actions**.

| # | Pemeriksaan |
|---|---|
| 1 | Identitas di README terisi |
| 2 | Notebook **benar-benar sudah dijalankan** (bukan sekadar disimpan) |
| 3 | Tidak ada sel yang error |
| 4 | Label referensi (`Y_REFERENSI`) tidak dibaca sebelum Blok 8 |
| 5 | Semua algoritma lewat `buat_pipeline` yang sama (tidak ada scaler tambahan) |
| 6 | Anggaran pencarian setara: setiap `ParameterSampler` memakai `n_iter=ANGGARAN_PARAM` |
| 7 | Lantai, dua metrik internal, stabilitas, simpangan baku, dan seed dilaporkan |
| 8 | `ALGORITMA_SAYA` terisi dengan algoritma selain K-Means dan DBSCAN |
| 9 | Empat temuan lengkap di laporan |
| 10 | Kartu Validitas Struktur dan Research Gap Final terisi lengkap; paragraf perubahan gap menyebut uji (U1 sampai U4) |
| 11 | Penggunaan bantuan AI diungkapkan (atau ditulis "Tidak memakai AI") |

**Pemeriksaan ini bukan nilai Anda.** Ia memastikan pekerjaan lengkap dan tidak melanggar aturan validitas dasar. Centang hijau penuh tetap bisa berujung nilai sedang bila analisis Anda dangkal; itulah yang dinilai. Lihat `docs/RUBRIK.md`.

Menjalankan pemeriksa sebelum push:

```bash
python tools/check_submission.py                 # semua pemeriksaan
python tools/check_submission.py --daftar        # daftar kunci
python tools/check_submission.py --only label    # satu pemeriksaan
```

Pemeriksa hanya memakai pustaka standar Python.

---

## Aturan

- **Label dikunci sampai Blok 8.** Memilih `k`, `eps`, atau algoritma dengan melihat label membuat hasil Anda tidak berlaku untuk penelitian nyata, yang tidak punya label.
- **Preprocessing dan anggaran pencarian sama untuk semua algoritma.** Jangan memberi algoritma favorit Anda lebih banyak percobaan atau scaler sendiri.
- Dataset di notebook adalah data pembelajaran (bawaan scikit-learn dan sintetis). Jangan dipakai sebagai dasar klaim empiris atau benchmark penelitian.
- Boleh berdiskusi; notebook dan laporan dikerjakan sendiri. Sebutkan bantuan AI beserta bagian yang dibantu di Bagian 5 laporan, termasuk bila memakai agen yang menjalankan notebook atau menulis ke repositori. Dosen dapat meminta penjelasan lisan singkat tentang angka di laporan Anda.

---

## Bila macet

| Gejala | Tindakan |
|---|---|
| `NameError: ANGGARAN_PARAM` atau `buat_pipeline` | Anda melompati Blok 2. **Runtime → Run all** dari atas. |
| `TypeError` di Blok 5 setelah mengisi `ALGORITMA_SAYA` | Fungsi pembuat harus menerima `**p`, misalnya `lambda **p: AgglomerativeClustering(**p)`, dan nama parameter di ruang pencarian tanpa awalan. |
| Algoritma Anda "tidak ada yang valid" di semua dataset | Rentang parameternya tidak cocok untuk data yang sudah distandardisasi. Perbaiki rentangnya, bukan aturan pilihnya. |
| Pemeriksaan #5 gagal | Hapus scaler dari `ALGORITMA_SAYA`; `buat_pipeline` sudah menstandardisasi. |
| Pemeriksaan #8 gagal padahal sudah diisi | Nama algoritma tidak boleh memuat "kmeans" atau "dbscan"; pilih keluarga lain. |
| Angka Anda berbeda tipis dari teman | Wajar bila versi scikit-learn berbeda; lihat log Blok 0 dan Blok 11. |
| Pemeriksaan "sudah dijalankan" gagal | **Runtime → Run all**, simpan, push ulang. |

---

## Lisensi & atribusi

Materi: CC BY-SA 4.0. Kode di `tools/`: MIT. Lihat `LICENSE`.
Disiapkan oleh GIGA ITS Lab, Departemen Teknik Informatika, Institut Teknologi Sepuluh Nopember.
