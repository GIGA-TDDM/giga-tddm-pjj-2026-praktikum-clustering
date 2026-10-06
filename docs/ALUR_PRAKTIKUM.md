# Alur Praktikum · 12 Blok

Peta ini menjelaskan **maksud** setiap blok, bukan jawabannya. Bacalah sebelum mulai agar Anda tahu ke mana arah pekerjaan.

Perkiraan waktu: 3 jam, termasuk menulis interpretasi dan laporan. Runtime notebook sendiri sekitar 1 sampai 2 menit.

---

## Tahap 1 · Siapkan medan yang adil (Blok 0 sampai 3)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **0** | Versi library, `RANDOM_STATE` | Mengapa hasil K-Means dan t-SNE bisa berbeda antar komputer? |
| **1** | Enam dataset dengan karakter berbeda, label dikunci | Apa yang Anda lihat di plot mentah, sebelum algoritma apa pun? |
| **2** | Protokol: label dikunci, `buat_pipeline`, `ANGGARAN_PARAM`, aturan pilih | Mengapa memilih `k` dengan label sama dengan tuning di test set? |
| **3** | Lantai: silhouette pada data tanpa struktur | Berapa skor yang didapat ketika sebenarnya tidak ada cluster? |

Konsep kunci: **lantai**. Silhouette 0,4 terdengar lumayan, sampai Anda tahu data acak pun mendapat angka itu.

## Tahap 2 · Cari dan pilih tanpa label (Blok 4 sampai 5)

| Blok | Isi | Pertanyaan |
|---|---|---|
| **4** | k-distance plot, ruang pencarian, **tugas kode Anda**: `ALGORITMA_SAYA` | Mengapa algoritma tambahan Anda cocok untuk karakter data tertentu? |
| **5** | Pencarian `ANGGARAN_PARAM` konfigurasi per algoritma, pilih dengan silhouette | Dataset mana yang skornya tinggi tetapi dekat lantai? |

## Tahap 3 · Uji apa yang tidak bisa dilihat mata (Blok 6 sampai 7)

| Blok | Isi | Pertanyaan |
|---|---|---|
| **6** | Sensitivitas terhadap `k`; stabilitas antar subsampel | Apakah stabil berarti bermakna? |
| **7** | PCA data nyata; t-SNE pada data acak lalu K-Means di atasnya | Apa yang dibuktikan, dan tidak dibuktikan, oleh sebuah plot? |

Konsep kunci: **visualisasi adalah alat komunikasi, bukan alat validasi**.

## Tahap 4 · Buka label dan tafsirkan (Blok 8 sampai 11)

| Blok | Isi | Pertanyaan |
|---|---|---|
| **8** | Label dibuka **satu kali**: ARI, NMI, harga tidak punya label, peran standardisasi | Kapan silhouette dan ARI tidak sepakat? |
| **9** | Profil cluster Dataset E | Bisakah cluster dijelaskan dengan bahasa domain? |
| **10** | Ringkasan lintas dataset | Adakah algoritma yang terbaik untuk semua karakter data? |
| **11** | Log reproduksibilitas | Apa yang harus tercatat agar orang lain bisa mengulang? |

Konsep kunci: **kecocokan algoritma adalah sifat pasangan algoritma dan data**, sama seperti strong baseline di Praktikum 2.

---

## Dari praktikum ke penelitian Anda

Sel opsional di akhir notebook menyediakan `jalankan_protokol(X_riset)`: lantai, pencarian beranggaran setara, dan stabilitas dalam satu panggilan, tanpa label. Menjalankannya pada data penelitian Anda dan menulis hasilnya di Bagian 6 laporan dinilai sebagai **nilai tambah**. Kartu Validitas Struktur di Bagian 2 laporan memakai **Empat Uji Validitas Struktur** dari sesi pekan 6 dan memuat **Research Gap Final**, luaran RPS pekan 6: versi kelas, versi revisi, dan apa yang berubah.
