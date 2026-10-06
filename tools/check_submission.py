#!/usr/bin/env python3
"""
Pemeriksa kelengkapan pekerjaan Praktikum 3 (Clustering).

Menjalankan sebelas pemeriksaan struktural pada notebook, laporan, dan README.
Ini BUKAN penilai. Ia tidak menilai kualitas analisis, hanya memastikan pekerjaan
lengkap dan tidak melanggar aturan validitas paling dasar: label dibaca sebelum
konfigurasi dipilih, preprocessing berbeda antar algoritma, atau anggaran
pencarian yang tidak setara.

Pakai:
    python tools/check_submission.py
    python tools/check_submission.py --only label
    python tools/check_submission.py --daftar

Keluar dengan kode 1 bila ada pemeriksaan yang gagal.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Akar repositori mahasiswa. Default: direktori kerja saat ini, sehingga skrip
# tetap benar baik dijalankan dari dalam repositori maupun sebagai salinan
# tepercaya dari luar (autograder: python "$CLASSROOM50_BUNDLE_DIR/check_submission.py").
ROOT = Path.cwd()
PLACEHOLDER = re.compile(r"_\(isi\)_|\(isi\)|^\s*$|^-+$|^_+$", re.IGNORECASE)
ALGORITMA_WAJIB = ("kmeans", "dbscan")
BLOK_LABEL = re.compile(r"^\s*##\s*Blok\s+8\b", re.MULTILINE)

hasil: list[tuple[bool, str, str]] = []


def cek(ok: bool, judul: str, pesan: str = "") -> bool:
    hasil.append((ok, judul, pesan))
    return ok


def baca(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def isi_kosong(nilai: str) -> bool:
    nilai = nilai.strip().strip("*_` ")
    return not nilai or bool(PLACEHOLDER.match(nilai))


def sumber(sel) -> str:
    s = sel.get("source", "")
    return "".join(s) if isinstance(s, list) else s


# --------------------------------------------------------------------------- 1
def cek_identitas(readme: str | None) -> None:
    if readme is None:
        cek(False, "Identitas di README terisi", "README.md tidak ditemukan")
        return
    kosong = []
    for label in ("Nama", "NRP", "Username GitHub"):
        m = re.search(rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|([^|]*)\|", readme)
        if m is None or isi_kosong(m.group(1)):
            kosong.append(label)
    cek(not kosong, "Identitas di README terisi",
        f"belum diisi: {', '.join(kosong)}" if kosong else "")


# ------------------------------------------------------------------------- 2-3
def muat_notebook(path: Path):
    teks = baca(path)
    if teks is None:
        cek(False, "Notebook ditemukan dan valid", f"{path} tidak ditemukan")
        return None
    try:
        return json.loads(teks)
    except json.JSONDecodeError as e:
        cek(False, "Notebook ditemukan dan valid", f"JSON rusak: {e}")
        return None


def sel_kode(nb):
    return [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]


def cek_dijalankan(nb) -> None:
    belum = [i for i, c in enumerate(sel_kode(nb), 1)
             if sumber(c).strip() and c.get("execution_count") is None]
    cek(not belum, "Notebook sudah dijalankan (output tersimpan)",
        f"{len(belum)} sel kode belum dijalankan. Runtime -> Run all, simpan, push ulang."
        if belum else "")


def cek_tanpa_error(nb) -> None:
    err = []
    for i, c in enumerate(sel_kode(nb), 1):
        for out in c.get("outputs", []):
            if out.get("output_type") == "error":
                err.append(f"sel {i}: {out.get('ename', 'Error')}")
    cek(not err, "Tidak ada sel yang error", "; ".join(err[:3]))


# ------------------------------------------------------------------ 4-8 (kode)
def _tanpa_komentar(teks: str) -> str:
    """Buang baris komentar penuh, agar contoh berkomentar tidak dihitung."""
    return "\n".join(b for b in teks.splitlines() if not b.lstrip().startswith("#"))


def _kode(nb) -> str:
    return "\n".join(_tanpa_komentar(sumber(c)) for c in sel_kode(nb))


def _kode_sebelum_label(nb) -> str | None:
    """Kode di semua sel sebelum judul 'Blok 8'. None bila judul itu hilang."""
    potong = []
    for c in nb.get("cells", []):
        if c.get("cell_type") == "markdown" and BLOK_LABEL.search(sumber(c)):
            return "\n".join(potong)
        if c.get("cell_type") == "code":
            potong.append(_tanpa_komentar(sumber(c)))
    return None


def _badan_fungsi(kode: str, nama: str) -> str:
    """Teks definisi fungsi `nama` sampai baris tak berindentasi berikutnya."""
    m = re.search(rf"^def\s+{re.escape(nama)}\s*\(.*?(?=^\S|\Z)", kode, re.DOTALL | re.MULTILINE)
    return m.group(0) if m else ""


def _panggilan(kode: str, nama: str) -> list[str]:
    """Isi tiap pemanggilan `nama(...)`, dengan penyeimbangan kurung."""
    out = []
    for m in re.finditer(rf"\b{re.escape(nama)}\s*\(", kode):
        i, depth = m.end(), 1
        while i < len(kode) and depth:
            depth += {"(": 1, ")": -1}.get(kode[i], 0)
            i += 1
        out.append(kode[m.end():i - 1])
    return out


def cek_label(nb) -> None:
    judul = "Label dikunci sampai Blok 8"
    awal = _kode_sebelum_label(nb)
    if awal is None:
        cek(False, judul, "judul '## Blok 8' tidak ditemukan; jangan mengubah struktur blok notebook.")
        return
    pesan = []
    # Y_REFERENSI hanya boleh DIISI sebelum Blok 8, tidak boleh dibaca.
    tanpa_isi = re.sub(r"\bY_REFERENSI\s*\[[^\]\n]*\]\s*=(?!=)", "", awal)
    tanpa_isi = re.sub(r"\bY_REFERENSI\s*=\s*\{", "", tanpa_isi)
    baca_label = re.findall(r"\bY_REFERENSI\b", tanpa_isi)
    if baca_label:
        pesan.append(f"Y_REFERENSI dibaca {len(baca_label)} kali sebelum Blok 8")
    # Metrik eksternal tidak boleh dipakai sebelum Blok 8, kecuali ARI antar dua
    # hasil clustering di dalam fungsi stabilitas (tidak memakai label).
    luar_stabilitas = awal.replace(_badan_fungsi(awal, "stabilitas"), "")
    for f in ("adjusted_rand_score", "normalized_mutual_info_score", "adjusted_mutual_info_score",
              "homogeneity_score", "completeness_score", "v_measure_score", "fowlkes_mallows_score"):
        n = len(_panggilan(luar_stabilitas, f))
        if n:
            pesan.append(f"{f} dipakai {n} kali sebelum Blok 8 (di luar fungsi stabilitas)")
    cek(not pesan, judul, "; ".join(pesan) +
        (". Konfigurasi harus dipilih tanpa label." if pesan else ""))


def cek_preprocessing(nb) -> None:
    judul = "Preprocessing sama untuk semua algoritma (buat_pipeline)"
    k = _kode(nb)
    badan = _badan_fungsi(k, "buat_pipeline")
    pesan = []
    if not badan:
        pesan.append("fungsi buat_pipeline tidak ditemukan")
    elif "StandardScaler(" not in badan:
        pesan.append("buat_pipeline tidak memuat StandardScaler")
    luar = k.replace(badan, "") if badan else k
    for pola, teks in ((r"\bPipeline\s*\(", "Pipeline"), (r"\bmake_pipeline\s*\(", "make_pipeline"),
                       (r"\b(?:Standard|MinMax|Robust|MaxAbs)Scaler\s*\(", "scaler"),
                       (r"\bnormalize\s*\(", "normalize")):
        n = len(re.findall(pola, luar))
        if n:
            pesan.append(f"{n} {teks} dibuat di luar buat_pipeline")
    cek(not pesan, judul, "; ".join(pesan) +
        (". Semua algoritma harus lewat buat_pipeline yang sama." if pesan else ""))


def cek_anggaran(nb) -> None:
    k = _kode(nb)
    pesan = []
    if not re.search(r"^\s*ANGGARAN_PARAM\s*=\s*\d+", k, re.MULTILINE):
        pesan.append("ANGGARAN_PARAM tidak ditetapkan sebagai bilangan bulat")
    for terlarang in ("GridSearchCV", "RandomizedSearchCV", "ParameterGrid"):
        if re.search(rf"\b{terlarang}\s*\(", k):
            pesan.append(f"{terlarang} dipakai; gunakan ParameterSampler dengan n_iter=ANGGARAN_PARAM")
    cari = _panggilan(k, "ParameterSampler")
    if not cari:
        pesan.append("tidak ada ParameterSampler")
    salah = [c for c in cari if not re.search(r"n_iter\s*=\s*ANGGARAN_PARAM\b", c)]
    if salah:
        pesan.append(f"{len(salah)} pemanggilan ParameterSampler tanpa n_iter=ANGGARAN_PARAM")
    cek(not pesan, "Anggaran pencarian setara untuk semua algoritma", "; ".join(pesan))


def cek_validitas(nb) -> None:
    k = _kode(nb)
    butuh = {
        "lantai (lantai_silhouette dipanggil)": lambda: len(_panggilan(k, "lantai_silhouette")) >= 2,
        "silhouette_score": lambda: bool(re.search(r"silhouette_score\s*\(", k)),
        "davies_bouldin_score": lambda: bool(re.search(r"davies_bouldin_score\s*\(", k)),
        "stabilitas (dipanggil)": lambda: len(_panggilan(k, "stabilitas")) >= 2,
        "simpangan baku (.std / np.std)": lambda: bool(re.search(r"(?:\.std|np\.std)\s*\(", k)),
        "RANDOM_STATE": lambda: bool(re.search(r"^\s*RANDOM_STATE\s*=\s*\d+", k, re.MULTILINE)),
    }
    kurang = [n for n, f in butuh.items() if not f()]
    cek(not kurang, "Lantai, metrik internal ganda, stabilitas, dan seed",
        f"tidak ditemukan: {', '.join(kurang)}" if kurang else "")


def cek_algoritma(nb) -> None:
    judul = "Algoritma tambahan (ALGORITMA_SAYA) terisi"
    k = _kode(nb)
    m = re.search(r"^\s*ALGORITMA_SAYA\s*=\s*\{", k, re.MULTILINE)
    if m is None:
        cek(False, judul, "ALGORITMA_SAYA tidak ditemukan di Blok 4.")
        return
    i, depth = m.end(), 1
    while i < len(k) and depth:
        depth += {"{": 1, "}": -1}.get(k[i], 0)
        i += 1
    kunci = re.findall(r"[\"']([^\"']+)[\"']\s*:\s*\(", k[m.end():i - 1])
    if not kunci:
        cek(False, judul, "isi ALGORITMA_SAYA di Blok 4 dengan satu algoritma dari keluarga berbeda.")
        return
    lain = [n for n in kunci if not any(w in re.sub(r"[\s_\-]", "", n.lower()) for w in ALGORITMA_WAJIB)]
    cek(bool(lain), judul,
        "" if lain else f"{', '.join(kunci)} termasuk keluarga algoritma wajib; tambahkan keluarga lain.")


# ---------------------------------------------------------------------- 9-11
def _bagian(teks: str, nomor: int) -> str:
    m = re.search(rf"^##\s*Bagian {nomor}\b(.*?)(?=^##\s|\Z)", teks, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else ""


def cek_temuan(path: Path, minimal: int = 4) -> None:
    teks = baca(path)
    judul = f"Minimal {minimal} temuan lengkap (Temuan/Bukti/Implikasi)"
    if teks is None:
        cek(False, judul, f"{path} tidak ditemukan")
        return
    blok = re.split(r"^###\s+Temuan\s+\d+\s*$", teks, flags=re.MULTILINE)[1:]
    lengkap, catatan = 0, []
    for n, b in enumerate(blok, 1):
        b = re.split(r"^##\s+", b, flags=re.MULTILINE)[0]
        kurang = []
        for label in ("Temuan", "Bukti", "Implikasi"):
            m = re.search(rf"\*\*{label}:\*\*(.*?)(?=\n\s*\*\*|\Z)", b, re.DOTALL)
            if m is None or len(m.group(1).strip().strip("_*` ")) < 15:
                kurang.append(label)
        if kurang:
            catatan.append(f"Temuan {n} kurang: {'/'.join(kurang)}")
        else:
            lengkap += 1
    cek(lengkap >= minimal, judul,
        f"baru {lengkap} dari {minimal} lengkap. " + "; ".join(catatan[:3]) if lengkap < minimal else "")


LABEL_KARTU = ("Bagian penelitian yang bergantung pada struktur tanpa label",
               "Klaim yang ingin dibuat", "Lantai atau pembanding",
               "Bukti kuantitatif dan stabilitas", "Risiko overinterpretasi dan cara mengujinya",
               "Research gap final, versi kelas", "Research gap final, versi revisi",
               "Apa yang berubah dari v1 dan uji mana yang mengubahnya")
LABEL_PERUBAHAN = LABEL_KARTU[-1]
SLOT_KOSONG = re.compile(r"\*\*\[[^\]]*\]\*\*")


def _isian_kartu(isi: str, label: str) -> str | None:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*(.*?)(?=\n\s*\*\*|\n##|\Z)", isi, re.DOTALL)
    if m is None:
        return None
    # petunjuk _(...)_ dan baris scaffold yang slotnya masih **[...]** tidak dihitung sebagai isian
    isian = re.sub(r"_\(.*?\)_", "", m.group(1), flags=re.DOTALL)
    return "\n".join(b for b in isian.splitlines() if not SLOT_KOSONG.search(b))


def cek_kartu(path: Path) -> None:
    teks = baca(path)
    judul = "Kartu Validitas Struktur dan Research Gap Final terisi lengkap"
    if teks is None:
        cek(False, judul, f"{path} tidak ditemukan")
        return
    isi = _bagian(teks, 2)
    kosong = []
    for label in LABEL_KARTU:
        isian = _isian_kartu(isi, label)
        if isian is None or len(isian.strip().strip("_*`> ")) < 15 or isi_kosong(isian):
            kosong.append(label)
    pesan = f"belum terisi: {', '.join(kosong)}" if kosong else ""
    if LABEL_PERUBAHAN not in kosong:
        perubahan = _isian_kartu(isi, LABEL_PERUBAHAN) or ""
        if not re.search(r"\bU\s?[1-4]\b|\buji\s+[1-4]\b", perubahan, re.IGNORECASE):
            pesan = "paragraf perubahan gap belum menyebut uji mana (U1 sampai U4) yang mengubahnya"
    cek(not pesan, judul, pesan)


def cek_ai(path: Path) -> None:
    teks = baca(path)
    judul = "Penggunaan bantuan AI diungkapkan (Bagian 5)"
    if teks is None:
        cek(False, judul, f"{path} tidak ditemukan")
        return
    isi = _bagian(teks, 5)
    terisi = []
    for baris in isi.splitlines():
        if not baris.strip().startswith("|") or re.match(r"^\s*\|[\s|:-]+\|\s*$", baris):
            continue
        sel = [s.strip() for s in baris.strip().strip("|").split("|")]
        if sel and sel[0].lower() == "alat":
            continue
        if sel and not isi_kosong(sel[0]) and len(sel[0].strip("_*` ")) >= 3:
            terisi.append(sel)
    cek(bool(terisi), judul,
        "" if terisi else "isi minimal satu baris tabel, atau tulis 'Tidak memakai AI' di kolom Alat.")


# --------------------------------------------------------------------------- #
PEMERIKSAAN = {
    "identitas":     "identitas di README terisi",
    "dijalankan":    "notebook sudah dijalankan",
    "error":         "tidak ada sel error",
    "label":         "label dikunci sampai Blok 8",
    "preprocessing": "preprocessing sama untuk semua algoritma",
    "anggaran":      "anggaran pencarian setara (n_iter=ANGGARAN_PARAM)",
    "validitas":     "lantai, metrik internal ganda, stabilitas, seed",
    "algoritma":     "algoritma tambahan ALGORITMA_SAYA terisi",
    "temuan":        "empat temuan lengkap",
    "kartu":         "Kartu Validitas Struktur dan Research Gap Final lengkap",
    "ai":            "penggunaan bantuan AI diungkapkan",
}


def main() -> int:
    p = argparse.ArgumentParser(description="Pemeriksa kelengkapan Praktikum 3 (Clustering)",
                                epilog="Kunci --only: " + ", ".join(PEMERIKSAAN))
    p.add_argument("--notebook", default="notebooks/praktikum03_clustering.ipynb")
    p.add_argument("--laporan", default="laporan/LAPORAN.md")
    p.add_argument("--readme", default="README.md")
    p.add_argument("--root", metavar="DIR", help="akar repositori (default: direktori kerja)")
    p.add_argument("--only", metavar="KUNCI", help="jalankan satu pemeriksaan saja (autograder per-tes)")
    p.add_argument("--daftar", action="store_true", help="tampilkan kunci --only lalu keluar")
    a = p.parse_args()

    global ROOT
    if a.root:
        ROOT = Path(a.root).resolve()

    if a.daftar:
        for k, v in PEMERIKSAAN.items():
            print(f"{k:14s} {v}")
        return 0
    if a.only and a.only not in PEMERIKSAAN:
        print(f"Kunci '{a.only}' tidak dikenal. Pilihan: {', '.join(PEMERIKSAAN)}")
        return 2

    pilih = lambda k: a.only in (None, k)
    kunci_nb = ("dijalankan", "error", "label", "preprocessing", "anggaran", "validitas", "algoritma")

    if pilih("identitas"):
        cek_identitas(baca(ROOT / a.readme))

    nb = None
    if any(pilih(k) for k in kunci_nb):
        nb = muat_notebook(ROOT / a.notebook)
    if nb is not None:
        for kunci, fungsi in (("dijalankan", cek_dijalankan), ("error", cek_tanpa_error),
                              ("label", cek_label), ("preprocessing", cek_preprocessing),
                              ("anggaran", cek_anggaran), ("validitas", cek_validitas),
                              ("algoritma", cek_algoritma)):
            if pilih(kunci):
                fungsi(nb)

    if pilih("temuan"):
        cek_temuan(ROOT / a.laporan)
    if pilih("kartu"):
        cek_kartu(ROOT / a.laporan)
    if pilih("ai"):
        cek_ai(ROOT / a.laporan)

    lolos = sum(1 for ok, _, _ in hasil if ok)
    total = len(hasil)

    if a.only:
        ok, judul, pesan = hasil[-1] if hasil else (False, a.only, "pemeriksaan tidak berjalan")
        print(f"{'PEMERIKSAAN_LOLOS' if ok else 'PEMERIKSAAN_GAGAL'}: {judul}")
        if pesan:
            print(f"  -> {pesan}")
        return 0 if ok else 1

    baris = ["", f"PEMERIKSAAN KELENGKAPAN: {lolos}/{total} lolos", "=" * 58]
    for ok, judul, pesan in hasil:
        baris.append(f"{'[ OK ]' if ok else '[GAGAL]'} {judul}")
        if pesan:
            baris.append(f"        -> {pesan}")
    baris.append("=" * 58)
    baris.append(
        "Semua pemeriksaan lolos. Ini syarat kelengkapan, bukan nilai Anda; "
        "kualitas analisis dinilai terpisah (lihat docs/RUBRIK.md)."
        if lolos == total else "Perbaiki butir yang GAGAL lalu push ulang.")
    print("\n".join(baris))

    ringkasan = os.environ.get("GITHUB_STEP_SUMMARY")
    if ringkasan:
        with open(ringkasan, "a", encoding="utf-8") as f:
            f.write(f"## Pemeriksaan kelengkapan: {lolos}/{total} lolos\n\n")
            f.write("| Status | Pemeriksaan | Catatan |\n|---|---|---|\n")
            for ok, judul, pesan in hasil:
                f.write(f"| {'✅' if ok else '❌'} | {judul} | {pesan or '-'} |\n")

    return 0 if lolos == total else 1


if __name__ == "__main__":
    sys.exit(main())
