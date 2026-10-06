# Rubrik Penilaian

Total 100 poin, ditambah nilai tambah opsional. Pemeriksaan otomatis **tidak menggantikan** rubrik ini: ia hanya gerbang kelengkapan. Pekerjaan yang gagal pemeriksaan dinilai setelah diperbaiki, dengan potongan keterlambatan bila melewati tenggat.

---

## A. Kelengkapan & Reproduksibilitas: 15 poin

| Poin | Kriteria |
|---|---|
| 13 sampai 15 | Notebook jalan penuh tanpa error, seed dan log versi lengkap, identitas terisi, commit rapi, `ALGORITMA_SAYA` terisi dan berjalan |
| 9 sampai 12 | Jalan penuh, satu-dua kelalaian pencatatan |
| 5 sampai 8 | Ada sel tidak dijalankan atau error dibiarkan |
| 0 sampai 4 | Notebook tidak dapat dijalankan ulang |

## B. Validitas Protokol: 25 poin

| Poin | Kriteria |
|---|---|
| 22 sampai 25 | Label tidak dipakai sebelum Blok 8; semua algoritma lewat `buat_pipeline` yang sama; anggaran pencarian setara; lantai dan stabilitas dilaporkan; ruang parameter algoritma tambahan masuk akal untuk data yang sudah distandardisasi |
| 16 sampai 21 | Protokol benar, satu komponen lemah pada algoritma tambahan (misalnya rentang parameter yang tidak pernah menghasilkan konfigurasi valid) |
| 9 sampai 15 | Protokol sebagian benar, ada pelanggaran kecil |
| 0 sampai 8 | Konfigurasi dipilih dengan label, atau preprocessing berbeda antar algoritma |

**Diskualifikasi komponen ini (0 poin):** `k`, `eps`, atau algoritma dipilih berdasarkan ARI/NMI terhadap label referensi.

## C. Kualitas Analisis (Empat Temuan): 30 poin

Yang dinilai adalah **rantai bukti**, bukan panjang tulisan.

| Poin | Kriteria |
|---|---|
| 26 sampai 30 | Keempat temuan menyebut angka dan blok asalnya; setiap skor internal dibandingkan dengan lantainya; membedakan penilaian internal dari eksternal; menjelaskan karakter data yang membuat satu algoritma cocok; tidak menyimpulkan dari plot saja |
| 20 sampai 25 | Bukti angka lengkap, implikasi sebagian generik |
| 12 sampai 19 | Temuan benar tetapi implikasi generik ("perlu diperhatikan") |
| 0 sampai 11 | Menarasikan output tanpa penalaran, atau kurang dari empat temuan |

**Penalti klaim visual:** klaim bahwa cluster "terpisah jelas", "bermakna", atau "berhasil" yang hanya didukung plot, tanpa metrik di ruang asli, lantai, atau stabilitas, memotong 3 poin per klaim.

## D. Kartu Validitas Struktur dan Research Gap Final: 20 poin

### D1. Struktur dalam penelitian Anda (Bagian 2a): 10 poin

| Poin | Kriteria |
|---|---|
| 9 sampai 10 | Menunjuk bagian penelitian sendiri yang bergantung pada struktur tanpa label; klaim ditulis seperti di paper; lantai atau pembanding yang tepat (U1); metrik internal dipilih dengan alasan yang menyebut bentuk data, dan rencana stabilitas (U2, U3); risiko overinterpretasi dan uji pembantahnya (U4) |
| 6 sampai 8 | Lengkap, satu komponen lemah |
| 3 sampai 5 | Tanpa lantai atau pembanding |
| 0 sampai 2 | Generik, atau memakai dataset praktikum alih-alih penelitian sendiri |

### D2. Research Gap Final (Bagian 2b, luaran pertemuan 6): 10 poin

Yang dinilai adalah **empat uji dan kejelasan perubahan dari v1 ke versi revisi**, bukan kerapian bahasa.

| Poin | Kriteria |
|---|---|
| 9 sampai 10 | Versi kelas disalin apa adanya; versi revisi mengisi kelima slot dengan konkret (baseline kuat, minimal dua sumber atau pencarian yang diperluas, siapa yang terbantu, eksperimen pada data sendiri); paragraf perubahan menyebut uji yang Goyah atau Gugur beserta buktinya, dan langkah menutup uji paling berisiko |
| 6 sampai 8 | Revisi lengkap, tetapi perubahan atau bukti per uji masih kabur |
| 3 sampai 5 | Gap masih "belum ada yang memakai metode X", atau tidak ada perbandingan dengan v1 dan versi kelas |
| 0 sampai 2 | Generik, atau versi revisi sama dengan versi kelas tanpa penjelasan uji yang sudah dijalankan |

## E. Audit Klaim Visual & Refleksi: 10 poin

| Poin | Kriteria |
|---|---|
| 9 sampai 10 | Audit merujuk hasil praktikum sendiri (lantai, t-SNE data acak, silhouette vs ARI, stabilitas) dan menyebut uji konkret yang harus diminta; refleksi menyebut perubahan cara menilai klaim |
| 6 sampai 8 | Menyebut kelemahan dan alasan, uji yang diminta masih kabur |
| 3 sampai 5 | Audit umum tanpa merujuk hasil Anda |
| 0 sampai 2 | Menerima klaim tanpa penalaran |

---

## Nilai tambah: Protokol pada Data Penelitian Sendiri (opsional)

Hingga **+10 poin** di luar 100, untuk Bagian 6 laporan yang disertai sel opsional notebook yang benar-benar dijalankan pada data penelitian Anda.

| Poin | Kriteria |
|---|---|
| 8 sampai 10 | Data penelitian sendiri dijelaskan (sumber, ukuran, representasi, subsampel); `jalankan_protokol` dijalankan dan tabelnya ditempel; interpretasi membandingkan skor dengan lantai dan stabilitas, lalu menarik konsekuensi untuk desain penelitian |
| 4 sampai 7 | Dijalankan dan dilaporkan, interpretasi masih dangkal |
| 1 sampai 3 | Dijalankan, tanpa interpretasi |

---

## Penggunaan AI

Menggunakan AI diperbolehkan; tidak menyebutkannya tidak. Tingkat pemakaian AI tidak mengurangi nilai dengan sendirinya: isi dinilai dengan rubrik di atas. Bagian 5 laporan yang kosong atau tidak bermakna diminta direvisi; bila tidak direvisi, dianggap tidak diungkapkan. Dosen dapat meminta penjelasan lisan singkat tentang angka di laporan Anda sendiri.

---

## Yang membedakan nilai A dari nilai B

Nilai B diberikan untuk pekerjaan yang **benar**: protokol adil, angka lengkap dilaporkan.

Nilai A menuntut **penilaian (judgement)**: menunjukkan bahwa Anda tahu kapan sebuah struktur tidak boleh dipercaya. Contoh yang layak A: menolak mengklaim cluster karena silhouette tidak jauh dari lantai; menjelaskan mengapa silhouette memilih jawaban yang salah pada bentuk melengkung; menunjukkan bahwa stabil tidak sama dengan bermakna; mengusulkan pembanding atau uji yang tepat untuk penelitian Anda sendiri.

---

## Keterlambatan

| Keterlambatan | Pengali |
|---|---|
| sampai 24 jam | 0,90 |
| 24 sampai 72 jam | 0,75 |
| lebih dari 72 jam | Dinilai hanya bila ada alasan yang disetujui sebelumnya |
