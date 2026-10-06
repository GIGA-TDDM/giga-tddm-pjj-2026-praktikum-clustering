# Data Card · Praktikum 3

Repositori ini **tidak menyertakan berkas data**. Keenam dataset dibangkitkan atau dimuat langsung oleh notebook (Blok 1).

| Kode | Nama | Sumber | Ukuran | Label referensi | Karakter |
|---|---|---|---|---|---|
| A | Globular | `make_blobs`, 3 pusat, `random_state=42` | 600 × 2 | 3 kelompok | Gumpalan bulat terpisah: kasus ideal |
| B | Bulan sabit | `make_moons`, `noise=0.08` | 600 × 2 | 2 kelompok | Non-globular, melengkung |
| C | Noise | `make_blobs` 540 titik + 60 titik seragam acak | 600 × 2 | 3 kelompok, noise = `-1` | 10% titik tidak termasuk cluster mana pun |
| D | Kepadatan & skala | `make_blobs` ukuran 300/200/100, simpangan 0,4/1,2/2,2; fitur 2 dikali 50 | 600 × 2 | 3 kelompok | Kepadatan berbeda dan satuan fitur tidak setara |
| E | Wine | Bawaan scikit-learn (`load_wine`), UCI | 178 × 13 | 3 varietas anggur | Data nyata, dimensi lebih tinggi |
| K | Kontrol acak | Seragam acak di persegi satuan | 600 × 2 | Satu kelompok (tidak ada struktur) | Pembanding: skor yang didapat tanpa struktur |

## Peringatan penggunaan

- Dataset A, B, C, D, dan K **sintetis**. Tidak merepresentasikan populasi nyata mana pun.
- Label referensi hanya untuk menilai metode di Blok 8. Di penelitian clustering yang sebenarnya label seperti ini biasanya tidak ada; karena itu label dikunci sampai konfigurasi dipilih.
- Pada Dataset C, titik noise diberi label `-1`. Algoritma yang memaksa setiap titik masuk cluster (misalnya K-Means) akan dinilai lebih rendah oleh ARI karena itu; ini disengaja.
- Pada Dataset K, ARI dan NMI tidak bermakna karena referensinya hanya satu kelompok. Dataset ini dinilai lewat lantai (Blok 3) dan stabilitas (Blok 6).
- Dataset E adalah data kimia anggur terbuka yang lazim untuk pengajaran; varietasnya bukan "cluster sejati" yang dijamin, hanya satu cara pengelompokan yang diketahui.

## Reproduksibilitas

Angka Anda dapat berbeda tipis dari angka teman bila versi scikit-learn berbeda (inisialisasi K-Means dan t-SNE berubah antar versi). Karena itu Blok 0 dan Blok 11 mencatat versi library, `RANDOM_STATE`, dan `ANGGARAN_PARAM`.
