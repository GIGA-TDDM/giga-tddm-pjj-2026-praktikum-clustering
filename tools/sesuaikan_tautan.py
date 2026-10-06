#!/usr/bin/env python3
"""
Menyesuaikan tautan GitHub dan Colab dengan repositori tempat berkas ini berada.

Dua pekerjaan:

1. Mengganti placeholder `__REPO_SLUG__`, `__REPO_NAME__`, `__REPO_SLUG_BADGE__`
   pada repositori yang baru dibuat dari template.

2. Memperbaiki repositori yang terlanjur memuat nama repositori TEMPLATE pada
   badge-nya: kejadian ketika workflow inisialisasi sempat berjalan di
   repositori template itu sendiri sebelum dijadikan sumber salinan.

Yang sengaja TIDAK disentuh: URL `raw.githubusercontent.com` dan konstanta
`REPO_TEMPLATE` di notebook. Keduanya memang harus menunjuk repositori template
yang publik, karena repositori mahasiswa bersifat privat dan URL raw-nya ditolak.

Pakai:
    python tools/sesuaikan_tautan.py --slug ORG/repo-saya --name repo-saya \
        [--template ORG/giga-tddm-pjj-2026-praktikum-clustering] [--periksa]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BERKAS = ("README.md", "notebooks/praktikum03_clustering.ipynb")

# Batas akhir nama repositori. Jangan pakai \b: tanda '-' dihitung sebagai batas
# kata, sehingga nama template (awalan nama repositori mahasiswa) ikut cocok di
# dalam `...-baseline-<username>` dan username tertempel berulang di tiap push.
AKHIR = r"(?=\.git\b|[^\w.\-]|$)"


def badge(slug: str) -> str:
    """Escape untuk teks badge shields.io."""
    return slug.replace("-", "--").replace("_", "__").replace("/", "%2F")


def sesuaikan(teks: str, slug: str, nama: str, template: str | None) -> str:
    teks = teks.replace("__REPO_SLUG_BADGE__", badge(slug))
    teks = teks.replace("__REPO_SLUG__", slug)
    teks = teks.replace("__REPO_NAME__", nama)

    if template and template.lower() != slug.lower():
        t = re.escape(template)
        # Hanya tautan yang seharusnya menunjuk repositori ini sendiri.
        teks = re.sub(rf"(colab\.research\.google\.com/github/){t}{AKHIR}", rf"\g<1>{slug}", teks)
        teks = re.sub(rf"(github\.com/){t}{AKHIR}", rf"\g<1>{slug}", teks)
        teks = re.sub(rf"(?<!/){re.escape(badge(template))}(?=-181717)", badge(slug), teks)
        # `%cd <nama-template>` pada petunjuk klon
        teks = re.sub(rf"(%cd\s+|cd\s+){re.escape(template.split('/')[-1])}{AKHIR}", rf"\g<1>{nama}", teks)
        # raw.githubusercontent.com sengaja dibiarkan menunjuk template.
    return teks


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--slug", required=True, help="owner/repo repositori ini")
    p.add_argument("--name", help="nama repositori tanpa owner (default: bagian akhir --slug)")
    p.add_argument("--template", help="owner/repo template, untuk memperbaiki tautan yang terlanjur salah")
    p.add_argument("--periksa", action="store_true", help="hanya laporkan, jangan tulis")
    p.add_argument("berkas", nargs="*", default=None, help=f"default: {' '.join(BERKAS)}")
    a = p.parse_args()

    nama = a.name or a.slug.split("/")[-1]
    daftar = a.berkas or list(BERKAS)
    berubah = []

    for nama_berkas in daftar:
        f = Path(nama_berkas)
        if not f.exists():
            continue
        asli = f.read_text(encoding="utf-8")
        baru = sesuaikan(asli, a.slug, nama, a.template)
        if baru != asli:
            berubah.append(nama_berkas)
            if not a.periksa:
                f.write_text(baru, encoding="utf-8")

    if berubah:
        print(("perlu disesuaikan: " if a.periksa else "disesuaikan: ") + ", ".join(berubah))
        return 0 if not a.periksa else 1
    print("tautan sudah sesuai")
    return 0


if __name__ == "__main__":
    sys.exit(main())
