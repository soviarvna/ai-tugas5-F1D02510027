
import json

# Membaca aturan dari file JSON
with open("aturan.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Tampilan awal program
print("=" * 45)
print(" SISTEM PAKAR PRIORITAS BELAJAR MAHASISWA")
print("=" * 45)

print("\nJawablah pertanyaan berikut dengan:")
print("y = Ya")
print("t = Tidak")

# Menyimpan fakta dari jawaban pengguna
fakta = set()

for pertanyaan in data["pertanyaan"]:
    while True:
        jawaban = input(
            "\n" + pertanyaan["teks"] + " (y/t): "
        ).lower().strip()

        if jawaban == "y":
            fakta.add(pertanyaan["fakta"])
            break

        elif jawaban == "t":
            break

        else:
            print("Jawaban tidak valid! Masukkan y atau t.")

# Proses Forward Chaining
aturan_dipakai = []
aturan_yang_sudah_dijalankan = set()

while True:
    ada_fakta_baru = False

    for aturan in data["aturan"]:

        if aturan["id"] in aturan_yang_sudah_dijalankan:
            continue

        syarat = aturan["jika"]

        # Memeriksa kondisi AND dan OR
        if aturan["mode"] == "dan":
            cocok = all(item in fakta for item in syarat)

        else:
            cocok = any(item in fakta for item in syarat)

        # Jika aturan terpenuhi
        if cocok:
            hasil = aturan["maka"]

            aturan_yang_sudah_dijalankan.add(aturan["id"])

            if hasil not in fakta:
                fakta.add(hasil)
                aturan_dipakai.append(aturan)
                ada_fakta_baru = True

    # Menghentikan proses jika tidak ada fakta baru
    if not ada_fakta_baru:
        break

# Menampilkan hasil akhir
print("\n")
print("=" * 45)
print("          HASIL PRIORITAS BELAJAR")
print("=" * 45)

# Menentukan hasil berdasarkan fakta
if "prioritas_utama" in fakta:

    print("\nPrioritas Belajar : PRIORITAS UTAMA")
    print("Alasan:")
    print("- Terdapat tugas atau ujian yang mendesak.")
    print("- Kamu perlu segera menyelesaikan tugas")
    print("  atau mempersiapkan ujian.")

elif "prioritas_tinggi" in fakta:

    print("\nPrioritas Belajar : PRIORITAS TINGGI")
    print("Alasan:")
    print("- Materi mata kuliah sulit dipahami.")
    print("- Masih terdapat tugas yang belum selesai.")
    print("- Kamu perlu lebih banyak waktu untuk belajar.")

elif "prioritas_rutin" in fakta:

    print("\nPrioritas Belajar : PRIORITAS RUTIN")
    print("Alasan:")
    print("- Kamu sudah memahami materi dengan baik.")
    print("- Belum ada deadline yang mendesak.")
    print("- Tetap lakukan belajar secara rutin.")

else:

    print("\nBelum ada prioritas khusus yang ditemukan.")
    print("Alasan:")
    print("- Jawaban yang diberikan belum memenuhi")
    print("  aturan untuk menghasilkan kesimpulan.")
    print("- Tetap perhatikan jadwal tugas dan ujian.")

# Menampilkan catatan program
print("\n" + "-" * 45)
print("CATATAN:")
print(data["batas"])
print("-" * 45)

print("\nTerima kasih telah menggunakan program ini!")
