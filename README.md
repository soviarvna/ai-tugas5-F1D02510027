
# SISTEM PAKAR PENENTUAN PRIORITAS BELAJAR MAHASISWA

## 1. Nama dan NIM

- **Nama:** Sovia Rovana Fikri
- **NIM:** F1D02510027
- **Mata Kuliah:** Kecerdasan Buatan

## 2. Topik dan Cara Menjalankan Program

### Topik

Sistem Pakar Penentuan Prioritas Belajar Mahasiswa.

Program ini dibuat untuk membantu mahasiswa menentukan prioritas belajar berdasarkan kondisi perkuliahan, seperti deadline tugas, jadwal ujian, tingkat kesulitan materi, pemahaman terhadap materi, tugas yang belum selesai, dan bobot nilai.

Sistem memberikan tiga kategori hasil, yaitu:

1. **Prioritas Utama:** Materi atau tugas yang perlu segera diperhatikan karena kondisinya mendesak.
2. **Prioritas Tinggi:** Materi yang membutuhkan perhatian lebih karena sulit dipahami atau berkaitan dengan tugas yang belum selesai.
3. **Prioritas Rutin:** Materi yang tetap perlu dipelajari secara teratur meskipun tidak dalam kondisi mendesak.

Jika tidak ada aturan yang terpenuhi, sistem akan menampilkan bahwa tidak ada prioritas khusus yang dapat ditentukan.

### Bahasa dan Versi

- Bahasa pemrograman: Python
- Versi: Python 3
- Format basis pengetahuan: JSON
- Metode inferensi: Forward Chaining

### File Program

- `main.py` : Berisi kode utama program dan proses Forward Chaining.
- `aturan.json` : Berisi fakta, pertanyaan, aturan IF-THEN, dan sumber pengetahuan.

### Cara Menjalankan Program

1. Pastikan Python 3 sudah terpasang di komputer.
2. Simpan file `main.py` dan `aturan.json` dalam satu folder.
3. Buka folder tersebut menggunakan Visual Studio Code.
4. Buka terminal pada folder program.
5. Jalankan perintah berikut:

```bash
python main.py
```

Jika perintah tersebut tidak berhasil, gunakan:

```bash
py main.py
```

6. Setelah program berjalan, jawab pertanyaan yang diberikan.
7. Masukkan `y` untuk jawaban Ya dan `t` untuk jawaban Tidak.
8. Setelah semua pertanyaan dijawab, program akan menampilkan hasil prioritas belajar beserta alasan penentuannya.

## 3. Daftar Sumber dan Tabel Aturan

### A. Daftar Sumber

Sumber pengetahuan digunakan sebagai dasar dalam menyusun aturan pada sistem pakar. Sumber yang digunakan berasal dari beberapa universitas yang membahas manajemen waktu dan strategi belajar.

**Sumber 1**

- Judul: Key Time Management Skills
- Penerbit: Monash University
- URL: https://www.monash.edu/student-academic-success/goal-setting-and-time-management/key-time-management-skills

**Sumber 2**

- Judul: Time Management
- Penerbit: University of Sydney
- URL: https://www.sydney.edu.au/students/study-skills/time-management.html

**Sumber 3**

- Judul: Effective Study Strategies
- Penerbit: Cornell University
- URL: https://lsc.cornell.edu/how-to-study/studying-for-and-taking-exams/effective-study-strategies/

Tanggal akses seluruh sumber: 13 November 2026.

### B. Tabel Aturan (Rule Base)

Basis pengetahuan pada sistem ini terdiri dari tujuh aturan IF-THEN yang digunakan untuk menghasilkan kesimpulan.

| Kode | Aturan IF-THEN | Sumber |
|---|---|---|
| R1 | IF deadline_dekat OR ujian_dekat THEN tenggat_mendesak | S1, S2 |
| R2 | IF materi_sulit AND pemahaman_rendah THEN perlu_pendalaman | S2, S3 |
| R3 | IF tugas_belum_selesai AND tenggat_mendesak THEN beban_tugas_mendesak | S1, S2 |
| R4 | IF tenggat_mendesak AND bobot_nilai_tinggi THEN prioritas_utama | S1, S2 |
| R5 | IF beban_tugas_mendesak THEN prioritas_utama | S1, S2 |
| R6 | IF perlu_pendalaman AND tugas_belum_selesai THEN prioritas_tinggi | S2, S3 |
| R7 | IF pemahaman_baik AND deadline_tidak_dekat THEN prioritas_rutin | S3 |

### C. Keterangan Fakta

- `deadline_dekat` : Deadline tugas sudah dekat.
- `ujian_dekat` : Jadwal ujian sudah dekat.
- `materi_sulit` : Materi perkuliahan sulit dipahami.
- `pemahaman_rendah` : Pemahaman terhadap materi masih rendah.
- `tugas_belum_selesai` : Masih terdapat tugas yang belum selesai.
- `bobot_nilai_tinggi` : Tugas atau ujian memiliki bobot nilai tinggi.
- `pemahaman_baik` : Mahasiswa sudah memahami materi dengan baik.
- `deadline_tidak_dekat` : Deadline tugas masih cukup lama.

### D. Keterangan Sumber pada Aturan

- S1: Monash University.
- S2: University of Sydney.
- S3: Cornell University.

## 4. Metode yang Dipilih dan Alasannya

Metode inferensi yang digunakan dalam sistem pakar ini adalah **Forward Chaining (FC)**.

Forward Chaining merupakan metode penalaran yang dimulai dari fakta atau kondisi awal yang diberikan oleh pengguna. Fakta tersebut kemudian dicocokkan dengan aturan yang tersedia sampai sistem mendapatkan kesimpulan.

Metode Forward Chaining dipilih karena sesuai dengan cara kerja program. Pengguna memberikan jawaban terlebih dahulu, kemudian sistem memproses jawaban tersebut untuk menentukan prioritas belajar mahasiswa.

### Langkah Kerja Forward Chaining

1. Pengguna menjawab pertanyaan yang diberikan oleh program.
2. Jawaban pengguna disimpan sebagai fakta.
3. Sistem mencocokkan fakta dengan aturan yang terdapat dalam file `aturan.json`.
4. Jika kondisi suatu aturan terpenuhi, sistem menghasilkan fakta atau kesimpulan baru.
5. Fakta baru dapat digunakan untuk memenuhi aturan berikutnya.
6. Proses pencocokan dilakukan sampai tidak ada aturan baru yang dapat dijalankan.
7. Sistem menampilkan hasil akhir berupa prioritas belajar beserta alasan penentuannya.

### Contoh Proses Forward Chaining

Misalnya pengguna memberikan fakta berikut:

- `deadline_dekat` = Ya
- `bobot_nilai_tinggi` = Ya

Proses penalarannya:

1. Fakta `deadline_dekat` memenuhi kondisi pada aturan R1 sehingga menghasilkan `tenggat_mendesak`.
2. Fakta `tenggat_mendesak` dan `bobot_nilai_tinggi` memenuhi aturan R4.
3. Sistem menghasilkan kesimpulan `prioritas_utama`.

Dengan demikian, hasil akhir dari contoh tersebut adalah **Prioritas Utama**.

Metode ini tidak menggunakan rumus perhitungan numerik karena proses penalarannya dilakukan dengan mencocokkan fakta terhadap aturan IF-THEN.

## 5. Tiga Kasus Uji dan Screenshot

Pengujian dilakukan untuk mengetahui apakah sistem dapat memberikan kesimpulan sesuai dengan fakta dan aturan yang telah dibuat.

### Kasus 1

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Deadline tugas sudah dekat? | Ya |
| Jadwal ujian sudah dekat? | Tidak |
| Materi sulit dipahami? | Tidak |
| Pemahaman terhadap materi masih rendah? | Tidak |
| Masih ada tugas yang belum selesai? | Tidak |
| Bobot nilai tinggi? | Ya |
| Sudah memahami materi dengan baik? | Tidak |
| Deadline masih cukup lama? | Tidak |

**Hasil:** Prioritas Utama.

**Alasan:** Deadline tugas sudah dekat dan bobot nilai tinggi. Kondisi tersebut memenuhi aturan R1 dan R4.

**Screenshot hasil pengujian:**

![Kasus 1](screenshot/kasus1.png)

### Kasus 2

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Deadline tugas sudah dekat? | Tidak |
| Jadwal ujian sudah dekat? | Tidak |
| Materi sulit dipahami? | Ya |
| Pemahaman terhadap materi masih rendah? | Ya |
| Masih ada tugas yang belum selesai? | Ya |
| Bobot nilai tinggi? | Tidak |
| Sudah memahami materi dengan baik? | Tidak |
| Deadline masih cukup lama? | Tidak |

**Hasil:** Prioritas Tinggi.

**Alasan:** Materi sulit dipahami, pemahaman masih rendah, dan terdapat tugas yang belum selesai. Kondisi tersebut memenuhi aturan R2 dan R6.

**Screenshot hasil pengujian:**

![Kasus 2](screenshot/kasus2.png)

### Kasus 3

**Kondisi yang dimasukkan:**

| Pertanyaan | Jawaban |
|---|---|
| Deadline tugas sudah dekat? | Tidak |
| Jadwal ujian sudah dekat? | Tidak |
| Materi sulit dipahami? | Tidak |
| Pemahaman terhadap materi masih rendah? | Tidak |
| Masih ada tugas yang belum selesai? | Tidak |
| Bobot nilai tinggi? | Tidak |
| Sudah memahami materi dengan baik? | Ya |
| Deadline masih cukup lama? | Ya |

**Hasil:** Prioritas Rutin.

**Alasan:** Mahasiswa sudah memahami materi dengan baik dan deadline masih cukup lama. Kondisi tersebut memenuhi aturan R7.

**Screenshot hasil pengujian:**

![Kasus 3](screenshot/kasus3.png)

## 6. Batas Keberlakuan Sistem

Sistem pakar ini menggunakan pengetahuan yang disusun berdasarkan sumber dari Monash University, University of Sydney, dan Cornell University mengenai manajemen waktu serta strategi belajar. Sistem ditujukan untuk membantu mahasiswa menentukan prioritas belajar berdasarkan kondisi deadline tugas, jadwal ujian, tingkat kesulitan materi, pemahaman mahasiswa, dan bobot nilai. Sistem ini hanya dapat memberikan hasil berdasarkan fakta dan aturan yang telah dimasukkan ke dalam basis pengetahuan. Oleh karena itu, hasil yang diberikan merupakan saran atau rekomendasi untuk membantu mahasiswa mengatur kegiatan belajar, bukan keputusan akhir yang harus selalu diikuti. Mahasiswa tetap perlu mempertimbangkan kondisi dan kebutuhan belajarnya masing-masing.

## 7. Penggunaan Alat Bantu AI

Dalam proses pembuatan tugas ini, AI digunakan sebagai alat bantu untuk memahami konsep sistem pakar, menyusun aturan IF-THEN, membantu pembuatan kode program Python, serta menyusun dokumentasi README.

Hasil yang diberikan oleh AI kemudian diperiksa dan disesuaikan kembali agar sesuai dengan kebutuhan tugas. Program dan aturan yang digunakan juga dipelajari kembali agar dapat dipahami dan dijalankan dengan baik.
