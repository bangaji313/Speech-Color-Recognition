# Speech Color Recognition 

Proyek Tugas Besar Mata Kuliah **IFB-306 Pengenalan Ucapan dan Teks ke Ucapan**  
Semester Genap 2024/2025 — Institut Teknologi Nasional (ITENAS)

## Anggota Kelompok

| NRP        | Nama Lengkap                    |
|------------|----------------------------------|
| 152022064  | Muhammad Figo Razzan Fadillah    |
| 152022065  | Maulana Seno Aji Yudhantara      |
| 152022077  | Naizirun De Jesus Da Silva       |

---

## Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem **Speech Recognition** yang dapat mengenali kata-kata warna dalam Bahasa Indonesia dari input suara. Kata-kata warna tersebut adalah:

- Merah
- Kuning
- Hijau
- Biru
- Hitam
- Putih
- Warna

---

## Dataset

- Audio direkam oleh 3 penutur berbeda (anggota kelompok)
- Setiap kelas memiliki:
  - 5 audio asli `.wav`
  - 10 audio hasil augmentasi (pitch shift, time stretch, noise)
- Total 15 audio per kelas × 7 kelas × 3 penutur

---

##  Metode yang Digunakan

- **Ekstraksi Fitur**: MFCC (Mel-Frequency Cepstral Coefficients)
- **Metode Klasifikasi**:
  - Dynamic Time Warping (DTW)
  - Hidden Markov Model (HMM)

---

##  Hasil Evaluasi

| Metode | Akurasi Train | Akurasi Test |
|--------|----------------|---------------|
| DTW    | 100%           | 94%           |
| HMM    | 68%            | 65%           |

DTW memberikan hasil yang lebih stabil pada dataset kecil dan variasi terbatas, sedangkan HMM cenderung memerlukan data lebih banyak dan preprocessing tambahan.

