# Bacaan Lanjutan

Setelah praktikum selesai. Bacaan ini opsional, urut dari yang paling langsung terkait dengan yang Anda kerjakan. Cari melalui judul dan penulis; periksa sendiri bahwa versi yang Anda baca adalah versi terbitan resmi.

## Algoritma yang dipakai

- **Ester, M., Kriegel, H.-P., Sander, J. & Xu, X. (1996).** *A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise.* KDD. Makalah asli DBSCAN, termasuk heuristik k-distance di Blok 4.
- **Campello, R. J. G. B., Moulavi, D. & Sander, J. (2013).** *Density-Based Clustering Based on Hierarchical Density Estimates.* PAKDD. HDBSCAN: jawaban atas masalah satu `eps` untuk kepadatan berbeda (Dataset D).

## Menilai cluster tanpa dan dengan label

- **Rousseeuw, P. J. (1987).** *Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis.* Journal of Computational and Applied Mathematics. Asal silhouette; perhatikan asumsi kekompakan yang membuatnya lemah pada bentuk melengkung.
- **Tibshirani, R., Walther, G. & Hastie, T. (2001).** *Estimating the Number of Clusters in a Data Set via the Gap Statistic.* JRSS B. Ide lantai dari data acak referensi, yang dipakai Blok 3 dalam bentuk sederhana.
- **Hubert, L. & Arabie, P. (1985).** *Comparing Partitions.* Journal of Classification. ARI.
- **Vinh, N. X., Epps, J. & Bailey, J. (2010).** *Information Theoretic Measures for Clusterings Comparison.* JMLR. NMI, AMI, dan kapan masing-masing bias.

## Stabilitas

- **Ben-Hur, A., Elisseeff, A. & Guyon, I. (2002).** *A Stability Based Method for Discovering Structure in Clustered Data.* Pacific Symposium on Biocomputing. Dasar uji subsampel di Blok 6.
- **von Luxburg, U. (2010).** *Clustering Stability: An Overview.* Foundations and Trends in Machine Learning. Mengapa stabil tidak sama dengan benar.

## Visualisasi yang menyesatkan

- **Wattenberg, M., Viégas, F. & Johnson, I. (2016).** *How to Use t-SNE Effectively.* Distill. Contoh visual t-SNE pada data acak dan pengaruh perplexity.
- **Kobak, D. & Berens, P. (2019).** *The Art of Using t-SNE for Single-Cell Transcriptomics.* Nature Communications. Praktik baik melaporkan t-SNE di paper.

## Sikap ilmiah

- **Hennig, C. (2015).** *What Are the True Clusters?* Pattern Recognition Letters. Tidak ada "cluster sejati" tanpa tujuan; pilihan metode adalah pilihan definisi.

## Pertanyaan untuk penelitian Anda

1. Paper terakhir yang Anda baca yang memuat plot t-SNE atau UMAP: apakah ada metrik di ruang asli, pembanding, dan parameter visualisasinya?
2. Bila penelitian Anda memakai clustering atau pengelompokan, apa lantainya?
3. Apakah hasil pengelompokan Anda stabil terhadap seed dan subsampel, dan apakah Anda melaporkannya?
