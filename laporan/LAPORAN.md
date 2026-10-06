# Laporan Praktikum 3 · Clustering

| | |
|---|---|
| **Nama** | _(isi)_ |
| **NRP** | _(isi)_ |
| **Tanggal** | _(isi)_ |

---

## Bagian 1: Empat Temuan

Format wajib setiap temuan: **Temuan → Bukti → Implikasi**.
Bukti menyebut angka konkret beserta blok asalnya. Implikasi menyebut konsekuensinya terhadap cara Anda memilih, mengevaluasi, atau melaporkan hasil clustering, bukan sekadar "perlu diperhatikan".

Contoh yang benar (jangan dihapus; pakai sebagai acuan bentuk):

> **Temuan:** Skala fitur Dataset D tidak setara.
> **Bukti:** Blok 1, rentang fitur 1 sekitar −2,5 sampai 9,1, sedangkan fitur 2 sekitar −145 sampai 618.
> **Implikasi:** Tanpa standardisasi, jarak Euclid hampir seluruhnya ditentukan fitur 2; standardisasi dimasukkan ke `buat_pipeline` sehingga berlaku sama untuk semua algoritma.

### Temuan 1

_Pertanyaan pemandu: berapa silhouette yang didapat tanpa struktur apa pun, dan dataset mana yang skornya tampak tinggi tetapi tidak jauh dari lantainya? (Blok 3, 5)_

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 2

_Pertanyaan pemandu: di karakter data mana K-Means unggul, dan di mana algoritma berbasis kepadatan unggul? Kaitkan dengan bentuk, noise, dimensi, dan skala. (Blok 5, 8, 10)_

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 3

_Pertanyaan pemandu: apakah konfigurasi yang dipilih silhouette juga yang terbaik menurut label? Di mana silhouette menyesatkan, dan berapa harga tidak punya label? (Blok 8)_

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 4

_Pertanyaan pemandu: apakah cluster yang stabil atau tampak rapi di plot pasti bermakna? Apa yang ditunjukkan Dataset K dan t-SNE pada data acak? (Blok 6, 7)_

**Temuan:**
**Bukti:**
**Implikasi:**

---

## Bagian 2: Kartu Validitas Struktur (penelitian Anda)

Untuk **penelitian Anda sendiri**, bukan dataset praktikum. Kartu ini memakai **Empat Uji Validitas Struktur** dari sesi pekan 6, dua kali: pertama pada struktur dalam penelitian Anda (butir 2a), lalu pada research gap Anda (butir 2b).

| Uji | Pada struktur tanpa label | Pada research gap |
|---|---|---|
| **U1 · Kontrol acak** | Apakah skor dan plot berbeda dari data tanpa struktur? | Apakah gap masih ada setelah pencarian diperluas (sinonim, basis data kedua, terbitan 2024 sampai 2026)? |
| **U2 · Stabilitas** | Apakah struktur bertahan bila seed, subsampel, atau parameter diubah? | Apakah gap muncul di lebih dari satu paper atau setting? |
| **U3 · Asumsi alat** | Apakah metrik dan algoritma cocok dengan bentuk data, dan dihitung di ruang yang benar? | Apakah gap bertahan bila metrik dan baseline diganti ke yang tepat? |
| **U4 · Makna** | Apakah struktur itu bermakna untuk domain atau tugas lanjutan? | Bila gap ditutup, siapa yang terbantu, dan dapatkah diuji dalam satu semester dengan data Anda? |

### 2a · Struktur dalam penelitian Anda

Hampir setiap penelitian punya bagian yang bergantung pada struktur tanpa label: clustering, topik, segmentasi, pengelompokan dokumen, pseudo-label, atau plot embedding (t-SNE/UMAP) sebagai bukti. Bila penelitian Anda benar-benar tidak punya bagian seperti itu, pakai satu klaim struktur atau gambar embedding dari paper acuan utama Anda. Setiap butir minimal satu-dua kalimat yang konkret.

**Bagian penelitian yang bergantung pada struktur tanpa label:** _(apa, di tahap mana, dengan data apa)_

**Klaim yang ingin dibuat:** _(kalimat klaim seperti yang akan tertulis di paper Anda)_

**Lantai atau pembanding:** _(U1: data acak/permutasi, baseline clustering, representasi sederhana; apa yang harus dikalahkan)_

**Bukti kuantitatif dan stabilitas:** _(U2 dan U3: metrik internal mana dan mengapa cocok dengan bentuk data Anda; stabilitas terhadap seed, subsampel, atau hyperparameter)_

**Risiko overinterpretasi dan cara mengujinya:** _(U4: apa yang bisa membuat struktur itu palsu atau tidak bermakna, dan uji yang akan membantahnya)_

### 2b · Research Gap Final (luaran pertemuan 6)

Bagian ini menggantikan tugas Research Gap Final yang terpisah. Isi ketiga butir.

**Research gap final, versi kelas:** _(salin apa adanya dari baris Anda di Kartu Research Gap Final di FigJam, sesi 6 Oktober; jangan diperbaiki)_

**Research gap final, versi revisi:** _(versi setelah komentar sejawat dan praktikum ini, memakai lima slot berikut)_

> Pada **[tugas dan data saya]**, baseline kuat **[metode]** sudah **[apa yang sudah terbukti]**, tetapi belum **[aspek yang belum ditangani]**.
> Gap ini terlihat di **[minimal dua sumber, atau hasil pencarian yang diperluas]**.
> Gap ini bermakna karena **[siapa yang terbantu]** dan dapat diuji dengan **[eksperimen atau ukuran]** pada data saya.
> Uji yang paling berisiko bagi gap ini adalah **[U1 sampai U4]**, dan cara saya menutupnya: **[langkah]**.
> *(Opsional, bahan pekan 7)* Draf kasar RQ: **[...]**

**Apa yang berubah dari v1 dan uji mana yang mengubahnya:** _(satu paragraf: bandingkan Candidate Gap v1 pekan 5, versi kelas, dan versi revisi. Sebut uji mana (U1 sampai U4) yang Goyah atau Gugur, bukti apa yang Anda temukan, dan apa yang Anda ubah karenanya. Bila gap tidak berubah, jelaskan uji mana yang sudah Anda jalankan dan mengapa gap itu bertahan)_

---

## Bagian 3: Audit Klaim Visual

Satu paragraf utuh. Bayangkan Anda menemukan kalimat ini di paper: *"Visualisasi t-SNE menunjukkan lima cluster yang terpisah jelas; metode kami berhasil menemukan segmen yang bermakna."* Serang klaim itu dengan hasil Anda sendiri dari praktikum ini. Bukti apa yang tidak ada, dan uji apa yang Anda minta dari penulisnya?

_(tulis di sini)_

---

## Bagian 4: Refleksi Singkat

Satu hal yang berubah dalam cara Anda menilai klaim "kami menemukan cluster" setelah pekan ini (sekitar 100 sampai 150 kata):

_(tulis di sini)_

---

## Bagian 5: Penggunaan Bantuan AI

Sebutkan alat yang Anda pakai dan untuk bagian apa. Menggunakan AI diperbolehkan; tidak menyebutkannya tidak. Bila Anda memakai agen yang menjalankan notebook atau menulis langsung ke repositori (misalnya Claude Code, Codex, Cursor, OpenCode), sebutkan itu. Bila tidak memakai AI sama sekali, tulis `Tidak memakai AI` di kolom Alat. Tabel kosong dianggap belum diisi.

| Alat | Dipakai untuk bagian | Apa yang Anda verifikasi sendiri |
|---|---|---|
| | | |

---

## Bagian 6 (opsional, nilai tambah): Protokol pada Data Penelitian Anda

Jalankan `jalankan_protokol(X_riset)` di sel opsional notebook. Tempel tabel hasilnya di sini, sebutkan data yang dipakai (sumber, ukuran, subsampel bila ada, fitur atau representasi apa), lalu tulis satu paragraf: apakah ada struktur yang mengalahkan lantai dan stabil? Apa artinya bagi penelitian Anda?

_(opsional)_
